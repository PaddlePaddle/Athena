from collections import namedtuple
from dataclasses import dataclass
from typing import List

@dataclass
class VectorType:
  value: List["Type"]

  def GetShortStr(self):
    return "[%s]"%s(", ".join([e.GetShortStr() for e in self.value]))

@dataclass
class DenseTensorType:
  shape: List[int]
  dtype: "Type"

  def GetShortStr(self):
    return "%sx%s"%(
      "x".join([str(dim) for dim in self.shape]),
      self.dtype.GetShortStr()
    )

@dataclass
class BFloat16Type:
  def GetShortStr(self):
    return "bf16"

@dataclass
class Float16Type:
  def GetShortStr(self):
    return "f16"

@dataclass
class Float32Type:
  def GetShortStr(self):
    return "f32"

@dataclass
class Float64Type:
  def GetShortStr(self):
    return "f64"
  
@dataclass
class Int8Type:
  def GetShortStr(self):
    return "i8"
  
@dataclass
class UInt8Type:
  def GetShortStr(self):
    return "ui8"
  
@dataclass
class Int16Type:
  def GetShortStr(self):
    return "i16"
  
@dataclass
class Int32Type:
  def GetShortStr(self):
    return "i32"
  
@dataclass
class Int64Type:
  def GetShortStr(self):
    return "i64"
  
@dataclass
class IndexType:
  def GetShortStr(self):
    return "index"
  
@dataclass
class BoolType:
  def GetShortStr(self):
    return "b"
  
@dataclass
class Complex64Type:
  def GetShortStr(self):
    return "c64"
  
@dataclass
class Complex128Type:
  def GetShortStr(self):
    return "c128"

@dataclass
class UnclassifiedType:
  args: list
  kwargs: dict