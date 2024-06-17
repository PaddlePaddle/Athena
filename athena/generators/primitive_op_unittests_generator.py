from dataclasses import dataclass
from athena.ir_converters.paddle_op_converter import ConvertToPaddleOp
from athena.ir_converters.paddle_tensor_converter import ConvertToPaddleTensor
from athena.generators.paddle_op_call_generator import PaddleOpCallGenerator
import typing as t
from athena.util.input_tensor_desc import (
  InputTensorDesc,
  MakeInputTensorDesc
)
import athena.ir.ir_type as ir_type
import athena.ir.ir_tensor as ir_tensor
import athena.ir.ir_symbol as ir_symbol
from collections import namedtuple
import os
from jinja2 import Template
import hashlib

InputSpecDesc = namedtuple("InputSpecDesc", [
  "shape",
  "dtype",
])

@dataclass
class PrimitiveOpStmt:
  op_expr: str
  input_tensor_names: t.List[str]
  input_spec_shape_dtypes: t.List[InputSpecDesc]
  example_inputs_meta: t.List[InputTensorDesc]

class PrimitiveOpUnittestsGenerator:

  def __init__(self, is_dynamic, op_example_inputs_meta_getter):
    self.is_dynamic = is_dynamic
    self.op_example_inputs_meta_getter = op_example_inputs_meta_getter
    self.paddle_op_call_generator = PaddleOpCallGenerator()

  def Generate(self, uid_and_ops):
    ops = [
      PrimitiveOpStmt(
        op_expr=self.GetOpExpr(programd_id, op),
        input_tensor_names=self.GetInputTensorNames(programd_id, op),
        input_spec_shape_dtypes=self.GetInputSpecShapeAndDtype(programd_id, op),
        example_inputs_meta=self.GetExampleInputsMeta(programd_id, op)
      )
      for programd_id, op in uid_and_ops
      if self.op_example_inputs_meta_getter.HasAllInputs(
        programd_id, op.op_id, num_inputs=len(op.input_types)
      )
      if all(
        type(input_type) is ir_type.DenseTensorType
        for input_type in op.input_types
      )
      if all(
        type(output_type) is ir_type.DenseTensorType
        for output_type in op.output_types
      )
    ]
    return self._RenderTemplate(ops)

  def GetOpExpr(self, programd_id, op):
    op = ConvertToPaddleOp(op)
    input_tensors = self.GetInputTensors(op)
    return self.paddle_op_call_generator.GenerateOpCall(op, *input_tensors)

  def GetInputTensorNames(self, programd_id, op):
    return [t.name for t in self.GetInputTensors(op)]
  
  def GetInputSpecShapeAndDtype(self, programd_id, op):
    def GetInputSpecShape(input_idx):
      example_tensor_meta = self.GetExampleTensorMeta(programd_id, op, input_idx)
      shape = example_tensor_meta.shape
      return [None for _ in shape] if self.is_dynamic else shape
    return [
      InputSpecDesc(
        shape=GetInputSpecShape(input_idx),
        dtype=tensor.dtype
      )
      for input_idx, tensor in enumerate(self.GetInputTensors(op))
    ]

  def GetExampleTensorMeta(self, programd_id, op, input_idx):
    return self.op_example_inputs_meta_getter.Get(
      programd_id,
      op.op_id,
      input_idx
    )
  
  def GetExampleInputsMeta(self, programd_id, op):
    def GetExampleTensorMeta(input_idx):
      return self.GetExampleTensorMeta(programd_id, op, input_idx)
    return [
      MakeInputTensorDesc(
        input_tensor,
        lambda t: GetExampleTensorMeta(input_idx).shape,
        lambda t: GetExampleTensorMeta(input_idx).data,
      )
      for input_idx, input_tensor in enumerate(self.GetInputTensors(op))
    ]

  def GetInputTensors(self, op):
    return [
      ConvertToPaddleTensor(
        ir_tensor.Tensor(
          local_name_prefix="in_",
          name=f"input_{input_idx}",
          arg_name_as_input=None,
          defining_op_name=None,
          type=input_type,
          dim_exprs=ir_symbol.NullShapeOrDataDimExprs()
        )
      )
      for input_idx, input_type in enumerate(op.input_types)
    ]
  
  def _RenderTemplate(self, ops):
    template = self._GetTemplate("template_primitive_op_unittest.py")
    cached_test_class_names = set()
    empty_str = lambda x:""
    return template.render(
      ops=ops,
      get_sha_hash_prefix=lambda x: GetSha256sum(x)[0:32],
      is_cached_before=lambda x: x in cached_test_class_names,
      cache=lambda x: empty_str(cached_test_class_names.add(x))
    )

  def _GetTemplate(self, template_name):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(f"{dir_path}/{template_name}", "r") as f:
      return Template(f.read())

def GetSha256sum(content):
  m = hashlib.sha256()
  m.update(content.encode())
  return m.hexdigest()