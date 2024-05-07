import athena.ir.ir_attr as ir_attr

class AttrTrait:

  def a_bool(self, value):
    return ir_attr.BoolAttribute(value)

  def a_c64(self, real, imag):
    return ir_attr.Complex64Attribute(real, imag)

  def a_c128(self, real, imag):
    return ir_attr.Complex128Attribute(real, imag)

  def a_f32(self, value):
    return ir_attr.Float32Attribute(value)

  def a_f64(self, value):
    return ir_attr.Float64Attribute(value)

  def a_i32(self, value):
    return ir_attr.Int32Attribute(value)

  def a_index(self, value):
    return ir_attr.IndexAttribute(value)

  def a_i64(self, value):
    return ir_attr.Int64Attribute(value)

  def a_pointer(self, value):
    return ir_attr.PointerAttribute(value)

  def a_type(self, value):
    return ir_attr.TypeAttribute(value)

  def a_str(self, value):
    return ir_attr.StrAttribute(value)

  def a_array(self, *value):
    return ir_attr.ArrayAttribute(value)

  def a_tensorname(self, value):
    return ir_attr.TensorNameAttribute(value)

  def a_intarray(self, *value):
    return ir_attr.IntArrayAttribute(value)

  def a_scalar(self, value):
    return ir_attr.ScalarAttribute(value)

  def a_dtype(self, dtype_name):
    return ir_attr.DataTypeAttribute(dtype_name)

  def a_place(self, type, devcie = None):
    return ir_attr.PlaceAttribute(type, devcie)

  def a_layout(self, name):
    return ir_attr.DataLayoutAttribute(name)

  def a_kernel(self, value=None):
    return ir_attr.KernelAttributeAttribute(value)

  def a_group_info(self, value=None):
    return ir_attr.GroupInfoAttribute(value)

  def a_cinn_kernel_info(self, value=None):
    return ir_attr.CINNKernelInfoAttribute(value)

  def a_symbol(self, value=None):
    return ir_attr.SymbolAttribute(value)

  def UnclassifiedAttribute(self, value=None):
    return ir_attr.UnclassifiedAttribute(value)
