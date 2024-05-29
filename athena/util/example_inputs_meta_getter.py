from collections import namedtuple
from dataclasses import dataclass
import typing as t

InputMetaKey = namedtuple('InputMetaKey', ['random_logging_id', 'input_name'])

@dataclass
class InputMeta:
  name: str
  shape: t.List[int]
  data: t.Optional[t.List[int]]

class ExampleInputsMetaGetter:
  def __init__(self, records):
    self.input_meta_key2value = self._MakeInputMetaKey2Value(records)

  def HasAllInputNames(self, random_logging_id, input_names) -> bool:
    for input_name in input_names:
      key = InputMetaKey(random_logging_id, input_name)
      if key not in self.input_meta_key2value:
        return False
    return True

  def Get(self, random_logging_id, input_name) -> InputMeta:
    return self.input_meta_key2value[InputMetaKey(random_logging_id, input_name)]

  def _MakeInputMetaKey2Value(self, records):
    input_meta_key2value = {}
    for record in records:
      key = InputMetaKey(record.random_logging_id, record.input_name)
      input_meta_key2value[key] = InputMeta(
        name=record.input_name,
        shape=record.shape,
        data=None
      )
    return input_meta_key2value