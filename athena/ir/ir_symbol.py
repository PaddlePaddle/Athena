from dataclasses import dataclass
from typing import List, Optional

@dataclass
class DimExpr:
  pass


@dataclass
class Int64(DimExpr):
  value: int


@dataclass
class String(DimExpr):
  value: str


@dataclass
class Negative(DimExpr):
  operand: DimExpr


@dataclass
class Reciprocal(DimExpr):
  operand: DimExpr


@dataclass
class Add(DimExpr):
  operands: List[DimExpr]


@dataclass
class Mul(DimExpr):
  operands: List[DimExpr]


@dataclass
class Max(DimExpr):
  operands: List[DimExpr]


@dataclass
class Min(DimExpr):
  operands: List[DimExpr]


@dataclass
class Broadcast(DimExpr):
  operands: List[DimExpr]


@dataclass
class ShapeOrDataDimExprs:
  pass

@dataclass
class TensorShapeOrDataDimExprs(ShapeOrDataDimExprs):
  shape: List[DimExpr]
  data: Optional[List[DimExpr]]

@dataclass
class TensorListShapeOrDataDimExprs(ShapeOrDataDimExprs):
  value: List[TensorShapeOrDataDimExprs]