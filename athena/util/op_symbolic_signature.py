from dataclasses import dataclass
import typing as t
from athena.util.op_stringized_expr import OpStringizedExpr
from athena.ir.ir_symbol import ShapeOrDataDimExprs
from athena.util.hash_combine import hash_combine

@dataclass
class OpSymbolicSignature:
  op_expr: OpStringizedExpr
  inputs_dim_exprs: t.List[ShapeOrDataDimExprs]
  outputs_dim_exprs: t.List[ShapeOrDataDimExprs]

  def __hash__(self):
    hash_value = hash(self.op_expr)
    for symbolic_dim_exprs in self.all_dim_exprs():
      hash_value = hash_combine(hash_value, hash(symbolic_dim_exprs))
    return hash_value

  def all_dim_exprs(self):
    yield from self.inputs_dim_exprs
    yield from self.outputs_dim_exprs