class PirProgram_0:

  def __init__(self):

    self.data_201 = self.Op("pd_op.data", 201, input_types=[], output_types=[self.t_dtensor([1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), place=self.a_place("undefined", 0), name=self.a_str("x"), shape=self.a_intarray(1, -1, 768), stop_gradient=self.a_array(self.a_bool(False))))

    self.full_202 = self.Op("pd_op.full", 202, input_types=[], output_types=[self.t_dtensor([1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), place=self.a_place("undefined", 0), shape=self.a_intarray(1), value=self.a_f32("0"), stop_gradient=self.a_array(self.a_bool(True))))

    self.reduce_sum_233 = self.Op("cinn_op.reduce_sum", 233, input_types=[self.t_dtensor([1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(keep_dim=self.a_bool(False), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array()))

    self.full_212 = self.Op("pd_op.full", 212, input_types=[], output_types=[self.t_dtensor([1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), place=self.a_place("undefined", 0), shape=self.a_intarray(1), value=self.a_f32("0"), stop_gradient=self.a_array(self.a_bool(True))))

    self.greater_than_213 = self.Op("pd_op.greater_than", 213, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([1], self.t_f32())], output_types=[self.t_dtensor([1], self.t_bool())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.full_214 = self.Op("pd_op.full", 214, input_types=[], output_types=[self.t_dtensor([1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), place=self.a_place("undefined", 0), shape=self.a_intarray(1), value=self.a_f32("1"), stop_gradient=self.a_array(self.a_bool(True))))

    self.less_than_215 = self.Op("pd_op.less_than", 215, input_types=[self.t_dtensor([1], self.t_f32()), self.t_dtensor([1], self.t_f32())], output_types=[self.t_dtensor([1], self.t_bool())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True))))

    self.logical_and_216 = self.Op("pd_op.logical_and", 216, input_types=[self.t_dtensor([1], self.t_bool()), self.t_dtensor([1], self.t_bool())], output_types=[self.t_dtensor([1], self.t_bool())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True))))

    self.yield_237 = self.Op("cf.yield", 237, input_types=[self.t_dtensor([1], self.t_bool())], output_types=[], attrs=dict())

    self.group_236 = self.Op("cinn_op.group", 236, input_types=[], output_types=[self.t_dtensor([1], self.t_bool())], attrs=dict(), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.exp_218 = self.Op("pd_op.exp", 218, input_types=[self.t_dtensor([1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.subtract_219 = self.Op("pd_op.subtract", 219, input_types=[self.t_dtensor([1, -1, 768], self.t_f32()), self.t_dtensor([1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_235 = self.Op("cinn_op.reduce_sum", 235, input_types=[self.t_dtensor([1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(keep_dim=self.a_bool(False), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array()))

    self.scale_234 = self.Op("cinn_op.scale", 234, input_types=[self.t_dtensor([1], self.t_f32())], output_types=[self.t_dtensor([1], self.t_f32())], attrs=dict(bias=self.a_f32("1"), stop_gradient=self.a_array(self.a_bool(True)), bias_after_scale=self.a_bool(True), scale=self.a_f32("1")))

    self.full_224 = self.Op("pd_op.full", 224, input_types=[], output_types=[self.t_dtensor([1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), place=self.a_place("undefined", 0), shape=self.a_intarray(1), value=self.a_f32("0"), stop_gradient=self.a_array(self.a_bool(True))))

    self.greater_than_225 = self.Op("pd_op.greater_than", 225, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([1], self.t_f32())], output_types=[self.t_dtensor([1], self.t_bool())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.full_226 = self.Op("pd_op.full", 226, input_types=[], output_types=[self.t_dtensor([1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), place=self.a_place("undefined", 0), shape=self.a_intarray(1), value=self.a_f32("1"), stop_gradient=self.a_array(self.a_bool(True))))

    self.less_than_227 = self.Op("pd_op.less_than", 227, input_types=[self.t_dtensor([1], self.t_f32()), self.t_dtensor([1], self.t_f32())], output_types=[self.t_dtensor([1], self.t_bool())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True))))

    self.logical_and_228 = self.Op("pd_op.logical_and", 228, input_types=[self.t_dtensor([1], self.t_bool()), self.t_dtensor([1], self.t_bool())], output_types=[self.t_dtensor([1], self.t_bool())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True))))

    self.yield_241 = self.Op("cf.yield", 241, input_types=[self.t_dtensor([1, -1, 768], self.t_f32()), self.t_dtensor([1], self.t_f32()), self.t_dtensor([1], self.t_bool())], output_types=[], attrs=dict())

    self.group_240 = self.Op("cinn_op.group", 240, input_types=[], output_types=[self.t_dtensor([1, -1, 768], self.t_f32()), self.t_dtensor([1], self.t_f32()), self.t_dtensor([1], self.t_bool())], attrs=dict(), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.yield_229 = self.Op("cf.yield", 229, input_types=[self.t_dtensor([1], self.t_bool()), self.t_dtensor([1], self.t_f32()), self.t_dtensor([1, -1, 768], self.t_f32())], output_types=[], attrs=dict())

    self.while_217 = self.Op("pd_op.while", 217, input_types=[self.t_dtensor([1], self.t_bool()), self.t_dtensor([1], self.t_f32()), self.t_dtensor([1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([1], self.t_f32()), self.t_dtensor([1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True), self.a_bool(False))), block_positional_arg_names=[[["arg_1225560416", "arg_1225560272"]]], block_keyword_arg_names=[[{}]])

    self.exp_230 = self.Op("pd_op.exp", 230, input_types=[self.t_dtensor([1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.yield_239 = self.Op("cf.yield", 239, input_types=[self.t_dtensor([1, -1, 768], self.t_f32())], output_types=[], attrs=dict())

    self.group_238 = self.Op("cinn_op.group", 238, input_types=[], output_types=[self.t_dtensor([1, -1, 768], self.t_f32())], attrs=dict(), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.shadow_output_231 = self.Op("builtin.shadow_output", 231, input_types=[self.t_dtensor([1, -1, 768], self.t_f32())], output_types=[], attrs=dict(output_name=self.a_str("output_1")))

    self.module_199 = self.Op("builtin.module", 199, input_types=[], output_types=[], attrs=dict(program=self.a_pointer("0x48b86270")), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    

  def group_236_block00(self, call, data_2010, full_2020):

    def ret_lambda():

      reduce_sum_2330, = call(self.reduce_sum_233, data_2010)

      full_2120, = call(self.full_212)

      greater_than_2130, = call(self.greater_than_213, reduce_sum_2330, full_2120)

      full_2140, = call(self.full_214)

      less_than_2150, = call(self.less_than_215, full_2020, full_2140)

      logical_and_2160, = call(self.logical_and_216, greater_than_2130, less_than_2150)

      return call(self.yield_237, logical_and_2160)

    return ret_lambda

    

  def group_240_block00(self, call, arg_1225560272, arg_1225560416):

    def ret_lambda():

      exp_2180, = call(self.exp_218, arg_1225560272)

      subtract_2190, = call(self.subtract_219, exp_2180, arg_1225560272)

      reduce_sum_2350, = call(self.reduce_sum_235, subtract_2190)

      scale_2340, = call(self.scale_234, arg_1225560416)

      full_2240, = call(self.full_224)

      greater_than_2250, = call(self.greater_than_225, reduce_sum_2350, full_2240)

      full_2260, = call(self.full_226)

      less_than_2270, = call(self.less_than_227, scale_2340, full_2260)

      logical_and_2280, = call(self.logical_and_228, greater_than_2250, less_than_2270)

      return call(self.yield_241, subtract_2190, scale_2340, logical_and_2280)

    return ret_lambda

    

  def while_217_block00(self, call):

    def ret_lambda(arg_1225560416, arg_1225560272):

      group_2400, group_2401, group_2402, = call(self.group_240, blocks=[[(self.group_240_block00, arg_1225560272, arg_1225560416)]])

      return call(self.yield_229, group_2402, group_2401, group_2400)

    return ret_lambda

    

  def group_238_block00(self, call, while_2171):

    def ret_lambda():

      exp_2300, = call(self.exp_230, while_2171)

      return call(self.yield_239, exp_2300)

    return ret_lambda

    

  def module_199_block00(self, call):

    def ret_lambda():

      data_2010, = call(self.data_201)

      full_2020, = call(self.full_202)

      group_2360, = call(self.group_236, blocks=[[(self.group_236_block00, data_2010, full_2020)]])

      while_2170, while_2171, = call(self.while_217, group_2360, full_2020, data_2010, blocks=[[(self.while_217_block00,)]])

      group_2380, = call(self.group_238, blocks=[[(self.group_238_block00, while_2171)]])

      call(self.shadow_output_231, group_2380)

    return ret_lambda

    

  def __call__(self, call, *args, **kwargs):

    self.SetArgs(args)

    self.SetKeywordArgs(kwargs)

    return call(self.module_199, blocks=[[(self.module_199_block00,)]])


