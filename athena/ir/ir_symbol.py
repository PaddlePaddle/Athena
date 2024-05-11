from dataclasses import dataclass
from typing import List, Optional
from athena.util.hash_combine import hash_combine

@dataclass
class DimExpr:
  pass

  def __hash__(self):
    return id(DimExpr)

@dataclass
class Int64(DimExpr):
  value: int

  def GetShortStr(self, parent_cls=None):
    return f"{self.value}"

  def __hash__(self):
    return hash_combine(id(type(self)), hash(self.value))

@dataclass
class String(DimExpr):
  value: str

  def GetShortStr(self, parent_cls=None):
    return f"{self.value}"

  def __hash__(self):
    return hash_combine(id(type(self)), hash(self.value))


@dataclass
class Negative(DimExpr):
  operand: DimExpr

  def GetShortStr(self, parent_cls=None):
    return f"-{self.operand.GetShortStr()}"

  def __hash__(self):
    return hash_combine(id(type(self)), hash(self.operand))


@dataclass
class Reciprocal(DimExpr):
  operand: DimExpr

  def GetShortStr(self, parent_cls=None):
    return f"(1 / {self.operand.GetShortStr()})"

  def __hash__(self):
    return hash_combine(id(type(self)), hash(self.operand))


@dataclass
class Add(DimExpr):
  operands: List[DimExpr]

  def GetShortStr(self, parent_cls=None):
    def ConvertOperand(i, operand):
      if type(operand) is Negative:
        return "-" + operand.operand.GetShortStr(Add)
      else:
        return ("+" if i > 0 else "") + operand.GetShortStr(Add)
    ret = "".join([
      ConvertOperand(i, operand)
      for i, operand in enumerate(self.operands)
    ])
    if parent_cls is Mul:
      return f"({ret})"
    return f"{ret}"

  def __hash__(self):
    hash_value = 0
    for operand in self.operands:
      hash_value = hash_combine(hash_value, hash(operand))
    return hash_combine(id(type(self)), hash_value)


@dataclass
class Mul(DimExpr):
  operands: List[DimExpr]

  def GetShortStr(self, parent_cls=None):
    def ConvertOperand(i, operand):
      if type(operand) is Reciprocal:
        return "/" + operand.operand.GetShortStr(Mul)
      else:
        return ("*" if i > 0 else "") + operand.GetShortStr(Mul)
    ret = "".join([
      ConvertOperand(i, operand)
      for i, operand in enumerate(self.operands)
    ])
    return f"{ret}"

  def __hash__(self):
    hash_value = 0
    for operand in self.operands:
      hash_value = hash_combine(hash_value, hash(operand))
    return hash_combine(id(type(self)), hash_value)


@dataclass
class Max(DimExpr):
  operands: List[DimExpr]

  def GetShortStr(self, parent_cls=None):
    return f"max({', '.join(o.GetShortStr() for o in self.operands)})"

  def __hash__(self):
    hash_value = 0
    for operand in self.operands:
      hash_value = hash_combine(hash_value, hash(operand))
    return hash_combine(id(type(self)), hash_value)


@dataclass
class Min(DimExpr):
  operands: List[DimExpr]

  def GetShortStr(self, parent_cls=None):
    return f"min({', '.join(o.GetShortStr() for o in self.operands)})"

  def __hash__(self):
    hash_value = 0
    for operand in self.operands:
      hash_value = hash_combine(hash_value, hash(operand))
    return hash_combine(id(type(self)), hash_value)


@dataclass
class Broadcast(DimExpr):
  operands: List[DimExpr]

  def GetShortStr(self, parent_cls=None):
    return f"bc({', '.join(o.GetShortStr() for o in self.operands)})"

  def __hash__(self):
    hash_value = 0
    for operand in self.operands:
      hash_value = hash_combine(hash_value, hash(operand))
    return hash_combine(id(type(self)), hash_value)


@dataclass
class ShapeOrDataDimExprs:
  pass

@dataclass
class TensorShapeOrDataDimExprs(ShapeOrDataDimExprs):
  shape: List[DimExpr]
  data: Optional[List[DimExpr]]

  def GetShapeShortStr(self):
    return self.GetDimExprsShortStr(self.shape)

  def GetDataShortStr(self):
    if self.data is None:
      return "None"
    return self.GetDimExprsShortStr(self.data)

  def GetDimExprsShortStr(self, dim_exprs):
    return f"[{', '.join(d.GetShortStr() for d in dim_exprs)}]"

@dataclass
class TensorListShapeOrDataDimExprs(ShapeOrDataDimExprs):
  value: List[TensorShapeOrDataDimExprs]

  def GetShapeShortStr(self):
    return f"[{', '.join(v.GetShapeShortStr() for v in self.value)}]"

  def GetDataShortStr(self):
    return f"[{', '.join(v.GetDataShortStr() for v in self.value)}]"
