from dataclasses import dataclass

@dataclass
class Tensor:
  local_name_prefix: str
  name: str
  type: "Type"

  @property
  def shape(self):
    return self.type.shape

  @property
  def dtype(self):
    return self.type.dtype