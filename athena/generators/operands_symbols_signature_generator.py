import typing as t
import athena.ir.ir_attr as ir_attr
import athena.ir.ir_constraint as ir_constraint
from dataclasses import dataclass
from athena.util.primitive_op_extractor import PrimitiveOpExtractor
from athena.util.load_pir_py_classes import (
    GetProgramClasses,
)
from athena.util.ir_program_util import IsBackwardProgram, GetProgramId
from athena.ir_converters.paddle_op_converter import ConvertToPaddleOp
from athena.generators.paddle_op_call_generator import PaddleOpCallGenerator
from athena.ir_converters.paddle_tensor_converter import ConvertToPaddleTensor
import athena.ir.ir_tensor as ir_tensor
import athena.ir.ir_symbol as ir_symbol
import hashlib


@dataclass
class OpOperandsSymbolsSignature:
    op_expr: str
    operands_symbols_signature: ir_attr.ArrayAttribute
    constraints: t.List[ir_constraint.Constraint]

    def GetOpExprHashStr(self) -> str:
        return self.GetSha256sum(self.op_expr)[0:32]

    def GetSha256sum(self, content):
        m = hashlib.sha256()
        m.update(content.encode())
        return m.hexdigest()


class OperandsSymbolsSignatureGenerator:
    def __init__(self, ir_program_file: str):
        self.ir_program_file = ir_program_file
        self.paddle_op_call_generator = PaddleOpCallGenerator()

    def Generate(self) -> t.Iterator[OpOperandsSymbolsSignature]:
        primitive_op_extractor = PrimitiveOpExtractor()
        ir_programs = [
            ir_program
            for cls in GetProgramClasses(self.ir_program_file)
            for ir_program in [cls()]
            if not IsBackwardProgram(ir_program)
        ]
        ir_program_ops = [
            (ir_program, op)
            for ir_program in ir_programs
            for op in primitive_op_extractor.Extract(ir_program)
        ]

        for ir_program, op in ir_program_ops:
            op_expr = self.GetOpExpr(op)
            yield OpOperandsSymbolsSignature(
                op_expr=op_expr,
                operands_symbols_signature=op.__operands_symbols_signature__,
                constraints=ir_program.CollectConstraints(),
            )

    def GetOpExpr(self, op):
        op = ConvertToPaddleOp(op)
        input_tensors = self.GetOpOperandTensors(op)
        return self.paddle_op_call_generator.GenerateOpCall(op, *input_tensors)

    def GetOpOperandTensors(self, op):
        return [
            ConvertToPaddleTensor(
                ir_tensor.Tensor(
                    local_name_prefix="in_",
                    name=f"input_{input_idx}",
                    arg_name_as_input=None,
                    defining_op_name=None,
                    type=input_type,
                    dim_exprs=ir_symbol.NullShapeOrDataDimExprs(),
                )
            )
            for input_idx, input_type in enumerate(op.input_types)
        ]
