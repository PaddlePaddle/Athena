import athena.ir.ir_type as ir_type

class TypeTrait:

  def t_vec(self, *args):
    return ir_type.VectorType(args)

  def t_dtensor(self, shape, dtype):
    return ir_type.DenseTensorType(shape, dtype)

  def t_bf16(self):
    return ir_type.BFloat16Type()

  def t_f16(self):
    return ir_type.Float16Type()

  def t_f32(self):
    return ir_type.Float32Type()

  def t_f64(self):
    return ir_type.Float64Type()

  def t_i8(self):
    return ir_type.Int8Type()

  def t_ui8(self):
    return ir_type.UInt8Type()

  def t_i16(self):
    return ir_type.Int16Type()

  def t_i32(self):
    return ir_type.Int32Type()

  def t_i64(self):
    return ir_type.Int64Type()

  def t_index(self):
    return ir_type.IndexType()

  def t_bool(self):
    return ir_type.BoolType()

  def t_c64(self):
    return ir_type.Complex64Type()

  def t_c128(self):
    return ir_type.Complex128Type()

  def UnclassifiedType(self, *args, **kwargs):
    return ir_type.UnclassifiedType(args, kwargs)