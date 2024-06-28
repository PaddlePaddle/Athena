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
from athena.generators.paddle_c_ops_arg_names import op_name2args

InputSpecDesc = namedtuple("InputSpecDesc", [
  "shape",
  "dtype",
])

@dataclass
class PrimitiveOpStmt:
  op: "Op"
  op_expr: str
  input_tensor_names: t.List[str]
  input_spec_shape_dtypes: t.List[InputSpecDesc]
  example_inputs_meta: t.List[InputTensorDesc]

class PrimitiveOpUnittestsGenerator:

  def __init__(self, input_spec_mode, op_example_inputs_meta_getter):
    self.input_spec_modes = [input_spec_mode] if input_spec_mode != "all" else [
      "original", "pure_static", "pure_dynamic"
    ]
    self.op_example_inputs_meta_getter = op_example_inputs_meta_getter
    self.paddle_op_call_generator = PaddleOpCallGenerator()

  def Generate(self, uid_and_ops):
    ops = [
      PrimitiveOpStmt(
        op=op,
        op_expr=self.GetOpExpr(programd_id, op),
        input_tensor_names=self.GetInputTensorNames(programd_id, op),
        input_spec_shape_dtypes=self.GetInputSpecShapeAndDtype(
          input_spec_mode=input_spec_mode,
          programd_id=programd_id,
          op=op,
        ),
        example_inputs_meta=self.GetExampleInputsMeta(programd_id, op)
      )
      for input_spec_mode in self.input_spec_modes
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
  
  def GetInputSpecShapeAndDtype(self, input_spec_mode, programd_id, op):
    if input_spec_mode == "original":
      def GetInputSpecShape(input_idx, tensor):
        return [(dim if dim >= 0 else None) for dim in tensor.shape]
    elif input_spec_mode == "pure_dynamic":
      def GetInputSpecShape(input_idx, tensor):
        return [None for _ in tensor.shape]
    elif input_spec_mode == "pure_static":
      def GetInputSpecShape(input_idx, tensor):
        return self.GetExampleTensorMeta(programd_id, op, input_idx).shape
    else:
      raise NotImplementedError
    return [
      InputSpecDesc(
        shape=GetInputSpecShape(input_idx, tensor),
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
    PADDLE_DEBUG_ENABLE_CINN = os.getenv('PADDLE_DEBUG_ENABLE_CINN') not in {
        "0",
        "False",
        "false",
        "OFF",
    }
    return template.render(
      ops=ops,
      get_sha_hash_prefix=lambda x: GetSha256sum(x)[0:32],
      is_cached_before=lambda x: x in cached_test_class_names,
      get_pos_arg_type_name=self.GetPosArgTypeName,
      cache=lambda x: empty_str(cached_test_class_names.add(x)),
      PADDLE_DEBUG_ENABLE_CINN=PADDLE_DEBUG_ENABLE_CINN,
    )

  def GetPosArgTypeName(self, op_stmt, input_idx):
    op = op_stmt.op
    op_name = op.GetValidPyVarNameComponents()[-1]
    if op_name not in op_name2args:
      return False
    args = op_name2args[op_name]
    pos_arg_type_names = [
      type_name
      for type_name, arg_name in args
      if arg_name not in op.attrs
    ]
    assert input_idx < len(pos_arg_type_names), f"op.name:{op.name}, args:{args}"
    type_name = pos_arg_type_names[input_idx]
    return type_name

  def _GetTemplate(self, template_name):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(f"{dir_path}/{template_name}", "r") as f:
      return Template(f.read())

def GetSha256sum(content):
  m = hashlib.sha256()
  m.update(content.encode())
  return m.hexdigest()