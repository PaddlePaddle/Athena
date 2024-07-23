from collections import namedtuple
from dataclasses import dataclass
import typing as t
import athena.ir.ir_type as ir_type

OpInputMetaKey = namedtuple("InputMetaKey", ["program_id", "op_id", "input_idx"])

ShapeType = t.List[int]


@dataclass
class OpInputMeta:
    op_id: int
    input_idx: int
    shape: t.Union[ShapeType, t.List[ShapeType], None]
    data: t.Union[ShapeType, t.List[ShapeType], None]


class OpExampleInputsMetaGetter:
    def __init__(self, records):
        self.input_meta_key2value = self._MakeOpInputMetaKey2Value(records)

    def HasAllInputs(self, program_id, op) -> bool:
        op_id = op.op_id
        num_inputs = len(op.input_types)
        for input_idx in range(num_inputs):
            if isinstance(op.input_types[input_idx], ir_type.NullType):
                continue
            key = OpInputMetaKey(program_id, op_id, input_idx)
            if key not in self.input_meta_key2value:
                return False
        return True

    def Get(self, program_id, op_id, input_idx) -> OpInputMeta:
        key = OpInputMetaKey(program_id, op_id, input_idx)
        return self.input_meta_key2value.get(key, None)

    def _MakeOpInputMetaKey2Value(self, records):
        input_meta_key2value = {}
        for record in records:
            key = OpInputMetaKey(
                record.program_id,
                record.op_id,
                record.input_idx,
            )
            input_meta_key2value[key] = OpInputMeta(
                op_id=record.op_id,
                input_idx=record.input_idx,
                shape=record.shape,
                data=record.data,
            )
        return input_meta_key2value


def MakeOpExampleInputsMetaGetter(name_and_classes):
    classes = [
        cls
        for name, cls in name_and_classes
        if name.startswith("PirProgram_op_input_tensor_meta_")
    ]
    return OpExampleInputsMetaGetter(records=classes)
