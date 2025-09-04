class PirProgram_568323062710701940:

  def __init__(self):

    self.parameter_52 = self.Op("builtin.parameter", 52, input_types=[], output_types=[self.t_dtensor([1], self.t_f32())], attrs={"is_parameter":self.a_array(self.a_bool(True)), "is_distributed":self.a_array(self.a_bool(False)), "need_clip":self.a_array(self.a_bool(True)), "persistable":self.a_array(self.a_bool(True)), "stop_gradient":self.a_array(self.a_bool(False)), "trainable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("linear_2.b_0"), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_53 = self.Op("builtin.parameter", 53, input_types=[], output_types=[self.t_dtensor([5, 1], self.t_f32())], attrs={"is_parameter":self.a_array(self.a_bool(True)), "is_distributed":self.a_array(self.a_bool(False)), "need_clip":self.a_array(self.a_bool(True)), "persistable":self.a_array(self.a_bool(True)), "stop_gradient":self.a_array(self.a_bool(False)), "trainable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("linear_2.w_0"), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_54 = self.Op("builtin.parameter", 54, input_types=[], output_types=[self.t_dtensor([3], self.t_f32())], attrs={"is_parameter":self.a_array(self.a_bool(True)), "is_distributed":self.a_array(self.a_bool(False)), "need_clip":self.a_array(self.a_bool(True)), "persistable":self.a_array(self.a_bool(True)), "stop_gradient":self.a_array(self.a_bool(False)), "trainable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("linear_1.b_0"), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_55 = self.Op("builtin.parameter", 55, input_types=[], output_types=[self.t_dtensor([5, 3], self.t_f32())], attrs={"is_parameter":self.a_array(self.a_bool(True)), "is_distributed":self.a_array(self.a_bool(False)), "need_clip":self.a_array(self.a_bool(True)), "persistable":self.a_array(self.a_bool(True)), "stop_gradient":self.a_array(self.a_bool(False)), "trainable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("linear_1.w_0"), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_56 = self.Op("builtin.parameter", 56, input_types=[], output_types=[self.t_dtensor([5], self.t_f32())], attrs={"is_parameter":self.a_array(self.a_bool(True)), "is_distributed":self.a_array(self.a_bool(False)), "need_clip":self.a_array(self.a_bool(True)), "persistable":self.a_array(self.a_bool(True)), "stop_gradient":self.a_array(self.a_bool(False)), "trainable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("linear_0.b_0"), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_57 = self.Op("builtin.parameter", 57, input_types=[], output_types=[self.t_dtensor([10, 5], self.t_f32())], attrs={"is_parameter":self.a_array(self.a_bool(True)), "is_distributed":self.a_array(self.a_bool(False)), "need_clip":self.a_array(self.a_bool(True)), "persistable":self.a_array(self.a_bool(True)), "stop_gradient":self.a_array(self.a_bool(False)), "trainable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("linear_0.w_0"), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.data_58 = self.Op("pd_op.data", 58, input_types=[], output_types=[self.t_dtensor([-1, 10], self.t_f32())], attrs={"stop_gradient":self.a_array(self.a_bool(True)), "name":self.a_str("x"), "shape":self.a_intarray(-1, 10), "dtype":self.a_dtype("float32"), "place":self.a_place("undefined", 0), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.matmul_59 = self.Op("pd_op.matmul", 59, input_types=[self.t_dtensor([-1, 10], self.t_f32()), self.t_dtensor([10, 5], self.t_f32())], output_types=[self.t_dtensor([-1, 5], self.t_f32())], attrs={"struct_name":self.a_str("/Linear/"), "stop_gradient":self.a_array(self.a_bool(False)), "transpose_x":self.a_bool(False), "transpose_y":self.a_bool(False), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.add_60 = self.Op("pd_op.add", 60, input_types=[self.t_dtensor([-1, 5], self.t_f32()), self.t_dtensor([5], self.t_f32())], output_types=[self.t_dtensor([-1, 5], self.t_f32())], attrs={"struct_name":self.a_str("/Linear/"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.tanh_61 = self.Op("pd_op.tanh", 61, input_types=[self.t_dtensor([-1, 5], self.t_f32())], output_types=[self.t_dtensor([-1, 5], self.t_f32())], attrs={"stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.matmul_62 = self.Op("pd_op.matmul", 62, input_types=[self.t_dtensor([-1, 5], self.t_f32()), self.t_dtensor([5, 3], self.t_f32())], output_types=[self.t_dtensor([-1, 3], self.t_f32())], attrs={"struct_name":self.a_str("/Linear_1/"), "stop_gradient":self.a_array(self.a_bool(False)), "transpose_x":self.a_bool(False), "transpose_y":self.a_bool(False), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.add_63 = self.Op("pd_op.add", 63, input_types=[self.t_dtensor([-1, 3], self.t_f32()), self.t_dtensor([3], self.t_f32())], output_types=[self.t_dtensor([-1, 3], self.t_f32())], attrs={"struct_name":self.a_str("/Linear_1/"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.matmul_64 = self.Op("pd_op.matmul", 64, input_types=[self.t_dtensor([-1, 5], self.t_f32()), self.t_dtensor([5, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 1], self.t_f32())], attrs={"struct_name":self.a_str("/Linear_2/"), "stop_gradient":self.a_array(self.a_bool(False)), "transpose_x":self.a_bool(False), "transpose_y":self.a_bool(False), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.add_65 = self.Op("pd_op.add", 65, input_types=[self.t_dtensor([-1, 1], self.t_f32()), self.t_dtensor([1], self.t_f32())], output_types=[self.t_dtensor([-1, 1], self.t_f32())], attrs={"struct_name":self.a_str("/Linear_2/"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.shadow_output_66 = self.Op("builtin.shadow_output", 66, input_types=[self.t_dtensor([-1, 3], self.t_f32())], output_types=[], attrs={"output_name":self.a_str("output_0"), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array()})

    self.shadow_output_67 = self.Op("builtin.shadow_output", 67, input_types=[self.t_dtensor([-1, 1], self.t_f32())], output_types=[], attrs={"output_name":self.a_str("output_1"), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array()})

    self.module_50 = self.Op("builtin.module", 50, input_types=[], output_types=[], attrs={"program":self.a_pointer("0x97b8880"), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array()}, block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]], block_positional_arg_types=[[[]]], block_keyword_arg_types=[[[]]], )

    

  def module_50_block00(self, call):

    def ret_lambda_module_50_block00():

      parameter_520, = call(self.parameter_52)

      parameter_530, = call(self.parameter_53)

      parameter_540, = call(self.parameter_54)

      parameter_550, = call(self.parameter_55)

      parameter_560, = call(self.parameter_56)

      parameter_570, = call(self.parameter_57)

      data_580, = call(self.data_58)

      matmul_590, = call(self.matmul_59, data_580, parameter_570)

      add_600, = call(self.add_60, matmul_590, parameter_560)

      tanh_610, = call(self.tanh_61, add_600)

      matmul_620, = call(self.matmul_62, tanh_610, parameter_550)

      add_630, = call(self.add_63, matmul_620, parameter_540)

      matmul_640, = call(self.matmul_64, tanh_610, parameter_530)

      add_650, = call(self.add_65, matmul_640, parameter_520)

      call(self.shadow_output_66, add_630)

      call(self.shadow_output_67, add_650)

    return ret_lambda_module_50_block00

    

  def __call__(self, call, *args, **kwargs):

    self.SetArgs(args)

    self.SetKeywordArgs(kwargs)

    return call(self.module_50, blocks=[[(self.module_50_block00,)]])


