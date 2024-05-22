from typing import Dict, List
from dataclasses import dataclass
from athena.generators.global_tensor_converter import GlobalTensorConverter

@dataclass
class OpInpOutNameSignature:
  op_id : int
  in_names: List[str]
  out_names: List[str]

def GetOpId2TensorNamesUsedByDownstream(
  func,
  free_vars,
  args,
  get_local_name,
) -> Dict[int, List[str]]:
  in_out_name_sig_extractor = OpInOutNameSignatureExtractor(get_local_name)
  in_out_names_sigs = in_out_name_sig_extractor.Extract(func, free_vars, args)
  tensor_name2idx = _GetTensorName2Idx(
    in_out_names_sigs,
    free_vars,
    get_local_name,
  )
  op_id2used = {}
  for i, in_out_names_sig in enumerate(in_out_names_sigs):
    all_input_names_used_by_downstream = _GetAllInputNamesUsedByDownStream(
      in_out_names_sigs, i
    )
    current_defined_names_used_by_downstream = {
      name
      for name in all_input_names_used_by_downstream
      if tensor_name2idx[name][0] < i
    }
    op_id2used[in_out_names_sig.op_id] = _GetSorted(
      current_defined_names_used_by_downstream,
      key=lambda name : tensor_name2idx[name]
    )
  return op_id2used

def _GetSorted(names, key):
  return sorted(list(names), key=key)

def _GetAllInputNamesUsedByDownStream(in_out_names_sigs, idx):
  names = set()
  for in_out_names_sig in in_out_names_sigs[idx:]:
    for in_name in in_out_names_sig.in_names:
      names.add(in_name)
  return names

def _GetTensorName2Idx(in_out_names_sigs, input_tensors, get_local_name):
  tensor_name2idx = {}
  for j, input_tensor in enumerate(input_tensors):
    tensor_name2idx[get_local_name(input_tensor)] = (-1, j)
  for i, in_out_names_sig in enumerate(in_out_names_sigs):
    for j, out_name in enumerate(in_out_names_sig.out_names):
      tensor_name2idx[out_name] = (i, j)
  return tensor_name2idx

class OpInOutNameSignatureExtractor:

  def __init__(self, get_local_name):
    self.in_out_names_sigs = []
    self.get_local_name = get_local_name
  
  def Extract(self, func, free_vars, args):
    func(self, *free_vars)(*args)
    return self.in_out_names_sigs

  def __call__(self, op, *input_tensors, **kwargs):
    assert len(kwargs) == 0
    results = op.GetResults()
    in_names = [self.get_local_name(tensor) for tensor in input_tensors]
    out_names = [self.get_local_name(tensor) for tensor in results]
    self.in_out_names_sigs.append(OpInpOutNameSignature(
      op_id=op.op_id,
      in_names=in_names,
      out_names=out_names,
    ))
    return results