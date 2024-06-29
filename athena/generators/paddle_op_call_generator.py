import athena.ir.ir_attr as ir_attr
import athena.ir.ir_type as ir_type
from athena.generators.paddle_c_ops_arg_names import GetCOpsArgNames
import sys

class GSOutputDimGenerator:

  def __init__(self, module_name, inputs, symbol_bindings):
    self.m = module_name
    self.symbol2py_code = {
      symbol_name: self._GenerateSymbolInputExpr(tag, inputs, tensor_idx, dim_idx)
      for tag, symbol_name, tensor_idx, dim_idx
        in self._GetSymbolBindings(inputs, symbol_bindings)
    }

  def Generate(self, dim_expr_attr):
    method_name = f"_Generate{type(dim_expr_attr).__name__}"
    return getattr(self, method_name)(dim_expr_attr)

  def _GenerateInt64Attribute(self, dim_expr_attr):
    return f"{dim_expr_attr.value}"

  def _GenerateStrAttribute(self, dim_expr_attr):
    return self.symbol2py_code[dim_expr_attr.value]

  def _GenerateArrayAttribute(self, dim_expr_attr):
    method_name = f"_Generate{dim_expr_attr.value[0].value}"
    return getattr(self, method_name)(*dim_expr_attr.value)

  def _GenerateNegative(self, _, operand):
    raise f"(- {self.Generate(operand)})"

  def _GenerateReciprocal(self, _, operand):
    raise NotImplementedError("dead code")

  def _GenerateAdd(self, _, *args):
    def IsNegtive(operand):
      return (
        type(operand) is ir_attr.ArrayAttribute
        and operand.value[0].value == "Negative"
      )
    def ConvertOperand(i, operand):
      if IsNegtive(operand):
        return (" - " if i > 0 else "-") + self.Generate(operand.value[1])
      else:
        return (" + " if i > 0 else "") + self.Generate(operand)
    ret = "".join([
      ConvertOperand(i, operand)
      for i, operand in enumerate(args)
    ])
    return f"({ret})"

  def _GenerateMul(self, _, *args):
    def IsReciprocal(operand):
      return (
        type(operand) is ir_attr.ArrayAttribute
        and operand.value[0].value == "Reciprocal"
      )
    def ConvertOperand(i, operand):
      if IsReciprocal(operand):
        return (" / " if i > 0 else "1 / ") + self.Generate(operand.value[1])
      else:
        return (" * " if i > 0 else "") + self.Generate(operand)
    ret = "".join([
      ConvertOperand(i, operand)
      for i, operand in enumerate(args)
    ])
    return f"({ret})"

  def _GenerateMax(self, _, arg0, *args):
    ret = self.Generate(lhs)
    for arg in args:
      ret = f"{self.m}.maximum({ret}, {self.Generate(arg)})"
    return ret

  def _GenerateMin(self, _, arg0, *args):
    ret = self.Generate(lhs)
    for arg in args:
      ret = f"{self.m}.minimum({ret}, {self.Generate(arg)})"
    return ret

  def _GenerateBroadcast(self, _, *args):
    empties = [
      f"{self.m}.empty({self.Generate(arg)})"
      for arg in args
    ]
    empties_sum = " + ".join(empties)
    return f"{self.m}.shape({empties_sum})"

  def _GenerateSymbolInputExpr(self, tag, inputs, tensor_idx, dim_idx):
    method_name = f"_{tag}"
    return getattr(self, method_name)(inputs, tensor_idx, dim_idx)

  def _ShapeSymbolBinding(self, inputs, tensor_idx, dim_idx):
    return f"{inputs[tensor_idx].name}.shape[{dim_idx}]"

  def _DataSymbolBinding(self, inputs, tensor_idx, dim_idx):
    return f"{inputs[tensor_idx].name}[{dim_idx}]"

  def _GetSymbolBindings(self, inputs, symbol_bindings):
    for binding in symbol_bindings.value:
      tag, symbol_name, tensor_idx, dim_idx = binding.value
      yield tag.value, symbol_name.value, tensor_idx.value, dim_idx.value


class PaddleOpCallGenerator:

  def __init__(self, module_name="paddle"):
    self.m = module_name

  def GenerateOpCall(self, op, *inputs):
    method_name = op.GetPyVarName()
    if hasattr(self, method_name):
      return getattr(self, method_name)(op, *inputs)
    return self._GenerateOpCall(op, *inputs)

  def _GenerateOpCall(self, op, *inputs):
    c_ops_arg_names = GetCOpsArgNames(self.PaddleMethodName(op))
    def ValidCOpsCall():
      if op.GetValidPyVarNameComponents()[0] != "pd_op":
        return False
      if c_ops_arg_names is None:
        return False
      attr_names = [
        attr_name
        for attr_name in c_ops_arg_names
        if attr_name in op.attrs
      ]
      assert len(inputs) + len(attr_names) == len(c_ops_arg_names), f"op: {op.name}, len(inputs): {len(inputs)}, attr_names: {attr_names}, c_ops_arg_names: {c_ops_arg_names}"
      return True
    if ValidCOpsCall():
      return self.GenerateCOpsCall(op, inputs, c_ops_arg_names)
    assert op.GetValidPyVarNameComponents()[0] == "pd_op", f"op.name: {op.name}"
    return self.GenerateDefaultOpCall(self.m, op, *inputs)

  def PaddleMethodName(self, op):
    return op.GetValidPyVarNameComponents()[-1]

  def GetOpAttrs(self, op):
    ignored_attr_names = {
      "__operands_symbols_signature__",
      "__results_symbols_signature__",
      "stop_gradient",
      "place",
    }
    for attr_name, attr_value in op.attrs.items():
      if attr_name in ignored_attr_names:
        continue
      yield attr_name, attr_value

  def GenerateDefaultOpCall(self, m, op, *inputs):
    input_names = ", ".join([t.name if t is not None else "None" for t in inputs])
    attr_str = ", ".join([
      f"{attr_name}={attr_value}"
      for attr_name, attr_value in self.GetOpAttrs(op)
    ])
    if len(attr_str) > 0:
      attr_str = ", " + attr_str
    return f"{m}.{self.PaddleMethodName(op)}({input_names}{attr_str})"

  def GenerateCOpsCall(self, op, inputs, arg_names):
    pos_arg_idx = -1
    def GetPosArgVarName():
      nonlocal pos_arg_idx
      pos_arg_idx += 1
      t = inputs[pos_arg_idx]
      if t is None:
        return "None"
      if isinstance(t.type, ir_type.NullType):
        return "None"
      return t.name
    m = f"{self.m}._C_ops"
    args = [
      op.attrs[arg_name] if arg_name in op.attrs else GetPosArgVarName()
      for arg_name in arg_names
    ]
    args_str = ", ".join(args)
    return f"{m}.{self.PaddleMethodName(op)}({args_str})"

  def pd_op_dropout(self, op, *inputs):
    op_call_str = self._GenerateOpCall(op, *inputs)
    return f"{op_call_str}, None"

  def pd_op_layer_norm(self, op, *inputs):
    op_call_str = self._GenerateOpCall(op, *inputs)
    return f"{op_call_str}, None, None"

  def pd_op_huber_loss(self, op, *inputs):
    op_call_str = self._GenerateOpCall(op, *inputs)
    return f"{op_call_str}, None"

  def pd_op_one_hot(self, op, x, num_classes):
    return f"{self.m}._C_ops.one_hot({x.name} % {num_classes.name}, {num_classes.name})"

  def pd_op_squeeze(self, op, *inputs):
    op_call_str = self._GenerateOpCall(op, *inputs)
    return f"{op_call_str}, None"

  def pd_op_flatten(self, op, *inputs):
    op_call_str = self._GenerateOpCall(op, *inputs)
    return f"{op_call_str}, None"

  def pd_op_assign(self, op, x):
    return x.name

  def pd_op_sigmoid(self, op, x):
    return f"{self.m}.nn.functional.sigmoid({x.name})"

  def pd_op_set_value_(self, op, x, starts, ends, steps):
    return f"{self.m}._C_ops.set_value_({x.name}, {starts.name}, {ends.name}, {steps.name}, {op.attrs['axes']}, {op.attrs['decrease_axes']}, {op.attrs['none_axes']}, {op.attrs['shape']}, {op.attrs['values']})"

  def pd_op_gather_nd(self, op, x, index):
    return f"{self.m}.gather_nd({x.name}, {index.name})"

  def pd_op_subtract(self, op, x, y):
    return f"{x.name} - {y.name}"

  def pd_op_rsqrt(self, op, x):
    return f"{self.m}.rsqrt({x.name})"

  def pd_op_expand(self, op, x, shape):
    return f"{self.m}.expand({x.name}, {shape.name})"

  def cf_yield(self, op, *inputs):
    return None

  def builtin_shadow_output(self, op, *inputs):
    return None

  def pd_op_fetch(self, op, *inputs):
    return None

  def builtin_parameter(self, op):
    return None

  def pd_op_data(self, op):
    return None

  def pd_op_elementwise_pow(self, op, x, y):
    return f"{self.m}.pow({x.name}, {y.name})"

  def builtin_combine(self, op, *inputs):
    operands = ", ".join([input.name for input in inputs])
    return f"[{operands}]"

  def builtin_split(self, op, x):
    return x.name

  def pd_op_matmul(self, op, x, y):
    return f"{self.m}.matmul({x.name}, {y.name}, transpose_x={op.attrs['transpose_x']}, transpose_y={op.attrs['transpose_y']})"

  def pd_op_share_data_(self, op, x):
    return f"{x.name}.detach()"

  def pd_op_split(self, op, x, y, z):
    return f"{self.m}.split({x.name}, {y.name}, {z.name})"

  def pd_op_full_int_array(self, op):
    return op.attrs['value']

  def cinn_op_yield_store(self, op, x):
    return f"{x.name},"

  def cinn_op_concat(self, op, *inputs):
    operands = ", ".join([input.name for input in inputs])
    return f"{self.m}.concat([{operands}], axis={op.attrs['axis']})"

  def cinn_op_slice(self, op, x):
    return f"{self.m}.slice({x.name}, axes={op.attrs['axes']}, starts={op.attrs['starts']}, ends={op.attrs['ends']})"

  def cinn_op_reduce_sum(self, op, x):
    return f"{self.m}.sum({x.name}, keepdim={op.attrs['keep_dim']}, axis={op.attrs['dim']})"

  def cinn_op_reduce_prod(self, op, x):
    return f"{self.m}.prod({x.name}, keepdim={op.attrs['keep_dim']}, axis={op.attrs['dim']})"

  def pd_op_sqrt(self, op, x):
    return f"{self.m}.sqrt({x.name})"

  def pd_op_transpose(self, op, x):
    return f"{self.m}.transpose({x.name}, perm={op.attrs['perm']})"

  def pd_op_add(self, op, x, y):
    return f"{x.name} + {y.name}"

  def pd_op_multiply(self, op, x, y):
    return f"{x.name} * {y.name}"

  def pd_op_divide(self, op, x, y):
    return f"{x.name} / {y.name}"

  def pd_op_greater_than(self, op, x, y):
    return f"{x.name} > {y.name}"

  def pd_op_less_than(self, op, x, y):
    return f"{x.name} < {y.name}"

  def pd_op_logical_and(self, op, x, y):
    return f"{self.m}.logical_and({x.name}, {y.name})"

  def pd_op_maximum(self, op, x, y):
    return f"{self.m}.maximum({x.name}, {y.name})"

  def cinn_op_scale(self, op, x):
    return f"{x.name} * {op.attrs['scale']} + {op.attrs['bias']}"

  def cinn_op_broadcast(self, op, x):
    return f"{self.m}.broadcast_to({x.name}, {op.attrs['out_shape']})"

  def cinn_op_reshape(self, op, x):
    return f"{self.m}.reshape({x.name}, {op.attrs['shape']})"

  def pd_op_reshape(self, op, x, shape):
    return f"{self.m}.reshape({x.name}, {shape.name}), None"

  def pd_op_unsqueeze(self, op, x, axis):
    return f"{self.m}.unsqueeze({x.name}, {axis.name}), None"

  def pd_op_sin(self, op, x):
    return f"{self.m}.sin({x.name})"

  def pd_op_erf(self, op, x):
    return f"{self.m}.erf({x.name})"

  def pd_op_cos(self, op, x):
    return f"{self.m}.cos({x.name})"

  def cinn_op_generate_shape(self, op, *inputs):
    generator = GSOutputDimGenerator(
      self.m, inputs,
      symbol_bindings=op.base_op.attrs['symbol_bindings'],
    )
    output_dims = ", ".join([
      generator.Generate(dim_expr)
      for dim_expr in op.base_op.attrs['output_dim_exprs'].value
    ])
    input_args = ", ".join([input.name for input in inputs])
    return f"[{output_dims}] # inputs: {input_args}"