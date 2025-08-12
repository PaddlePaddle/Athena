from athena.ir_converters.paddle_op_converter import ConvertToPaddleOp
from athena.ir_converters.paddle_tensor_converter import ConvertToPaddleTensor
from athena.generators.paddle_op_call_generator import PaddleOpCallGenerator
from athena.generators.global_tensor_converter import GlobalTensorConverter
from athena.util.name_generator import NameGenerator
from dataclasses import dataclass
from typing import List, Union, Callable
from athena.generators.block_name_generator import BlockNameGenerator
from athena.util.tensor_topo import (
    GetOpId2TensorNamesUsedByMeAndDownstream,
    GetOpId2OpPipeInOutNamesSignature,
    OpPipeInOutNamesSignature,
)
from athena.generators.block_name_generator import BlockNameGenerator
from athena.util.input_output_tensors_extractor import InputOutputTensorsExtractor
from athena.util.block_op_calls_extractor import BlockOpCallsExtractor
import athena.util.lambda_util as fn


@dataclass
class IndentedPyCode:
    pycode: Callable[Callable[str, str], str]
    num_tabs: int


@dataclass
class PyCodeStmt:
    op: "Op"
    op_unique_local_name: str
    pycode: List[IndentedPyCode]
    input_tensor_names: List[str]
    output_tensor_names: List[str]
    inputs_type_strs: List[str]
    outputs_type_strs: List[str]
    inputs_shape_symbol_strs: List[str]
    outputs_shape_symbol_strs: List[str]
    inputs_data_symbol_strs: List[str]
    outputs_data_symbol_strs: List[str]
    tensors_used_by_me_and_downstream: List[str]
    tensors_used_by_downstream: List[str]
    op_func_in_out_names_signature: OpPipeInOutNamesSignature

    @property
    def op_name(self):
        return self.op.name

    @property
    def op_id(self):
        return self.op.op_id


class PaddleFuncBodyGenerator:
    def __init__(self, func, block_name_generator: BlockNameGenerator = None):
        self.func = func
        self.input_output_tensors_extractor = InputOutputTensorsExtractor(func)
        self.block_name_generator = (
            block_name_generator if block_name_generator is not None else None
        )
        self.stmts: List[PyCodeStmt] = []
        self.op_call_generator = PaddleOpCallGenerator()
        self.tensor_converter = GlobalTensorConverter()
        self.op_name_generator = NameGenerator()
        self.op_id2used_by_me_and_downstream = {}
        self.output_local_tensors = []
        self.block_op_calls = []
        self.body_op_id2op_index = {}

    def Generate(self, free_vars, args):
        input_tensors, output_tensors = self.input_output_tensors_extractor.Extract(
            free_vars, args
        )
        input_local_tensors = [
            self.tensor_converter.ConvertToLocalTensor(tensor)
            for tensor in input_tensors
        ]
        self.output_local_tensors = [
            self.tensor_converter.ConvertToLocalTensor(tensor)
            for tensor in output_tensors
        ]

        def get_local_name(tensor):
            if tensor is None:
                return None
            return self.tensor_converter.ConvertToLocalTensor(tensor).name

        self.op_id2used_by_me_and_downstream = GetOpId2TensorNamesUsedByMeAndDownstream(
            self.func, free_vars, args, get_local_name
        )
        self.op_id2op_func_in_out_names_signature = GetOpId2OpPipeInOutNamesSignature(
            self.op_id2used_by_me_and_downstream,
            self.func,
            free_vars,
            args,
            get_local_name,
        )
        self.block_op_calls = BlockOpCallsExtractor().Extract(
            self.func, free_vars, args
        )
        for index, op_call in enumerate(self.block_op_calls.body_op_calls):
            self.body_op_id2op_index[op_call.op.op_id] = index
        for op_call in self.block_op_calls.body_op_calls:
            self(op_call.op, *op_call.input_tensors, **op_call.kwargs)
        return input_local_tensors, self.stmts, self.output_local_tensors

    def GetTensorNamesUsedByDownstream(self, op_id):
        op_index = self.body_op_id2op_index[op_id]
        if (op_index + 1) == len(self.block_op_calls.body_op_calls):
            return [tensor.name for tensor in self.output_local_tensors]
        next_op_id = self.block_op_calls.body_op_calls[op_index + 1].op.op_id
        return self.op_id2used_by_me_and_downstream[next_op_id]

    def __call__(self, op, *input_tensors, **kwargs):
        op_py_varname = op.GetPyVarName()
        if hasattr(self, op_py_varname):
            return getattr(self, op_py_varname)(op, *input_tensors, **kwargs)
        stmts_method_name = f"get_stmts_{op_py_varname}"
        get_stmts = (
            getattr(self, stmts_method_name)
            if hasattr(self, stmts_method_name)
            else self.GetStmtPyCode
        )
        return self.CollectPyCodeStmt(get_stmts, op, *input_tensors, **kwargs)

    def get_stmts_builtin_split(self, local_output_tensor_names, op, x):
        x_name = x.name
        output_unpack_str = fn.join_map(local_output_tensor_names)
        return [self.Indent0(lambda f: f"{output_unpack_str(f)}, = {f(x_name)}")]

    def get_stmts_pd_op_while(
        self,
        local_output_tensor_names,
        op,
        *local_input_tensors,
        **kwargs,
    ):
        block_func, *free_vars = kwargs["blocks"][0][0]
        cond, *args = local_input_tensors
        free_vars = [self.tensor_converter.ConvertToLocalTensor(t) for t in free_vars]
        output_unpack_str = fn.join_map(local_output_tensor_names)
        input_var_str = fn.join_map([t.name for t in local_input_tensors])
        block_name = BlockNameGenerator().Generate(op, region_idx=0, block_idx=0)
        block_args_str = fn.join_map([t.name for t in [*free_vars, *args]])
        arg_str = fn.join_map([t.name for t in args])
        cond_name = cond.name
        return [
            self.Indent0(lambda f: f"import os"),
            self.Indent0(
                lambda f: f"ATHENA_WHILE_LOOP_LIMIT = os.getenv('ATHENA_WHILE_LOOP_LIMIT')"
            ),
            self.Indent0(
                lambda f: f"kWhileLoopLimit = (128 if ATHENA_WHILE_LOOP_LIMIT is None else int(ATHENA_WHILE_LOOP_LIMIT))"
            ),
            self.Indent0(lambda f: f"while_loop_counter_{op.op_id} = 0"),
            self.Indent0(lambda f: f"while {f(cond_name)}:"),
            self.Indent1(
                lambda f: f"{input_var_str(f)}, = self.{block_name}({block_args_str(f)})"
            ),
            self.Indent1(lambda f: f"while_loop_counter_{op.op_id} += 1"),
            self.Indent1(
                lambda f: f"if while_loop_counter_{op.op_id} > kWhileLoopLimit:"
            ),
            self.Indent2(lambda f: f"break"),
            self.Indent1(lambda f: f""),
            self.Indent0(lambda f: f"{output_unpack_str(f)}, = {arg_str(f)},"),
        ]

    def get_stmts_pd_op_if(
        self,
        local_output_tensor_names,
        op,
        cond,
        **kwargs,
    ):
        _, *true_branch_free_vars = kwargs["blocks"][0][0]
        _, *false_branch_free_vars = kwargs["blocks"][1][0]
        true_branch_input_names = fn.join_map(
            [
                local_tensor.name
                for t in true_branch_free_vars
                for local_tensor in [self.tensor_converter.ConvertToLocalTensor(t)]
            ]
        )
        false_branch_input_names = fn.join_map(
            [
                local_tensor.name
                for t in false_branch_free_vars
                for local_tensor in [self.tensor_converter.ConvertToLocalTensor(t)]
            ]
        )
        ret = fn.join_map(local_output_tensor_names)
        true_block_name = BlockNameGenerator().Generate(op, region_idx=0, block_idx=0)
        false_block_name = BlockNameGenerator().Generate(op, region_idx=1, block_idx=0)
        cond_name = cond.name
        return [
            self.Indent0(lambda f: f"if {f(cond_name)}:"),
            self.Indent1(
                lambda f: f"{ret(f)}, = self.{true_block_name}({true_branch_input_names(f)})"
            ),
            self.Indent0(lambda f: f"else:"),
            self.Indent1(
                lambda f: f"{ret(f)}, = self.{false_block_name}({false_branch_input_names(f)})"
            ),
        ]

    def Indent0(self, pycode: Callable[Callable[str, str], str]):
        assert callable(pycode)
        return IndentedPyCode(pycode=pycode, num_tabs=0)

    def Indent1(self, pycode: Callable[Callable[str, str], str]):
        assert callable(pycode)
        return IndentedPyCode(pycode=pycode, num_tabs=1)

    def Indent2(self, pycode: Callable[Callable[str, str], str]):
        assert callable(pycode)
        return IndentedPyCode(pycode=pycode, num_tabs=2)

    def CollectPyCodeStmt(self, GetStmtPyCode, op, *input_tensors, **kwargs):
        outputs_type_strs = [t.GetShortStr() for t in op.output_types]
        inputs_type_strs = [t.GetShortStr() for t in op.input_types]
        outputs_shape_symbol_strs = [
            s.value.GetShapeShortStr() for s in op.__results_symbols_signature__.value
        ]
        inputs_shape_symbol_strs = [
            s.value.GetShapeShortStr() for s in op.__operands_symbols_signature__.value
        ]
        outputs_data_symbol_strs = [
            s.value.GetDataShortStr() for s in op.__results_symbols_signature__.value
        ]
        inputs_data_symbol_strs = [
            s.value.GetDataShortStr() for s in op.__operands_symbols_signature__.value
        ]
        op = ConvertToPaddleOp(op)
        input_local_tensors = [
            self.tensor_converter.ConvertToLocalTensor(input_tensor)
            for input_tensor in input_tensors
        ]
        local_output_tensor_names = [
            self.tensor_converter.ConvertToLocalTensor(output_tensor).name
            for output_tensor in op.GetResults()
        ]
        stmts = GetStmtPyCode(
            local_output_tensor_names, op, *input_local_tensors, **kwargs
        )
        if len(stmts) == 0:
            return op.GetResults()

        def GetTensorName(tensor):
            return tensor.name if tensor is not None else "None"

        self.stmts.append(
            PyCodeStmt(
                op=op,
                op_unique_local_name=self.op_name_generator.Generate(
                    key=op.op_id,
                    prefix=f"op_{op.GetNameSuffix()}",
                ),
                input_tensor_names=[GetTensorName(t) for t in input_local_tensors],
                output_tensor_names=local_output_tensor_names,
                inputs_type_strs=inputs_type_strs,
                outputs_type_strs=outputs_type_strs,
                inputs_shape_symbol_strs=inputs_shape_symbol_strs,
                outputs_shape_symbol_strs=outputs_shape_symbol_strs,
                inputs_data_symbol_strs=inputs_data_symbol_strs,
                outputs_data_symbol_strs=outputs_data_symbol_strs,
                pycode=stmts,
                tensors_used_by_me_and_downstream=self.op_id2used_by_me_and_downstream[
                    op.op_id
                ],
                tensors_used_by_downstream=self.GetTensorNamesUsedByDownstream(
                    op.op_id
                ),
                op_func_in_out_names_signature=self.op_id2op_func_in_out_names_signature[
                    op.op_id
                ],
            )
        )
        return op.GetResults()

    def GetStmtPyCode(
        self, local_output_tensor_names, op, *input_local_tensors, **kwargs
    ):
        assert len(kwargs) == 0
        local_output_unpack_str = fn.join_map(local_output_tensor_names)
        local_op_call_expr = self.op_call_generator.GenerateOpCall(
            op, *input_local_tensors
        )
        if local_op_call_expr is None:
            return []
        pycode = (
            local_op_call_expr
            if len(local_output_tensor_names) == 0
            else lambda f: f"{local_output_unpack_str(f)} = {local_op_call_expr(f)}"
        )
        return [IndentedPyCode(pycode=pycode, num_tabs=0)]
