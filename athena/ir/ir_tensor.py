from dataclasses import dataclass
from typing import List, Union

from athena.ir.ir_symbol import ShapeOrDataDimExprs

@dataclass
class Tensor:
  local_name_prefix: str
  name: str
  type: "Type"
  dim_exprs: ShapeOrDataDimExprs

  @property
  def shape(self):
    return self.type.shape

  @property
  def dtype(self):
    return self.type.dtype
