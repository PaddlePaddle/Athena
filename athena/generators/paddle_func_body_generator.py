from athena.ir_converters.paddle_op_converter import ConvertToPaddleOp
from athena.generators.paddle_op_call_generator import PaddleOpCallGenerator
from athena.generators.global_tensor_converter import GlobalTensorConverter
from dataclasses import dataclass
from typing import List

from athena.util.tensor_topo import GetOpId2TensorNamesUsedByDownstream

@dataclass
class PyCodeStmt:
  pycode: str
  inputs_type_strs: List[str]
  outputs_type_strs: List[str]
  inputs_shape_symbol_strs: List[str]
  outputs_shape_symbol_strs: List[str]
  inputs_data_symbol_strs: List[str]
  outputs_data_symbol_strs: List[str]
  tensors_used_by_downstream: List[str]

class PaddleFuncBodyGenerator:
  def __init__(self, func):
    self.func = func
    self.stmts : List[PyCodeStmt] = []
    self.op_call_generator = PaddleOpCallGenerator()
    self.tensor_converter = GlobalTensorConverter()
    self.op_id2used_by_downstream = {}

  def Generate(self, input_tensors):
    local_input_tensors = [
      self.tensor_converter.ConvertToLocalTensor(input_tensor)
      for input_tensor in input_tensors
    ]
    def get_local_name(tensor):
      return self.tensor_converter.ConvertToLocalTensor(tensor).name
    self.op_id2used_by_downstream = GetOpId2TensorNamesUsedByDownstream(
      self.func, input_tensors, get_local_name
    )
    self.func(self, *input_tensors)
    return local_input_tensors, self.stmts

  def cinn_op_fusion(self, op, blocks):
    block_func, *free_vars = blocks[0][0]
    return block_func(self, *free_vars)()

  def __call__(self, op, *input_tensors, **kwargs):
    if len(kwargs) > 0:
      return getattr(self, op.GetPyVarName())(op, *input_tensors, **kwargs)
    outputs_type_strs = [t.GetShortStr() for t in op.output_types]
    inputs_type_strs = [t.GetShortStr() for t in op.input_types]
    outputs_shape_symbol_strs = [
      s.value.GetShapeShortStr()
      for s in op.__results_symbols_signature__.value
    ]
    inputs_shape_symbol_strs = [
      s.value.GetShapeShortStr()
      for s in op.__operands_symbols_signature__.value
    ]
    outputs_data_symbol_strs = [
      s.value.GetDataShortStr()
      for s in op.__results_symbols_signature__.value
    ]
    inputs_data_symbol_strs = [
      s.value.GetDataShortStr()
      for s in op.__operands_symbols_signature__.value
    ]
    op = ConvertToPaddleOp(op)
    local_input_tensors = [
      self.tensor_converter.ConvertToLocalTensor(input_tensor)
      for input_tensor in input_tensors
    ]
    local_output_tensor_names = [
      self.tensor_converter.ConvertToLocalTensor(output_tensor).name
      for output_tensor in op.GetResults()
    ]
    local_output_unpack_str = ", ".join(local_output_tensor_names)
    local_op_call_expr = self.op_call_generator.GenerateOpCall(op, *local_input_tensors)
    if local_op_call_expr is None:
      pass 
    elif len(local_output_tensor_names) == 0:
      pycode = f"{local_op_call_expr}"
    else:
      pycode = f"{local_output_unpack_str} = {local_op_call_expr}"
    self.stmts.append(PyCodeStmt(
      inputs_type_strs=inputs_type_strs,
      outputs_type_strs=outputs_type_strs,
      inputs_shape_symbol_strs=inputs_shape_symbol_strs,
      outputs_shape_symbol_strs=outputs_shape_symbol_strs,
      inputs_data_symbol_strs=inputs_data_symbol_strs,
      outputs_data_symbol_strs=outputs_data_symbol_strs,
      pycode=pycode,
      tensors_used_by_downstream=self.op_id2used_by_downstream[op.op_id],
    ))
    return op.GetResults()