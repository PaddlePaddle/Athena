from athena.ir_converters.paddle_op_converter import ConvertToPaddleOp
from athena.ir_converters.paddle_tensor_converter import ConvertToPaddleTensor
from athena.generators.paddle_op_call_generator import PaddleOpCallGenerator
from athena.generators.global_tensor_converter import GlobalTensorConverter
from athena.util.name_generator import NameGenerator
from dataclasses import dataclass
from typing import List, Union
from athena.generators.block_name_generator import BlockNameGenerator
from athena.util.tensor_topo import (
  GetOpId2TensorNamesUsedByMeAndDownstream,
  GetOpId2OpPipeInOutNamesSignature,
  OpPipeInOutNamesSignature
)
from athena.generators.block_name_generator import BlockNameGenerator
from athena.util.input_output_tensors_extractor import InputOutputTensorsExtractor
from athena.util.block_op_calls_extractor import BlockOpCallsExtractor

@dataclass
class IndentedPyCode:
  pycode: str
  num_tabs: int

@dataclass
class PyCodeStmt:
  op_name: str
  op_unique_local_name: str
  pycode: List[IndentedPyCode]
  inputs_type_strs: List[str]
  outputs_type_strs: List[str]
  inputs_shape_symbol_strs: List[str]
  outputs_shape_symbol_strs: List[str]
  inputs_data_symbol_strs: List[str]
  outputs_data_symbol_strs: List[str]
  tensors_used_by_me_and_downstream: List[str]
  op_func_in_out_names_signature: OpPipeInOutNamesSignature

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
    self.op_name_generator = NameGenerator()
    self.op_id2used_by_me_and_downstream = {}
    self.output_local_tensors = []

  def Generate(self, free_vars, args):
    def get_local_name(tensor):
      if tensor is None:
        return None
      return self.tensor_converter.ConvertToLocalTensor(tensor).name
    self.op_id2used_by_me_and_downstream = GetOpId2TensorNamesUsedByMeAndDownstream(
      self.func, free_vars, args, get_local_name
    )
    self.op_id2op_func_in_out_names_signature = GetOpId2OpPipeInOutNamesSignature(
      self.func, free_vars, args, get_local_name
    )
    block_op_calls = BlockOpCallsExtractor().Extract(self.func, free_vars, args)
    for op_call in block_op_calls.body_op_calls:
      self(op_call.op, *op_call.input_tensors, **op_call.kwargs)
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
    op_py_varname = op.GetPyVarName()
    if hasattr(self, op_py_varname):
      return getattr(self, op_py_varname)(op, *input_tensors, **kwargs)
    stmts_method_name = f"get_stmts_{op_py_varname}"
    get_stmts = (
      getattr(self, stmts_method_name)
      if hasattr(self, stmts_method_name)
      else self.GetStmtPyCode
    )
    return self.CollectPyCodeStmt(get_stmts, op, *input_tensors, **kwargs)

  def get_stmts_builtin_split(self, local_output_tensor_names, op, x):
    output_unpack_str = ", ".join(local_output_tensor_names)
    return [self.Indent0(f"{output_unpack_str}, = {x.name}")]

  def get_stmts_pd_op_while(
    self,
    local_output_tensor_names,
    op,
    *local_input_tensors,
    **kwargs,
  ):
    block_func, *free_vars = kwargs["blocks"][0][0]
    cond, *args = local_input_tensors
    free_vars = [self.tensor_converter.ConvertToLocalTensor(t) for t in free_vars]
    output_unpack_str = ", ".join(local_output_tensor_names)
    input_var_str = ", ".join(t.name for t in local_input_tensors)
    block_name = BlockNameGenerator().Generate(op, region_idx=0, block_idx=0)
    block_args_str = ", ".join(t.name for t in [*free_vars, *local_input_tensors])
    arg_str = ", ".join(t.name for t in args)
    return [
      self.Indent0(f"while {cond.name}:"),
      self.Indent1(f"{input_var_str}, = self.{block_name}({block_args_str})"),
      self.Indent0(f"{output_unpack_str}, = {arg_str},"),
    ]

  def Indent0(self, pycode):
    return IndentedPyCode(pycode=pycode, num_tabs=0)

  def Indent1(self, pycode):
    return IndentedPyCode(pycode=pycode, num_tabs=1)

  def CollectPyCodeStmt(self, GetStmtPyCode, op, *input_tensors, **kwargs):
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
    stmts = GetStmtPyCode(local_output_tensor_names, op, *input_local_tensors, **kwargs)
    if len(stmts) == 0:
      return op.GetResults()
    self.stmts.append(PyCodeStmt(
      op_name=op.name,
      op_unique_local_name=self.op_name_generator.Generate(
        key=op.op_id,
        prefix=f"op_{op.GetNameSuffix()}",
      ),
      inputs_type_strs=inputs_type_strs,
      outputs_type_strs=outputs_type_strs,
      inputs_shape_symbol_strs=inputs_shape_symbol_strs,
      outputs_shape_symbol_strs=outputs_shape_symbol_strs,
      inputs_data_symbol_strs=inputs_data_symbol_strs,
      outputs_data_symbol_strs=outputs_data_symbol_strs,
      pycode=stmts,
      tensors_used_by_me_and_downstream=self.op_id2used_by_me_and_downstream[op.op_id],
      op_func_in_out_names_signature=self.op_id2op_func_in_out_names_signature[op.op_id],
    ))
    return op.GetResults()

  def GetStmtPyCode(self, local_output_tensor_names, op, *input_local_tensors, **kwargs):
    assert len(kwargs) == 0
    local_output_unpack_str = ", ".join(local_output_tensor_names)
    local_op_call_expr = self.op_call_generator.GenerateOpCall(op, *input_local_tensors)
    if local_op_call_expr is None:
      return [] 
    elif len(local_output_tensor_names) == 0:
      pycode = f"{local_op_call_expr}"
    else:
      pycode = f"{local_output_unpack_str} = {local_op_call_expr}"
    return [IndentedPyCode(pycode=pycode, num_tabs=0)]