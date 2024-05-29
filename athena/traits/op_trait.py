import athena.ir.ir_op as ir_op


class OpTrait:

  def Op(
    self, name, op_id, input_types, output_types, attrs,
    block_positional_arg_names = None, block_keyword_arg_names = None,
    block_positional_arg_types = None, block_keyword_arg_types = None
  ):
    return ir_op.Op(
      name=name,
      op_id=op_id,
      input_types=input_types,
      output_types=output_types,
      attrs=attrs,
      block_positional_arg_names=block_positional_arg_names,
      block_keyword_arg_names=block_keyword_arg_names,
      block_positional_arg_types=block_positional_arg_types,
      block_keyword_arg_types=block_keyword_arg_types,
      __operands_symbols_signature__=attrs['__operands_symbols_signature__'],
      __results_symbols_signature__=attrs['__results_symbols_signature__'],
    )