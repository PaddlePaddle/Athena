class PirProgram_1837543161329705917:

  def __init__(self):

    self.data_20 = self.Op("pd_op.data", 20, input_types=[], output_types=[self.t_dtensor([4, 6], self.t_f32())], attrs={"stop_gradient":self.a_array(self.a_bool(True)), "name":self.a_str("x"), "shape":self.a_intarray(4, 6), "dtype":self.a_dtype("float32"), "place":self.a_place("undefined", 0), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.full_21 = self.Op("pd_op.full", 21, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"stop_gradient":self.a_array(self.a_bool(True)), "shape":self.a_intarray(1), "value":self.a_f64("1"), "dtype":self.a_dtype("int32"), "place":self.a_place("cpu"), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.split_with_num_22 = self.Op("pd_op.split_with_num", 22, input_types=[self.t_dtensor([4, 6], self.t_f32()), self.t_dtensor([1], self.t_i32())], output_types=[self.t_vec(self.t_dtensor([4, 3], self.t_f32()), self.t_dtensor([4, 3], self.t_f32()))], attrs={"stop_gradient":self.a_array(self.a_bool(True)), "num":self.a_i32(2), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.split_23 = self.Op("builtin.split", 23, input_types=[self.t_vec(self.t_dtensor([4, 3], self.t_f32()), self.t_dtensor([4, 3], self.t_f32()))], output_types=[self.t_dtensor([4, 3], self.t_f32()), self.t_dtensor([4, 3], self.t_f32())], attrs={"stop_gradient":self.a_array(self.a_bool(True), self.a_bool(True)), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.shadow_output_24 = self.Op("builtin.shadow_output", 24, input_types=[self.t_dtensor([4, 3], self.t_f32())], output_types=[], attrs={"output_name":self.a_str("output_0"), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array()})

    self.shadow_output_25 = self.Op("builtin.shadow_output", 25, input_types=[self.t_dtensor([4, 3], self.t_f32())], output_types=[], attrs={"output_name":self.a_str("output_1"), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array()})

    self.module_18 = self.Op("builtin.module", 18, input_types=[], output_types=[], attrs={"program":self.a_pointer("0xb66bb90"), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array()}, block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]], block_positional_arg_types=[[[]]], block_keyword_arg_types=[[[]]], )

    

  def module_18_block00(self, call):

    def ret_lambda_module_18_block00():

      data_200, = call(self.data_20)

      full_210, = call(self.full_21)

      split_with_num_220, = call(self.split_with_num_22, data_200, full_210)

      split_230, split_231, = call(self.split_23, split_with_num_220)

      call(self.shadow_output_24, split_230)

      call(self.shadow_output_25, split_231)

    return ret_lambda_module_18_block00

    

  def __call__(self, call, *args, **kwargs):

    self.SetArgs(args)

    self.SetKeywordArgs(kwargs)

    return call(self.module_18, blocks=[[(self.module_18_block00,)]])


