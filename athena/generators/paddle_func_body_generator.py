from athena.ir_converters.paddle_op_converter import ConvertToPaddleOp
from athena.ir_converters.paddle_tensor_converter import ConvertToPaddleTensor
from athena.generators.paddle_op_call_generator import PaddleOpCallGenerator
from athena.generators.global_tensor_converter import GlobalTensorConverter
from dataclasses import dataclass
from typing import List, Union

from athena.util.tensor_topo import GetOpId2TensorNamesUsedByDownstream
from athena.generators.block_name_generator import BlockNameGenerator
from athena.util.input_output_tensors_extractor import InputOutputTensorsExtractor

@dataclass
class IndentedPyCode:
  pycode: str
  num_tabs: int

@dataclass
class PyCodeStmt:
  op_name: str
  pycode: List[IndentedPyCode]
  inputs_type_strs: List[str]
  outputs_type_strs: List[str]
  inputs_shape_symbol_strs: List[str]
  outputs_shape_symbol_strs: List[str]
  inputs_data_symbol_strs: List[str]
  outputs_data_symbol_strs: List[str]
  tensors_used_by_downstream: List[str]

class PaddleFuncBodyGenerator:
  def __init__(self, func, block_name_generator: BlockNameGenerator = None):
    self.func = func
    self.input_output_tensors_extractor = InputOutputTensorsExtractor(func)
    self.block_name_generator = (
      block_name_generator if block_name_generator is not None else None
    )
    self.stmts : List[PyCodeStmt] = []
    self.op_call_generator = PaddleOpCallGenerator()
    self.tensor_converter = GlobalTensorConverter()
    self.op_id2used_by_downstream = {}
    self.output_local_tensors = []

  def Generate(self, free_vars, args):
    def get_local_name(tensor):
      return self.tensor_converter.ConvertToLocalTensor(tensor).name
    self.op_id2used_by_downstream = GetOpId2TensorNamesUsedByDownstream(
      self.func, free_vars, args, get_local_name
    )
    self.func(self, *free_vars)(*args)
    input_tensors, output_tensors = self.input_output_tensors_extractor.Extract(
      free_vars,
      args
    )
    input_local_tensors = [
      self.tensor_converter.ConvertToLocalTensor(tensor)
      for tensor in input_tensors
    ]
    output_local_tensors = [
      self.tensor_converter.ConvertToLocalTensor(tensor)
      for tensor in output_tensors
    ]
    return input_local_tensors, self.stmts, output_local_tensors

  def __call__(self, op, *input_tensors, **kwargs):
    if hasattr(self, op.GetPyVarName()): 
      return getattr(self, op.GetPyVarName())(op, *input_tensors, **kwargs)
    return self.CollectPyCodeStmt(self.GetStmtPyCode, op, *input_tensors, **kwargs)

  def builtin_split(self, op, x):
    def GetStmtPyCode(local_output_tensor_names, op, x):
      output_unpack_str = ", ".join(local_output_tensor_names)
      pycode = f"{output_unpack_str}, = {x.name}"
      return [IndentedPyCode(pycode=pycode, num_tabs=0)]
    return self.CollectPyCodeStmt(GetStmtPyCode, op, x)

  def CollectPyCodeStmt(self, GetStmtPyCode, op, *input_tensors, **kwargs):
    assert len(kwargs) == 0
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
    input_local_tensors = [
      self.tensor_converter.ConvertToLocalTensor(input_tensor)
      for input_tensor in input_tensors
    ]
    local_output_tensor_names = [
      self.tensor_converter.ConvertToLocalTensor(output_tensor).name
      for output_tensor in op.GetResults()
    ]
    pycode = GetStmtPyCode(local_output_tensor_names, op, *input_local_tensors)
    if pycode is None:
      return op.GetResults()
    self.stmts.append(PyCodeStmt(
      op_name=op.name,
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

  def GetStmtPyCode(self, local_output_tensor_names, op, *input_local_tensors):
    local_output_unpack_str = ", ".join(local_output_tensor_names)
    local_op_call_expr = self.op_call_generator.GenerateOpCall(op, *input_local_tensors)
    if local_op_call_expr is None:
      pycode = None 
    elif len(local_output_tensor_names) == 0:
      pycode = f"{local_op_call_expr}"
    else:
      pycode = f"{local_output_unpack_str} = {local_op_call_expr}"
    return [IndentedPyCode(pycode=pycode, num_tabs=0)]