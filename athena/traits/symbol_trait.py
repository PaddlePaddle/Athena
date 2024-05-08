import athena.ir.ir_symbol as ir_symbol

class SymbolTrait:

  def s_int64(self, value):
    return ir_symbol.Int64(value)

  def s_str(self, value):
    return ir_symbol.String(value)

  def s_negative(self, value):
    return ir_symbol.Negative(value)

  def s_reciprocal(self, value):
    return ir_symbol.Reciprocal(value)

  def s_add(self, *args):
    return ir_symbol.Add(args)

  def s_mul(self, *args):
    return ir_symbol.Mul(args)

  def s_max(self, *args):
    return ir_symbol.Max(args)

  def s_min(self, *args):
    return ir_symbol.Min(args)

  def s_broadcast(self, *args):
    return ir_symbol.Broadcast(args)

  def s_tensor_shape_or_data(self, shape, data):
    return ir_symbol.TensorShapeOrDataDimExprs(shape=shape, data=data)

  def s_tensor_list_shape_or_data(self, *args):
    return ir_symbol.TensorListShapeOrDataDimExprs(args)