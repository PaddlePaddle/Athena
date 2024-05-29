from typing import Dict, List
from collections import OrderedDict
from dataclasses import dataclass
import sys
from athena.util.input_output_tensors_extractor import InputOutputTensorsExtractor
from athena.util.block_op_calls_extractor import BlockOpCallsExtractor

@dataclass
class OpInpOutNameSignature:
  op_id : int
  in_names: List[str]
  out_names: List[str]

@dataclass
class OpPipeInOutNamesSignature:
  op_id : int
  in_names: List[str]
  out_names: List[str]

def GetOpId2OpPipeInOutNamesSignature(
  func,
  free_vars,
  args,
  get_local_name,
) -> Dict[int, OpPipeInOutNamesSignature]:
  op_id2used = GetOpId2TensorNamesUsedByMeAndDownstream(
    func, free_vars, args, get_local_name
  )
  extractor = InputOutputTensorsExtractor(func)
  input_tensors, output_tensors = extractor.Extract(free_vars, args)
  def get_in_names_list():
    in_names_list = [
      names_used_by_me_and_downstream
      for _, names_used_by_me_and_downstream in op_id2used.items()
    ]
    in_names_list[0] = [get_local_name(t) for t in input_tensors]
    return in_names_list

  def get_out_names_list():
    out_names_list = [
      names_used_by_me_and_downstream
      for _, names_used_by_me_and_downstream in op_id2used.items()
    ]
    out_names_list = out_names_list[1:]
    out_names_list += [get_local_name(t) for t in output_tensors]
    return out_names_list

  def get_op_id_list():
    return [op_id for op_id, _ in op_id2used.items()]
    
  op_id2op_pipe_in_out_names_sig = OrderedDict()
  tuple_list = zip(get_op_id_list(), get_in_names_list(), get_out_names_list())
  for op_id, in_names, out_names in tuple_list:
    op_id2op_pipe_in_out_names_sig[op_id] = OpPipeInOutNamesSignature(
      op_id=op_id,
      in_names=in_names,
      out_names=out_names,
    )
  return op_id2op_pipe_in_out_names_sig

def GetOpId2TensorNamesUsedByMeAndDownstream(
  func,
  free_vars,
  args,
  get_local_name,
) -> Dict[int, List[str]]:
  in_out_name_sig_extractor = OpInOutNameSignatureExtractor(get_local_name)
  in_out_names_sigs = in_out_name_sig_extractor.Extract(func, free_vars, args)
  input_tensors, output_tensors = InputOutputTensorsExtractor(func).Extract(free_vars, args)
  output_tensor_names = [get_local_name(tensor) for tensor in output_tensors]
  tensor_name2producer_idx = _GetTensorName2ProducerIdx(
    in_out_names_sigs,
    input_tensors,
    get_local_name,
  )
  op_id2used = OrderedDict()
  block_op_calls = BlockOpCallsExtractor().Extract(func, free_vars, args)
  for op_call in block_op_calls.input_op_calls:
    op_id2used[op_call.op.op_id] = [get_local_name(t) for t in input_tensors]
  for i, in_out_names_sig in enumerate(in_out_names_sigs):
    all_input_names_used_by_me_and_downstream = _GetAllInputNamesUsedByDownStream(
      in_out_names_sigs, i
    )
    all_input_names_used_by_me_and_downstream = {
      *all_input_names_used_by_me_and_downstream,
      *output_tensor_names,
    }
    current_defined_names_used_by_me_and_downstream = {
      name
      for name in all_input_names_used_by_me_and_downstream
      if tensor_name2producer_idx[name][0] < i
    }
    op_id2used[in_out_names_sig.op_id] = _GetSorted(
      current_defined_names_used_by_me_and_downstream,
      key=lambda name : tensor_name2producer_idx[name]
    )
  for op_call in block_op_calls.output_op_calls:
    op_id2used[op_call.op.op_id] = [get_local_name(t) for t in output_tensors]
  return op_id2used


def _GetSorted(names, key):
  return sorted(list(names), key=key)

def _GetAllInputNamesUsedByDownStream(in_out_names_sigs, idx):
  names = set()
  for in_out_names_sig in in_out_names_sigs[idx:]:
    for in_name in in_out_names_sig.in_names:
      names.add(in_name)
  return names

def _GetTensorName2ProducerIdx(in_out_names_sigs, input_tensors, get_local_name):
  tensor_name2idx = {}
  for j, input_tensor in enumerate(input_tensors):
    tensor_name2idx[get_local_name(input_tensor)] = (-1, j)
  for i, in_out_names_sig in enumerate(in_out_names_sigs):
    for j, out_name in enumerate(in_out_names_sig.out_names):
      if out_name in tensor_name2idx:
        continue
      tensor_name2idx[out_name] = (i, j)
  return tensor_name2idx

class OpInOutNameSignatureExtractor:

  def __init__(self, get_local_name):
    self.in_out_names_sigs = []
    self.get_local_name = get_local_name
  
  def Extract(self, func, free_vars, args):
    body_op_calls = BlockOpCallsExtractor().Extract(func, free_vars, args).body_op_calls
    for op_call in body_op_calls:
      self(op_call.op, op_call.input_tensors, op_call.kwargs)
    return self.in_out_names_sigs

  def __call__(self, op, input_tensors, kwargs):
    input_tensors = [t for t in input_tensors if t is not None]
    if hasattr(self, op.GetPyVarName()):
      return getattr(self, op.GetPyVarName())(op, *input_tensors, **kwargs)
    free_vars = []
    if len(kwargs) > 0:
      for region in kwargs['blocks']:
        for block_tuple in region:
          free_vars = [*free_vars, *block_tuple[1:]]
    input_tensors = [*free_vars, *input_tensors]
    in_names = [self.get_local_name(tensor) for tensor in input_tensors]
    out_names = [self.get_local_name(tensor) for tensor in op.GetResults()]
    self.in_out_names_sigs.append(OpInpOutNameSignature(
      op_id=op.op_id,
      in_names=in_names,
      out_names=out_names,
    ))
