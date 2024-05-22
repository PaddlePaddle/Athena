from athena.ir.ir_block import Block

class BlockNameGenerator:

  def __init__(self):
    self.prefix2seq_no = {}
    self.owner_op_id2local_op_name = {}

  def Generate(self, block: Block):
    local_op_name = self.GetOrCreateLocalOpName(block)
    return f"{local_op_name}_{block.region_idx}_{block.block_idx}"

  def GetOrCreateLocalOpName(self, block: Block):
    op_id = block.owner_op.op_id
    if op_id not in self.owner_op_id2local_op_name:
      local_op_name = self.CreateLocalOpName(block.owner_op.GetPyVarName())
      self.owner_op_id2local_op_name[op_id] = local_op_name
    return self.owner_op_id2local_op_name[op_id]

  def CreateLocalOpName(self, prefix):
    if prefix not in self.prefix2seq_no:
      self.prefix2seq_no[prefix] = -1
    self.prefix2seq_no[prefix] += 1
    return f"{prefix}_{self.prefix2seq_no[prefix]}"
