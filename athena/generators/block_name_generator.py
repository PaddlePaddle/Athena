
class BlockNameGenerator:

  def __init__(self):
    self.seq_no = 0
    self.global_op_id2seq_no = {}

  def Generate(self, op, region_idx, block_idx):
    return self.GenerateGlobalName(op, region_idx, block_idx)

  def GenerateGlobalName(self, op, region_idx, block_idx):
    return f"{op.GetPyVarName()}_{op.op_id}_{region_idx}_{block_idx}"

  def GenerateLocalName(self, op, region_idx, block_idx):
    local_op_id = self.GetLocalOpId(op.op_id)
    return f"{op.GetPyVarName()}_{local_op_id}_{region_idx}_{block_idx}"

  def GetLocalOpId(self, global_op_id):
    if global_op_id not in self.global_op_id2seq_no:
      self.global_op_id2seq_no[global_op_id] = self.seq_no
      self.seq_no += 1
    return self.global_op_id2seq_no[global_op_id]
