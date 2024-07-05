from dataclasses import dataclass
from athena.ir_converters.paddle_op_converter import ConvertToPaddleOp
from athena.ir_converters.paddle_tensor_converter import ConvertToPaddleTensor
from athena.ir_converters.paddle_type_converter import ConvertTypeToString
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
import typing as t

InputSpecDesc = namedtuple("InputSpecDesc", [
  "shape",
  "dtype",
])

@dataclass
class TensorId:
  pass

@dataclass
class NullTensorId(TensorId):
  pass

@dataclass
class OperandTensorId(TensorId):
  operand_tensor_idx: int

@dataclass
class TensorListMemberId(TensorId):
  operand_tensor_list_idx: int
  tensor_list_member_idx: int

@dataclass
class OperandId:
  operand_idx: int

  def get_operand_tensor_id(self, op: "Op") -> t.Optional[OperandTensorId]:
    input_type = op.input_types[self.operand_idx]
    if not isinstance(input_type, ir_type.DenseTensorType):
      return None
    return OperandTensorId(self.operand_idx)

  def get_null_tensor_id(self, op: "Op") -> t.Optional[NullTensorId]:
    input_type = op.input_types[self.operand_idx]
    if not isinstance(input_type, ir_type.NullType):
      return None
    return NullTensorId()
    
  def get_tensor_list_member_ids(
    self,
    op: "Op"
  ) -> t.Optional[t.List[TensorListMemberId]]:
    input_type = op.input_types[self.operand_idx]
    if not isinstance(input_type, ir_type.VectorType):
      return None
    return [
      TensorListMemberId(
        operand_tensor_list_idx=self.operand_idx,
        tensor_list_member_idx=i,
      )
      for i in range(len(input_type.value))
    ]

@dataclass
class PrimitiveOpStmt:
  op_expr: str
  tensor_ids: t.List[TensorId]
  operand_ids: t.List[OperandId]
  operand_tensor_id4operand_id: t.Callable[OperandId, t.Optional[OperandTensorId]]
  null_tensor_id4operand_id: t.Callable[OperandId, t.Optional[NullTensorId]]
  tensor_list_member_ids4operand_id: t.Callable[OperandId,
                                                t.Optional[t.List[TensorListMemberId]]]
  tensor_name4tensor_id: t.Callable[TensorId, str]
  tensor_name4operand_id: t.Callable[OperandId, str]
  input_spec_shape_dtype4tensor_id: t.Callable[TensorId, InputSpecDesc]
  example_input_meta4tensor_id: t.Callable[TensorId, InputTensorDesc]
  example_input_data4operand_id: t.Callable[OperandId, t.Optional[t.List[int]]]
  immediate_value4operand_id: t.Callable[[OperandId, t.Any], t.Any]

class ConstraintUnittestsGenerator:

  def __init__(self, op_example_inputs_meta_getter):
    self.input_spec_modes = ['pure_dynamic']
    self.op_example_inputs_meta_getter = op_example_inputs_meta_getter
    self.graph_input_tensor_name_prefix = "arg"
    self.paddle_op_call_generator = PaddleOpCallGenerator()

  def Generate(self, uid_and_ops):
    valid_operand_types = (ir_type.DenseTensorType, ir_type.NullType, ir_type.VectorType)
    ops = [
      PrimitiveOpStmt(
        tensor_ids=self.GetTensorIds(program_id, op),
        operand_ids=self.GetOperandIds(op),
        operand_tensor_id4operand_id=self.MakeOperandTensorId4OperandId(op),
        null_tensor_id4operand_id=self.MakeNullTensorId4OperandId(op),
        tensor_list_member_ids4operand_id=self.MakeTensorListMemberIds4OperandId(op),
        op_expr=self.GetOpExpr(program_id, op),
        tensor_name4tensor_id=self.MakeTensorName4TensorId(op),
        tensor_name4operand_id=self.MakeTensorName4OperandId(op),
        input_spec_shape_dtype4tensor_id=self.MakeInputSpecShapeAndDtype4TensorId(
          input_spec_mode=input_spec_mode,
          program_id=program_id,
          op=op,
        ),
        example_input_meta4tensor_id=self.MakeExampleInputsMeta4TensorId(
          program_id=program_id,
          op=op,
        ),
        example_input_data4operand_id=self.MakeExampleInputData4OperandId(
          program_id=program_id,
          op=op,
        ),
        immediate_value4operand_id=self.MakeImmediateValue4OperandId(op),
      )
      for input_spec_mode in self.input_spec_modes
      for program_id, op in uid_and_ops
      if self.op_example_inputs_meta_getter.HasAllInputs(
        program_id, op.op_id, num_inputs=len(op.input_types)
      )
      if all(
        isinstance(input_type, valid_operand_types)
        for input_type in op.input_types
      )
      if all(
        isinstance(output_type, valid_operand_types)
        for output_type in op.output_types
      )
    ]
    return self._RenderTemplate(ops)

  def MakeImmediateValue4OperandId(self, op):
    def ImmediateValue4OperandId(operand_id, data):
      return self.GetImmediateValue4OperandId(op, operand_id, data)
    return ImmediateValue4OperandId

  def GetImmediateValue4OperandId(self, op, operand_id, data):
    if data is None:
      return None
    cpp_type_name = self.GetCppOperandTypeName(op, operand_id.operand_idx)
    if cpp_type_name == 'IntArray':
      if op.name == 'pd_op.reshape':
        if any(dim < 0 for dim in data):
          return data
        else:
          return None
      else:
        return data
    if cpp_type_name == 'Scalar[]':
      return data
    if cpp_type_name in {'Scalar', 'Scalar(int)', 'Scalar(int64_t)', 'Scalar(float)', 'Scalar(double)'}:
      if isinstance(data, list):
        return data[0]
      else:
        return data
    return None
  
  def MakeExampleInputsMeta4TensorId(self, program_id, op):
    return lambda tensor_id: self.GetExampleInputsMeta4TensorId(
      program_id=program_id,
      op=op,
      tensor_id=tensor_id,
    )

  def GetExampleInputsMeta4TensorId(self, program_id, op, tensor_id):
    if isinstance(tensor_id, NullTensorId):
      return None
    if isinstance(tensor_id, OperandTensorId):
      return self.GetExampleInputsMeta(
        program_id=program_id,
        op=op,
        input_idx=tensor_id.operand_tensor_idx,
      )
    if isinstance(tensor_id, TensorListMemberId):
      tensor_meta = self.GetExampleTensorMeta(
        program_id=program_id,
        op=op,
        input_idx=tensor_id.operand_tensor_list_idx,
      )
      input_type = op.input_types[tensor_id.operand_tensor_list_idx]
      dtype = input_type.value[tensor_id.tensor_list_member_idx].dtype
      return MakeInputTensorDesc(
        shape=tensor_meta.shape[tensor_id.tensor_list_member_idx],
        dtype=ConvertTypeToString(dtype),
        data=tensor_meta.data[tensor_id.tensor_list_member_idx],
      )
    raise NotImplementedError()

  def IsOperandImmediateValue(self, program_id, op, operand_id):
    data = self.GetExampleTensorMeta(
      program_id=program_id,
      op=op,
      input_idx=operand_id.operand_idx,
    ).input_idx
    if data is None:
      return False
    immediate_value = self.GetImmediateValue4OperandId(op, operand_id, data)
    return immediate_value is not None

  def MakeExampleInputData4OperandId(self, program_id, op):
    return lambda operand_id: self.GetExampleTensorMeta(
      program_id=program_id,
      op=op,
      input_idx=operand_id.operand_idx,
    ).data

  def MakeInputSpecShapeAndDtype4TensorId(self, input_spec_mode, program_id, op):
    return lambda tensor_id: self.InputSpecShapeAndDtype4TensorId(
      input_spec_mode=input_spec_mode,
      program_id=program_id,
      op=op,
      tensor_id=tensor_id,
    )

  def InputSpecShapeAndDtype4TensorId(
    self,
    input_spec_mode,
    program_id,
    op,
    tensor_id,
  ):
    if isinstance(tensor_id, NullTensorId):
      return None
    elif isinstance(tensor_id, OperandTensorId):
      return self.InputSpecShapeAndDtype4OperandId(
        input_spec_mode=input_spec_mode,
        program_id=program_id,
        op=op,
        operand_id=OperandId(tensor_id.operand_tensor_idx)
      )
    elif isinstance(tensor_id, TensorListMemberId):
      operand_spec = self.InputSpecShapeAndDtype4OperandId(
        input_spec_mode=input_spec_mode,
        program_id=program_id,
        op=op,
        operand_id=OperandId(tensor_id.operand_tensor_list_idx)
      )
      return InputSpecDesc(
        shape=operand_spec.shape[tensor_id.tensor_list_member_idx],
        dtype=operand_spec.dtype[tensor_id.tensor_list_member_idx],
      )
    else:
      raise NotImplementedError()

  def InputSpecShapeAndDtype4OperandId(
    self,
    input_spec_mode,
    program_id,
    op,
    operand_id,
  ):
    input_idx = operand_id.operand_idx
    tensor = self.GetOpOperandTensors(op)[input_idx]
    if isinstance(tensor.type, ir_type.DenseTensorType):
      def GetShape():
        if input_spec_mode == "pure_dynamic":
          return [None for _ in tensor.shape]
        else:
          raise NotImplementedError
      dtype = tensor.dtype
    elif isinstance(tensor.type, ir_type.VectorType):
      def GetShape():
        if input_spec_mode == "pure_dynamic":
          return [[None for _ in t.shape] for t in tensor.type.value]
        else:
          raise NotImplementedError
      dtype = [x.dtype for x in tensor.type.value]
    else:
      dtype = None
    return InputSpecDesc(
      shape=GetShape(),
      dtype=dtype,
    )

  def MakeTensorName4OperandId(self, op):
    operand_tensors = self.GetOpOperandTensors(op)
    return lambda operand_id: operand_tensors[operand_id.operand_idx].name
  
  def MakeTensorName4TensorId(self, op):
    def TensorName4TensorId(tensor_id):
      if isinstance(tensor_id, NullTensorId):
        return "None"
      if isinstance(tensor_id, OperandTensorId):
        return f"{self.graph_input_tensor_name_prefix}_{tensor_id.operand_tensor_idx}"
      if isinstance(tensor_id, TensorListMemberId):
        i = tensor_id.operand_tensor_list_idx
        j = tensor_id.tensor_list_member_idx
        return f"{self.graph_input_tensor_name_prefix}_{i}_{j}"
    return TensorName4TensorId

  def MakeTensorListMemberIds4OperandId(self, op):
    return lambda operand_id: operand_id.get_tensor_list_member_ids(op)

  def MakeNullTensorId4OperandId(self, op):
    return lambda operand_id: operand_id.get_null_tensor_id(op)

  def MakeOperandTensorId4OperandId(self, op):
    return lambda operand_id: operand_id.get_operand_tensor_id(op)

  def GetOperandIds(self, op):
    return [OperandId(i) for i in range(len(op.input_types))]

  def GetTensorIds(self, program_id, op):
    def YieldOpOperandTensorId(input_idx):
      input_type = op.input_types[input_idx]
      if isinstance(input_type, ir_type.NullType):
        yield from []
      elif isinstance(input_type, ir_type.DenseTensorType):
        if not self.IsOperandImmediateValue(program_id, op, OperandId(input_idx)):
          yield OperandTensorId(input_idx)
      elif isinstance(input_type, ir_type.VectorType):
        yield from (
          TensorListMemberId(
            operand_tensor_list_idx=input_idx,
            tensor_list_member_idx=i,
          )
          for i in range(len(input_type.value))
        )
      else:
        raise NotImplementedError()
    return [
      tensor_id
      for input_idx in range(len(op.input_types))
      for tensor_id in YieldOpOperandTensorId(input_idx)
    ]


  def GetOpExpr(self, program_id, op):
    op = ConvertToPaddleOp(op)
    input_tensors = self.GetOpOperandTensors(op)
    return self.paddle_op_call_generator.GenerateOpCall(op, *input_tensors)

  def GetInputSpecShapeAndDtype(self, input_spec_mode, program_id, op):
    if input_spec_mode == "pure_dynamic":
      def GetInputSpecShape(input_idx, tensor):
        return [None for _ in tensor.shape]
    else:
      raise NotImplementedError
    return [
      InputSpecDesc(
        shape=GetInputSpecShape(input_idx, tensor),
        dtype=tensor.dtype,
      )
      for input_idx, tensor in enumerate(self.GetOpOperandTensors(op))
    ]

  def GetExampleTensorMeta(self, program_id, op, input_idx):
    return self.op_example_inputs_meta_getter.Get(
      program_id,
      op.op_id,
      input_idx
    )
  
  def GetExampleInputsMeta(self, program_id, op, input_idx):
    tensor_meta = self.GetExampleTensorMeta(program_id, op, input_idx)
    input_type = op.input_types[input_idx]
    if not isinstance(input_type, ir_type.DenseTensorType):
      raise NotImplementedError()
    dtype = ConvertTypeToString(input_type.dtype)
    return MakeInputTensorDesc(
      shape=tensor_meta.shape,
      dtype=dtype,
      data=tensor_meta.data,
    )

  def GetOpOperandTensors(self, op):
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
    template = self._GetTemplate("template_constraint_unittest.py")
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
      cache=lambda x: empty_str(cached_test_class_names.add(x)),
      PADDLE_DEBUG_ENABLE_CINN=PADDLE_DEBUG_ENABLE_CINN,
    )

  def GetCppOperandTypeName(self, op, input_idx):
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