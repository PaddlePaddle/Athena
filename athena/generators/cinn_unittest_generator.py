from athena.ir.ir_tensor import Tensor
from athena.ir_converters.paddle_op_converter import ConvertToPaddleOp

class CinnUnittestGenerator:

  def pd_op_while(self, op, *inputs, **kwargs):
    cond, *args = inputs
    arg_names = op.block_positional_arg_names[0][0]
    block_func, *free_vars = kwargs['blocks'][0][0]
    def GetArgTensor(i, arg_name):
      return Tensor(
        local_name_prefix="arg",
        name=arg_name,
        type=inputs[i].type,
      )
    return block_func(self, *free_vars)(**{
      arg_name:GetArgTensor(i, arg_name) for i, arg_name in enumerate(arg_names)
    })

  def builtin_module(self, op, *inputs, **kwargs):
    block_func, = kwargs['blocks'][0][0]
    return block_func(self)()

  def __call__(self, op, *inputs, **kwargs):
    op = ConvertToPaddleOp(op)
    method_name = op.GetPyVarName()
    if hasattr(self, method_name):
      getattr(self, method_name)(op, *inputs, **kwargs)
    return op.GetResults()
