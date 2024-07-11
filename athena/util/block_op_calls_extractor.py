from dataclasses import dataclass
import typing as t

@dataclass
class OpCall:
  op: "Op"
  input_tensors: t.List["Tensor"]
  kwargs: t.Dict[str, t.Any]

@dataclass
class BlockOpCalls:
  input_op_calls: t.List[OpCall]
  body_op_calls: t.List[OpCall]
  output_op_calls: t.List[OpCall]


class BlockOpCallsExtractor:

  def __init__(self):
    self.block_op_calls = BlockOpCalls([], [], [])

  def Extract(self, func, free_vars, args) -> BlockOpCalls:
    func(self, *free_vars)(*args)
    return self.block_op_calls

  def cf_yield(self, op, *inputs):
    self.block_op_calls.output_op_calls.append(OpCall(
      op=op,
      input_tensors=inputs,
      kwargs={}
    ))
    return op.GetResults()

  def builtin_shadow_output(self, op, *inputs):
    self.block_op_calls.output_op_calls.append(OpCall(
      op=op,
      input_tensors=inputs,
      kwargs={}
    ))
    return op.GetResults()

  def pd_op_fetch(self, op, *inputs):
    self.block_op_calls.output_op_calls.append(OpCall(
      op=op,
      input_tensors=inputs,
      kwargs={}
    ))
    return op.GetResults()

  def builtin_parameter(self, op):
    self.block_op_calls.input_op_calls.append(OpCall(
      op=op,
      input_tensors=[],
      kwargs={}
    ))
    return op.GetResults()

  def builtin_constant(self, op):
    self.block_op_calls.input_op_calls.append(OpCall(
      op=op,
      input_tensors=[],
      kwargs={}
    ))
    return op.GetResults()

  def pd_op_data(self, op):
    self.block_op_calls.input_op_calls.append(OpCall(
      op=op,
      input_tensors=[],
      kwargs={}
    ))
    return op.GetResults()

  def pd_op_feed(self, op):
    self.block_op_calls.input_op_calls.append(OpCall(
      op=op,
      input_tensors=[],
      kwargs={}
    ))
    return op.GetResults()

  def __call__(self, op, *input_tensors, **kwargs):
    if hasattr(self, op.GetPyVarName()):
      return getattr(self, op.GetPyVarName())(op, *input_tensors, **kwargs)
    self.block_op_calls.body_op_calls.append(OpCall(
      op=op,
      input_tensors=input_tensors,
      kwargs=kwargs,
    ))
    return op.GetResults()