from collections import namedtuple
from dataclasses import dataclass
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

  def HasAllInputNames(self, program_id, input_names) -> bool:
    for input_name in input_names:
      key = InputMetaKey(program_id, input_name)
      if key not in self.input_meta_key2value:
        return False
    return True

  def Get(self, program_id, input_name) -> InputMeta:
    return self.input_meta_key2value[InputMetaKey(program_id, input_name)]

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