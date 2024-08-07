from dataclasses import dataclass
from athena.ir_converters.paddle_op_converter import ConvertToPaddleOp
from athena.ir_converters.paddle_tensor_converter import ConvertToPaddleTensor
from athena.ir_converters.paddle_type_converter import ConvertTypeToString
from athena.generators.paddle_op_call_generator import PaddleOpCallGenerator
from athena.generators.paddle_func_body_generator import PyCodeStmt
import typing as t
from athena.util.input_tensor_desc import InputTensorDesc, MakeInputTensorDesc
import athena.ir.ir_type as ir_type
import athena.ir.ir_tensor as ir_tensor
import athena.ir.ir_symbol as ir_symbol
from collections import namedtuple
import os
import jinja2

import hashlib
from athena.generators.paddle_c_ops_arg_names import op_name2args
import typing as t
import random
from athena.util.ops_func_signature import (
    InputSpecDesc,
    TensorId,
    NullTensorId,
    OperandTensorId,
    TensorListMemberId,
    OperandId,
    OpsFuncSignature,
)
from collections import OrderedDict, defaultdict
import itertools


@dataclass
class SequenceFuncDesc:
    ops_func_signature: OpsFuncSignature
    output_tensor_names: t.List[str]
    seq_stmts: t.List[PyCodeStmt]
    get_unused_tensor_name: t.Callable[PyCodeStmt, t.List[str]]


class SequenceUnittestsGenerator:

    def __init__(self, program_id, op_example_inputs_meta_getter):
        self.program_id = program_id
        self.op_example_inputs_meta_getter = op_example_inputs_meta_getter
        self.input_spec_mode = "original"

    def Generate(self, seq_stmts):
        seq_func_desc = self.MakeSequenceFuncDesc(seq_stmts)
        return self._RenderTemplate(seq_func_desc)

    def MakeSequenceFuncDesc(self, seq_stmts):
        op_id2seq_stmt = OrderedDict((stmt.op_id, stmt) for stmt in seq_stmts)
        ops_func_signature = OpsFuncSignature(
            tensor_ids=self.GetTensorIds(op_id2seq_stmt),
            operand_ids=self.GetOperandIds(op_id2seq_stmt),
            operand_tensor_id4operand_id=self.MakeOperandTensorId4OperandId(
                op_id2seq_stmt
            ),
            null_tensor_id4operand_id=self.MakeNullTensorId4OperandId(op_id2seq_stmt),
            tensor_list_member_ids4operand_id=self.MakeTensorListMemberIds4OperandId(
                op_id2seq_stmt
            ),
            tensor_name4tensor_id=self.MakeTensorName4TensorId(op_id2seq_stmt),
            tensor_name4operand_id=self.MakeTensorName4OperandId(op_id2seq_stmt),
            input_spec_shape_dtype4tensor_id=self.MakeInputSpecShapeAndDtype4TensorId(
                op_id2seq_stmt,
            ),
            example_input_meta4tensor_id=self.MakeExampleInputsMeta4TensorId(
                op_id2seq_stmt,
            ),
            example_input_data4operand_id=self.MakeExampleInputData4OperandId(
                op_id2seq_stmt,
            ),
            immediate_value4operand_id=self.MakeImmediateValue4OperandId(
                op_id2seq_stmt
            ),
            immediate_value4int_array_member_id=(
                self.MakeImmediateValue4IntArrayMemberId(op_id2seq_stmt)
            ),
        )
        output_tensor_names = self.GetOutputTensorNames(seq_stmts)

        def GetUnusedTensorName(stmt):
            return list(
                set(stmt.tensors_used_by_me_and_downstream)
                - set(stmt.tensors_used_by_downstream)
            )

        return SequenceFuncDesc(
            ops_func_signature=ops_func_signature,
            output_tensor_names=output_tensor_names,
            seq_stmts=seq_stmts,
            get_unused_tensor_name=GetUnusedTensorName,
        )

    def GetOutputTensorNames(self, seq_stmts):
        tensors_used_by_downstream = set(seq_stmts[-1].tensors_used_by_downstream)
        return [
            tensor_name
            for stmt in seq_stmts
            for tensor_name in stmt.output_tensor_names
            if tensor_name in tensors_used_by_downstream
        ]

    def MakeImmediateValue4OperandId(
        self, op_id2seq_stmt: OrderedDict[int, PyCodeStmt]
    ):
        def ImmediateValue4OperandId(operand_id, data):
            op = op_id2seq_stmt[operand_id.op_id].op
            return self.GetImmediateValue4OperandId(op, operand_id, data)

        return ImmediateValue4OperandId

    def MakeImmediateValue4IntArrayMemberId(
        self, op_id2seq_stmt: OrderedDict[int, PyCodeStmt]
    ):
        def ImmediateValue4IntArrayMemberId(tensor_id):
            program_id = self.program_id
            op = op_id2seq_stmt[tensor_id.op_id].op
            return self.GetImmediateValue4IntArrayMemberId(program_id, op, tensor_id)

        return ImmediateValue4IntArrayMemberId

    def GetImmediateValue4OperandId(self, op, operand_id, data):
        if data is None:
            return None
        cpp_type_name = self.GetCppOperandTypeName(op, operand_id.operand_idx)
        if cpp_type_name == "IntArray":
            return None
        if cpp_type_name == "Scalar[]":
            return data
        if cpp_type_name in {
            "Scalar",
            "Scalar(int)",
            "Scalar(int64_t)",
            "Scalar(float)",
            "Scalar(double)",
        }:
            if isinstance(data, list):
                return data[0]
            else:
                return data
        return None

    def GetImmediateValue4IntArrayMemberId(self, program_id, op, tensor_id):
        if isinstance(tensor_id, NullTensorId):
            return (None, None)

        def GetOperandIdx(tensor_id):
            if isinstance(tensor_id, TensorListMemberId):
                return tensor_id.operand_tensor_list_idx
            if isinstance(tensor_id, OperandTensorId):
                return tensor_id.operand_tensor_idx
            raise NotImplementedError(f"unknown TensorId subclass {type(tensor_id)}")

        cpp_type_name = self.GetCppOperandTypeName(op, GetOperandIdx(tensor_id))
        if cpp_type_name != "IntArray":
            return (None, None)
        tensor_meta = self.GetExampleInputsMeta4TensorId(
            program_id=program_id,
            op=op,
            tensor_id=tensor_id,
        )
        if tensor_meta is None:
            return (None, None)
        return (tensor_meta.data, tensor_meta.dtype)

    def MakeExampleInputsMeta4TensorId(
        self, op_id2seq_stmt: OrderedDict[int, PyCodeStmt]
    ):
        def GetExampleInputsMeta4TensorId(tensor_id):
            program_id = self.program_id
            op = op_id2seq_stmt[tensor_id.op_id].op
            return self.GetExampleInputsMeta4TensorId(
                program_id=program_id,
                op=op,
                tensor_id=tensor_id,
            )

        return GetExampleInputsMeta4TensorId

    def GetExampleInputsMeta4TensorId(self, program_id, op, tensor_id):
        if isinstance(tensor_id, NullTensorId):
            return None
        if isinstance(tensor_id, OperandTensorId):
            return self.GetExampleInputsMeta(
                program_id=program_id,
                op=op,
                input_idx=tensor_id.operand_tensor_idx,
            )
        if isinstance(tensor_id, TensorListMemberId):
            tensor_meta = self.GetExampleTensorMeta(
                program_id=program_id,
                op=op,
                input_idx=tensor_id.operand_tensor_list_idx,
            )
            input_type = op.input_types[tensor_id.operand_tensor_list_idx]
            dtype = input_type.value[tensor_id.tensor_list_member_idx].dtype
            return MakeInputTensorDesc(
                shape=tensor_meta.shape[tensor_id.tensor_list_member_idx],
                dtype=ConvertTypeToString(dtype),
                data=tensor_meta.data[tensor_id.tensor_list_member_idx],
            )
        raise NotImplementedError()

    def IsOperandImmediateValue(self, program_id, op, operand_id):
        data = self.GetExampleTensorMeta(
            program_id=program_id,
            op=op,
            input_idx=operand_id.operand_idx,
        )
        if data is None:
            return False
        immediate_value = self.GetImmediateValue4OperandId(op, operand_id, data.data)
        return immediate_value is not None

    def MakeExampleInputData4OperandId(
        self, op_id2seq_stmt: OrderedDict[int, PyCodeStmt]
    ):
        def Get(operand_id):
            op = op_id2seq_stmt[operand_id.op_id].op
            if isinstance(op.input_types[operand_id.operand_idx], ir_type.NullType):
                return None
            program_id = self.program_id
            op = op_id2seq_stmt[operand_id.op_id].op
            data = self.GetExampleTensorMeta(
                program_id=program_id,
                op=op,
                input_idx=operand_id.operand_idx,
            )
            return data.data if data is not None else None

        return Get

    def MakeInputSpecShapeAndDtype4TensorId(
        self, op_id2seq_stmt: OrderedDict[int, PyCodeStmt]
    ):
        def GetInputSpecShapeAndDtype4TensorId(tensor_id):
            input_spec_mode = self.input_spec_mode
            program_id = self.program_id
            op = op_id2seq_stmt[tensor_id.op_id].op
            return self.InputSpecShapeAndDtype4TensorId(
                input_spec_mode=input_spec_mode,
                program_id=program_id,
                op=op,
                tensor_id=tensor_id,
            )

        return GetInputSpecShapeAndDtype4TensorId

    def InputSpecShapeAndDtype4TensorId(
        self,
        input_spec_mode,
        program_id,
        op,
        tensor_id,
    ):
        if isinstance(tensor_id, NullTensorId):
            return None
        elif isinstance(tensor_id, OperandTensorId):
            return self.InputSpecShapeAndDtype4OperandId(
                input_spec_mode=input_spec_mode,
                program_id=program_id,
                op=op,
                operand_id=OperandId(op.op_id, tensor_id.operand_tensor_idx),
            )
        elif isinstance(tensor_id, TensorListMemberId):
            operand_spec = self.InputSpecShapeAndDtype4OperandId(
                input_spec_mode=input_spec_mode,
                program_id=program_id,
                op=op,
                operand_id=OperandId(op.op_id, tensor_id.operand_tensor_list_idx),
            )
            return InputSpecDesc(
                shape=operand_spec.shape[tensor_id.tensor_list_member_idx],
                dtype=operand_spec.dtype[tensor_id.tensor_list_member_idx],
            )
        else:
            raise NotImplementedError()

    def InputSpecShapeAndDtype4OperandId(
        self,
        input_spec_mode,
        program_id,
        op,
        operand_id,
    ):
        input_idx = operand_id.operand_idx
        tensor = self.GetOpOperandTensor(op, input_idx)
        if isinstance(tensor.type, ir_type.DenseTensorType):

            def GetShape():
                if input_spec_mode == "original":
                    return [(dim if dim >= 0 else None) for dim in tensor.shape]
                elif input_spec_mode == "pure_dynamic":
                    return [None for _ in tensor.shape]
                elif input_spec_mode == "pure_static":
                    return self.GetExampleTensorMeta(program_id, op, input_idx).shape
                else:
                    raise NotImplementedError

            dtype = tensor.dtype
        elif isinstance(tensor.type, ir_type.VectorType):

            def GetShape():
                if input_spec_mode == "original":
                    return [
                        [(dim if dim >= 0 else None) for dim in t.shape]
                        for t in tensor.type.value
                    ]
                elif input_spec_mode == "pure_dynamic":
                    return [[None for _ in t.shape] for t in tensor.type.value]
                elif input_spec_mode == "pure_static":
                    return self.GetExampleTensorMeta(program_id, op, input_idx).shape
                else:
                    raise NotImplementedError

            dtype = [x.dtype for x in tensor.type.value]
        else:
            dtype = None
        return InputSpecDesc(
            shape=GetShape(),
            dtype=dtype,
        )

    def MakeTensorName4OperandId(self, op_id2seq_stmt: OrderedDict[int, PyCodeStmt]):
        def GetSourceNames(op_id):
            return op_id2seq_stmt[op_id].input_tensor_names

        def TensorName4OperandId(operand_id):
            return operand_id.get_source_name(GetSourceNames)

        return TensorName4OperandId

    def MakeTensorName4TensorId(self, op_id2seq_stmt: OrderedDict[int, PyCodeStmt]):
        def GetSourceNames(op_id):
            return op_id2seq_stmt[op_id].input_tensor_names

        def TensorName4TensorId(tensor_id):
            return tensor_id.get_source_name(GetSourceNames)

        return TensorName4TensorId

    def MakeTensorListMemberIds4OperandId(
        self, op_id2seq_stmt: OrderedDict[int, PyCodeStmt]
    ):
        def TensorListMemberIds4OperandId(operand_id):
            op = op_id2seq_stmt[operand_id.op_id].op
            return operand_id.get_tensor_list_member_ids(op)

        return TensorListMemberIds4OperandId

    def MakeNullTensorId4OperandId(self, op_id2seq_stmt: OrderedDict[int, PyCodeStmt]):
        def NullTensorId4OperandId(operand_id):
            op = op_id2seq_stmt[operand_id.op_id].op
            return operand_id.get_null_tensor_id(op)

        return NullTensorId4OperandId

    def MakeOperandTensorId4OperandId(
        self, op_id2seq_stmt: OrderedDict[int, PyCodeStmt]
    ):
        def OperandTensorId4OperandId(operand_id):
            op = op_id2seq_stmt[operand_id.op_id].op
            return operand_id.get_operand_tensor_id(op)

        return OperandTensorId4OperandId

    def GetOperandIds(self, op_id2seq_stmt: OrderedDict[int, PyCodeStmt]):
        inner_output_tensor_names = set(
            tensor_name
            for _, stmt in op_id2seq_stmt.items()
            for tensor_name in stmt.output_tensor_names
        )

        def GetSourceNames(op_id):
            return op_id2seq_stmt[op_id].input_tensor_names

        existed_tensor_names = set()
        return [
            operand_id
            for op_id, stmt in op_id2seq_stmt.items()
            for operand_idx in range(len(stmt.input_tensor_names))
            if stmt.input_tensor_names[operand_idx] not in inner_output_tensor_names
            for operand_id in [OperandId(op_id, operand_idx)]
            for tensor_name in [operand_id.get_source_name(GetSourceNames)]
            if tensor_name not in existed_tensor_names
            for _ in [existed_tensor_names.add(tensor_name)]
        ]

    def GetTensorIds(self, op_id2seq_stmt: OrderedDict[int, PyCodeStmt]):
        def YieldOpOperandTensorId(operand_id):
            op = op_id2seq_stmt[operand_id.op_id].op
            input_idx = operand_id.operand_idx
            input_type = op.input_types[input_idx]
            if isinstance(input_type, ir_type.NullType):
                yield from []
            elif isinstance(input_type, ir_type.DenseTensorType):
                if not self.IsOperandImmediateValue(self.program_id, op, operand_id):
                    yield OperandTensorId(operand_id.op_id, input_idx)
            elif isinstance(input_type, ir_type.VectorType):
                yield from (
                    TensorListMemberId(
                        op_id=operand_id.op_id,
                        operand_tensor_list_idx=input_idx,
                        tensor_list_member_idx=i,
                    )
                    for i in range(len(input_type.value))
                )
            else:
                raise NotImplementedError()

        def GetSourceNames(op_id):
            return op_id2seq_stmt[op_id].input_tensor_names

        existed_tensor_names = set()
        return [
            tensor_id
            for operand_id in self.GetOperandIds(op_id2seq_stmt)
            for tensor_id in YieldOpOperandTensorId(operand_id)
            for tensor_name in [tensor_id.get_source_name(GetSourceNames)]
            if tensor_name not in existed_tensor_names
            for _ in [existed_tensor_names.add(tensor_name)]
        ]

    def GetInputSpecShapeAndDtype(self, input_spec_mode, program_id, op):
        if input_spec_mode == "original":

            def GetInputSpecShape(input_idx, tensor):
                return [(dim if dim >= 0 else None) for dim in tensor.shape]

        elif input_spec_mode == "pure_dynamic":

            def GetInputSpecShape(input_idx, tensor):
                return [None for _ in tensor.shape]

        elif input_spec_mode == "pure_static":

            def GetInputSpecShape(input_idx, tensor):
                return self.GetExampleTensorMeta(program_id, op, input_idx).shape

        else:
            raise NotImplementedError
        return [
            InputSpecDesc(
                shape=GetInputSpecShape(input_idx, tensor),
                dtype=tensor.dtype,
            )
            for input_idx, tensor in enumerate(self.GetOpOperandTensors(op))
        ]

    def GetExampleTensorMeta(self, program_id, op, input_idx):
        return self.op_example_inputs_meta_getter.Get(program_id, op.op_id, input_idx)

    def GetExampleInputsMeta(self, program_id, op, input_idx):
        tensor_meta = self.GetExampleTensorMeta(program_id, op, input_idx)
        if tensor_meta is None:
            raise ValueError(
                f"program_id: {program_id}, op_id: {op.op_id}, input_idx: {input_idx}"
            )
        input_type = op.input_types[input_idx]
        if not isinstance(input_type, ir_type.DenseTensorType):
            raise NotImplementedError()
        dtype = ConvertTypeToString(input_type.dtype)
        return MakeInputTensorDesc(
            shape=tensor_meta.shape,
            dtype=dtype,
            data=tensor_meta.data,
        )

    def GetOpOperandTensors(self, op):
        return [
            self.GetOpOperandTensor(op, input_idx)
            for input_idx, _ in enumerate(op.input_types)
        ]

    def GetOpOperandTensor(self, op, input_idx):
        return ConvertToPaddleTensor(
            ir_tensor.Tensor(
                local_name_prefix="in_",
                name=f"input_{input_idx}",
                arg_name_as_input=None,
                defining_op_name=None,
                type=op.input_types[input_idx],
                dim_exprs=ir_symbol.NullShapeOrDataDimExprs(),
            )
        )

    def _RenderTemplate(self, seq_func_desc):
        template = jinja_env.get_template("template_sequence_unittest.jinja")
        PADDLE_DEBUG_ENABLE_CINN = os.getenv("PADDLE_DEBUG_ENABLE_CINN") not in {
            "0",
            "False",
            "false",
            "OFF",
        }
        counter = itertools.count()
        name2counter = defaultdict(lambda: next(counter))
        return template.render(
            seq_func_desc=seq_func_desc,
            PADDLE_DEBUG_ENABLE_CINN=PADDLE_DEBUG_ENABLE_CINN,
            tensor_name_converter=lambda x: f"t{name2counter[x]}",
        )

    def GetCppOperandTypeName(self, op, input_idx):
        op_name = op.GetValidPyVarNameComponents()[-1]
        if op_name not in op_name2args:
            return False
        args = op_name2args[op_name]
        pos_arg_type_names = [
            type_name for type_name, arg_name in args if arg_name not in op.attrs
        ]
        assert input_idx < len(pos_arg_type_names), f"op.name:{op.name}, args:{args}"
        type_name = pos_arg_type_names[input_idx]
        return type_name

    def _GetTemplate(self, template_name):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(f"{dir_path}/{template_name}", "r") as f:
            return jinja_env.get_template(f.read())


def GetSha256sum(content):
    m = hashlib.sha256()
    m.update(content.encode())
    return m.hexdigest()


jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(
        searchpath=os.path.dirname(os.path.realpath(__file__))
    )
)
jinja_env.filters["py_map"] = lambda values, f: map(f, values)
