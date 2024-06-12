from dataclasses import dataclass
from typing import List, Union
import typing as t

from athena.ir.ir_symbol import ShapeOrDataDimExprs

@dataclass
class Tensor:
  local_name_prefix: str
  name: str
  arg_name_as_input: t.Optional[str]
  defining_op_name: t.Optional[str]
  type: "Type"
  dim_exprs: ShapeOrDataDimExprs

  @property
  def shape(self):
    return self.type.shape

  @property
  def dtype(self):
    return self.type.dtype
