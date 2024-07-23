from athena.util.op_stringized_expr import OpStringizedExpr
from athena.util.op_symbolic_signature import OpSymbolicSignature
import typing as t
from athena.util.load_pir_py_classes import (
    GetProgramClasses,
)
from athena.util.ir_program_util import (
    IsBackwardProgram,
)
from athena.generators.paddle_op_call_generator import PaddleOpCallGenerator
from athena.ir_converters.paddle_op_converter import ConvertToPaddleOp
from athena.ir_converters.paddle_tensor_converter import ConvertToPaddleTensor
import athena.ir.ir_tensor as ir_tensor
import athena.ir.ir_symbol as ir_symbol


class OpSymbolicSignatureGenerator:
    def __init__(
        self,
        func: t.Callable[[], t.Any],
        exec_programs_filepath: str,
        input_name_prefix: str,
    ):
        self.func = func
        self.exec_programs_filepath = exec_programs_filepath
        self.paddle_op_call_generator = PaddleOpCallGenerator()
        self.input_name_prefix = input_name_prefix

    def Generate(self) -> t.List[OpSymbolicSignature]:
        primitive_op_extractor = PrimitiveOpExtractor()
        return [
            OpSymbolicSignature(
                op_expr=OpStringizedExpr(
                    op_name=op.name,
                    op_expr=self.GetOpExpr(op),
                    input_name_prefix=self.input_name_prefix,
                    num_results=len(op.output_types),
                ),
                inputs_dim_exprs=[
                    x.value for x in op.__operands_symbols_signature__.value
                ],
                outputs_dim_exprs=[
                    x.value for x in op.__results_symbols_signature__.value
                ],
            )
            for cls in GetProgramClasses(self.exec_programs_filepath)
            for ir_program in [cls()]
            if not IsBackwardProgram(ir_program)
            for op in primitive_op_extractor.Extract(ir_program)
        ]

    def GetOpExpr(self, op):
        op = ConvertToPaddleOp(op)
        input_tensors = self.GetInputTensors(op)
        return self.paddle_op_call_generator.GenerateOpCall(op, *input_tensors)

    def GetInputTensorNames(self, op):
        return [t.name for t in self.GetInputTensors(op)]

    def GetInputTensors(self, op):
        return [
            ConvertToPaddleTensor(
                ir_tensor.Tensor(
                    local_name_prefix=self.input_name_prefix,
                    name=f"{self.input_name_prefix}{input_idx}",
                    arg_name_as_input=None,
                    defining_op_name=None,
                    type=input_type,
                    dim_exprs=ir_symbol.NullShapeOrDataDimExprs(),
                )
            )
            for input_idx, input_type in enumerate(op.input_types)
        ]
