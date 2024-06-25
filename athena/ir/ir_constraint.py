from dataclasses import dataclass
import typing as t
import athena.ir.ir_symbol as ir_symbol

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
class EqualConstraint(Constraint):
  equal_dim_exprs: t.List[ir_symbol.DimExpr]

@dataclass
class BroadcastableConstraint(Constraint):
  braodcastable_dim_exprs: t.List[ir_symbol.DimExpr]

@dataclass
class GtOneConstraint(Constraint):
  gt_one_dim_expr: ir_symbol.DimExpr

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