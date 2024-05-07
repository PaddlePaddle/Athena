import athena.ir.ir_attr as ir_attr

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

  def _GenerateAdd(self, _, lhs, rhs):
    if type(rhs) is ir_attr.ArrayAttribute and rhs.value[0].value == "Negative":
      return f"({self.Generate(lhs)} - {self.Generate(rhs.value[1])})"
    return f"({self.Generate(lhs)} + {self.Generate(rhs)})"

  def _GenerateMul(self, _, lhs, rhs):
    if type(rhs) is ir_attr.ArrayAttribute and rhs.value[0].value == "Reciprocal":
      return f"({self.Generate(lhs)} / {self.Generate(rhs.value[1])})"
    return f"({self.Generate(lhs)} * {self.Generate(rhs)})"

  def _GenerateMax(self, _, lhs, rhs):
    return f"{self.m}.maximum({self.Generate(lhs)}, {self.Generate(rhs)})"

  def _GenerateMin(self, _, lhs, rhs):
    return f"{self.m}.minimum({self.Generate(lhs)}, {self.Generate(rhs)})"

  def _GenerateBroadcast(self, _, lhs, rhs):
    lhs_placeholder = f"{self.m}.empty({self.Generate(lhs)})"
    rhs_placeholder = f"{self.m}.empty({self.Generate(rhs)})"
    return f"{self.m}.shape({lhs_placeholder} + {rhs_placeholder})"

  def _GenerateSymbolInputExpr(self, tag, inputs, tensor_idx, dim_idx):
    method_name = f"_{tag}"
    return getattr(self, method_name)(inputs, tensor_idx, dim_idx)

  def _ShapeSymbolBinding(self, inputs, tensor_idx, dim_idx):
    return f"{self.m}.shape({inputs[tensor_idx].name})[{dim_idx}]"

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
    return getattr(self, op.GetPyVarName())(op, *inputs)

  def pd_op_gather_nd(self, op, x, index):
    return f"{self.m}.gather_nd({x.name}, {index.name})"

  def pd_op_subtract(self, op, x, y):
    return f"{x.name} - {y.name}"

  def cf_yield(self, op, *inputs):
    return "return " + ", ".join([input.name for input in inputs])

  def pd_op_exp(self, op, x):
    return f"{self.m}.exp({x.name})"

  def pd_op_rsqrt(self, op, x):
    return f"{self.m}.rsqrt({x.name})"

  def pd_op_expand(self, op, x, shape):
    return f"{self.m}.expand({x.name}, {shape.name})"

  def pd_op_full(self, op):
    return f"{self.m}.full(shape={op.attrs['shape']}, dtype='{op.attrs['dtype']}', fill_value={op.attrs['value']})"

  def builtin_shadow_output(self, op):
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

  def pd_op_concat(self, op, x, y):
    return f"{self.m}.concat({x.name}, {y.name})"

  def pd_op_sum(self, op, x, axis):
    return f"{self.m}.sum({x.name}, keepdim={op.attrs['keepdim']}, axis={axis.name})"

  def pd_op_matmul(self, op, x, y):
    return f"{self.m}.matmul({x.name}, {y.name}, transpose_x={op.attrs['transpose_x']}, transpose_y={op.attrs['transpose_y']})"

  def pd_op_split(self, op, x, y, z):
    return f"{self.m}.split({x.name}, {y.name}, {z.name})"

  def builtin_split(self, op, x):
    return f"{x.name}"

  def pd_op_full_int_array(self, op):
    values = ", ".join(map(str, op.attrs['value']))
    return f"[{values}]"

  def cinn_op_yield_store(self, op, x):
    return f"{x.name}"

  def cinn_op_concat(self, op, *inputs):
    operands = ", ".join([input.name for input in inputs])
    return f"{self.m}.concat([{operands}], axis={op.attrs['axis']})"

  def cinn_op_slice(self, op, x):
    return f"{self.m}.slice({x.name}, axes={op.attrs['axes']}, starts={op.attrs['starts']}, ends={op.attrs['ends']})"

  def cinn_op_reduce_sum(self, op, x):
    return f"{self.m}.sum({x.name}, keepdim={op.attrs['keep_dim']}, axis={op.attrs['dim']})"

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

  def cinn_op_scale(self, op, x):
    return f"{x.name} * {op.attrs['scale']} + {op.attrs['bias']}"

  def pd_op_cast(self, op, x):
    return f"{self.m}.cast({x.name}, dtype='{op.attrs['dtype']}')"

  def cinn_op_broadcast(self, op, x):
    return f"{self.m}.broadcast_to({x.name}, {op.attrs['out_shape']})"

  def cinn_op_reshape(self, op, x):
    return f"{self.m}.reshape({x.name}, {op.attrs['shape']})"

  def pd_op_reshape(self, op, x, shape):
    return f"{self.m}.reshape({x.name}, {shape.name}), None"

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