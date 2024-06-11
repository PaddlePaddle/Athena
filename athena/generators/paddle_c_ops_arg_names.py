from athena.generators.autogen_op_name_and_arg_names import op_name_x_arg_names

def GetCOpsArgNames(op_name):
  return op_name2arg_names.get(op_name, None)

op_name2arg_names = {
  k:v for k, *v in op_name_x_arg_names
}
