from dataclasses import dataclass
import typing as t
from athena.util.input_tensor_desc import InputTensorDesc
import athena.ir.ir_type as ir_type
from collections import namedtuple

InputSpecDesc = namedtuple(
    "InputSpecDesc",
    [
        "shape",
        "dtype",
    ],
)


@dataclass
class TensorId:
    pass


@dataclass
class NullTensorId(TensorId):
    pass

    def get_source_name(self, get_source_names: t.Callable[int, t.List[str]]) -> str:
        return "None"

@dataclass
class OperandTensorId(TensorId):
    op_id: int
    operand_tensor_idx: int

    def get_source_name(self, get_source_names: t.Callable[int, t.List[str]]) -> str:
        return get_source_names(self.op_id)[self.operand_tensor_idx]

@dataclass
class TensorListMemberId(TensorId):
    op_id: int
    operand_tensor_list_idx: int
    tensor_list_member_idx: int

    def get_source_name(self, get_source_names: t.Callable[int, t.List[str]]) -> str:
        source_name = get_source_names(self.op_id)[self.operand_tensor_list_idx]
        return f"{source_name}_{self.tensor_list_member_idx}"


@dataclass
class OperandId:
    op_id: int
    operand_idx: int

    def get_operand_tensor_id(self, op: "Op") -> t.Optional[OperandTensorId]:
        input_type = op.input_types[self.operand_idx]
        if not isinstance(input_type, ir_type.DenseTensorType):
            return None
        return OperandTensorId(self.op_id, self.operand_idx)

    def get_null_tensor_id(self, op: "Op") -> t.Optional[NullTensorId]:
        input_type = op.input_types[self.operand_idx]
        if not isinstance(input_type, ir_type.NullType):
            return None
        return NullTensorId()

    def get_tensor_list_member_ids(
        self, op: "Op"
    ) -> t.Optional[t.List[TensorListMemberId]]:
        input_type = op.input_types[self.operand_idx]
        if not isinstance(input_type, ir_type.VectorType):
            return None
        return [
            TensorListMemberId(
                self.op_id,
                operand_tensor_list_idx=self.operand_idx,
                tensor_list_member_idx=i,
            )
            for i in range(len(input_type.value))
        ]

    def get_source_name(self, get_source_names: t.Callable[int, t.List[str]]) -> str:
        return get_source_names(self.op_id)[self.operand_idx]

@dataclass
class OpsFuncSignature:
    tensor_ids: t.List[TensorId]
    operand_ids: t.List[OperandId]
    operand_tensor_id4operand_id: t.Callable[OperandId, t.Optional[OperandTensorId]]
    null_tensor_id4operand_id: t.Callable[OperandId, t.Optional[NullTensorId]]
    tensor_list_member_ids4operand_id: t.Callable[
        OperandId, t.Optional[t.List[TensorListMemberId]]
    ]
    tensor_name4tensor_id: t.Callable[TensorId, str]
    tensor_name4operand_id: t.Callable[OperandId, str]
    input_spec_shape_dtype4tensor_id: t.Callable[TensorId, InputSpecDesc]
    example_input_meta4tensor_id: t.Callable[TensorId, InputTensorDesc]
    example_input_data4operand_id: t.Callable[OperandId, t.Optional[t.List[int]]]
    immediate_value4operand_id: t.Callable[[OperandId, t.Any], t.Any]
    immediate_value4int_array_member_id: t.Callable[[TensorId, t.Any], t.Any]