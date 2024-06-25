from athena.generators.autogen_op_name_and_arg_names import op_name_x_arg_names

def GetCOpsArgNames(op_name):
  return op_name2arg_names.get(op_name, None)


op_name2args = {
  op_name:args for op_name, *args in op_name_x_arg_names
}

op_name2arg_names = {
  op_name:[a[1] for a in args] for op_name, *args in op_name_x_arg_names
}
