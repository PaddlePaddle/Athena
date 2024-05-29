import athena.ir.paddle_op as paddle_op
from athena.ir_converters.paddle_attr_converter import ConvertAttributeToString

def ConvertToPaddleOp(op):
  return paddle_op.Op(
    name=op.name,
    op_id=op.op_id,
    input_types=op.input_types,
    output_types=op.output_types,
    attrs={name:ConvertAttributeToString(attr) for name, attr in op.attrs.items()},
    block_positional_arg_names=op.block_positional_arg_names,
    block_keyword_arg_names=op.block_keyword_arg_names,
    block_positional_arg_types=op.block_positional_arg_types,
    block_keyword_arg_types=op.block_keyword_arg_types,
    base_op=op,
    __operands_symbols_signature__=op.__operands_symbols_signature__,
    __results_symbols_signature__=op.__results_symbols_signature__,
  )