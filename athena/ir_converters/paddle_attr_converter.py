import athena.ir.ir_attr

def ConvertAttributeToString(attr):
  return getattr(AttributeToStringConverter, type(attr).__name__)(attr)

class AttributeToStringConverter:
  def BoolAttribute(attr):
    return str(attr.value)

  def Complex64Attribute(attr):
    return f"complex({attr.real}, {attr.imag})"

  def Complex128Attribute(attr):
    return f"complex({attr.real}, {attr.imag})"

  def Float32Attribute(attr):
    return attr.value

  def Float64Attribute(attr):
    return attr.value

  def Int32Attribute(attr):
    return str(attr.value)

  def IndexAttribute(attr):
    return str(attr.value)

  def Int64Attribute(attr):
    return str(attr.value)

  def PointerAttribute(attr):
    return f"'{attr.value}'"

  def TypeAttribute(attr):
    return f"'{attr.value}'"

  def StrAttribute(attr):
    return f"'{attr.value}'"

  def ArrayAttribute(attr):
    return "[" + ", ".join(map(ConvertAttributeToString, attr.value)) + "]"

  def TensorNameAttribute(attr):
    return f"'{attr.value}'"

  def IntArrayAttribute(attr):
    return "[" + ", ".join(map(str, attr.value)) + "]"

  def ScalarAttribute(attr):
    raise "NotImplemented('ScalarAttribute Converter not implemented.')"

  def DataTypeAttribute(attr):
    return attr.value

  def PlaceAttribute(attr):
    return f"'{attr.type}:{attr.device}'"

  def DataLayoutAttribute(attr):
    return f"'{attr.value}'"

  def KernelAttribute(attr):
    return "None"

  def GroupInfoAttribute(attr):
    return "None"

  def CINNKernelInfoAttribute(attr):
    return "None"

  def SymbolAttribute(attr):
    return "None"

  def UnclassifiedAttribute(attr):
    return "None"
