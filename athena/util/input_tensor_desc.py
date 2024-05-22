from collections import namedtuple

InputTensorDesc = namedtuple("InputTensorDesc", [
  "shape",
  "dtype",
  "big_dtype",
  "data",
  "min",
  "max",
])

def MakeInputTensorDesc(input_tensor, GetShapeInstance, GetDataInstance):
  return InputTensorDesc(
    shape=GetShapeInstance(input_tensor),
    dtype=input_tensor.dtype,
    big_dtype=_GetBigType(input_tensor),
    data=GetDataInstance(input_tensor),
    min=getattr(InitMinGetter, input_tensor.dtype)(),
    max=getattr(InitMaxGetter, input_tensor.dtype)(),
  )

def _GetBigType(tensor):
  return type2bigger_type[tensor.dtype]

type2bigger_type = dict(
  bool="bool",
  bfloat16="float64",
  float16="float64",
  float32="float64",
  int16="int64",
  int32="int64",
  int64="int64",
)

class InitMinGetter:
  def bool():
    return "False" 

  def bfloat16():
    return "-0.5" 

  def float16():
    return "-0.5" 

  def float32():
    return "-0.5" 

  def float64():
    return "-0.5"

  def int32():
    return "0"

  def int64():
    return "0"


class InitMaxGetter:
  def bool():
    return "False" 

  def bfloat16():
    return "0.5" 

  def float16():
    return "0.5" 

  def float32():
    return "0.5" 

  def float64():
    return "0.5" 
    
  def int32():
    return "1"

  def int64():
    return "1"

