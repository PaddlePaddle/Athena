from athena.ir.ir_block import Block
import typing as t

class BlocksGenerator:
  def __init__(self, ir_program):
    self.ir_program = ir_program
    self.block_owner_ops = []

  def Generate(self) -> t.List[Block]:
    self.ir_program(self)
    return self.block_owner_ops

  def get_block_func(self, op, region_idx, block_idx, block_func):
    method_name = f"get_block_func_{op.GetPyVarName()}"
    if hasattr(self, method_name):
      return getattr(self, method_name)(op, region_idx, block_idx, block_func)
    return block_func
  
  def get_block_func_pd_op_while(self, op, region_idx, block_idx, block_func):
    return lambda *free_vars: lambda *args: block_func(*free_vars)(*args[1:])

  def __call__(self, op, *args, **kwargs):
    block_key = 'blocks'
    results = op.GetResults()
    if block_key not in kwargs:
      return results
    for region_idx, region in enumerate(kwargs[block_key]):
      for block_idx, block_tuple in enumerate(region):
        block_func, *free_vars = block_tuple
        block_func = self.get_block_func(op, region_idx, block_idx, block_func)
        block_func(self, *free_vars)(*args)
        self.block_owner_ops.append(
          Block(
            owner_op=op,
            is_entry_block=(op.name == "builtin.module"),
            region_idx=region_idx,
            block_idx=block_idx,
            block_func=block_func,
            free_vars=free_vars,
            args=args,
          )
        )
    return results