from collections import namedtuple
from dataclasses import dataclass
import athena.ir.ir_type as ir_type
import typing as t

InputMetaKey = namedtuple('InputMetaKey', ['program_id', 'input_name'])

@dataclass
class InputMeta:
  name: str
  shape: t.List[int]
  data: t.Optional[t.List[int]]

class ExampleInputsMetaGetter:
  def __init__(self, records):
    self.input_meta_key2value = self._MakeInputMetaKey2Value(records)

  def HasAllInputExamples(self, program_id, input_tensors) -> bool:
    return all(self.Has(program_id, input_tensor) for input_tensor in input_tensors)

  def Has(self, program_id, input_tensor) -> InputMeta:
    key = InputMetaKey(program_id, input_tensor.arg_name_as_input)
    if key in self.input_meta_key2value:
      return True
    shape = self.GetInputStaticShape(input_tensor)
    return shape is not None

  def Get(self, program_id, input_tensor) -> InputMeta:
    key = InputMetaKey(program_id, input_tensor.arg_name_as_input)
    if key in self.input_meta_key2value:
      return self.input_meta_key2value[key]
    shape = self.GetInputStaticShape(input_tensor)
    if shape is None:
      raise NotImplementedError()
    return InputMeta(
      name=input_tensor.arg_name_as_input,
      shape=shape,
      data=None
    )

  def GetInputStaticShape(self, input_tensor):
    if not isinstance(input_tensor.type, ir_type.DenseTensorType):
      return None
    for dim in input_tensor.shape:
      if dim < 0:
        return None
    return input_tensor.shape

  def _MakeInputMetaKey2Value(self, records):
    input_meta_key2value = {}
    for record in records:
      key = InputMetaKey(record.program_id, record.input_name)
      input_meta_key2value[key] = InputMeta(
        name=record.input_name,
        shape=record.shape,
        data=None
      )
    return input_meta_key2value