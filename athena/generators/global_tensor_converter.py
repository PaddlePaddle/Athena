from athena.ir.ir_tensor import Tensor

class GlobalTensorConverter:

  def __init__(self):
    self.local_name_prefix2seq_no = {}
    self.global_name2local_tensor = {}

  def ConvertToLocalTensor(self, tensor, prefix = None):
    if tensor is None:
      return None
    if tensor.name not in self.global_name2local_tensor:
      prefix = tensor.local_name_prefix if prefix is None else prefix
      self.global_name2local_tensor[tensor.name] = Tensor(
        local_name_prefix=prefix,
        name=f"{prefix}_{self._GetLocalNameSeqNo(prefix)}",
        arg_name_as_input=tensor.arg_name_as_input,
        defining_op_name=tensor.defining_op_name,
        type=tensor.type,
        dim_exprs=tensor.dim_exprs
      )
    return self.global_name2local_tensor[tensor.name]

  def _GetLocalNameSeqNo(self, local_name_prefix):
    if local_name_prefix not in self.local_name_prefix2seq_no:
      self.local_name_prefix2seq_no[local_name_prefix] = 0
    local_name_seq_no = self.local_name_prefix2seq_no[local_name_prefix]
    self.local_name_prefix2seq_no[local_name_prefix] += 1
    return local_name_seq_no