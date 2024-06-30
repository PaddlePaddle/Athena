from dataclasses import dataclass
import typing as t
import athena.ir.ir_symbol as ir_symbol
from athena.util.hash_combine import hash_combine

@dataclass
class ConstraintRecord:
  pass

@dataclass
class EqualConstraintRecord(ConstraintRecord):
  lhs: ir_symbol.DimExpr
  rhs: ir_symbol.DimExpr

@dataclass
class BroadcastableConstraintRecord(ConstraintRecord):
  lhs: ir_symbol.DimExpr
  rhs: ir_symbol.DimExpr

@dataclass
class GtOneConstraintRecord(ConstraintRecord):
  value: ir_symbol.DimExpr

@dataclass
class Constraint:
  pass

@dataclass
class NoConstraint(Constraint):
  no_dim_exprs: t.List[ir_symbol.DimExpr]

  def __hash__(self):
    hash_value = id(NoConstraint)
    for dim_expr in self.equal_dim_exprs:
      hash_value = hash_combine(hash_value, hash(dim_expr))
    return hash_value

@dataclass
class EqualConstraint(Constraint):
  equal_dim_exprs: t.List[ir_symbol.DimExpr]

  def __hash__(self):
    hash_value = id(EqualConstraint)
    for dim_expr in self.equal_dim_exprs:
      hash_value = hash_combine(hash_value, hash(dim_expr))
    return hash_value

@dataclass
class BroadcastableConstraint(Constraint):
  braodcastable_dim_exprs: t.List[ir_symbol.DimExpr]

  def __hash__(self):
    hash_value = id(BroadcastableConstraint)
    for dim_expr in self.braodcastable_dim_exprs:
      hash_value = hash_combine(hash_value, hash(dim_expr))
    return hash_value

@dataclass
class GtOneConstraint(Constraint):
  gt_one_dim_expr: ir_symbol.DimExpr

  def __hash__(self):
    hash_value = id(GtOneConstraint)
    hash_value = hash_combine(hash_value, hash(self.gt_one_dim_expr))
    return hash_value

@dataclass
class SymmetricDimVar:
  pass

@dataclass
class SymbolSymmetricDimVar(SymmetricDimVar):
  symbol: str

@dataclass
class ComposedSymmetricDimVar(SymmetricDimVar):
  symmetric_dim_vars: t.List[SymmetricDimVar]

@dataclass
class AnySymmetricDimVar(ComposedSymmetricDimVar):
  pass

@dataclass
class AddSymmetricDimVar(ComposedSymmetricDimVar):
  pass

@dataclass
class MulSymmetricDimVar(ComposedSymmetricDimVar):
  pass

@dataclass
class MaxSymmetricDimVar(ComposedSymmetricDimVar):
  pass

@dataclass
class MinSymmetricDimVar(ComposedSymmetricDimVar):
  pass

@dataclass
class BroadcastSymmetricDimVar(ComposedSymmetricDimVar):
  pass