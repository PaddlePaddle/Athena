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
    base_op=op,
  )