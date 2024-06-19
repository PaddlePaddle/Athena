import athena.ir.ir_op as ir_op

def IsBackwardProgram(ir_program):
  for name, op in vars(ir_program).items():
    if not isinstance(op, ir_op.Op):
      continue
    if op.name != "builtin.module":
      continue
    keyword_arg_names = op.block_keyword_arg_names[0][0]
    if len(keyword_arg_names) > 0:
      return True
  return False

def GetProgramId(ir_program):
  return int(type(ir_program).__name__[len('PirProgram_'):])
