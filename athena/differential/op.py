from dataclasses import dataclass
from typing import Union

@dataclass
class Op:
  def __add__(lhs, rhs):
    return Add(lhs, self.TryWrapToConstant(rhs))

  def __sub__(lhs, rhs):
    return Add(lhs, Negative(self.TryWrapToConstant(rhs)))

  def __mul__(lhs, rhs):
    return Mul(lhs, self.TryWrapToConstant(rhs))

  def __div__(lhs, rhs):
    return Mul(lhs, Reciprocal(self.TryWrapToConstant(rhs)))

  def max(lhs, rhs):
    return Max(lhs, self.TryWrapToConstant(rhs))

  def min(lhs, rhs):
    return Min(lhs, self.TryWrapToConstant(rhs))

  def broadcast(lhs, rhs):
    return Broadcast(lhs, self.TryWrapToConstant(rhs))

  def TryWrapToConstant(value):
    if type(value) in {int, float}:
      return Constant(value)
    return value

@dataclass
class Constant(Op):
  value: Union[float, int]

@dataclass
class Param(Op):
  name: str

@dataclass
class Negative(Op):
  operand: Op

@dataclass
class Reciprocal(Op):
  operand: Op

@dataclass
class Add(Op):
  lhs: Op
  rhs: Op

@dataclass
class Mul(Op):
  lhs: Op
  rhs: Op

@dataclass
class Max(Op):
  lhs: Op
  rhs: Op

@dataclass
class Min(Op):
  lhs: Op
  rhs: Op

@dataclass
class Broadcast(Op):
  lhs: Op
  rhs: Op