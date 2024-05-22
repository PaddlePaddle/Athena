from athena.ir.ir_block import Block
from athena.ir.ir_op import Op
from athena.ir.ir_tensor import Tensor
from typing import List, Tuple
from athena.generators.paddle_func_body_generator import (
  PaddleFuncBodyGenerator
)
from athena.generators.block_name_generator import BlockNameGenerator


class PaddleBlockUnittestStmtsGenerator:

  def __init__(self, block_name_generator: BlockNameGenerator):
    self.block_name_generator = block_name_generator

  def Generate(self, block: Block) -> Tuple[List[Tensor], List["PyCodeStmt"]]:
    paddle_func_body_generator = PaddleFuncBodyGenerator(
      block.block_func,
      self.block_name_generator,
    )
    return paddle_func_body_generator.Generate(block.free_vars, block.args)
