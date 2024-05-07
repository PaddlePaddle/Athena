from athena.ir_converters.paddle_op_converter import ConvertToPaddleOp
from athena.generators.paddle_op_call_generator import PaddleOpCallGenerator
from athena.generators.global_tensor_converter import GlobalTensorConverter

class PaddleFuncBodyGenerator:
  def __init__(self, func):
    self.func = func
    self.stmts = []
    self.op_call_generator = PaddleOpCallGenerator()
    self.tensor_converter = GlobalTensorConverter()

  def Generate(self, input_tensors):
    local_input_tensors = [
      self.tensor_converter.ConvertToLocalTensor(input_tensor)
      for input_tensor in input_tensors
    ]
    self.func(self, *input_tensors)
    return local_input_tensors, self.stmts

  def cinn_op_fusion(self, op, blocks):
    block_func, *free_vars = blocks[0][0]
    return block_func(self, *free_vars)()

  def __call__(self, op, *input_tensors, **kwargs):
    signature = f"(%s) <- (%s)" % (
      ", ".join(t.GetShortStr() for t in op.output_types),
      ", ".join(t.GetShortStr() for t in op.input_types)
    )
    self.stmts.append(f"# {signature}")
    op = ConvertToPaddleOp(op)
    assert len(kwargs) == 0
    local_input_tensors = [
      self.tensor_converter.ConvertToLocalTensor(input_tensor)
      for input_tensor in input_tensors
    ]
    local_output_tensor_names = [
      self.tensor_converter.ConvertToLocalTensor(output_tensor).name
      for output_tensor in op.GetResults()
    ]
    local_output_unpack_str = ", ".join(local_output_tensor_names)
    local_op_call_expr = self.op_call_generator.GenerateOpCall(op, *local_input_tensors)
    if local_op_call_expr is None:
      pass 
    elif len(local_output_tensor_names) == 0:
      self.stmts.append(f"{local_op_call_expr}")
    else:
      self.stmts.append(f"{local_output_unpack_str} = {local_op_call_expr}")
    self.stmts.append("")
    return op.GetResults()