from dataclasses import dataclass
import typing as t
import athena.ir.ir_symbol as ir_symbol

@dataclass
class EqualConstraint:
  lhs: ir_symbol.DimExpr
  rhs: ir_symbol.DimExpr

@dataclass
class BroadcastableConstraint:
  lhs: ir_symbol.DimExpr
  rhs: ir_symbol.DimExpr

@dataclass
class GtOneConstraint:
  value: ir_symbol.DimExpr

@dataclass
class ConstraintManager:
  eq_cstrs: t.List[t.List[ir_symbol.DimExpr]]
  broadcastable_cstrs: t.List[t.List[ir_symbol.DimExpr]]
  gt_one_cstrs: t.List[ir_symbol.DimExpr]
