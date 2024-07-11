from athena.ir.ir_block import Block
import typing as t

class BlocksGenerator:
  def __init__(self, ir_program):
    self.ir_program = ir_program
    self.block_owner_ops = []

  def Generate(self) -> t.List[Block]:
    self.ir_program(self)
    return self.block_owner_ops

  def get_block_func_args(self, op, owner_op_args, region_idx, block_idx):
    method_name = f"get_block_func_args_{op.GetPyVarName()}"
    if hasattr(self, method_name):
      return getattr(self, method_name)(op, owner_op_args, region_idx, block_idx)
    return owner_op_args

  def get_block_func_args_pd_op_while(self, op, owner_op_args, region_idx, block_idx):
    return owner_op_args[1:]

  def get_block_func_args_pd_op_if(self, op, owner_op_args, region_idx, block_idx):
    return []

  def get_block_func_args_builtin_module(self, op, owner_op_args, region_idx, block_idx):
    # TODO
    return owner_op_args

  def __call__(self, op, *owner_op_args, **kwargs):
    block_key = 'blocks'
    results = op.GetResults()
    if block_key not in kwargs:
      return results
    for region_idx, region in enumerate(kwargs[block_key]):
      for block_idx, block_tuple in enumerate(region):
        block_func, *free_vars = block_tuple
        args = self.get_block_func_args(op, owner_op_args, region_idx, block_idx)
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