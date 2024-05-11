import os
from jinja2 import Template
from collections import namedtuple
from athena.generators.paddle_func_body_generator import (
  PaddleFuncBodyGenerator
)
import athena.ir.ir_symbol as ir_symbol
from athena.util.dim_exprs_extractor import DimExprsExtractor
from athena.util.dim_instance_generator import DimInstanceGenerator

class PaddleUnittestGenerator:

  def __init__(self, unittest_class_name, func, body_generator = None):
    self.unittest_class_name = unittest_class_name
    self.func = func
    self.body_generator = body_generator
    if self.body_generator is None:
      self.body_generator = PaddleFuncBodyGenerator(func)

  def Generate(self, input_tensors):
    all_dim_exprs = DimExprsExtractor().Extract(self.func, input_tensors)
    dim_instance_generator = DimInstanceGenerator(all_dim_exprs)
    input_tensors, body_code_stmts = self.body_generator.Generate(input_tensors)
    return RenderTemplate(
      unittest_class_name=self.unittest_class_name,
      input_tensors=input_tensors,
      body_code_stmts=body_code_stmts,
      dim_instance_generator=dim_instance_generator
    )


type2bigger_type = dict(
  bool="bool",
  bfloat16="float64",
  float16="float64",
  float32="float64",
  int16="int64",
  int32="int64",
  int64="int64",
)

InputTensorMeta = namedtuple("InputTensorMeta", [
  "shape",
  "dtype",
  "big_dtype",
  "data", # `big_dtype` must be "dim"
  "min",
  "max",
])

InputSpecDesc = namedtuple("InputSpecDesc", [
  "shape",
  "dtype",
])


def RenderTemplate(
  unittest_class_name,
  input_tensors: list,
  body_code_stmts: list,
  dim_instance_generator: DimInstanceGenerator
):
  template = _GetTemplate("template_paddle_unittest.py")
  input_arg_names = [
    input_tensor.name for input_tensor in input_tensors
  ]
  def GetShapeInstanceFromDimExprs(tensor):
    if type(tensor.dim_exprs) is not ir_symbol.TensorShapeOrDataDimExprs:
      return []
    return [
      dim_instance_generator.GetDimInstance(dim_expr)
      for dim_expr in tensor.dim_exprs.shape
    ]
  def GetData(tensor):
    return None
  def GetBigType(tensor):
    if GetData(tensor) is not None:
      return "dim"
    return type2bigger_type[tensor.dtype]
  input_tensor_descs = [
    InputTensorMeta(
      shape=GetShapeInstanceFromDimExprs(input_tensor),
      dtype=input_tensor.dtype,
      big_dtype=GetBigType(input_tensor),
      data=GetData(input_tensor),
      min=getattr(InitMinGetter, input_tensor.dtype)(),
      max=getattr(InitMaxGetter, input_tensor.dtype)(),
    )
    for input_tensor in input_tensors
  ]
  input_spec_shape_dtypes = [
    InputSpecDesc(
      shape=[(dim if dim >= 0 else None) for dim in input_tensor.shape],
      dtype=input_tensor.dtype
    )
    for input_tensor in input_tensors
  ]
  return template.render(
    stmts=list(enumerate(body_code_stmts)),
    unittest_class_name=unittest_class_name,
    input_arg_names=input_arg_names,
    input_tensor_descs=input_tensor_descs,
    input_spec_shape_dtypes=input_spec_shape_dtypes,
  )

def _GetTemplate(template_name):
  dir_path = os.path.dirname(os.path.realpath(__file__))
  with open(f"{dir_path}/{template_name}", "r") as f:
    return Template(f.read())


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

