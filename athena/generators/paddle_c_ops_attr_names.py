from athena.generators.autogen_op_name_and_attr_names import op_name_x_attr_names

def GetCOpsAttrNames(op_name):
  return op_name2attr_names.get(op_name, None)

op_name2attr_names = {
  k:v for k, v in op_name_x_attr_names
}
