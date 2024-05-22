from athena.ir.ir_block import Block

class BlocksGenerator:
  def __init__(self, ir_program):
    self.ir_program = ir_program
    self.block_owner_ops = []

  def Generate(self):
    self.ir_program(self)
    return self.block_owner_ops

  def __call__(self, op, *args, **kwargs):
    block_key = 'blocks'
    results = op.GetResults()
    if block_key not in kwargs:
      return results
    for region_idx, region in enumerate(kwargs[block_key]):
      for block_idx, block_tuple in enumerate(region):
        block_func, *free_vars = block_tuple
        block_func(self, *free_vars)(*args)
        self.block_owner_ops.append(
          Block(
            owner_op=op,
            is_entry_block=(op.name == "builtin.module"),
            region_idx=region_idx,
            block_idx=block_idx,
            block_func=block_func,
            free_vars=free_vars,
            args=(),
          )
        )
    return results