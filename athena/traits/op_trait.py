import athena.ir.ir_op as ir_op


class OpTrait:

  def Op(
    self, name, op_id, input_types, output_types, attrs,
    block_positional_arg_names = None, block_keyword_arg_names = None
  ):
    return ir_op.Op(
      name, op_id, input_types, output_types, attrs,
      block_positional_arg_names, block_keyword_arg_names
    )