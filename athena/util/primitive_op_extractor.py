from athena.ir.ir_op import Op

class PrimitiveOpExtractor:

  def Extract(self, ir_program):
    return [
      op
      for _, op in vars(ir_program).items()
      if isinstance(op, Op)
      if op.name not in self.GetInputOutputOpNames()
      if op.block_positional_arg_names is None
      if op.block_keyword_arg_names is None
      if len(op.GetResults()) > 0
    ]

  def GetInputOutputOpNames(self):
    return {
      "pd_op.data",
      "builtin.parameter",
      "cf.yield",
      "builtin.shadow_output",
      "pd_op.fetch",
    }