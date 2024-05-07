from contextlib import contextmanager
from athena.generators.cinn_unittest_generator import CinnUnittestGenerator
from athena.generators.paddle_unittest_generator import PaddleUnittestGenerator

class GroupOpUnittestGenerator(CinnUnittestGenerator):

  def __init__(self):
    self.op_name2unittest = {}

  def Generate(self, ir_program):
    self.op_name2unittest = {}
    ir_program(self)
    return self.op_name2unittest

  def cinn_op_group(self, op, blocks):
    block_func, *free_vars = blocks[0][0]
    unittest_class_name = "TestGroup"
    unittest_generator = PaddleUnittestGenerator(
      unittest_class_name=unittest_class_name,
      func=lambda *args: block_func(*args)()
    )
    self.op_name2unittest[op.GetUniqueName()] = unittest_generator.Generate(free_vars)
    return op.GetResults()