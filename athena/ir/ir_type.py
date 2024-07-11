from dataclasses import dataclass
from typing import List

@dataclass
class NullType:
  
  def GetShortStr(self):
    return "None"


@dataclass
class VectorType:
  value: List["Type"]

  def GetShortStr(self):
    return "[%s]"%(", ".join([e.GetShortStr() for e in self.value]))

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
class SelectedRowsType:
  pass

@dataclass
class DenseTensorArrayType:
  pass

@dataclass
class SparseCooTensorType:
  pass

@dataclass
class SparseCsrTensorType:
  pass

@dataclass
class BFloat16Type:
  def GetShortStr(self):
    return "bf16"

  def __hash__(self):
    return id(BFloat16Type)

@dataclass
class Float16Type:
  def GetShortStr(self):
    return "f16"

  def __hash__(self):
    return id(Float16Type)

@dataclass
class Float32Type:
  def GetShortStr(self):
    return "f32"

  def __hash__(self):
    return id(Float32Type)

@dataclass
class Float64Type:
  def GetShortStr(self):
    return "f64"

  def __hash__(self):
    return id(Float64Type)

@dataclass
class Int8Type:
  def GetShortStr(self):
    return "i8"
  
  def __hash__(self):
    return id(Int8Type)

@dataclass
class UInt8Type:
  def GetShortStr(self):
    return "ui8"
  
  def __hash__(self):
    return id(UInt8Type)

@dataclass
class Int16Type:
  def GetShortStr(self):
    return "i16"
  
  def __hash__(self):
    return id(Int16Type)

@dataclass
class Int32Type:
  def GetShortStr(self):
    return "i32"
  
  def __hash__(self):
    return id(Int32Type)

@dataclass
class Int64Type:
  def GetShortStr(self):
    return "i64"
  
  def __hash__(self):
    return id(Int64Type)

@dataclass
class IndexType:
  def GetShortStr(self):
    return "index"
  
  def __hash__(self):
    return id(IndexType)

@dataclass
class BoolType:
  def GetShortStr(self):
    return "b"
  
  def __hash__(self):
    return id(BoolType)

@dataclass
class Complex64Type:
  def GetShortStr(self):
    return "c64"
  
  def __hash__(self):
    return id(Complex64Type)

@dataclass
class Complex128Type:
  def GetShortStr(self):
    return "c128"

  def __hash__(self):
    return id(Complex128Type)

@dataclass
class UnclassifiedType:
  args: list
  kwargs: dict