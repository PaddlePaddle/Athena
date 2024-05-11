class PirProgram_1:

  def __init__(self):

    self.data_201 = self.Op("pd_op.data", 201, input_types=[], output_types=[self.t_dtensor([1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), place=self.a_place("undefined", 0), name=self.a_str("x"), shape=self.a_intarray(1, -1, 768), stop_gradient=self.a_array(self.a_bool(False)), __operands_symbols_signature__=self.a_array(), __results_symbols_signature__=self.a_array(self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1), self.s_str("S0"), self.s_int64(768)], None)))))

    self.full_202 = self.Op("pd_op.full", 202, input_types=[], output_types=[self.t_dtensor([1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), place=self.a_place("undefined", 0), shape=self.a_intarray(1), value=self.a_f32("0"), stop_gradient=self.a_array(self.a_bool(True)), __operands_symbols_signature__=self.a_array(), __results_symbols_signature__=self.a_array(self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1)], [self.s_int64(0)])))))

    self.reduce_sum_244 = self.Op("cinn_op.reduce_sum", 244, input_types=[self.t_dtensor([1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(keep_dim=self.a_bool(False), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(), __operands_symbols_signature__=self.a_array(self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1), self.s_str("S0"), self.s_int64(768)], None))), __results_symbols_signature__=self.a_array(self.a_symbol(self.s_tensor_shape_or_data([], None)))))

    self.full_245 = self.Op("pd_op.full", 245, input_types=[], output_types=[self.t_dtensor([1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), place=self.a_place("undefined", 0), shape=self.a_intarray(1), value=self.a_f32("0"), stop_gradient=self.a_array(self.a_bool(True)), __operands_symbols_signature__=self.a_array(), __results_symbols_signature__=self.a_array(self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1)], [self.s_int64(0)])))))

    self.broadcast_246 = self.Op("cinn_op.broadcast", 246, input_types=[self.t_dtensor([], self.t_f32())], output_types=[self.t_dtensor([1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), out_shape=self.a_array(self.a_i64(1)), broadcast_axes=self.a_array(), __operands_symbols_signature__=self.a_array(self.a_symbol(self.s_tensor_shape_or_data([], None))), __results_symbols_signature__=self.a_array(self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1)], None)))))

    self.greater_than_247 = self.Op("pd_op.greater_than", 247, input_types=[self.t_dtensor([1], self.t_f32()), self.t_dtensor([1], self.t_f32())], output_types=[self.t_dtensor([1], self.t_bool())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), __operands_symbols_signature__=self.a_array(self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1)], None)), self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1)], [self.s_int64(0)]))), __results_symbols_signature__=self.a_array(self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1)], None)))))

    self.full_248 = self.Op("pd_op.full", 248, input_types=[], output_types=[self.t_dtensor([1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), place=self.a_place("undefined", 0), shape=self.a_intarray(1), value=self.a_f32("1"), stop_gradient=self.a_array(self.a_bool(True)), __operands_symbols_signature__=self.a_array(), __results_symbols_signature__=self.a_array(self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1)], [self.s_int64(1)])))))

    self.less_than_249 = self.Op("pd_op.less_than", 249, input_types=[self.t_dtensor([1], self.t_f32()), self.t_dtensor([1], self.t_f32())], output_types=[self.t_dtensor([1], self.t_bool())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), __operands_symbols_signature__=self.a_array(self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1)], [self.s_int64(0)])), self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1)], [self.s_int64(1)]))), __results_symbols_signature__=self.a_array(self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1)], None)))))

    self.logical_and_250 = self.Op("pd_op.logical_and", 250, input_types=[self.t_dtensor([1], self.t_bool()), self.t_dtensor([1], self.t_bool())], output_types=[self.t_dtensor([1], self.t_bool())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), __operands_symbols_signature__=self.a_array(self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1)], None)), self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1)], None))), __results_symbols_signature__=self.a_array(self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1)], None)))))

    self.yield_252 = self.Op("cf.yield", 252, input_types=[self.t_dtensor([1], self.t_bool())], output_types=[], attrs=dict(__operands_symbols_signature__=self.a_array(self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1)], None))), __results_symbols_signature__=self.a_array()))

    self.fusion_251 = self.Op("cinn_op.fusion", 251, input_types=[], output_types=[self.t_dtensor([1], self.t_bool())], attrs=dict(group_info=self.a_group_info(), __operands_symbols_signature__=self.a_array(), __results_symbols_signature__=self.a_array(self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1)], None)))), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.scale_256 = self.Op("cinn_op.scale", 256, input_types=[self.t_dtensor([1], self.t_f32())], output_types=[self.t_dtensor([1], self.t_f32())], attrs=dict(bias=self.a_f32("1"), stop_gradient=self.a_array(self.a_bool(True)), bias_after_scale=self.a_bool(True), scale=self.a_f32("1"), __operands_symbols_signature__=self.a_array(self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1)], None))), __results_symbols_signature__=self.a_array(self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1)], None)))))

    self.yield_258 = self.Op("cf.yield", 258, input_types=[self.t_dtensor([1], self.t_f32())], output_types=[], attrs=dict(__operands_symbols_signature__=self.a_array(self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1)], None))), __results_symbols_signature__=self.a_array()))

    self.fusion_257 = self.Op("cinn_op.fusion", 257, input_types=[], output_types=[self.t_dtensor([1], self.t_f32())], attrs=dict(group_info=self.a_group_info(), __operands_symbols_signature__=self.a_array(), __results_symbols_signature__=self.a_array(self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1)], None)))), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.exp_259 = self.Op("pd_op.exp", 259, input_types=[self.t_dtensor([1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), __operands_symbols_signature__=self.a_array(self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1), self.s_str("S0"), self.s_int64(768)], None))), __results_symbols_signature__=self.a_array(self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1), self.s_str("S0"), self.s_int64(768)], None)))))

    self.subtract_260 = self.Op("pd_op.subtract", 260, input_types=[self.t_dtensor([1, -1, 768], self.t_f32()), self.t_dtensor([1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), __operands_symbols_signature__=self.a_array(self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1), self.s_str("S0"), self.s_int64(768)], None)), self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1), self.s_str("S0"), self.s_int64(768)], None))), __results_symbols_signature__=self.a_array(self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1), self.s_str("S0"), self.s_int64(768)], None)))))

    self.yield_262 = self.Op("cf.yield", 262, input_types=[self.t_dtensor([1, -1, 768], self.t_f32())], output_types=[], attrs=dict(__operands_symbols_signature__=self.a_array(self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1), self.s_str("S0"), self.s_int64(768)], None))), __results_symbols_signature__=self.a_array()))

    self.fusion_261 = self.Op("cinn_op.fusion", 261, input_types=[], output_types=[self.t_dtensor([1, -1, 768], self.t_f32())], attrs=dict(group_info=self.a_group_info(), __operands_symbols_signature__=self.a_array(), __results_symbols_signature__=self.a_array(self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1), self.s_str("S0"), self.s_int64(768)], None)))), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.reduce_sum_263 = self.Op("cinn_op.reduce_sum", 263, input_types=[self.t_dtensor([1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(keep_dim=self.a_bool(False), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(), __operands_symbols_signature__=self.a_array(self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1), self.s_str("S0"), self.s_int64(768)], None))), __results_symbols_signature__=self.a_array(self.a_symbol(self.s_tensor_shape_or_data([], None)))))

    self.full_264 = self.Op("pd_op.full", 264, input_types=[], output_types=[self.t_dtensor([1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), place=self.a_place("undefined", 0), shape=self.a_intarray(1), value=self.a_f32("0"), stop_gradient=self.a_array(self.a_bool(True)), __operands_symbols_signature__=self.a_array(), __results_symbols_signature__=self.a_array(self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1)], [self.s_int64(0)])))))

    self.broadcast_265 = self.Op("cinn_op.broadcast", 265, input_types=[self.t_dtensor([], self.t_f32())], output_types=[self.t_dtensor([1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), out_shape=self.a_array(self.a_i64(1)), broadcast_axes=self.a_array(), __operands_symbols_signature__=self.a_array(self.a_symbol(self.s_tensor_shape_or_data([], None))), __results_symbols_signature__=self.a_array(self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1)], None)))))

    self.greater_than_266 = self.Op("pd_op.greater_than", 266, input_types=[self.t_dtensor([1], self.t_f32()), self.t_dtensor([1], self.t_f32())], output_types=[self.t_dtensor([1], self.t_bool())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), __operands_symbols_signature__=self.a_array(self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1)], None)), self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1)], [self.s_int64(0)]))), __results_symbols_signature__=self.a_array(self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1)], None)))))

    self.full_267 = self.Op("pd_op.full", 267, input_types=[], output_types=[self.t_dtensor([1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), place=self.a_place("undefined", 0), shape=self.a_intarray(1), value=self.a_f32("1"), stop_gradient=self.a_array(self.a_bool(True)), __operands_symbols_signature__=self.a_array(), __results_symbols_signature__=self.a_array(self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1)], [self.s_int64(1)])))))

    self.less_than_268 = self.Op("pd_op.less_than", 268, input_types=[self.t_dtensor([1], self.t_f32()), self.t_dtensor([1], self.t_f32())], output_types=[self.t_dtensor([1], self.t_bool())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), __operands_symbols_signature__=self.a_array(self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1)], None)), self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1)], [self.s_int64(1)]))), __results_symbols_signature__=self.a_array(self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1)], None)))))

    self.logical_and_269 = self.Op("pd_op.logical_and", 269, input_types=[self.t_dtensor([1], self.t_bool()), self.t_dtensor([1], self.t_bool())], output_types=[self.t_dtensor([1], self.t_bool())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), __operands_symbols_signature__=self.a_array(self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1)], None)), self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1)], None))), __results_symbols_signature__=self.a_array(self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1)], None)))))

    self.yield_271 = self.Op("cf.yield", 271, input_types=[self.t_dtensor([1], self.t_bool())], output_types=[], attrs=dict(__operands_symbols_signature__=self.a_array(self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1)], None))), __results_symbols_signature__=self.a_array()))

    self.fusion_270 = self.Op("cinn_op.fusion", 270, input_types=[], output_types=[self.t_dtensor([1], self.t_bool())], attrs=dict(group_info=self.a_group_info(), __operands_symbols_signature__=self.a_array(), __results_symbols_signature__=self.a_array(self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1)], None)))), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.yield_229 = self.Op("cf.yield", 229, input_types=[self.t_dtensor([1], self.t_bool()), self.t_dtensor([1], self.t_f32()), self.t_dtensor([1, -1, 768], self.t_f32())], output_types=[], attrs=dict(__operands_symbols_signature__=self.a_array(self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1)], None)), self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1)], None)), self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1), self.s_str("S0"), self.s_int64(768)], None))), __results_symbols_signature__=self.a_array()))

    self.while_217 = self.Op("pd_op.while", 217, input_types=[self.t_dtensor([1], self.t_bool()), self.t_dtensor([1], self.t_f32()), self.t_dtensor([1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([1], self.t_f32()), self.t_dtensor([1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True), self.a_bool(False)), __operands_symbols_signature__=self.a_array(self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1)], None)), self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1)], [self.s_int64(0)])), self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1), self.s_str("S0"), self.s_int64(768)], None))), __results_symbols_signature__=self.a_array(self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1)], None)), self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1), self.s_str("S0"), self.s_int64(768)], None)))), block_positional_arg_names=[[["arg_1212682608", "arg_1212717648"]]], block_keyword_arg_names=[[{}]])

    self.exp_253 = self.Op("pd_op.exp", 253, input_types=[self.t_dtensor([1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), __operands_symbols_signature__=self.a_array(self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1), self.s_str("S0"), self.s_int64(768)], None))), __results_symbols_signature__=self.a_array(self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1), self.s_str("S0"), self.s_int64(768)], None)))))

    self.yield_255 = self.Op("cf.yield", 255, input_types=[self.t_dtensor([1, -1, 768], self.t_f32())], output_types=[], attrs=dict(__operands_symbols_signature__=self.a_array(self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1), self.s_str("S0"), self.s_int64(768)], None))), __results_symbols_signature__=self.a_array()))

    self.fusion_254 = self.Op("cinn_op.fusion", 254, input_types=[], output_types=[self.t_dtensor([1, -1, 768], self.t_f32())], attrs=dict(group_info=self.a_group_info(), __operands_symbols_signature__=self.a_array(), __results_symbols_signature__=self.a_array(self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1), self.s_str("S0"), self.s_int64(768)], None)))), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.shadow_output_231 = self.Op("builtin.shadow_output", 231, input_types=[self.t_dtensor([1, -1, 768], self.t_f32())], output_types=[], attrs=dict(output_name=self.a_str("output_0"), __operands_symbols_signature__=self.a_array(self.a_symbol(self.s_tensor_shape_or_data([self.s_int64(1), self.s_str("S0"), self.s_int64(768)], None))), __results_symbols_signature__=self.a_array()))

    self.module_199 = self.Op("builtin.module", 199, input_types=[], output_types=[], attrs=dict(program=self.a_pointer("0x4890b720"), __operands_symbols_signature__=self.a_array(), __results_symbols_signature__=self.a_array()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    

  def fusion_251_block00(self, call, data_2010, full_2020):

    def ret_lambda():

      reduce_sum_2440, = call(self.reduce_sum_244, data_2010)

      full_2450, = call(self.full_245)

      broadcast_2460, = call(self.broadcast_246, reduce_sum_2440)

      greater_than_2470, = call(self.greater_than_247, broadcast_2460, full_2450)

      full_2480, = call(self.full_248)

      less_than_2490, = call(self.less_than_249, full_2020, full_2480)

      logical_and_2500, = call(self.logical_and_250, greater_than_2470, less_than_2490)

      return call(self.yield_252, logical_and_2500)

    return ret_lambda

    

  def fusion_257_block00(self, call, arg_1212682608):

    def ret_lambda():

      scale_2560, = call(self.scale_256, arg_1212682608)

      return call(self.yield_258, scale_2560)

    return ret_lambda

    

  def fusion_261_block00(self, call, arg_1212717648):

    def ret_lambda():

      exp_2590, = call(self.exp_259, arg_1212717648)

      subtract_2600, = call(self.subtract_260, exp_2590, arg_1212717648)

      return call(self.yield_262, subtract_2600)

    return ret_lambda

    

  def fusion_270_block00(self, call, fusion_2610, fusion_2570):

    def ret_lambda():

      reduce_sum_2630, = call(self.reduce_sum_263, fusion_2610)

      full_2640, = call(self.full_264)

      broadcast_2650, = call(self.broadcast_265, reduce_sum_2630)

      greater_than_2660, = call(self.greater_than_266, broadcast_2650, full_2640)

      full_2670, = call(self.full_267)

      less_than_2680, = call(self.less_than_268, fusion_2570, full_2670)

      logical_and_2690, = call(self.logical_and_269, greater_than_2660, less_than_2680)

      return call(self.yield_271, logical_and_2690)

    return ret_lambda

    

  def while_217_block00(self, call):

    def ret_lambda(arg_1212682608, arg_1212717648):

      fusion_2570, = call(self.fusion_257, blocks=[[(self.fusion_257_block00, arg_1212682608)]])

      fusion_2610, = call(self.fusion_261, blocks=[[(self.fusion_261_block00, arg_1212717648)]])

      fusion_2700, = call(self.fusion_270, blocks=[[(self.fusion_270_block00, fusion_2610, fusion_2570)]])

      return call(self.yield_229, fusion_2700, fusion_2570, fusion_2610)

    return ret_lambda

    

  def fusion_254_block00(self, call, while_2171):

    def ret_lambda():

      exp_2530, = call(self.exp_253, while_2171)

      return call(self.yield_255, exp_2530)

    return ret_lambda

    

  def module_199_block00(self, call):

    def ret_lambda():

      data_2010, = call(self.data_201)

      full_2020, = call(self.full_202)

      fusion_2510, = call(self.fusion_251, blocks=[[(self.fusion_251_block00, data_2010, full_2020)]])

      while_2170, while_2171, = call(self.while_217, fusion_2510, full_2020, data_2010, blocks=[[(self.while_217_block00,)]])

      fusion_2540, = call(self.fusion_254, blocks=[[(self.fusion_254_block00, while_2171)]])

      call(self.shadow_output_231, fusion_2540)

    return ret_lambda

    

  def __call__(self, call, *args, **kwargs):

    self.SetArgs(args)

    self.SetKeywordArgs(kwargs)

    return call(self.module_199, blocks=[[(self.module_199_block00,)]])


