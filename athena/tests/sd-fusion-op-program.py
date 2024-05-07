class PirProgram_1:

  def __init__(self):

    self.parameter_4 = self.Op("builtin.parameter", 4, input_types=[], output_types=[self.t_dtensor([1, 77], self.t_i64())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("eager_tmp_0")))

    self.parameter_5 = self.Op("builtin.parameter", 5, input_types=[], output_types=[self.t_dtensor([49408, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("embedding_0.w_0")))

    self.parameter_6 = self.Op("builtin.parameter", 6, input_types=[], output_types=[self.t_dtensor([77, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("embedding_1.w_0")))

    self.parameter_7 = self.Op("builtin.parameter", 7, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_48.b_0")))

    self.parameter_8 = self.Op("builtin.parameter", 8, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_48.w_0")))

    self.parameter_9 = self.Op("builtin.parameter", 9, input_types=[], output_types=[self.t_dtensor([768, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_2.w_0")))

    self.parameter_10 = self.Op("builtin.parameter", 10, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_2.b_0")))

    self.parameter_11 = self.Op("builtin.parameter", 11, input_types=[], output_types=[self.t_dtensor([768, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_0.w_0")))

    self.parameter_12 = self.Op("builtin.parameter", 12, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_0.b_0")))

    self.parameter_13 = self.Op("builtin.parameter", 13, input_types=[], output_types=[self.t_dtensor([768, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_1.w_0")))

    self.parameter_14 = self.Op("builtin.parameter", 14, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_1.b_0")))

    self.parameter_15 = self.Op("builtin.parameter", 15, input_types=[], output_types=[self.t_dtensor([768, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_3.w_0")))

    self.parameter_16 = self.Op("builtin.parameter", 16, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_3.b_0")))

    self.parameter_17 = self.Op("builtin.parameter", 17, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_49.b_0")))

    self.parameter_18 = self.Op("builtin.parameter", 18, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_49.w_0")))

    self.parameter_19 = self.Op("builtin.parameter", 19, input_types=[], output_types=[self.t_dtensor([768, 3072], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_4.w_0")))

    self.parameter_20 = self.Op("builtin.parameter", 20, input_types=[], output_types=[self.t_dtensor([3072], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_4.b_0")))

    self.parameter_21 = self.Op("builtin.parameter", 21, input_types=[], output_types=[self.t_dtensor([3072, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_5.w_0")))

    self.parameter_22 = self.Op("builtin.parameter", 22, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_5.b_0")))

    self.parameter_23 = self.Op("builtin.parameter", 23, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_50.b_0")))

    self.parameter_24 = self.Op("builtin.parameter", 24, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_50.w_0")))

    self.parameter_25 = self.Op("builtin.parameter", 25, input_types=[], output_types=[self.t_dtensor([768, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_8.w_0")))

    self.parameter_26 = self.Op("builtin.parameter", 26, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_8.b_0")))

    self.parameter_27 = self.Op("builtin.parameter", 27, input_types=[], output_types=[self.t_dtensor([768, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_6.w_0")))

    self.parameter_28 = self.Op("builtin.parameter", 28, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_6.b_0")))

    self.parameter_29 = self.Op("builtin.parameter", 29, input_types=[], output_types=[self.t_dtensor([768, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_7.w_0")))

    self.parameter_30 = self.Op("builtin.parameter", 30, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_7.b_0")))

    self.parameter_31 = self.Op("builtin.parameter", 31, input_types=[], output_types=[self.t_dtensor([768, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_9.w_0")))

    self.parameter_32 = self.Op("builtin.parameter", 32, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_9.b_0")))

    self.parameter_33 = self.Op("builtin.parameter", 33, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_51.b_0")))

    self.parameter_34 = self.Op("builtin.parameter", 34, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_51.w_0")))

    self.parameter_35 = self.Op("builtin.parameter", 35, input_types=[], output_types=[self.t_dtensor([768, 3072], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_10.w_0")))

    self.parameter_36 = self.Op("builtin.parameter", 36, input_types=[], output_types=[self.t_dtensor([3072], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_10.b_0")))

    self.parameter_37 = self.Op("builtin.parameter", 37, input_types=[], output_types=[self.t_dtensor([3072, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_11.w_0")))

    self.parameter_38 = self.Op("builtin.parameter", 38, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_11.b_0")))

    self.parameter_39 = self.Op("builtin.parameter", 39, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_52.b_0")))

    self.parameter_40 = self.Op("builtin.parameter", 40, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_52.w_0")))

    self.parameter_41 = self.Op("builtin.parameter", 41, input_types=[], output_types=[self.t_dtensor([768, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_14.w_0")))

    self.parameter_42 = self.Op("builtin.parameter", 42, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_14.b_0")))

    self.parameter_43 = self.Op("builtin.parameter", 43, input_types=[], output_types=[self.t_dtensor([768, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_12.w_0")))

    self.parameter_44 = self.Op("builtin.parameter", 44, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_12.b_0")))

    self.parameter_45 = self.Op("builtin.parameter", 45, input_types=[], output_types=[self.t_dtensor([768, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_13.w_0")))

    self.parameter_46 = self.Op("builtin.parameter", 46, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_13.b_0")))

    self.parameter_47 = self.Op("builtin.parameter", 47, input_types=[], output_types=[self.t_dtensor([768, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_15.w_0")))

    self.parameter_48 = self.Op("builtin.parameter", 48, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_15.b_0")))

    self.parameter_49 = self.Op("builtin.parameter", 49, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_53.b_0")))

    self.parameter_50 = self.Op("builtin.parameter", 50, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_53.w_0")))

    self.parameter_51 = self.Op("builtin.parameter", 51, input_types=[], output_types=[self.t_dtensor([768, 3072], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_16.w_0")))

    self.parameter_52 = self.Op("builtin.parameter", 52, input_types=[], output_types=[self.t_dtensor([3072], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_16.b_0")))

    self.parameter_53 = self.Op("builtin.parameter", 53, input_types=[], output_types=[self.t_dtensor([3072, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_17.w_0")))

    self.parameter_54 = self.Op("builtin.parameter", 54, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_17.b_0")))

    self.parameter_55 = self.Op("builtin.parameter", 55, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_54.b_0")))

    self.parameter_56 = self.Op("builtin.parameter", 56, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_54.w_0")))

    self.parameter_57 = self.Op("builtin.parameter", 57, input_types=[], output_types=[self.t_dtensor([768, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_20.w_0")))

    self.parameter_58 = self.Op("builtin.parameter", 58, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_20.b_0")))

    self.parameter_59 = self.Op("builtin.parameter", 59, input_types=[], output_types=[self.t_dtensor([768, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_18.w_0")))

    self.parameter_60 = self.Op("builtin.parameter", 60, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_18.b_0")))

    self.parameter_61 = self.Op("builtin.parameter", 61, input_types=[], output_types=[self.t_dtensor([768, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_19.w_0")))

    self.parameter_62 = self.Op("builtin.parameter", 62, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_19.b_0")))

    self.parameter_63 = self.Op("builtin.parameter", 63, input_types=[], output_types=[self.t_dtensor([768, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_21.w_0")))

    self.parameter_64 = self.Op("builtin.parameter", 64, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_21.b_0")))

    self.parameter_65 = self.Op("builtin.parameter", 65, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_55.b_0")))

    self.parameter_66 = self.Op("builtin.parameter", 66, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_55.w_0")))

    self.parameter_67 = self.Op("builtin.parameter", 67, input_types=[], output_types=[self.t_dtensor([768, 3072], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_22.w_0")))

    self.parameter_68 = self.Op("builtin.parameter", 68, input_types=[], output_types=[self.t_dtensor([3072], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_22.b_0")))

    self.parameter_69 = self.Op("builtin.parameter", 69, input_types=[], output_types=[self.t_dtensor([3072, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_23.w_0")))

    self.parameter_70 = self.Op("builtin.parameter", 70, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_23.b_0")))

    self.parameter_71 = self.Op("builtin.parameter", 71, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_56.b_0")))

    self.parameter_72 = self.Op("builtin.parameter", 72, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_56.w_0")))

    self.parameter_73 = self.Op("builtin.parameter", 73, input_types=[], output_types=[self.t_dtensor([768, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_26.w_0")))

    self.parameter_74 = self.Op("builtin.parameter", 74, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_26.b_0")))

    self.parameter_75 = self.Op("builtin.parameter", 75, input_types=[], output_types=[self.t_dtensor([768, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_24.w_0")))

    self.parameter_76 = self.Op("builtin.parameter", 76, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_24.b_0")))

    self.parameter_77 = self.Op("builtin.parameter", 77, input_types=[], output_types=[self.t_dtensor([768, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_25.w_0")))

    self.parameter_78 = self.Op("builtin.parameter", 78, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_25.b_0")))

    self.parameter_79 = self.Op("builtin.parameter", 79, input_types=[], output_types=[self.t_dtensor([768, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_27.w_0")))

    self.parameter_80 = self.Op("builtin.parameter", 80, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_27.b_0")))

    self.parameter_81 = self.Op("builtin.parameter", 81, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_57.b_0")))

    self.parameter_82 = self.Op("builtin.parameter", 82, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_57.w_0")))

    self.parameter_83 = self.Op("builtin.parameter", 83, input_types=[], output_types=[self.t_dtensor([768, 3072], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_28.w_0")))

    self.parameter_84 = self.Op("builtin.parameter", 84, input_types=[], output_types=[self.t_dtensor([3072], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_28.b_0")))

    self.parameter_85 = self.Op("builtin.parameter", 85, input_types=[], output_types=[self.t_dtensor([3072, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_29.w_0")))

    self.parameter_86 = self.Op("builtin.parameter", 86, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_29.b_0")))

    self.parameter_87 = self.Op("builtin.parameter", 87, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_58.b_0")))

    self.parameter_88 = self.Op("builtin.parameter", 88, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_58.w_0")))

    self.parameter_89 = self.Op("builtin.parameter", 89, input_types=[], output_types=[self.t_dtensor([768, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_32.w_0")))

    self.parameter_90 = self.Op("builtin.parameter", 90, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_32.b_0")))

    self.parameter_91 = self.Op("builtin.parameter", 91, input_types=[], output_types=[self.t_dtensor([768, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_30.w_0")))

    self.parameter_92 = self.Op("builtin.parameter", 92, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_30.b_0")))

    self.parameter_93 = self.Op("builtin.parameter", 93, input_types=[], output_types=[self.t_dtensor([768, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_31.w_0")))

    self.parameter_94 = self.Op("builtin.parameter", 94, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_31.b_0")))

    self.parameter_95 = self.Op("builtin.parameter", 95, input_types=[], output_types=[self.t_dtensor([768, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_33.w_0")))

    self.parameter_96 = self.Op("builtin.parameter", 96, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_33.b_0")))

    self.parameter_97 = self.Op("builtin.parameter", 97, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_59.b_0")))

    self.parameter_98 = self.Op("builtin.parameter", 98, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_59.w_0")))

    self.parameter_99 = self.Op("builtin.parameter", 99, input_types=[], output_types=[self.t_dtensor([768, 3072], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_34.w_0")))

    self.parameter_100 = self.Op("builtin.parameter", 100, input_types=[], output_types=[self.t_dtensor([3072], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_34.b_0")))

    self.parameter_101 = self.Op("builtin.parameter", 101, input_types=[], output_types=[self.t_dtensor([3072, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_35.w_0")))

    self.parameter_102 = self.Op("builtin.parameter", 102, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_35.b_0")))

    self.parameter_103 = self.Op("builtin.parameter", 103, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_60.b_0")))

    self.parameter_104 = self.Op("builtin.parameter", 104, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_60.w_0")))

    self.parameter_105 = self.Op("builtin.parameter", 105, input_types=[], output_types=[self.t_dtensor([768, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_38.w_0")))

    self.parameter_106 = self.Op("builtin.parameter", 106, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_38.b_0")))

    self.parameter_107 = self.Op("builtin.parameter", 107, input_types=[], output_types=[self.t_dtensor([768, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_36.w_0")))

    self.parameter_108 = self.Op("builtin.parameter", 108, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_36.b_0")))

    self.parameter_109 = self.Op("builtin.parameter", 109, input_types=[], output_types=[self.t_dtensor([768, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_37.w_0")))

    self.parameter_110 = self.Op("builtin.parameter", 110, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_37.b_0")))

    self.parameter_111 = self.Op("builtin.parameter", 111, input_types=[], output_types=[self.t_dtensor([768, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_39.w_0")))

    self.parameter_112 = self.Op("builtin.parameter", 112, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_39.b_0")))

    self.parameter_113 = self.Op("builtin.parameter", 113, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_61.b_0")))

    self.parameter_114 = self.Op("builtin.parameter", 114, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_61.w_0")))

    self.parameter_115 = self.Op("builtin.parameter", 115, input_types=[], output_types=[self.t_dtensor([768, 3072], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_40.w_0")))

    self.parameter_116 = self.Op("builtin.parameter", 116, input_types=[], output_types=[self.t_dtensor([3072], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_40.b_0")))

    self.parameter_117 = self.Op("builtin.parameter", 117, input_types=[], output_types=[self.t_dtensor([3072, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_41.w_0")))

    self.parameter_118 = self.Op("builtin.parameter", 118, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_41.b_0")))

    self.parameter_119 = self.Op("builtin.parameter", 119, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_62.b_0")))

    self.parameter_120 = self.Op("builtin.parameter", 120, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_62.w_0")))

    self.parameter_121 = self.Op("builtin.parameter", 121, input_types=[], output_types=[self.t_dtensor([768, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_44.w_0")))

    self.parameter_122 = self.Op("builtin.parameter", 122, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_44.b_0")))

    self.parameter_123 = self.Op("builtin.parameter", 123, input_types=[], output_types=[self.t_dtensor([768, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_42.w_0")))

    self.parameter_124 = self.Op("builtin.parameter", 124, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_42.b_0")))

    self.parameter_125 = self.Op("builtin.parameter", 125, input_types=[], output_types=[self.t_dtensor([768, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_43.w_0")))

    self.parameter_126 = self.Op("builtin.parameter", 126, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_43.b_0")))

    self.parameter_127 = self.Op("builtin.parameter", 127, input_types=[], output_types=[self.t_dtensor([768, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_45.w_0")))

    self.parameter_128 = self.Op("builtin.parameter", 128, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_45.b_0")))

    self.parameter_129 = self.Op("builtin.parameter", 129, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_63.b_0")))

    self.parameter_130 = self.Op("builtin.parameter", 130, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_63.w_0")))

    self.parameter_131 = self.Op("builtin.parameter", 131, input_types=[], output_types=[self.t_dtensor([768, 3072], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_46.w_0")))

    self.parameter_132 = self.Op("builtin.parameter", 132, input_types=[], output_types=[self.t_dtensor([3072], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_46.b_0")))

    self.parameter_133 = self.Op("builtin.parameter", 133, input_types=[], output_types=[self.t_dtensor([3072, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_47.w_0")))

    self.parameter_134 = self.Op("builtin.parameter", 134, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_47.b_0")))

    self.parameter_135 = self.Op("builtin.parameter", 135, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_64.b_0")))

    self.parameter_136 = self.Op("builtin.parameter", 136, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_64.w_0")))

    self.parameter_137 = self.Op("builtin.parameter", 137, input_types=[], output_types=[self.t_dtensor([768, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_50.w_0")))

    self.parameter_138 = self.Op("builtin.parameter", 138, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_50.b_0")))

    self.parameter_139 = self.Op("builtin.parameter", 139, input_types=[], output_types=[self.t_dtensor([768, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_48.w_0")))

    self.parameter_140 = self.Op("builtin.parameter", 140, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_48.b_0")))

    self.parameter_141 = self.Op("builtin.parameter", 141, input_types=[], output_types=[self.t_dtensor([768, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_49.w_0")))

    self.parameter_142 = self.Op("builtin.parameter", 142, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_49.b_0")))

    self.parameter_143 = self.Op("builtin.parameter", 143, input_types=[], output_types=[self.t_dtensor([768, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_51.w_0")))

    self.parameter_144 = self.Op("builtin.parameter", 144, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_51.b_0")))

    self.parameter_145 = self.Op("builtin.parameter", 145, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_65.b_0")))

    self.parameter_146 = self.Op("builtin.parameter", 146, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_65.w_0")))

    self.parameter_147 = self.Op("builtin.parameter", 147, input_types=[], output_types=[self.t_dtensor([768, 3072], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_52.w_0")))

    self.parameter_148 = self.Op("builtin.parameter", 148, input_types=[], output_types=[self.t_dtensor([3072], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_52.b_0")))

    self.parameter_149 = self.Op("builtin.parameter", 149, input_types=[], output_types=[self.t_dtensor([3072, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_53.w_0")))

    self.parameter_150 = self.Op("builtin.parameter", 150, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_53.b_0")))

    self.parameter_151 = self.Op("builtin.parameter", 151, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_66.b_0")))

    self.parameter_152 = self.Op("builtin.parameter", 152, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_66.w_0")))

    self.parameter_153 = self.Op("builtin.parameter", 153, input_types=[], output_types=[self.t_dtensor([768, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_56.w_0")))

    self.parameter_154 = self.Op("builtin.parameter", 154, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_56.b_0")))

    self.parameter_155 = self.Op("builtin.parameter", 155, input_types=[], output_types=[self.t_dtensor([768, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_54.w_0")))

    self.parameter_156 = self.Op("builtin.parameter", 156, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_54.b_0")))

    self.parameter_157 = self.Op("builtin.parameter", 157, input_types=[], output_types=[self.t_dtensor([768, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_55.w_0")))

    self.parameter_158 = self.Op("builtin.parameter", 158, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_55.b_0")))

    self.parameter_159 = self.Op("builtin.parameter", 159, input_types=[], output_types=[self.t_dtensor([768, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_57.w_0")))

    self.parameter_160 = self.Op("builtin.parameter", 160, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_57.b_0")))

    self.parameter_161 = self.Op("builtin.parameter", 161, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_67.b_0")))

    self.parameter_162 = self.Op("builtin.parameter", 162, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_67.w_0")))

    self.parameter_163 = self.Op("builtin.parameter", 163, input_types=[], output_types=[self.t_dtensor([768, 3072], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_58.w_0")))

    self.parameter_164 = self.Op("builtin.parameter", 164, input_types=[], output_types=[self.t_dtensor([3072], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_58.b_0")))

    self.parameter_165 = self.Op("builtin.parameter", 165, input_types=[], output_types=[self.t_dtensor([3072, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_59.w_0")))

    self.parameter_166 = self.Op("builtin.parameter", 166, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_59.b_0")))

    self.parameter_167 = self.Op("builtin.parameter", 167, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_68.b_0")))

    self.parameter_168 = self.Op("builtin.parameter", 168, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_68.w_0")))

    self.parameter_169 = self.Op("builtin.parameter", 169, input_types=[], output_types=[self.t_dtensor([768, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_62.w_0")))

    self.parameter_170 = self.Op("builtin.parameter", 170, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_62.b_0")))

    self.parameter_171 = self.Op("builtin.parameter", 171, input_types=[], output_types=[self.t_dtensor([768, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_60.w_0")))

    self.parameter_172 = self.Op("builtin.parameter", 172, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_60.b_0")))

    self.parameter_173 = self.Op("builtin.parameter", 173, input_types=[], output_types=[self.t_dtensor([768, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_61.w_0")))

    self.parameter_174 = self.Op("builtin.parameter", 174, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_61.b_0")))

    self.parameter_175 = self.Op("builtin.parameter", 175, input_types=[], output_types=[self.t_dtensor([768, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_63.w_0")))

    self.parameter_176 = self.Op("builtin.parameter", 176, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_63.b_0")))

    self.parameter_177 = self.Op("builtin.parameter", 177, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_69.b_0")))

    self.parameter_178 = self.Op("builtin.parameter", 178, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_69.w_0")))

    self.parameter_179 = self.Op("builtin.parameter", 179, input_types=[], output_types=[self.t_dtensor([768, 3072], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_64.w_0")))

    self.parameter_180 = self.Op("builtin.parameter", 180, input_types=[], output_types=[self.t_dtensor([3072], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_64.b_0")))

    self.parameter_181 = self.Op("builtin.parameter", 181, input_types=[], output_types=[self.t_dtensor([3072, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_65.w_0")))

    self.parameter_182 = self.Op("builtin.parameter", 182, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_65.b_0")))

    self.parameter_183 = self.Op("builtin.parameter", 183, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_70.b_0")))

    self.parameter_184 = self.Op("builtin.parameter", 184, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_70.w_0")))

    self.parameter_185 = self.Op("builtin.parameter", 185, input_types=[], output_types=[self.t_dtensor([768, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_68.w_0")))

    self.parameter_186 = self.Op("builtin.parameter", 186, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_68.b_0")))

    self.parameter_187 = self.Op("builtin.parameter", 187, input_types=[], output_types=[self.t_dtensor([768, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_66.w_0")))

    self.parameter_188 = self.Op("builtin.parameter", 188, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_66.b_0")))

    self.parameter_189 = self.Op("builtin.parameter", 189, input_types=[], output_types=[self.t_dtensor([768, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_67.w_0")))

    self.parameter_190 = self.Op("builtin.parameter", 190, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_67.b_0")))

    self.parameter_191 = self.Op("builtin.parameter", 191, input_types=[], output_types=[self.t_dtensor([768, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_69.w_0")))

    self.parameter_192 = self.Op("builtin.parameter", 192, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_69.b_0")))

    self.parameter_193 = self.Op("builtin.parameter", 193, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_71.b_0")))

    self.parameter_194 = self.Op("builtin.parameter", 194, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_71.w_0")))

    self.parameter_195 = self.Op("builtin.parameter", 195, input_types=[], output_types=[self.t_dtensor([768, 3072], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_70.w_0")))

    self.parameter_196 = self.Op("builtin.parameter", 196, input_types=[], output_types=[self.t_dtensor([3072], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_70.b_0")))

    self.parameter_197 = self.Op("builtin.parameter", 197, input_types=[], output_types=[self.t_dtensor([3072, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_71.w_0")))

    self.parameter_198 = self.Op("builtin.parameter", 198, input_types=[], output_types=[self.t_dtensor([768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("linear_71.b_0")))

    self.parameter_199 = self.Op("builtin.parameter", 199, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_72.b_0")))

    self.parameter_200 = self.Op("builtin.parameter", 200, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(True)), stop_gradient=self.a_array(self.a_bool(False)), parameter_name=self.a_str("layer_norm_72.w_0")))

    self.feed_201 = self.Op("pd_op.feed", 201, input_types=[], output_types=[self.t_dtensor([-1, -1], self.t_i64())], attrs=dict(persistable=self.a_array(self.a_bool(False)), name=self.a_str("input_ids"), stop_gradient=self.a_array(self.a_bool(False)), col=self.a_i32(0)))

    self.shape_212 = self.Op("pd_op.shape", 212, input_types=[self.t_dtensor([-1, -1], self.t_i64())], output_types=[self.t_dtensor([2], self.t_i32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.slice_5646 = self.Op("cinn_op.slice", 5646, input_types=[self.t_dtensor([2], self.t_i32())], output_types=[self.t_dtensor([], self.t_i32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), decrease_axis=self.a_array(self.a_i64(0)), ends=self.a_array(self.a_i64(2)), infer_flags=self.a_array(self.a_i64(1)), axes=self.a_array(self.a_i64(0)), starts=self.a_array(self.a_i64(1))))

    self.yield_5648 = self.Op("cf.yield", 5648, input_types=[self.t_dtensor([], self.t_i32())], output_types=[], attrs=dict())

    self.fusion_5647 = self.Op("cinn_op.fusion", 5647, input_types=[], output_types=[self.t_dtensor([], self.t_i32())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.full_int_array_216 = self.Op("pd_op.full_int_array", 216, input_types=[], output_types=[self.t_dtensor([1], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), dtype=self.a_dtype("int64"), place=self.a_place("cpu"), value=self.a_array(self.a_i64(0))))

    self.combine_4012 = self.Op("builtin.combine", 4012, input_types=[self.t_dtensor([], self.t_i32())], output_types=[self.t_vec(self.t_dtensor([], self.t_i32()))], attrs=dict(stop_gradient=self.a_array(self.a_bool(True))))

    self.slice_218 = self.Op("pd_op.slice", 218, input_types=[self.t_dtensor([1, 77], self.t_i64()), self.t_dtensor([1], self.t_i64()), self.t_vec(self.t_dtensor([], self.t_i32()))], output_types=[self.t_dtensor([1, -1], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), decrease_axis=self.a_array(), persistable=self.a_array(self.a_bool(False)), axes=self.a_array(self.a_i64(1)), infer_flags=self.a_array(self.a_i64(-1))))

    self.embedding_219 = self.Op("pd_op.embedding", 219, input_types=[self.t_dtensor([-1, -1], self.t_i64()), self.t_dtensor([49408, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), padding_idx=self.a_i64(-1), stop_gradient=self.a_array(self.a_bool(False)), sparse=self.a_bool(False)))

    self.cast_5649 = self.Op("pd_op.cast", 5649, input_types=[self.t_dtensor([1, -1], self.t_i64())], output_types=[self.t_dtensor([1, -1], self.t_i64())], attrs=dict(persistable=self.a_array(self.a_bool(False)), dtype=self.a_dtype("int64"), stop_gradient=self.a_array(self.a_bool(False))))

    self.yield_5651 = self.Op("cf.yield", 5651, input_types=[self.t_dtensor([1, -1], self.t_i64())], output_types=[], attrs=dict())

    self.fusion_5650 = self.Op("cinn_op.fusion", 5650, input_types=[], output_types=[self.t_dtensor([1, -1], self.t_i64())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.embedding_221 = self.Op("pd_op.embedding", 221, input_types=[self.t_dtensor([1, -1], self.t_i64()), self.t_dtensor([77, 768], self.t_f16())], output_types=[self.t_dtensor([1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), padding_idx=self.a_i64(-1), stop_gradient=self.a_array(self.a_bool(False)), sparse=self.a_bool(False)))

    self.full_5652 = self.Op("pd_op.full", 5652, input_types=[], output_types=[self.t_dtensor([1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("1"), shape=self.a_intarray(1), place=self.a_place("cpu"), dtype=self.a_dtype("float32")))

    self.cast_5653 = self.Op("pd_op.cast", 5653, input_types=[self.t_dtensor([1], self.t_f32())], output_types=[self.t_dtensor([1], self.t_f16())], attrs=dict(dtype=self.a_dtype("float16"), stop_gradient=self.a_array(self.a_bool(True))))

    self.generate_shape_5654 = self.Op("cinn_op.generate_shape", 5654, input_types=[self.t_dtensor([-1, -1], self.t_i64())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(1), self.a_str("S1"), self.a_str("S1")), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5655 = self.Op("pd_op.expand", 5655, input_types=[self.t_dtensor([1], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_5656 = self.Op("pd_op.cast", 5656, input_types=[self.t_dtensor([-1, -1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, -1, -1], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(False)), dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.scale_5657 = self.Op("cinn_op.scale", 5657, input_types=[self.t_dtensor([-1, -1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, -1, -1], self.t_f32())], attrs=dict(bias=self.a_f32("0"), stop_gradient=self.a_array(self.a_bool(False)), bias_after_scale=self.a_bool(True), scale=self.a_f32("-3.40282e+38")))

    self.cast_5658 = self.Op("pd_op.cast", 5658, input_types=[self.t_dtensor([-1, -1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, -1, -1], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), dtype=self.a_dtype("float16"), stop_gradient=self.a_array(self.a_bool(False))))

    self.yield_5660 = self.Op("cf.yield", 5660, input_types=[self.t_dtensor([-1, -1, -1, -1], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_5659 = self.Op("cinn_op.fusion", 5659, input_types=[], output_types=[self.t_dtensor([-1, -1, -1, -1], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.triu_233 = self.Op("pd_op.triu", 233, input_types=[self.t_dtensor([-1, -1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, -1, -1], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), diagonal=self.a_i32(1), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_5661 = self.Op("cinn_op.generate_shape", 5661, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5662 = self.Op("pd_op.expand", 5662, input_types=[self.t_dtensor([1, -1, 768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_5663 = self.Op("pd_op.add", 5663, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.yield_5665 = self.Op("cf.yield", 5665, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_5664 = self.Op("cinn_op.fusion", 5664, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.cast_5666 = self.Op("pd_op.cast", 5666, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_5667 = self.Op("cinn_op.reduce_sum", 5667, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.yield_5669 = self.Op("cf.yield", 5669, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[], attrs=dict())

    self.fusion_5668 = self.Op("cinn_op.fusion", 5668, input_types=[], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.cast_5670 = self.Op("pd_op.cast", 5670, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.full_5671 = self.Op("pd_op.full", 5671, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_5672 = self.Op("cinn_op.generate_shape", 5672, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5673 = self.Op("pd_op.expand", 5673, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_5674 = self.Op("pd_op.divide", 5674, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_5675 = self.Op("cinn_op.generate_shape", 5675, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5676 = self.Op("pd_op.expand", 5676, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.subtract_5677 = self.Op("pd_op.subtract", 5677, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_5678 = self.Op("pd_op.multiply", 5678, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_5679 = self.Op("cinn_op.reduce_sum", 5679, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.full_5680 = self.Op("pd_op.full", 5680, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_5681 = self.Op("cinn_op.generate_shape", 5681, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5682 = self.Op("pd_op.expand", 5682, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_5683 = self.Op("pd_op.divide", 5683, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.full_5684 = self.Op("pd_op.full", 5684, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("1e-05"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_5685 = self.Op("cinn_op.generate_shape", 5685, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5686 = self.Op("pd_op.expand", 5686, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_5687 = self.Op("pd_op.add", 5687, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.rsqrt_5688 = self.Op("pd_op.rsqrt", 5688, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_5689 = self.Op("cinn_op.generate_shape", 5689, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5690 = self.Op("pd_op.expand", 5690, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_5691 = self.Op("pd_op.multiply", 5691, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_5692 = self.Op("pd_op.cast", 5692, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_5693 = self.Op("cinn_op.generate_shape", 5693, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5694 = self.Op("pd_op.expand", 5694, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_5695 = self.Op("pd_op.multiply", 5695, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_5696 = self.Op("pd_op.cast", 5696, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_5697 = self.Op("cinn_op.generate_shape", 5697, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5698 = self.Op("pd_op.expand", 5698, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_5699 = self.Op("pd_op.add", 5699, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_5700 = self.Op("pd_op.cast", 5700, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(dtype=self.a_dtype("float16"), stop_gradient=self.a_array(self.a_bool(False))))

    self.yield_5702 = self.Op("cf.yield", 5702, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_5701 = self.Op("cinn_op.fusion", 5701, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_242 = self.Op("pd_op.matmul", 242, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.matmul_246 = self.Op("pd_op.matmul", 246, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.matmul_254 = self.Op("pd_op.matmul", 254, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_5703 = self.Op("cinn_op.generate_shape", 5703, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5704 = self.Op("pd_op.expand", 5704, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_5705 = self.Op("pd_op.add", 5705, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.scale_5706 = self.Op("cinn_op.scale", 5706, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(bias=self.a_f32("0"), stop_gradient=self.a_array(self.a_bool(False)), bias_after_scale=self.a_bool(True), scale=self.a_f32("0.125")))

    self.generate_shape_5707 = self.Op("cinn_op.generate_shape", 5707, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(12), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.reshape_5708 = self.Op("pd_op.reshape", 5708, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16()), self.t_dtensor([0, -1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.transpose_5709 = self.Op("pd_op.transpose", 5709, input_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16())], output_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), perm=self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_5710 = self.Op("cinn_op.generate_shape", 5710, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_array(self.a_str("Mul"), self.a_str("S0"), self.a_i64(12)), self.a_i64(-1), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_5711 = self.Op("pd_op.reshape", 5711, input_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([0, -1, 12, -1, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_5713 = self.Op("cf.yield", 5713, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_5712 = self.Op("cinn_op.fusion", 5712, input_types=[], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.generate_shape_5714 = self.Op("cinn_op.generate_shape", 5714, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5715 = self.Op("pd_op.expand", 5715, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_5716 = self.Op("pd_op.add", 5716, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.generate_shape_5717 = self.Op("cinn_op.generate_shape", 5717, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(-1), self.a_i64(12), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_5718 = self.Op("pd_op.reshape", 5718, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16()), self.t_dtensor([0, -1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.transpose_5719 = self.Op("pd_op.transpose", 5719, input_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16())], output_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), perm=self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_5720 = self.Op("cinn_op.generate_shape", 5720, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_array(self.a_str("Mul"), self.a_str("S0"), self.a_i64(12)), self.a_i64(-1), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_5721 = self.Op("pd_op.reshape", 5721, input_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([0, -1, 12, -1, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_5723 = self.Op("cf.yield", 5723, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_5722 = self.Op("cinn_op.fusion", 5722, input_types=[], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.generate_shape_5724 = self.Op("cinn_op.generate_shape", 5724, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5725 = self.Op("pd_op.expand", 5725, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_5726 = self.Op("pd_op.add", 5726, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.generate_shape_5727 = self.Op("cinn_op.generate_shape", 5727, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(-1), self.a_i64(12), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_5728 = self.Op("pd_op.reshape", 5728, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16()), self.t_dtensor([0, -1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.transpose_5729 = self.Op("pd_op.transpose", 5729, input_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16())], output_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), perm=self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_5730 = self.Op("cinn_op.generate_shape", 5730, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_array(self.a_str("Mul"), self.a_str("S0"), self.a_i64(12)), self.a_i64(-1), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_5731 = self.Op("pd_op.reshape", 5731, input_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([0, -1, 12, -1, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_5733 = self.Op("cf.yield", 5733, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_5732 = self.Op("cinn_op.fusion", 5732, input_types=[], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_285 = self.Op("pd_op.matmul", 285, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(True)))

    self.generate_shape_5734 = self.Op("cinn_op.generate_shape", 5734, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("SS0"), self.a_i64(12), self.a_str("SS1"), self.a_str("SS1")), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS1"), self.a_i64(0), self.a_i64(1)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS1"), self.a_i64(1), self.a_i64(1)))))

    self.reshape_5735 = self.Op("pd_op.reshape", 5735, input_types=[self.t_dtensor([-1, -1, -1], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, 12, -1, -1], self.t_f16()), self.t_dtensor([0, -1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.generate_shape_5736 = self.Op("cinn_op.generate_shape", 5736, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(12), self.a_str("S1"), self.a_str("S1")), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5737 = self.Op("pd_op.expand", 5737, input_types=[self.t_dtensor([-1, -1, -1, -1], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_5738 = self.Op("pd_op.add", 5738, input_types=[self.t_dtensor([-1, 12, -1, -1], self.t_f16()), self.t_dtensor([-1, -1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, 12, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.generate_shape_5739 = self.Op("cinn_op.generate_shape", 5739, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_array(self.a_str("Mul"), self.a_str("SS0"), self.a_i64(12)), self.a_str("SS1"), self.a_str("SS1")), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS1"), self.a_i64(0), self.a_i64(1)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS1"), self.a_i64(1), self.a_i64(1)))))

    self.reshape_5740 = self.Op("pd_op.reshape", 5740, input_types=[self.t_dtensor([-1, 12, -1, -1], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16()), self.t_dtensor([0, -1, 12, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_5742 = self.Op("cf.yield", 5742, input_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_5741 = self.Op("cinn_op.fusion", 5741, input_types=[], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.softmax_294 = self.Op("pd_op.softmax", 294, input_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), axis=self.a_i32(-1), stop_gradient=self.a_array(self.a_bool(False))))

    self.matmul_295 = self.Op("pd_op.matmul", 295, input_types=[self.t_dtensor([-1, -1, -1], self.t_f16()), self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_5743 = self.Op("cinn_op.generate_shape", 5743, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(12), self.a_str("S1"), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.reshape_5744 = self.Op("pd_op.reshape", 5744, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16()), self.t_dtensor([0, -1, -1, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.transpose_5745 = self.Op("pd_op.transpose", 5745, input_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), perm=self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_5746 = self.Op("cinn_op.generate_shape", 5746, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.reshape_5747 = self.Op("pd_op.reshape", 5747, input_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([0, -1, -1, 12, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_5749 = self.Op("cf.yield", 5749, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_5748 = self.Op("cinn_op.fusion", 5748, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_304 = self.Op("pd_op.matmul", 304, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_5750 = self.Op("cinn_op.generate_shape", 5750, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5751 = self.Op("pd_op.expand", 5751, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_5752 = self.Op("pd_op.add", 5752, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.add_5753 = self.Op("pd_op.add", 5753, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.yield_5755 = self.Op("cf.yield", 5755, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_5754 = self.Op("cinn_op.fusion", 5754, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.cast_5756 = self.Op("pd_op.cast", 5756, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_5757 = self.Op("cinn_op.reduce_sum", 5757, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.yield_5759 = self.Op("cf.yield", 5759, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[], attrs=dict())

    self.fusion_5758 = self.Op("cinn_op.fusion", 5758, input_types=[], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.cast_5760 = self.Op("pd_op.cast", 5760, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.full_5761 = self.Op("pd_op.full", 5761, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_5762 = self.Op("cinn_op.generate_shape", 5762, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5763 = self.Op("pd_op.expand", 5763, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_5764 = self.Op("pd_op.divide", 5764, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_5765 = self.Op("cinn_op.generate_shape", 5765, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5766 = self.Op("pd_op.expand", 5766, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.subtract_5767 = self.Op("pd_op.subtract", 5767, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_5768 = self.Op("pd_op.multiply", 5768, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_5769 = self.Op("cinn_op.reduce_sum", 5769, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.full_5770 = self.Op("pd_op.full", 5770, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_5771 = self.Op("cinn_op.generate_shape", 5771, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5772 = self.Op("pd_op.expand", 5772, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_5773 = self.Op("pd_op.divide", 5773, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.full_5774 = self.Op("pd_op.full", 5774, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("1e-05"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_5775 = self.Op("cinn_op.generate_shape", 5775, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5776 = self.Op("pd_op.expand", 5776, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_5777 = self.Op("pd_op.add", 5777, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.rsqrt_5778 = self.Op("pd_op.rsqrt", 5778, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_5779 = self.Op("cinn_op.generate_shape", 5779, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5780 = self.Op("pd_op.expand", 5780, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_5781 = self.Op("pd_op.multiply", 5781, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_5782 = self.Op("pd_op.cast", 5782, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_5783 = self.Op("cinn_op.generate_shape", 5783, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5784 = self.Op("pd_op.expand", 5784, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_5785 = self.Op("pd_op.multiply", 5785, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_5786 = self.Op("pd_op.cast", 5786, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_5787 = self.Op("cinn_op.generate_shape", 5787, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5788 = self.Op("pd_op.expand", 5788, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_5789 = self.Op("pd_op.add", 5789, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_5790 = self.Op("pd_op.cast", 5790, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(dtype=self.a_dtype("float16"), stop_gradient=self.a_array(self.a_bool(False))))

    self.yield_5792 = self.Op("cf.yield", 5792, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_5791 = self.Op("cinn_op.fusion", 5791, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_308 = self.Op("pd_op.matmul", 308, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 3072], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_5793 = self.Op("cinn_op.generate_shape", 5793, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(3072)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5794 = self.Op("pd_op.expand", 5794, input_types=[self.t_dtensor([3072], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_5795 = self.Op("pd_op.add", 5795, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.scale_5796 = self.Op("cinn_op.scale", 5796, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(bias=self.a_f32("0"), stop_gradient=self.a_array(self.a_bool(False)), bias_after_scale=self.a_bool(True), scale=self.a_f32("1.702")))

    self.cast_5797 = self.Op("pd_op.cast", 5797, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.full_5798 = self.Op("pd_op.full", 5798, input_types=[], output_types=[self.t_dtensor([1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("1"), shape=self.a_intarray(1), place=self.a_place("cpu"), dtype=self.a_dtype("float32")))

    self.scale_5799 = self.Op("cinn_op.scale", 5799, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(bias=self.a_f32("0"), stop_gradient=self.a_array(self.a_bool(False)), bias_after_scale=self.a_bool(True), scale=self.a_f32("-1")))

    self.exp_5800 = self.Op("pd_op.exp", 5800, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_5801 = self.Op("cinn_op.generate_shape", 5801, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(3072)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5802 = self.Op("pd_op.expand", 5802, input_types=[self.t_dtensor([1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_5803 = self.Op("pd_op.add", 5803, input_types=[self.t_dtensor([-1, -1, -1], self.t_f32()), self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_5804 = self.Op("cinn_op.generate_shape", 5804, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(3072)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5805 = self.Op("pd_op.expand", 5805, input_types=[self.t_dtensor([1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_5806 = self.Op("pd_op.divide", 5806, input_types=[self.t_dtensor([-1, -1, -1], self.t_f32()), self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_5807 = self.Op("pd_op.cast", 5807, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(dtype=self.a_dtype("float16"), stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_5808 = self.Op("pd_op.multiply", 5808, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16()), self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.yield_5810 = self.Op("cf.yield", 5810, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_5809 = self.Op("cinn_op.fusion", 5809, input_types=[], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_314 = self.Op("pd_op.matmul", 314, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16()), self.t_dtensor([3072, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_5811 = self.Op("cinn_op.generate_shape", 5811, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5812 = self.Op("pd_op.expand", 5812, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_5813 = self.Op("pd_op.add", 5813, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.add_5814 = self.Op("pd_op.add", 5814, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.yield_5816 = self.Op("cf.yield", 5816, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_5815 = self.Op("cinn_op.fusion", 5815, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.cast_5817 = self.Op("pd_op.cast", 5817, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_5818 = self.Op("cinn_op.reduce_sum", 5818, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.yield_5820 = self.Op("cf.yield", 5820, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[], attrs=dict())

    self.fusion_5819 = self.Op("cinn_op.fusion", 5819, input_types=[], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.cast_5821 = self.Op("pd_op.cast", 5821, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.full_5822 = self.Op("pd_op.full", 5822, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_5823 = self.Op("cinn_op.generate_shape", 5823, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5824 = self.Op("pd_op.expand", 5824, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_5825 = self.Op("pd_op.divide", 5825, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_5826 = self.Op("cinn_op.generate_shape", 5826, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5827 = self.Op("pd_op.expand", 5827, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.subtract_5828 = self.Op("pd_op.subtract", 5828, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_5829 = self.Op("pd_op.multiply", 5829, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_5830 = self.Op("cinn_op.reduce_sum", 5830, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.full_5831 = self.Op("pd_op.full", 5831, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_5832 = self.Op("cinn_op.generate_shape", 5832, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5833 = self.Op("pd_op.expand", 5833, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_5834 = self.Op("pd_op.divide", 5834, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.full_5835 = self.Op("pd_op.full", 5835, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("1e-05"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_5836 = self.Op("cinn_op.generate_shape", 5836, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5837 = self.Op("pd_op.expand", 5837, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_5838 = self.Op("pd_op.add", 5838, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.rsqrt_5839 = self.Op("pd_op.rsqrt", 5839, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_5840 = self.Op("cinn_op.generate_shape", 5840, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5841 = self.Op("pd_op.expand", 5841, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_5842 = self.Op("pd_op.multiply", 5842, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_5843 = self.Op("pd_op.cast", 5843, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_5844 = self.Op("cinn_op.generate_shape", 5844, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5845 = self.Op("pd_op.expand", 5845, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_5846 = self.Op("pd_op.multiply", 5846, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_5847 = self.Op("pd_op.cast", 5847, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_5848 = self.Op("cinn_op.generate_shape", 5848, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5849 = self.Op("pd_op.expand", 5849, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_5850 = self.Op("pd_op.add", 5850, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_5851 = self.Op("pd_op.cast", 5851, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(dtype=self.a_dtype("float16"), stop_gradient=self.a_array(self.a_bool(False))))

    self.yield_5853 = self.Op("cf.yield", 5853, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_5852 = self.Op("cinn_op.fusion", 5852, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_325 = self.Op("pd_op.matmul", 325, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.matmul_329 = self.Op("pd_op.matmul", 329, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.matmul_337 = self.Op("pd_op.matmul", 337, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_5854 = self.Op("cinn_op.generate_shape", 5854, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5855 = self.Op("pd_op.expand", 5855, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_5856 = self.Op("pd_op.add", 5856, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.scale_5857 = self.Op("cinn_op.scale", 5857, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(bias=self.a_f32("0"), stop_gradient=self.a_array(self.a_bool(False)), bias_after_scale=self.a_bool(True), scale=self.a_f32("0.125")))

    self.generate_shape_5858 = self.Op("cinn_op.generate_shape", 5858, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(12), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.reshape_5859 = self.Op("pd_op.reshape", 5859, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16()), self.t_dtensor([0, -1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.transpose_5860 = self.Op("pd_op.transpose", 5860, input_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16())], output_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), perm=self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_5861 = self.Op("cinn_op.generate_shape", 5861, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_array(self.a_str("Mul"), self.a_str("S0"), self.a_i64(12)), self.a_i64(-1), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_5862 = self.Op("pd_op.reshape", 5862, input_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([0, -1, 12, -1, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_5864 = self.Op("cf.yield", 5864, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_5863 = self.Op("cinn_op.fusion", 5863, input_types=[], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.generate_shape_5865 = self.Op("cinn_op.generate_shape", 5865, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5866 = self.Op("pd_op.expand", 5866, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_5867 = self.Op("pd_op.add", 5867, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.generate_shape_5868 = self.Op("cinn_op.generate_shape", 5868, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(-1), self.a_i64(12), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_5869 = self.Op("pd_op.reshape", 5869, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16()), self.t_dtensor([0, -1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.transpose_5870 = self.Op("pd_op.transpose", 5870, input_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16())], output_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), perm=self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_5871 = self.Op("cinn_op.generate_shape", 5871, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_array(self.a_str("Mul"), self.a_str("S0"), self.a_i64(12)), self.a_i64(-1), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_5872 = self.Op("pd_op.reshape", 5872, input_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([0, -1, 12, -1, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_5874 = self.Op("cf.yield", 5874, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_5873 = self.Op("cinn_op.fusion", 5873, input_types=[], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.generate_shape_5875 = self.Op("cinn_op.generate_shape", 5875, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5876 = self.Op("pd_op.expand", 5876, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_5877 = self.Op("pd_op.add", 5877, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.generate_shape_5878 = self.Op("cinn_op.generate_shape", 5878, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(-1), self.a_i64(12), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_5879 = self.Op("pd_op.reshape", 5879, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16()), self.t_dtensor([0, -1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.transpose_5880 = self.Op("pd_op.transpose", 5880, input_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16())], output_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), perm=self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_5881 = self.Op("cinn_op.generate_shape", 5881, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_array(self.a_str("Mul"), self.a_str("S0"), self.a_i64(12)), self.a_i64(-1), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_5882 = self.Op("pd_op.reshape", 5882, input_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([0, -1, 12, -1, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_5884 = self.Op("cf.yield", 5884, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_5883 = self.Op("cinn_op.fusion", 5883, input_types=[], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_368 = self.Op("pd_op.matmul", 368, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(True)))

    self.generate_shape_5885 = self.Op("cinn_op.generate_shape", 5885, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("SS0"), self.a_i64(12), self.a_str("SS1"), self.a_str("SS1")), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS1"), self.a_i64(0), self.a_i64(1)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS1"), self.a_i64(1), self.a_i64(1)))))

    self.reshape_5886 = self.Op("pd_op.reshape", 5886, input_types=[self.t_dtensor([-1, -1, -1], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, 12, -1, -1], self.t_f16()), self.t_dtensor([0, -1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.generate_shape_5887 = self.Op("cinn_op.generate_shape", 5887, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(12), self.a_str("S1"), self.a_str("S1")), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5888 = self.Op("pd_op.expand", 5888, input_types=[self.t_dtensor([-1, -1, -1, -1], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_5889 = self.Op("pd_op.add", 5889, input_types=[self.t_dtensor([-1, 12, -1, -1], self.t_f16()), self.t_dtensor([-1, -1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, 12, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.generate_shape_5890 = self.Op("cinn_op.generate_shape", 5890, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_array(self.a_str("Mul"), self.a_str("SS0"), self.a_i64(12)), self.a_str("SS1"), self.a_str("SS1")), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS1"), self.a_i64(0), self.a_i64(1)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS1"), self.a_i64(1), self.a_i64(1)))))

    self.reshape_5891 = self.Op("pd_op.reshape", 5891, input_types=[self.t_dtensor([-1, 12, -1, -1], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16()), self.t_dtensor([0, -1, 12, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_5893 = self.Op("cf.yield", 5893, input_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_5892 = self.Op("cinn_op.fusion", 5892, input_types=[], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.softmax_377 = self.Op("pd_op.softmax", 377, input_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), axis=self.a_i32(-1), stop_gradient=self.a_array(self.a_bool(False))))

    self.matmul_378 = self.Op("pd_op.matmul", 378, input_types=[self.t_dtensor([-1, -1, -1], self.t_f16()), self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_5894 = self.Op("cinn_op.generate_shape", 5894, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(12), self.a_str("S1"), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.reshape_5895 = self.Op("pd_op.reshape", 5895, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16()), self.t_dtensor([0, -1, -1, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.transpose_5896 = self.Op("pd_op.transpose", 5896, input_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), perm=self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_5897 = self.Op("cinn_op.generate_shape", 5897, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.reshape_5898 = self.Op("pd_op.reshape", 5898, input_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([0, -1, -1, 12, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_5900 = self.Op("cf.yield", 5900, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_5899 = self.Op("cinn_op.fusion", 5899, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_387 = self.Op("pd_op.matmul", 387, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_5901 = self.Op("cinn_op.generate_shape", 5901, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5902 = self.Op("pd_op.expand", 5902, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_5903 = self.Op("pd_op.add", 5903, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.add_5904 = self.Op("pd_op.add", 5904, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.yield_5906 = self.Op("cf.yield", 5906, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_5905 = self.Op("cinn_op.fusion", 5905, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.cast_5907 = self.Op("pd_op.cast", 5907, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_5908 = self.Op("cinn_op.reduce_sum", 5908, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.yield_5910 = self.Op("cf.yield", 5910, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[], attrs=dict())

    self.fusion_5909 = self.Op("cinn_op.fusion", 5909, input_types=[], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.cast_5911 = self.Op("pd_op.cast", 5911, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.full_5912 = self.Op("pd_op.full", 5912, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_5913 = self.Op("cinn_op.generate_shape", 5913, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5914 = self.Op("pd_op.expand", 5914, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_5915 = self.Op("pd_op.divide", 5915, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_5916 = self.Op("cinn_op.generate_shape", 5916, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5917 = self.Op("pd_op.expand", 5917, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.subtract_5918 = self.Op("pd_op.subtract", 5918, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_5919 = self.Op("pd_op.multiply", 5919, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_5920 = self.Op("cinn_op.reduce_sum", 5920, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.full_5921 = self.Op("pd_op.full", 5921, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_5922 = self.Op("cinn_op.generate_shape", 5922, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5923 = self.Op("pd_op.expand", 5923, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_5924 = self.Op("pd_op.divide", 5924, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.full_5925 = self.Op("pd_op.full", 5925, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("1e-05"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_5926 = self.Op("cinn_op.generate_shape", 5926, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5927 = self.Op("pd_op.expand", 5927, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_5928 = self.Op("pd_op.add", 5928, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.rsqrt_5929 = self.Op("pd_op.rsqrt", 5929, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_5930 = self.Op("cinn_op.generate_shape", 5930, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5931 = self.Op("pd_op.expand", 5931, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_5932 = self.Op("pd_op.multiply", 5932, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_5933 = self.Op("pd_op.cast", 5933, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_5934 = self.Op("cinn_op.generate_shape", 5934, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5935 = self.Op("pd_op.expand", 5935, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_5936 = self.Op("pd_op.multiply", 5936, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_5937 = self.Op("pd_op.cast", 5937, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_5938 = self.Op("cinn_op.generate_shape", 5938, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5939 = self.Op("pd_op.expand", 5939, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_5940 = self.Op("pd_op.add", 5940, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_5941 = self.Op("pd_op.cast", 5941, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(dtype=self.a_dtype("float16"), stop_gradient=self.a_array(self.a_bool(False))))

    self.yield_5943 = self.Op("cf.yield", 5943, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_5942 = self.Op("cinn_op.fusion", 5942, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_391 = self.Op("pd_op.matmul", 391, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 3072], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_5944 = self.Op("cinn_op.generate_shape", 5944, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(3072)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5945 = self.Op("pd_op.expand", 5945, input_types=[self.t_dtensor([3072], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_5946 = self.Op("pd_op.add", 5946, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.scale_5947 = self.Op("cinn_op.scale", 5947, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(bias=self.a_f32("0"), stop_gradient=self.a_array(self.a_bool(False)), bias_after_scale=self.a_bool(True), scale=self.a_f32("1.702")))

    self.cast_5948 = self.Op("pd_op.cast", 5948, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.full_5949 = self.Op("pd_op.full", 5949, input_types=[], output_types=[self.t_dtensor([1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("1"), shape=self.a_intarray(1), place=self.a_place("cpu"), dtype=self.a_dtype("float32")))

    self.scale_5950 = self.Op("cinn_op.scale", 5950, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(bias=self.a_f32("0"), stop_gradient=self.a_array(self.a_bool(False)), bias_after_scale=self.a_bool(True), scale=self.a_f32("-1")))

    self.exp_5951 = self.Op("pd_op.exp", 5951, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_5952 = self.Op("cinn_op.generate_shape", 5952, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(3072)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5953 = self.Op("pd_op.expand", 5953, input_types=[self.t_dtensor([1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_5954 = self.Op("pd_op.add", 5954, input_types=[self.t_dtensor([-1, -1, -1], self.t_f32()), self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_5955 = self.Op("cinn_op.generate_shape", 5955, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(3072)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5956 = self.Op("pd_op.expand", 5956, input_types=[self.t_dtensor([1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_5957 = self.Op("pd_op.divide", 5957, input_types=[self.t_dtensor([-1, -1, -1], self.t_f32()), self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_5958 = self.Op("pd_op.cast", 5958, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(dtype=self.a_dtype("float16"), stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_5959 = self.Op("pd_op.multiply", 5959, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16()), self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.yield_5961 = self.Op("cf.yield", 5961, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_5960 = self.Op("cinn_op.fusion", 5960, input_types=[], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_397 = self.Op("pd_op.matmul", 397, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16()), self.t_dtensor([3072, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_5962 = self.Op("cinn_op.generate_shape", 5962, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5963 = self.Op("pd_op.expand", 5963, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_5964 = self.Op("pd_op.add", 5964, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.add_5965 = self.Op("pd_op.add", 5965, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.yield_5967 = self.Op("cf.yield", 5967, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_5966 = self.Op("cinn_op.fusion", 5966, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.cast_5968 = self.Op("pd_op.cast", 5968, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_5969 = self.Op("cinn_op.reduce_sum", 5969, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.yield_5971 = self.Op("cf.yield", 5971, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[], attrs=dict())

    self.fusion_5970 = self.Op("cinn_op.fusion", 5970, input_types=[], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.cast_5972 = self.Op("pd_op.cast", 5972, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.full_5973 = self.Op("pd_op.full", 5973, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_5974 = self.Op("cinn_op.generate_shape", 5974, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5975 = self.Op("pd_op.expand", 5975, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_5976 = self.Op("pd_op.divide", 5976, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_5977 = self.Op("cinn_op.generate_shape", 5977, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5978 = self.Op("pd_op.expand", 5978, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.subtract_5979 = self.Op("pd_op.subtract", 5979, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_5980 = self.Op("pd_op.multiply", 5980, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_5981 = self.Op("cinn_op.reduce_sum", 5981, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.full_5982 = self.Op("pd_op.full", 5982, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_5983 = self.Op("cinn_op.generate_shape", 5983, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5984 = self.Op("pd_op.expand", 5984, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_5985 = self.Op("pd_op.divide", 5985, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.full_5986 = self.Op("pd_op.full", 5986, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("1e-05"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_5987 = self.Op("cinn_op.generate_shape", 5987, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5988 = self.Op("pd_op.expand", 5988, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_5989 = self.Op("pd_op.add", 5989, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.rsqrt_5990 = self.Op("pd_op.rsqrt", 5990, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_5991 = self.Op("cinn_op.generate_shape", 5991, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5992 = self.Op("pd_op.expand", 5992, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_5993 = self.Op("pd_op.multiply", 5993, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_5994 = self.Op("pd_op.cast", 5994, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_5995 = self.Op("cinn_op.generate_shape", 5995, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_5996 = self.Op("pd_op.expand", 5996, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_5997 = self.Op("pd_op.multiply", 5997, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_5998 = self.Op("pd_op.cast", 5998, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_5999 = self.Op("cinn_op.generate_shape", 5999, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6000 = self.Op("pd_op.expand", 6000, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6001 = self.Op("pd_op.add", 6001, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_6002 = self.Op("pd_op.cast", 6002, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(dtype=self.a_dtype("float16"), stop_gradient=self.a_array(self.a_bool(False))))

    self.yield_6004 = self.Op("cf.yield", 6004, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6003 = self.Op("cinn_op.fusion", 6003, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_408 = self.Op("pd_op.matmul", 408, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.matmul_412 = self.Op("pd_op.matmul", 412, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.matmul_420 = self.Op("pd_op.matmul", 420, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_6005 = self.Op("cinn_op.generate_shape", 6005, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6006 = self.Op("pd_op.expand", 6006, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6007 = self.Op("pd_op.add", 6007, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.scale_6008 = self.Op("cinn_op.scale", 6008, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(bias=self.a_f32("0"), stop_gradient=self.a_array(self.a_bool(False)), bias_after_scale=self.a_bool(True), scale=self.a_f32("0.125")))

    self.generate_shape_6009 = self.Op("cinn_op.generate_shape", 6009, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(12), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.reshape_6010 = self.Op("pd_op.reshape", 6010, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16()), self.t_dtensor([0, -1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.transpose_6011 = self.Op("pd_op.transpose", 6011, input_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16())], output_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), perm=self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6012 = self.Op("cinn_op.generate_shape", 6012, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_array(self.a_str("Mul"), self.a_str("S0"), self.a_i64(12)), self.a_i64(-1), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_6013 = self.Op("pd_op.reshape", 6013, input_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([0, -1, 12, -1, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_6015 = self.Op("cf.yield", 6015, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6014 = self.Op("cinn_op.fusion", 6014, input_types=[], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.generate_shape_6016 = self.Op("cinn_op.generate_shape", 6016, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6017 = self.Op("pd_op.expand", 6017, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6018 = self.Op("pd_op.add", 6018, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.generate_shape_6019 = self.Op("cinn_op.generate_shape", 6019, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(-1), self.a_i64(12), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_6020 = self.Op("pd_op.reshape", 6020, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16()), self.t_dtensor([0, -1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.transpose_6021 = self.Op("pd_op.transpose", 6021, input_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16())], output_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), perm=self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6022 = self.Op("cinn_op.generate_shape", 6022, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_array(self.a_str("Mul"), self.a_str("S0"), self.a_i64(12)), self.a_i64(-1), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_6023 = self.Op("pd_op.reshape", 6023, input_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([0, -1, 12, -1, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_6025 = self.Op("cf.yield", 6025, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6024 = self.Op("cinn_op.fusion", 6024, input_types=[], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.generate_shape_6026 = self.Op("cinn_op.generate_shape", 6026, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6027 = self.Op("pd_op.expand", 6027, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6028 = self.Op("pd_op.add", 6028, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.generate_shape_6029 = self.Op("cinn_op.generate_shape", 6029, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(-1), self.a_i64(12), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_6030 = self.Op("pd_op.reshape", 6030, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16()), self.t_dtensor([0, -1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.transpose_6031 = self.Op("pd_op.transpose", 6031, input_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16())], output_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), perm=self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6032 = self.Op("cinn_op.generate_shape", 6032, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_array(self.a_str("Mul"), self.a_str("S0"), self.a_i64(12)), self.a_i64(-1), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_6033 = self.Op("pd_op.reshape", 6033, input_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([0, -1, 12, -1, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_6035 = self.Op("cf.yield", 6035, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6034 = self.Op("cinn_op.fusion", 6034, input_types=[], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_451 = self.Op("pd_op.matmul", 451, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(True)))

    self.generate_shape_6036 = self.Op("cinn_op.generate_shape", 6036, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("SS0"), self.a_i64(12), self.a_str("SS1"), self.a_str("SS1")), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS1"), self.a_i64(0), self.a_i64(1)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS1"), self.a_i64(1), self.a_i64(1)))))

    self.reshape_6037 = self.Op("pd_op.reshape", 6037, input_types=[self.t_dtensor([-1, -1, -1], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, 12, -1, -1], self.t_f16()), self.t_dtensor([0, -1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.generate_shape_6038 = self.Op("cinn_op.generate_shape", 6038, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(12), self.a_str("S1"), self.a_str("S1")), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6039 = self.Op("pd_op.expand", 6039, input_types=[self.t_dtensor([-1, -1, -1, -1], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6040 = self.Op("pd_op.add", 6040, input_types=[self.t_dtensor([-1, 12, -1, -1], self.t_f16()), self.t_dtensor([-1, -1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, 12, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.generate_shape_6041 = self.Op("cinn_op.generate_shape", 6041, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_array(self.a_str("Mul"), self.a_str("SS0"), self.a_i64(12)), self.a_str("SS1"), self.a_str("SS1")), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS1"), self.a_i64(0), self.a_i64(1)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS1"), self.a_i64(1), self.a_i64(1)))))

    self.reshape_6042 = self.Op("pd_op.reshape", 6042, input_types=[self.t_dtensor([-1, 12, -1, -1], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16()), self.t_dtensor([0, -1, 12, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_6044 = self.Op("cf.yield", 6044, input_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6043 = self.Op("cinn_op.fusion", 6043, input_types=[], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.softmax_460 = self.Op("pd_op.softmax", 460, input_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), axis=self.a_i32(-1), stop_gradient=self.a_array(self.a_bool(False))))

    self.matmul_461 = self.Op("pd_op.matmul", 461, input_types=[self.t_dtensor([-1, -1, -1], self.t_f16()), self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_6045 = self.Op("cinn_op.generate_shape", 6045, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(12), self.a_str("S1"), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.reshape_6046 = self.Op("pd_op.reshape", 6046, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16()), self.t_dtensor([0, -1, -1, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.transpose_6047 = self.Op("pd_op.transpose", 6047, input_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), perm=self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6048 = self.Op("cinn_op.generate_shape", 6048, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.reshape_6049 = self.Op("pd_op.reshape", 6049, input_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([0, -1, -1, 12, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_6051 = self.Op("cf.yield", 6051, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6050 = self.Op("cinn_op.fusion", 6050, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_470 = self.Op("pd_op.matmul", 470, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_6052 = self.Op("cinn_op.generate_shape", 6052, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6053 = self.Op("pd_op.expand", 6053, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6054 = self.Op("pd_op.add", 6054, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.add_6055 = self.Op("pd_op.add", 6055, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.yield_6057 = self.Op("cf.yield", 6057, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6056 = self.Op("cinn_op.fusion", 6056, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.cast_6058 = self.Op("pd_op.cast", 6058, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_6059 = self.Op("cinn_op.reduce_sum", 6059, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.yield_6061 = self.Op("cf.yield", 6061, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[], attrs=dict())

    self.fusion_6060 = self.Op("cinn_op.fusion", 6060, input_types=[], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.cast_6062 = self.Op("pd_op.cast", 6062, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.full_6063 = self.Op("pd_op.full", 6063, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_6064 = self.Op("cinn_op.generate_shape", 6064, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6065 = self.Op("pd_op.expand", 6065, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_6066 = self.Op("pd_op.divide", 6066, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6067 = self.Op("cinn_op.generate_shape", 6067, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6068 = self.Op("pd_op.expand", 6068, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.subtract_6069 = self.Op("pd_op.subtract", 6069, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_6070 = self.Op("pd_op.multiply", 6070, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_6071 = self.Op("cinn_op.reduce_sum", 6071, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.full_6072 = self.Op("pd_op.full", 6072, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_6073 = self.Op("cinn_op.generate_shape", 6073, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6074 = self.Op("pd_op.expand", 6074, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_6075 = self.Op("pd_op.divide", 6075, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.full_6076 = self.Op("pd_op.full", 6076, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("1e-05"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_6077 = self.Op("cinn_op.generate_shape", 6077, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6078 = self.Op("pd_op.expand", 6078, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6079 = self.Op("pd_op.add", 6079, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.rsqrt_6080 = self.Op("pd_op.rsqrt", 6080, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6081 = self.Op("cinn_op.generate_shape", 6081, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6082 = self.Op("pd_op.expand", 6082, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_6083 = self.Op("pd_op.multiply", 6083, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_6084 = self.Op("pd_op.cast", 6084, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6085 = self.Op("cinn_op.generate_shape", 6085, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6086 = self.Op("pd_op.expand", 6086, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_6087 = self.Op("pd_op.multiply", 6087, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_6088 = self.Op("pd_op.cast", 6088, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6089 = self.Op("cinn_op.generate_shape", 6089, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6090 = self.Op("pd_op.expand", 6090, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6091 = self.Op("pd_op.add", 6091, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_6092 = self.Op("pd_op.cast", 6092, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(dtype=self.a_dtype("float16"), stop_gradient=self.a_array(self.a_bool(False))))

    self.yield_6094 = self.Op("cf.yield", 6094, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6093 = self.Op("cinn_op.fusion", 6093, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_474 = self.Op("pd_op.matmul", 474, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 3072], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_6095 = self.Op("cinn_op.generate_shape", 6095, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(3072)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6096 = self.Op("pd_op.expand", 6096, input_types=[self.t_dtensor([3072], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6097 = self.Op("pd_op.add", 6097, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.scale_6098 = self.Op("cinn_op.scale", 6098, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(bias=self.a_f32("0"), stop_gradient=self.a_array(self.a_bool(False)), bias_after_scale=self.a_bool(True), scale=self.a_f32("1.702")))

    self.cast_6099 = self.Op("pd_op.cast", 6099, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.full_6100 = self.Op("pd_op.full", 6100, input_types=[], output_types=[self.t_dtensor([1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("1"), shape=self.a_intarray(1), place=self.a_place("cpu"), dtype=self.a_dtype("float32")))

    self.scale_6101 = self.Op("cinn_op.scale", 6101, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(bias=self.a_f32("0"), stop_gradient=self.a_array(self.a_bool(False)), bias_after_scale=self.a_bool(True), scale=self.a_f32("-1")))

    self.exp_6102 = self.Op("pd_op.exp", 6102, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6103 = self.Op("cinn_op.generate_shape", 6103, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(3072)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6104 = self.Op("pd_op.expand", 6104, input_types=[self.t_dtensor([1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6105 = self.Op("pd_op.add", 6105, input_types=[self.t_dtensor([-1, -1, -1], self.t_f32()), self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6106 = self.Op("cinn_op.generate_shape", 6106, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(3072)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6107 = self.Op("pd_op.expand", 6107, input_types=[self.t_dtensor([1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_6108 = self.Op("pd_op.divide", 6108, input_types=[self.t_dtensor([-1, -1, -1], self.t_f32()), self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_6109 = self.Op("pd_op.cast", 6109, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(dtype=self.a_dtype("float16"), stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_6110 = self.Op("pd_op.multiply", 6110, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16()), self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.yield_6112 = self.Op("cf.yield", 6112, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6111 = self.Op("cinn_op.fusion", 6111, input_types=[], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_480 = self.Op("pd_op.matmul", 480, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16()), self.t_dtensor([3072, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_6113 = self.Op("cinn_op.generate_shape", 6113, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6114 = self.Op("pd_op.expand", 6114, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6115 = self.Op("pd_op.add", 6115, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.add_6116 = self.Op("pd_op.add", 6116, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.yield_6118 = self.Op("cf.yield", 6118, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6117 = self.Op("cinn_op.fusion", 6117, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.cast_6119 = self.Op("pd_op.cast", 6119, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_6120 = self.Op("cinn_op.reduce_sum", 6120, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.yield_6122 = self.Op("cf.yield", 6122, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[], attrs=dict())

    self.fusion_6121 = self.Op("cinn_op.fusion", 6121, input_types=[], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.cast_6123 = self.Op("pd_op.cast", 6123, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.full_6124 = self.Op("pd_op.full", 6124, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_6125 = self.Op("cinn_op.generate_shape", 6125, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6126 = self.Op("pd_op.expand", 6126, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_6127 = self.Op("pd_op.divide", 6127, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6128 = self.Op("cinn_op.generate_shape", 6128, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6129 = self.Op("pd_op.expand", 6129, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.subtract_6130 = self.Op("pd_op.subtract", 6130, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_6131 = self.Op("pd_op.multiply", 6131, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_6132 = self.Op("cinn_op.reduce_sum", 6132, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.full_6133 = self.Op("pd_op.full", 6133, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_6134 = self.Op("cinn_op.generate_shape", 6134, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6135 = self.Op("pd_op.expand", 6135, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_6136 = self.Op("pd_op.divide", 6136, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.full_6137 = self.Op("pd_op.full", 6137, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("1e-05"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_6138 = self.Op("cinn_op.generate_shape", 6138, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6139 = self.Op("pd_op.expand", 6139, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6140 = self.Op("pd_op.add", 6140, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.rsqrt_6141 = self.Op("pd_op.rsqrt", 6141, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6142 = self.Op("cinn_op.generate_shape", 6142, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6143 = self.Op("pd_op.expand", 6143, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_6144 = self.Op("pd_op.multiply", 6144, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_6145 = self.Op("pd_op.cast", 6145, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6146 = self.Op("cinn_op.generate_shape", 6146, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6147 = self.Op("pd_op.expand", 6147, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_6148 = self.Op("pd_op.multiply", 6148, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_6149 = self.Op("pd_op.cast", 6149, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6150 = self.Op("cinn_op.generate_shape", 6150, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6151 = self.Op("pd_op.expand", 6151, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6152 = self.Op("pd_op.add", 6152, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_6153 = self.Op("pd_op.cast", 6153, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(dtype=self.a_dtype("float16"), stop_gradient=self.a_array(self.a_bool(False))))

    self.yield_6155 = self.Op("cf.yield", 6155, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6154 = self.Op("cinn_op.fusion", 6154, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_491 = self.Op("pd_op.matmul", 491, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.matmul_495 = self.Op("pd_op.matmul", 495, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.matmul_503 = self.Op("pd_op.matmul", 503, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_6156 = self.Op("cinn_op.generate_shape", 6156, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6157 = self.Op("pd_op.expand", 6157, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6158 = self.Op("pd_op.add", 6158, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.scale_6159 = self.Op("cinn_op.scale", 6159, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(bias=self.a_f32("0"), stop_gradient=self.a_array(self.a_bool(False)), bias_after_scale=self.a_bool(True), scale=self.a_f32("0.125")))

    self.generate_shape_6160 = self.Op("cinn_op.generate_shape", 6160, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(12), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.reshape_6161 = self.Op("pd_op.reshape", 6161, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16()), self.t_dtensor([0, -1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.transpose_6162 = self.Op("pd_op.transpose", 6162, input_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16())], output_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), perm=self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6163 = self.Op("cinn_op.generate_shape", 6163, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_array(self.a_str("Mul"), self.a_str("S0"), self.a_i64(12)), self.a_i64(-1), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_6164 = self.Op("pd_op.reshape", 6164, input_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([0, -1, 12, -1, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_6166 = self.Op("cf.yield", 6166, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6165 = self.Op("cinn_op.fusion", 6165, input_types=[], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.generate_shape_6167 = self.Op("cinn_op.generate_shape", 6167, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6168 = self.Op("pd_op.expand", 6168, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6169 = self.Op("pd_op.add", 6169, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.generate_shape_6170 = self.Op("cinn_op.generate_shape", 6170, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(-1), self.a_i64(12), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_6171 = self.Op("pd_op.reshape", 6171, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16()), self.t_dtensor([0, -1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.transpose_6172 = self.Op("pd_op.transpose", 6172, input_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16())], output_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), perm=self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6173 = self.Op("cinn_op.generate_shape", 6173, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_array(self.a_str("Mul"), self.a_str("S0"), self.a_i64(12)), self.a_i64(-1), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_6174 = self.Op("pd_op.reshape", 6174, input_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([0, -1, 12, -1, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_6176 = self.Op("cf.yield", 6176, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6175 = self.Op("cinn_op.fusion", 6175, input_types=[], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.generate_shape_6177 = self.Op("cinn_op.generate_shape", 6177, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6178 = self.Op("pd_op.expand", 6178, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6179 = self.Op("pd_op.add", 6179, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.generate_shape_6180 = self.Op("cinn_op.generate_shape", 6180, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(-1), self.a_i64(12), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_6181 = self.Op("pd_op.reshape", 6181, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16()), self.t_dtensor([0, -1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.transpose_6182 = self.Op("pd_op.transpose", 6182, input_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16())], output_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), perm=self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6183 = self.Op("cinn_op.generate_shape", 6183, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_array(self.a_str("Mul"), self.a_str("S0"), self.a_i64(12)), self.a_i64(-1), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_6184 = self.Op("pd_op.reshape", 6184, input_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([0, -1, 12, -1, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_6186 = self.Op("cf.yield", 6186, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6185 = self.Op("cinn_op.fusion", 6185, input_types=[], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_534 = self.Op("pd_op.matmul", 534, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(True)))

    self.generate_shape_6187 = self.Op("cinn_op.generate_shape", 6187, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("SS0"), self.a_i64(12), self.a_str("SS1"), self.a_str("SS1")), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS1"), self.a_i64(0), self.a_i64(1)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS1"), self.a_i64(1), self.a_i64(1)))))

    self.reshape_6188 = self.Op("pd_op.reshape", 6188, input_types=[self.t_dtensor([-1, -1, -1], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, 12, -1, -1], self.t_f16()), self.t_dtensor([0, -1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.generate_shape_6189 = self.Op("cinn_op.generate_shape", 6189, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(12), self.a_str("S1"), self.a_str("S1")), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6190 = self.Op("pd_op.expand", 6190, input_types=[self.t_dtensor([-1, -1, -1, -1], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6191 = self.Op("pd_op.add", 6191, input_types=[self.t_dtensor([-1, 12, -1, -1], self.t_f16()), self.t_dtensor([-1, -1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, 12, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.generate_shape_6192 = self.Op("cinn_op.generate_shape", 6192, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_array(self.a_str("Mul"), self.a_str("SS0"), self.a_i64(12)), self.a_str("SS1"), self.a_str("SS1")), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS1"), self.a_i64(0), self.a_i64(1)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS1"), self.a_i64(1), self.a_i64(1)))))

    self.reshape_6193 = self.Op("pd_op.reshape", 6193, input_types=[self.t_dtensor([-1, 12, -1, -1], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16()), self.t_dtensor([0, -1, 12, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_6195 = self.Op("cf.yield", 6195, input_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6194 = self.Op("cinn_op.fusion", 6194, input_types=[], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.softmax_543 = self.Op("pd_op.softmax", 543, input_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), axis=self.a_i32(-1), stop_gradient=self.a_array(self.a_bool(False))))

    self.matmul_544 = self.Op("pd_op.matmul", 544, input_types=[self.t_dtensor([-1, -1, -1], self.t_f16()), self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_6196 = self.Op("cinn_op.generate_shape", 6196, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(12), self.a_str("S1"), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.reshape_6197 = self.Op("pd_op.reshape", 6197, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16()), self.t_dtensor([0, -1, -1, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.transpose_6198 = self.Op("pd_op.transpose", 6198, input_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), perm=self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6199 = self.Op("cinn_op.generate_shape", 6199, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.reshape_6200 = self.Op("pd_op.reshape", 6200, input_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([0, -1, -1, 12, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_6202 = self.Op("cf.yield", 6202, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6201 = self.Op("cinn_op.fusion", 6201, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_553 = self.Op("pd_op.matmul", 553, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_6203 = self.Op("cinn_op.generate_shape", 6203, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6204 = self.Op("pd_op.expand", 6204, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6205 = self.Op("pd_op.add", 6205, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.add_6206 = self.Op("pd_op.add", 6206, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.yield_6208 = self.Op("cf.yield", 6208, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6207 = self.Op("cinn_op.fusion", 6207, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.cast_6209 = self.Op("pd_op.cast", 6209, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_6210 = self.Op("cinn_op.reduce_sum", 6210, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.yield_6212 = self.Op("cf.yield", 6212, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[], attrs=dict())

    self.fusion_6211 = self.Op("cinn_op.fusion", 6211, input_types=[], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.cast_6213 = self.Op("pd_op.cast", 6213, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.full_6214 = self.Op("pd_op.full", 6214, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_6215 = self.Op("cinn_op.generate_shape", 6215, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6216 = self.Op("pd_op.expand", 6216, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_6217 = self.Op("pd_op.divide", 6217, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6218 = self.Op("cinn_op.generate_shape", 6218, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6219 = self.Op("pd_op.expand", 6219, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.subtract_6220 = self.Op("pd_op.subtract", 6220, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_6221 = self.Op("pd_op.multiply", 6221, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_6222 = self.Op("cinn_op.reduce_sum", 6222, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.full_6223 = self.Op("pd_op.full", 6223, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_6224 = self.Op("cinn_op.generate_shape", 6224, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6225 = self.Op("pd_op.expand", 6225, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_6226 = self.Op("pd_op.divide", 6226, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.full_6227 = self.Op("pd_op.full", 6227, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("1e-05"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_6228 = self.Op("cinn_op.generate_shape", 6228, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6229 = self.Op("pd_op.expand", 6229, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6230 = self.Op("pd_op.add", 6230, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.rsqrt_6231 = self.Op("pd_op.rsqrt", 6231, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6232 = self.Op("cinn_op.generate_shape", 6232, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6233 = self.Op("pd_op.expand", 6233, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_6234 = self.Op("pd_op.multiply", 6234, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_6235 = self.Op("pd_op.cast", 6235, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6236 = self.Op("cinn_op.generate_shape", 6236, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6237 = self.Op("pd_op.expand", 6237, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_6238 = self.Op("pd_op.multiply", 6238, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_6239 = self.Op("pd_op.cast", 6239, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6240 = self.Op("cinn_op.generate_shape", 6240, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6241 = self.Op("pd_op.expand", 6241, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6242 = self.Op("pd_op.add", 6242, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_6243 = self.Op("pd_op.cast", 6243, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(dtype=self.a_dtype("float16"), stop_gradient=self.a_array(self.a_bool(False))))

    self.yield_6245 = self.Op("cf.yield", 6245, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6244 = self.Op("cinn_op.fusion", 6244, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_557 = self.Op("pd_op.matmul", 557, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 3072], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_6246 = self.Op("cinn_op.generate_shape", 6246, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(3072)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6247 = self.Op("pd_op.expand", 6247, input_types=[self.t_dtensor([3072], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6248 = self.Op("pd_op.add", 6248, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.scale_6249 = self.Op("cinn_op.scale", 6249, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(bias=self.a_f32("0"), stop_gradient=self.a_array(self.a_bool(False)), bias_after_scale=self.a_bool(True), scale=self.a_f32("1.702")))

    self.cast_6250 = self.Op("pd_op.cast", 6250, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.full_6251 = self.Op("pd_op.full", 6251, input_types=[], output_types=[self.t_dtensor([1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("1"), shape=self.a_intarray(1), place=self.a_place("cpu"), dtype=self.a_dtype("float32")))

    self.scale_6252 = self.Op("cinn_op.scale", 6252, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(bias=self.a_f32("0"), stop_gradient=self.a_array(self.a_bool(False)), bias_after_scale=self.a_bool(True), scale=self.a_f32("-1")))

    self.exp_6253 = self.Op("pd_op.exp", 6253, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6254 = self.Op("cinn_op.generate_shape", 6254, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(3072)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6255 = self.Op("pd_op.expand", 6255, input_types=[self.t_dtensor([1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6256 = self.Op("pd_op.add", 6256, input_types=[self.t_dtensor([-1, -1, -1], self.t_f32()), self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6257 = self.Op("cinn_op.generate_shape", 6257, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(3072)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6258 = self.Op("pd_op.expand", 6258, input_types=[self.t_dtensor([1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_6259 = self.Op("pd_op.divide", 6259, input_types=[self.t_dtensor([-1, -1, -1], self.t_f32()), self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_6260 = self.Op("pd_op.cast", 6260, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(dtype=self.a_dtype("float16"), stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_6261 = self.Op("pd_op.multiply", 6261, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16()), self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.yield_6263 = self.Op("cf.yield", 6263, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6262 = self.Op("cinn_op.fusion", 6262, input_types=[], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_563 = self.Op("pd_op.matmul", 563, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16()), self.t_dtensor([3072, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_6264 = self.Op("cinn_op.generate_shape", 6264, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6265 = self.Op("pd_op.expand", 6265, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6266 = self.Op("pd_op.add", 6266, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.add_6267 = self.Op("pd_op.add", 6267, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.yield_6269 = self.Op("cf.yield", 6269, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6268 = self.Op("cinn_op.fusion", 6268, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.cast_6270 = self.Op("pd_op.cast", 6270, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_6271 = self.Op("cinn_op.reduce_sum", 6271, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.yield_6273 = self.Op("cf.yield", 6273, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[], attrs=dict())

    self.fusion_6272 = self.Op("cinn_op.fusion", 6272, input_types=[], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.cast_6274 = self.Op("pd_op.cast", 6274, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.full_6275 = self.Op("pd_op.full", 6275, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_6276 = self.Op("cinn_op.generate_shape", 6276, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6277 = self.Op("pd_op.expand", 6277, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_6278 = self.Op("pd_op.divide", 6278, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6279 = self.Op("cinn_op.generate_shape", 6279, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6280 = self.Op("pd_op.expand", 6280, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.subtract_6281 = self.Op("pd_op.subtract", 6281, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_6282 = self.Op("pd_op.multiply", 6282, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_6283 = self.Op("cinn_op.reduce_sum", 6283, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.full_6284 = self.Op("pd_op.full", 6284, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_6285 = self.Op("cinn_op.generate_shape", 6285, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6286 = self.Op("pd_op.expand", 6286, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_6287 = self.Op("pd_op.divide", 6287, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.full_6288 = self.Op("pd_op.full", 6288, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("1e-05"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_6289 = self.Op("cinn_op.generate_shape", 6289, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6290 = self.Op("pd_op.expand", 6290, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6291 = self.Op("pd_op.add", 6291, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.rsqrt_6292 = self.Op("pd_op.rsqrt", 6292, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6293 = self.Op("cinn_op.generate_shape", 6293, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6294 = self.Op("pd_op.expand", 6294, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_6295 = self.Op("pd_op.multiply", 6295, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_6296 = self.Op("pd_op.cast", 6296, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6297 = self.Op("cinn_op.generate_shape", 6297, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6298 = self.Op("pd_op.expand", 6298, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_6299 = self.Op("pd_op.multiply", 6299, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_6300 = self.Op("pd_op.cast", 6300, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6301 = self.Op("cinn_op.generate_shape", 6301, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6302 = self.Op("pd_op.expand", 6302, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6303 = self.Op("pd_op.add", 6303, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_6304 = self.Op("pd_op.cast", 6304, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(dtype=self.a_dtype("float16"), stop_gradient=self.a_array(self.a_bool(False))))

    self.yield_6306 = self.Op("cf.yield", 6306, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6305 = self.Op("cinn_op.fusion", 6305, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_574 = self.Op("pd_op.matmul", 574, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.matmul_578 = self.Op("pd_op.matmul", 578, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.matmul_586 = self.Op("pd_op.matmul", 586, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_6307 = self.Op("cinn_op.generate_shape", 6307, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6308 = self.Op("pd_op.expand", 6308, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6309 = self.Op("pd_op.add", 6309, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.scale_6310 = self.Op("cinn_op.scale", 6310, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(bias=self.a_f32("0"), stop_gradient=self.a_array(self.a_bool(False)), bias_after_scale=self.a_bool(True), scale=self.a_f32("0.125")))

    self.generate_shape_6311 = self.Op("cinn_op.generate_shape", 6311, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(12), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.reshape_6312 = self.Op("pd_op.reshape", 6312, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16()), self.t_dtensor([0, -1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.transpose_6313 = self.Op("pd_op.transpose", 6313, input_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16())], output_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), perm=self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6314 = self.Op("cinn_op.generate_shape", 6314, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_array(self.a_str("Mul"), self.a_str("S0"), self.a_i64(12)), self.a_i64(-1), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_6315 = self.Op("pd_op.reshape", 6315, input_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([0, -1, 12, -1, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_6317 = self.Op("cf.yield", 6317, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6316 = self.Op("cinn_op.fusion", 6316, input_types=[], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.generate_shape_6318 = self.Op("cinn_op.generate_shape", 6318, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6319 = self.Op("pd_op.expand", 6319, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6320 = self.Op("pd_op.add", 6320, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.generate_shape_6321 = self.Op("cinn_op.generate_shape", 6321, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(-1), self.a_i64(12), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_6322 = self.Op("pd_op.reshape", 6322, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16()), self.t_dtensor([0, -1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.transpose_6323 = self.Op("pd_op.transpose", 6323, input_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16())], output_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), perm=self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6324 = self.Op("cinn_op.generate_shape", 6324, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_array(self.a_str("Mul"), self.a_str("S0"), self.a_i64(12)), self.a_i64(-1), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_6325 = self.Op("pd_op.reshape", 6325, input_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([0, -1, 12, -1, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_6327 = self.Op("cf.yield", 6327, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6326 = self.Op("cinn_op.fusion", 6326, input_types=[], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.generate_shape_6328 = self.Op("cinn_op.generate_shape", 6328, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6329 = self.Op("pd_op.expand", 6329, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6330 = self.Op("pd_op.add", 6330, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.generate_shape_6331 = self.Op("cinn_op.generate_shape", 6331, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(-1), self.a_i64(12), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_6332 = self.Op("pd_op.reshape", 6332, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16()), self.t_dtensor([0, -1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.transpose_6333 = self.Op("pd_op.transpose", 6333, input_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16())], output_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), perm=self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6334 = self.Op("cinn_op.generate_shape", 6334, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_array(self.a_str("Mul"), self.a_str("S0"), self.a_i64(12)), self.a_i64(-1), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_6335 = self.Op("pd_op.reshape", 6335, input_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([0, -1, 12, -1, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_6337 = self.Op("cf.yield", 6337, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6336 = self.Op("cinn_op.fusion", 6336, input_types=[], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_617 = self.Op("pd_op.matmul", 617, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(True)))

    self.generate_shape_6338 = self.Op("cinn_op.generate_shape", 6338, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("SS0"), self.a_i64(12), self.a_str("SS1"), self.a_str("SS1")), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS1"), self.a_i64(0), self.a_i64(1)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS1"), self.a_i64(1), self.a_i64(1)))))

    self.reshape_6339 = self.Op("pd_op.reshape", 6339, input_types=[self.t_dtensor([-1, -1, -1], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, 12, -1, -1], self.t_f16()), self.t_dtensor([0, -1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.generate_shape_6340 = self.Op("cinn_op.generate_shape", 6340, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(12), self.a_str("S1"), self.a_str("S1")), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6341 = self.Op("pd_op.expand", 6341, input_types=[self.t_dtensor([-1, -1, -1, -1], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6342 = self.Op("pd_op.add", 6342, input_types=[self.t_dtensor([-1, 12, -1, -1], self.t_f16()), self.t_dtensor([-1, -1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, 12, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.generate_shape_6343 = self.Op("cinn_op.generate_shape", 6343, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_array(self.a_str("Mul"), self.a_str("SS0"), self.a_i64(12)), self.a_str("SS1"), self.a_str("SS1")), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS1"), self.a_i64(0), self.a_i64(1)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS1"), self.a_i64(1), self.a_i64(1)))))

    self.reshape_6344 = self.Op("pd_op.reshape", 6344, input_types=[self.t_dtensor([-1, 12, -1, -1], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16()), self.t_dtensor([0, -1, 12, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_6346 = self.Op("cf.yield", 6346, input_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6345 = self.Op("cinn_op.fusion", 6345, input_types=[], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.softmax_626 = self.Op("pd_op.softmax", 626, input_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), axis=self.a_i32(-1), stop_gradient=self.a_array(self.a_bool(False))))

    self.matmul_627 = self.Op("pd_op.matmul", 627, input_types=[self.t_dtensor([-1, -1, -1], self.t_f16()), self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_6347 = self.Op("cinn_op.generate_shape", 6347, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(12), self.a_str("S1"), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.reshape_6348 = self.Op("pd_op.reshape", 6348, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16()), self.t_dtensor([0, -1, -1, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.transpose_6349 = self.Op("pd_op.transpose", 6349, input_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), perm=self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6350 = self.Op("cinn_op.generate_shape", 6350, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.reshape_6351 = self.Op("pd_op.reshape", 6351, input_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([0, -1, -1, 12, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_6353 = self.Op("cf.yield", 6353, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6352 = self.Op("cinn_op.fusion", 6352, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_636 = self.Op("pd_op.matmul", 636, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_6354 = self.Op("cinn_op.generate_shape", 6354, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6355 = self.Op("pd_op.expand", 6355, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6356 = self.Op("pd_op.add", 6356, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.add_6357 = self.Op("pd_op.add", 6357, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.yield_6359 = self.Op("cf.yield", 6359, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6358 = self.Op("cinn_op.fusion", 6358, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.cast_6360 = self.Op("pd_op.cast", 6360, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_6361 = self.Op("cinn_op.reduce_sum", 6361, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.yield_6363 = self.Op("cf.yield", 6363, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[], attrs=dict())

    self.fusion_6362 = self.Op("cinn_op.fusion", 6362, input_types=[], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.cast_6364 = self.Op("pd_op.cast", 6364, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.full_6365 = self.Op("pd_op.full", 6365, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_6366 = self.Op("cinn_op.generate_shape", 6366, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6367 = self.Op("pd_op.expand", 6367, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_6368 = self.Op("pd_op.divide", 6368, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6369 = self.Op("cinn_op.generate_shape", 6369, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6370 = self.Op("pd_op.expand", 6370, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.subtract_6371 = self.Op("pd_op.subtract", 6371, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_6372 = self.Op("pd_op.multiply", 6372, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_6373 = self.Op("cinn_op.reduce_sum", 6373, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.full_6374 = self.Op("pd_op.full", 6374, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_6375 = self.Op("cinn_op.generate_shape", 6375, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6376 = self.Op("pd_op.expand", 6376, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_6377 = self.Op("pd_op.divide", 6377, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.full_6378 = self.Op("pd_op.full", 6378, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("1e-05"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_6379 = self.Op("cinn_op.generate_shape", 6379, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6380 = self.Op("pd_op.expand", 6380, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6381 = self.Op("pd_op.add", 6381, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.rsqrt_6382 = self.Op("pd_op.rsqrt", 6382, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6383 = self.Op("cinn_op.generate_shape", 6383, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6384 = self.Op("pd_op.expand", 6384, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_6385 = self.Op("pd_op.multiply", 6385, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_6386 = self.Op("pd_op.cast", 6386, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6387 = self.Op("cinn_op.generate_shape", 6387, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6388 = self.Op("pd_op.expand", 6388, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_6389 = self.Op("pd_op.multiply", 6389, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_6390 = self.Op("pd_op.cast", 6390, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6391 = self.Op("cinn_op.generate_shape", 6391, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6392 = self.Op("pd_op.expand", 6392, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6393 = self.Op("pd_op.add", 6393, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_6394 = self.Op("pd_op.cast", 6394, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(dtype=self.a_dtype("float16"), stop_gradient=self.a_array(self.a_bool(False))))

    self.yield_6396 = self.Op("cf.yield", 6396, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6395 = self.Op("cinn_op.fusion", 6395, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_640 = self.Op("pd_op.matmul", 640, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 3072], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_6397 = self.Op("cinn_op.generate_shape", 6397, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(3072)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6398 = self.Op("pd_op.expand", 6398, input_types=[self.t_dtensor([3072], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6399 = self.Op("pd_op.add", 6399, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.scale_6400 = self.Op("cinn_op.scale", 6400, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(bias=self.a_f32("0"), stop_gradient=self.a_array(self.a_bool(False)), bias_after_scale=self.a_bool(True), scale=self.a_f32("1.702")))

    self.cast_6401 = self.Op("pd_op.cast", 6401, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.full_6402 = self.Op("pd_op.full", 6402, input_types=[], output_types=[self.t_dtensor([1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("1"), shape=self.a_intarray(1), place=self.a_place("cpu"), dtype=self.a_dtype("float32")))

    self.scale_6403 = self.Op("cinn_op.scale", 6403, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(bias=self.a_f32("0"), stop_gradient=self.a_array(self.a_bool(False)), bias_after_scale=self.a_bool(True), scale=self.a_f32("-1")))

    self.exp_6404 = self.Op("pd_op.exp", 6404, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6405 = self.Op("cinn_op.generate_shape", 6405, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(3072)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6406 = self.Op("pd_op.expand", 6406, input_types=[self.t_dtensor([1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6407 = self.Op("pd_op.add", 6407, input_types=[self.t_dtensor([-1, -1, -1], self.t_f32()), self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6408 = self.Op("cinn_op.generate_shape", 6408, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(3072)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6409 = self.Op("pd_op.expand", 6409, input_types=[self.t_dtensor([1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_6410 = self.Op("pd_op.divide", 6410, input_types=[self.t_dtensor([-1, -1, -1], self.t_f32()), self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_6411 = self.Op("pd_op.cast", 6411, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(dtype=self.a_dtype("float16"), stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_6412 = self.Op("pd_op.multiply", 6412, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16()), self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.yield_6414 = self.Op("cf.yield", 6414, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6413 = self.Op("cinn_op.fusion", 6413, input_types=[], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_646 = self.Op("pd_op.matmul", 646, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16()), self.t_dtensor([3072, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_6415 = self.Op("cinn_op.generate_shape", 6415, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6416 = self.Op("pd_op.expand", 6416, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6417 = self.Op("pd_op.add", 6417, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.add_6418 = self.Op("pd_op.add", 6418, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.yield_6420 = self.Op("cf.yield", 6420, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6419 = self.Op("cinn_op.fusion", 6419, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.cast_6421 = self.Op("pd_op.cast", 6421, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_6422 = self.Op("cinn_op.reduce_sum", 6422, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.yield_6424 = self.Op("cf.yield", 6424, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[], attrs=dict())

    self.fusion_6423 = self.Op("cinn_op.fusion", 6423, input_types=[], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.cast_6425 = self.Op("pd_op.cast", 6425, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.full_6426 = self.Op("pd_op.full", 6426, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_6427 = self.Op("cinn_op.generate_shape", 6427, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6428 = self.Op("pd_op.expand", 6428, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_6429 = self.Op("pd_op.divide", 6429, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6430 = self.Op("cinn_op.generate_shape", 6430, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6431 = self.Op("pd_op.expand", 6431, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.subtract_6432 = self.Op("pd_op.subtract", 6432, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_6433 = self.Op("pd_op.multiply", 6433, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_6434 = self.Op("cinn_op.reduce_sum", 6434, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.full_6435 = self.Op("pd_op.full", 6435, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_6436 = self.Op("cinn_op.generate_shape", 6436, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6437 = self.Op("pd_op.expand", 6437, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_6438 = self.Op("pd_op.divide", 6438, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.full_6439 = self.Op("pd_op.full", 6439, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("1e-05"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_6440 = self.Op("cinn_op.generate_shape", 6440, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6441 = self.Op("pd_op.expand", 6441, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6442 = self.Op("pd_op.add", 6442, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.rsqrt_6443 = self.Op("pd_op.rsqrt", 6443, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6444 = self.Op("cinn_op.generate_shape", 6444, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6445 = self.Op("pd_op.expand", 6445, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_6446 = self.Op("pd_op.multiply", 6446, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_6447 = self.Op("pd_op.cast", 6447, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6448 = self.Op("cinn_op.generate_shape", 6448, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6449 = self.Op("pd_op.expand", 6449, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_6450 = self.Op("pd_op.multiply", 6450, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_6451 = self.Op("pd_op.cast", 6451, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6452 = self.Op("cinn_op.generate_shape", 6452, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6453 = self.Op("pd_op.expand", 6453, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6454 = self.Op("pd_op.add", 6454, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_6455 = self.Op("pd_op.cast", 6455, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(dtype=self.a_dtype("float16"), stop_gradient=self.a_array(self.a_bool(False))))

    self.yield_6457 = self.Op("cf.yield", 6457, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6456 = self.Op("cinn_op.fusion", 6456, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_657 = self.Op("pd_op.matmul", 657, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.matmul_661 = self.Op("pd_op.matmul", 661, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.matmul_669 = self.Op("pd_op.matmul", 669, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_6458 = self.Op("cinn_op.generate_shape", 6458, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6459 = self.Op("pd_op.expand", 6459, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6460 = self.Op("pd_op.add", 6460, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.scale_6461 = self.Op("cinn_op.scale", 6461, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(bias=self.a_f32("0"), stop_gradient=self.a_array(self.a_bool(False)), bias_after_scale=self.a_bool(True), scale=self.a_f32("0.125")))

    self.generate_shape_6462 = self.Op("cinn_op.generate_shape", 6462, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(12), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.reshape_6463 = self.Op("pd_op.reshape", 6463, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16()), self.t_dtensor([0, -1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.transpose_6464 = self.Op("pd_op.transpose", 6464, input_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16())], output_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), perm=self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6465 = self.Op("cinn_op.generate_shape", 6465, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_array(self.a_str("Mul"), self.a_str("S0"), self.a_i64(12)), self.a_i64(-1), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_6466 = self.Op("pd_op.reshape", 6466, input_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([0, -1, 12, -1, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_6468 = self.Op("cf.yield", 6468, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6467 = self.Op("cinn_op.fusion", 6467, input_types=[], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.generate_shape_6469 = self.Op("cinn_op.generate_shape", 6469, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6470 = self.Op("pd_op.expand", 6470, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6471 = self.Op("pd_op.add", 6471, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.generate_shape_6472 = self.Op("cinn_op.generate_shape", 6472, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(-1), self.a_i64(12), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_6473 = self.Op("pd_op.reshape", 6473, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16()), self.t_dtensor([0, -1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.transpose_6474 = self.Op("pd_op.transpose", 6474, input_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16())], output_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), perm=self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6475 = self.Op("cinn_op.generate_shape", 6475, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_array(self.a_str("Mul"), self.a_str("S0"), self.a_i64(12)), self.a_i64(-1), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_6476 = self.Op("pd_op.reshape", 6476, input_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([0, -1, 12, -1, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_6478 = self.Op("cf.yield", 6478, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6477 = self.Op("cinn_op.fusion", 6477, input_types=[], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.generate_shape_6479 = self.Op("cinn_op.generate_shape", 6479, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6480 = self.Op("pd_op.expand", 6480, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6481 = self.Op("pd_op.add", 6481, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.generate_shape_6482 = self.Op("cinn_op.generate_shape", 6482, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(-1), self.a_i64(12), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_6483 = self.Op("pd_op.reshape", 6483, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16()), self.t_dtensor([0, -1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.transpose_6484 = self.Op("pd_op.transpose", 6484, input_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16())], output_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), perm=self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6485 = self.Op("cinn_op.generate_shape", 6485, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_array(self.a_str("Mul"), self.a_str("S0"), self.a_i64(12)), self.a_i64(-1), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_6486 = self.Op("pd_op.reshape", 6486, input_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([0, -1, 12, -1, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_6488 = self.Op("cf.yield", 6488, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6487 = self.Op("cinn_op.fusion", 6487, input_types=[], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_700 = self.Op("pd_op.matmul", 700, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(True)))

    self.generate_shape_6489 = self.Op("cinn_op.generate_shape", 6489, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("SS0"), self.a_i64(12), self.a_str("SS1"), self.a_str("SS1")), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS1"), self.a_i64(0), self.a_i64(1)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS1"), self.a_i64(1), self.a_i64(1)))))

    self.reshape_6490 = self.Op("pd_op.reshape", 6490, input_types=[self.t_dtensor([-1, -1, -1], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, 12, -1, -1], self.t_f16()), self.t_dtensor([0, -1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.generate_shape_6491 = self.Op("cinn_op.generate_shape", 6491, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(12), self.a_str("S1"), self.a_str("S1")), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6492 = self.Op("pd_op.expand", 6492, input_types=[self.t_dtensor([-1, -1, -1, -1], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6493 = self.Op("pd_op.add", 6493, input_types=[self.t_dtensor([-1, 12, -1, -1], self.t_f16()), self.t_dtensor([-1, -1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, 12, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.generate_shape_6494 = self.Op("cinn_op.generate_shape", 6494, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_array(self.a_str("Mul"), self.a_str("SS0"), self.a_i64(12)), self.a_str("SS1"), self.a_str("SS1")), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS1"), self.a_i64(0), self.a_i64(1)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS1"), self.a_i64(1), self.a_i64(1)))))

    self.reshape_6495 = self.Op("pd_op.reshape", 6495, input_types=[self.t_dtensor([-1, 12, -1, -1], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16()), self.t_dtensor([0, -1, 12, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_6497 = self.Op("cf.yield", 6497, input_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6496 = self.Op("cinn_op.fusion", 6496, input_types=[], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.softmax_709 = self.Op("pd_op.softmax", 709, input_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), axis=self.a_i32(-1), stop_gradient=self.a_array(self.a_bool(False))))

    self.matmul_710 = self.Op("pd_op.matmul", 710, input_types=[self.t_dtensor([-1, -1, -1], self.t_f16()), self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_6498 = self.Op("cinn_op.generate_shape", 6498, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(12), self.a_str("S1"), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.reshape_6499 = self.Op("pd_op.reshape", 6499, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16()), self.t_dtensor([0, -1, -1, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.transpose_6500 = self.Op("pd_op.transpose", 6500, input_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), perm=self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6501 = self.Op("cinn_op.generate_shape", 6501, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.reshape_6502 = self.Op("pd_op.reshape", 6502, input_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([0, -1, -1, 12, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_6504 = self.Op("cf.yield", 6504, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6503 = self.Op("cinn_op.fusion", 6503, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_719 = self.Op("pd_op.matmul", 719, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_6505 = self.Op("cinn_op.generate_shape", 6505, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6506 = self.Op("pd_op.expand", 6506, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6507 = self.Op("pd_op.add", 6507, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.add_6508 = self.Op("pd_op.add", 6508, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.yield_6510 = self.Op("cf.yield", 6510, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6509 = self.Op("cinn_op.fusion", 6509, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.cast_6511 = self.Op("pd_op.cast", 6511, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_6512 = self.Op("cinn_op.reduce_sum", 6512, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.yield_6514 = self.Op("cf.yield", 6514, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[], attrs=dict())

    self.fusion_6513 = self.Op("cinn_op.fusion", 6513, input_types=[], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.cast_6515 = self.Op("pd_op.cast", 6515, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.full_6516 = self.Op("pd_op.full", 6516, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_6517 = self.Op("cinn_op.generate_shape", 6517, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6518 = self.Op("pd_op.expand", 6518, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_6519 = self.Op("pd_op.divide", 6519, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6520 = self.Op("cinn_op.generate_shape", 6520, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6521 = self.Op("pd_op.expand", 6521, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.subtract_6522 = self.Op("pd_op.subtract", 6522, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_6523 = self.Op("pd_op.multiply", 6523, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_6524 = self.Op("cinn_op.reduce_sum", 6524, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.full_6525 = self.Op("pd_op.full", 6525, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_6526 = self.Op("cinn_op.generate_shape", 6526, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6527 = self.Op("pd_op.expand", 6527, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_6528 = self.Op("pd_op.divide", 6528, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.full_6529 = self.Op("pd_op.full", 6529, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("1e-05"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_6530 = self.Op("cinn_op.generate_shape", 6530, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6531 = self.Op("pd_op.expand", 6531, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6532 = self.Op("pd_op.add", 6532, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.rsqrt_6533 = self.Op("pd_op.rsqrt", 6533, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6534 = self.Op("cinn_op.generate_shape", 6534, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6535 = self.Op("pd_op.expand", 6535, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_6536 = self.Op("pd_op.multiply", 6536, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_6537 = self.Op("pd_op.cast", 6537, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6538 = self.Op("cinn_op.generate_shape", 6538, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6539 = self.Op("pd_op.expand", 6539, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_6540 = self.Op("pd_op.multiply", 6540, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_6541 = self.Op("pd_op.cast", 6541, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6542 = self.Op("cinn_op.generate_shape", 6542, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6543 = self.Op("pd_op.expand", 6543, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6544 = self.Op("pd_op.add", 6544, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_6545 = self.Op("pd_op.cast", 6545, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(dtype=self.a_dtype("float16"), stop_gradient=self.a_array(self.a_bool(False))))

    self.yield_6547 = self.Op("cf.yield", 6547, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6546 = self.Op("cinn_op.fusion", 6546, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_723 = self.Op("pd_op.matmul", 723, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 3072], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_6548 = self.Op("cinn_op.generate_shape", 6548, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(3072)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6549 = self.Op("pd_op.expand", 6549, input_types=[self.t_dtensor([3072], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6550 = self.Op("pd_op.add", 6550, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.scale_6551 = self.Op("cinn_op.scale", 6551, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(bias=self.a_f32("0"), stop_gradient=self.a_array(self.a_bool(False)), bias_after_scale=self.a_bool(True), scale=self.a_f32("1.702")))

    self.cast_6552 = self.Op("pd_op.cast", 6552, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.full_6553 = self.Op("pd_op.full", 6553, input_types=[], output_types=[self.t_dtensor([1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("1"), shape=self.a_intarray(1), place=self.a_place("cpu"), dtype=self.a_dtype("float32")))

    self.scale_6554 = self.Op("cinn_op.scale", 6554, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(bias=self.a_f32("0"), stop_gradient=self.a_array(self.a_bool(False)), bias_after_scale=self.a_bool(True), scale=self.a_f32("-1")))

    self.exp_6555 = self.Op("pd_op.exp", 6555, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6556 = self.Op("cinn_op.generate_shape", 6556, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(3072)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6557 = self.Op("pd_op.expand", 6557, input_types=[self.t_dtensor([1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6558 = self.Op("pd_op.add", 6558, input_types=[self.t_dtensor([-1, -1, -1], self.t_f32()), self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6559 = self.Op("cinn_op.generate_shape", 6559, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(3072)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6560 = self.Op("pd_op.expand", 6560, input_types=[self.t_dtensor([1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_6561 = self.Op("pd_op.divide", 6561, input_types=[self.t_dtensor([-1, -1, -1], self.t_f32()), self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_6562 = self.Op("pd_op.cast", 6562, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(dtype=self.a_dtype("float16"), stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_6563 = self.Op("pd_op.multiply", 6563, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16()), self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.yield_6565 = self.Op("cf.yield", 6565, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6564 = self.Op("cinn_op.fusion", 6564, input_types=[], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_729 = self.Op("pd_op.matmul", 729, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16()), self.t_dtensor([3072, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_6566 = self.Op("cinn_op.generate_shape", 6566, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6567 = self.Op("pd_op.expand", 6567, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6568 = self.Op("pd_op.add", 6568, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.add_6569 = self.Op("pd_op.add", 6569, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.yield_6571 = self.Op("cf.yield", 6571, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6570 = self.Op("cinn_op.fusion", 6570, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.cast_6572 = self.Op("pd_op.cast", 6572, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_6573 = self.Op("cinn_op.reduce_sum", 6573, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.yield_6575 = self.Op("cf.yield", 6575, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[], attrs=dict())

    self.fusion_6574 = self.Op("cinn_op.fusion", 6574, input_types=[], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.cast_6576 = self.Op("pd_op.cast", 6576, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.full_6577 = self.Op("pd_op.full", 6577, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_6578 = self.Op("cinn_op.generate_shape", 6578, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6579 = self.Op("pd_op.expand", 6579, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_6580 = self.Op("pd_op.divide", 6580, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6581 = self.Op("cinn_op.generate_shape", 6581, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6582 = self.Op("pd_op.expand", 6582, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.subtract_6583 = self.Op("pd_op.subtract", 6583, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_6584 = self.Op("pd_op.multiply", 6584, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_6585 = self.Op("cinn_op.reduce_sum", 6585, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.full_6586 = self.Op("pd_op.full", 6586, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_6587 = self.Op("cinn_op.generate_shape", 6587, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6588 = self.Op("pd_op.expand", 6588, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_6589 = self.Op("pd_op.divide", 6589, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.full_6590 = self.Op("pd_op.full", 6590, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("1e-05"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_6591 = self.Op("cinn_op.generate_shape", 6591, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6592 = self.Op("pd_op.expand", 6592, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6593 = self.Op("pd_op.add", 6593, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.rsqrt_6594 = self.Op("pd_op.rsqrt", 6594, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6595 = self.Op("cinn_op.generate_shape", 6595, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6596 = self.Op("pd_op.expand", 6596, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_6597 = self.Op("pd_op.multiply", 6597, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_6598 = self.Op("pd_op.cast", 6598, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6599 = self.Op("cinn_op.generate_shape", 6599, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6600 = self.Op("pd_op.expand", 6600, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_6601 = self.Op("pd_op.multiply", 6601, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_6602 = self.Op("pd_op.cast", 6602, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6603 = self.Op("cinn_op.generate_shape", 6603, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6604 = self.Op("pd_op.expand", 6604, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6605 = self.Op("pd_op.add", 6605, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_6606 = self.Op("pd_op.cast", 6606, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(dtype=self.a_dtype("float16"), stop_gradient=self.a_array(self.a_bool(False))))

    self.yield_6608 = self.Op("cf.yield", 6608, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6607 = self.Op("cinn_op.fusion", 6607, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_740 = self.Op("pd_op.matmul", 740, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.matmul_744 = self.Op("pd_op.matmul", 744, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.matmul_752 = self.Op("pd_op.matmul", 752, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_6609 = self.Op("cinn_op.generate_shape", 6609, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6610 = self.Op("pd_op.expand", 6610, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6611 = self.Op("pd_op.add", 6611, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.scale_6612 = self.Op("cinn_op.scale", 6612, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(bias=self.a_f32("0"), stop_gradient=self.a_array(self.a_bool(False)), bias_after_scale=self.a_bool(True), scale=self.a_f32("0.125")))

    self.generate_shape_6613 = self.Op("cinn_op.generate_shape", 6613, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(12), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.reshape_6614 = self.Op("pd_op.reshape", 6614, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16()), self.t_dtensor([0, -1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.transpose_6615 = self.Op("pd_op.transpose", 6615, input_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16())], output_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), perm=self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6616 = self.Op("cinn_op.generate_shape", 6616, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_array(self.a_str("Mul"), self.a_str("S0"), self.a_i64(12)), self.a_i64(-1), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_6617 = self.Op("pd_op.reshape", 6617, input_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([0, -1, 12, -1, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_6619 = self.Op("cf.yield", 6619, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6618 = self.Op("cinn_op.fusion", 6618, input_types=[], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.generate_shape_6620 = self.Op("cinn_op.generate_shape", 6620, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6621 = self.Op("pd_op.expand", 6621, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6622 = self.Op("pd_op.add", 6622, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.generate_shape_6623 = self.Op("cinn_op.generate_shape", 6623, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(-1), self.a_i64(12), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_6624 = self.Op("pd_op.reshape", 6624, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16()), self.t_dtensor([0, -1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.transpose_6625 = self.Op("pd_op.transpose", 6625, input_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16())], output_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), perm=self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6626 = self.Op("cinn_op.generate_shape", 6626, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_array(self.a_str("Mul"), self.a_str("S0"), self.a_i64(12)), self.a_i64(-1), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_6627 = self.Op("pd_op.reshape", 6627, input_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([0, -1, 12, -1, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_6629 = self.Op("cf.yield", 6629, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6628 = self.Op("cinn_op.fusion", 6628, input_types=[], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.generate_shape_6630 = self.Op("cinn_op.generate_shape", 6630, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6631 = self.Op("pd_op.expand", 6631, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6632 = self.Op("pd_op.add", 6632, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.generate_shape_6633 = self.Op("cinn_op.generate_shape", 6633, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(-1), self.a_i64(12), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_6634 = self.Op("pd_op.reshape", 6634, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16()), self.t_dtensor([0, -1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.transpose_6635 = self.Op("pd_op.transpose", 6635, input_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16())], output_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), perm=self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6636 = self.Op("cinn_op.generate_shape", 6636, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_array(self.a_str("Mul"), self.a_str("S0"), self.a_i64(12)), self.a_i64(-1), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_6637 = self.Op("pd_op.reshape", 6637, input_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([0, -1, 12, -1, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_6639 = self.Op("cf.yield", 6639, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6638 = self.Op("cinn_op.fusion", 6638, input_types=[], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_783 = self.Op("pd_op.matmul", 783, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(True)))

    self.generate_shape_6640 = self.Op("cinn_op.generate_shape", 6640, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("SS0"), self.a_i64(12), self.a_str("SS1"), self.a_str("SS1")), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS1"), self.a_i64(0), self.a_i64(1)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS1"), self.a_i64(1), self.a_i64(1)))))

    self.reshape_6641 = self.Op("pd_op.reshape", 6641, input_types=[self.t_dtensor([-1, -1, -1], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, 12, -1, -1], self.t_f16()), self.t_dtensor([0, -1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.generate_shape_6642 = self.Op("cinn_op.generate_shape", 6642, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(12), self.a_str("S1"), self.a_str("S1")), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6643 = self.Op("pd_op.expand", 6643, input_types=[self.t_dtensor([-1, -1, -1, -1], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6644 = self.Op("pd_op.add", 6644, input_types=[self.t_dtensor([-1, 12, -1, -1], self.t_f16()), self.t_dtensor([-1, -1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, 12, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.generate_shape_6645 = self.Op("cinn_op.generate_shape", 6645, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_array(self.a_str("Mul"), self.a_str("SS0"), self.a_i64(12)), self.a_str("SS1"), self.a_str("SS1")), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS1"), self.a_i64(0), self.a_i64(1)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS1"), self.a_i64(1), self.a_i64(1)))))

    self.reshape_6646 = self.Op("pd_op.reshape", 6646, input_types=[self.t_dtensor([-1, 12, -1, -1], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16()), self.t_dtensor([0, -1, 12, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_6648 = self.Op("cf.yield", 6648, input_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6647 = self.Op("cinn_op.fusion", 6647, input_types=[], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.softmax_792 = self.Op("pd_op.softmax", 792, input_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), axis=self.a_i32(-1), stop_gradient=self.a_array(self.a_bool(False))))

    self.matmul_793 = self.Op("pd_op.matmul", 793, input_types=[self.t_dtensor([-1, -1, -1], self.t_f16()), self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_6649 = self.Op("cinn_op.generate_shape", 6649, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(12), self.a_str("S1"), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.reshape_6650 = self.Op("pd_op.reshape", 6650, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16()), self.t_dtensor([0, -1, -1, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.transpose_6651 = self.Op("pd_op.transpose", 6651, input_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), perm=self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6652 = self.Op("cinn_op.generate_shape", 6652, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.reshape_6653 = self.Op("pd_op.reshape", 6653, input_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([0, -1, -1, 12, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_6655 = self.Op("cf.yield", 6655, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6654 = self.Op("cinn_op.fusion", 6654, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_802 = self.Op("pd_op.matmul", 802, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_6656 = self.Op("cinn_op.generate_shape", 6656, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6657 = self.Op("pd_op.expand", 6657, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6658 = self.Op("pd_op.add", 6658, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.add_6659 = self.Op("pd_op.add", 6659, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.yield_6661 = self.Op("cf.yield", 6661, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6660 = self.Op("cinn_op.fusion", 6660, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.cast_6662 = self.Op("pd_op.cast", 6662, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_6663 = self.Op("cinn_op.reduce_sum", 6663, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.yield_6665 = self.Op("cf.yield", 6665, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[], attrs=dict())

    self.fusion_6664 = self.Op("cinn_op.fusion", 6664, input_types=[], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.cast_6666 = self.Op("pd_op.cast", 6666, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.full_6667 = self.Op("pd_op.full", 6667, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_6668 = self.Op("cinn_op.generate_shape", 6668, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6669 = self.Op("pd_op.expand", 6669, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_6670 = self.Op("pd_op.divide", 6670, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6671 = self.Op("cinn_op.generate_shape", 6671, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6672 = self.Op("pd_op.expand", 6672, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.subtract_6673 = self.Op("pd_op.subtract", 6673, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_6674 = self.Op("pd_op.multiply", 6674, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_6675 = self.Op("cinn_op.reduce_sum", 6675, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.full_6676 = self.Op("pd_op.full", 6676, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_6677 = self.Op("cinn_op.generate_shape", 6677, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6678 = self.Op("pd_op.expand", 6678, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_6679 = self.Op("pd_op.divide", 6679, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.full_6680 = self.Op("pd_op.full", 6680, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("1e-05"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_6681 = self.Op("cinn_op.generate_shape", 6681, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6682 = self.Op("pd_op.expand", 6682, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6683 = self.Op("pd_op.add", 6683, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.rsqrt_6684 = self.Op("pd_op.rsqrt", 6684, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6685 = self.Op("cinn_op.generate_shape", 6685, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6686 = self.Op("pd_op.expand", 6686, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_6687 = self.Op("pd_op.multiply", 6687, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_6688 = self.Op("pd_op.cast", 6688, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6689 = self.Op("cinn_op.generate_shape", 6689, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6690 = self.Op("pd_op.expand", 6690, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_6691 = self.Op("pd_op.multiply", 6691, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_6692 = self.Op("pd_op.cast", 6692, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6693 = self.Op("cinn_op.generate_shape", 6693, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6694 = self.Op("pd_op.expand", 6694, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6695 = self.Op("pd_op.add", 6695, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_6696 = self.Op("pd_op.cast", 6696, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(dtype=self.a_dtype("float16"), stop_gradient=self.a_array(self.a_bool(False))))

    self.yield_6698 = self.Op("cf.yield", 6698, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6697 = self.Op("cinn_op.fusion", 6697, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_806 = self.Op("pd_op.matmul", 806, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 3072], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_6699 = self.Op("cinn_op.generate_shape", 6699, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(3072)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6700 = self.Op("pd_op.expand", 6700, input_types=[self.t_dtensor([3072], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6701 = self.Op("pd_op.add", 6701, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.scale_6702 = self.Op("cinn_op.scale", 6702, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(bias=self.a_f32("0"), stop_gradient=self.a_array(self.a_bool(False)), bias_after_scale=self.a_bool(True), scale=self.a_f32("1.702")))

    self.cast_6703 = self.Op("pd_op.cast", 6703, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.full_6704 = self.Op("pd_op.full", 6704, input_types=[], output_types=[self.t_dtensor([1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("1"), shape=self.a_intarray(1), place=self.a_place("cpu"), dtype=self.a_dtype("float32")))

    self.scale_6705 = self.Op("cinn_op.scale", 6705, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(bias=self.a_f32("0"), stop_gradient=self.a_array(self.a_bool(False)), bias_after_scale=self.a_bool(True), scale=self.a_f32("-1")))

    self.exp_6706 = self.Op("pd_op.exp", 6706, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6707 = self.Op("cinn_op.generate_shape", 6707, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(3072)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6708 = self.Op("pd_op.expand", 6708, input_types=[self.t_dtensor([1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6709 = self.Op("pd_op.add", 6709, input_types=[self.t_dtensor([-1, -1, -1], self.t_f32()), self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6710 = self.Op("cinn_op.generate_shape", 6710, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(3072)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6711 = self.Op("pd_op.expand", 6711, input_types=[self.t_dtensor([1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_6712 = self.Op("pd_op.divide", 6712, input_types=[self.t_dtensor([-1, -1, -1], self.t_f32()), self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_6713 = self.Op("pd_op.cast", 6713, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(dtype=self.a_dtype("float16"), stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_6714 = self.Op("pd_op.multiply", 6714, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16()), self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.yield_6716 = self.Op("cf.yield", 6716, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6715 = self.Op("cinn_op.fusion", 6715, input_types=[], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_812 = self.Op("pd_op.matmul", 812, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16()), self.t_dtensor([3072, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_6717 = self.Op("cinn_op.generate_shape", 6717, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6718 = self.Op("pd_op.expand", 6718, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6719 = self.Op("pd_op.add", 6719, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.add_6720 = self.Op("pd_op.add", 6720, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.yield_6722 = self.Op("cf.yield", 6722, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6721 = self.Op("cinn_op.fusion", 6721, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.cast_6723 = self.Op("pd_op.cast", 6723, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_6724 = self.Op("cinn_op.reduce_sum", 6724, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.yield_6726 = self.Op("cf.yield", 6726, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[], attrs=dict())

    self.fusion_6725 = self.Op("cinn_op.fusion", 6725, input_types=[], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.cast_6727 = self.Op("pd_op.cast", 6727, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.full_6728 = self.Op("pd_op.full", 6728, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_6729 = self.Op("cinn_op.generate_shape", 6729, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6730 = self.Op("pd_op.expand", 6730, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_6731 = self.Op("pd_op.divide", 6731, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6732 = self.Op("cinn_op.generate_shape", 6732, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6733 = self.Op("pd_op.expand", 6733, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.subtract_6734 = self.Op("pd_op.subtract", 6734, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_6735 = self.Op("pd_op.multiply", 6735, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_6736 = self.Op("cinn_op.reduce_sum", 6736, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.full_6737 = self.Op("pd_op.full", 6737, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_6738 = self.Op("cinn_op.generate_shape", 6738, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6739 = self.Op("pd_op.expand", 6739, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_6740 = self.Op("pd_op.divide", 6740, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.full_6741 = self.Op("pd_op.full", 6741, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("1e-05"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_6742 = self.Op("cinn_op.generate_shape", 6742, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6743 = self.Op("pd_op.expand", 6743, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6744 = self.Op("pd_op.add", 6744, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.rsqrt_6745 = self.Op("pd_op.rsqrt", 6745, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6746 = self.Op("cinn_op.generate_shape", 6746, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6747 = self.Op("pd_op.expand", 6747, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_6748 = self.Op("pd_op.multiply", 6748, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_6749 = self.Op("pd_op.cast", 6749, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6750 = self.Op("cinn_op.generate_shape", 6750, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6751 = self.Op("pd_op.expand", 6751, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_6752 = self.Op("pd_op.multiply", 6752, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_6753 = self.Op("pd_op.cast", 6753, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6754 = self.Op("cinn_op.generate_shape", 6754, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6755 = self.Op("pd_op.expand", 6755, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6756 = self.Op("pd_op.add", 6756, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_6757 = self.Op("pd_op.cast", 6757, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(dtype=self.a_dtype("float16"), stop_gradient=self.a_array(self.a_bool(False))))

    self.yield_6759 = self.Op("cf.yield", 6759, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6758 = self.Op("cinn_op.fusion", 6758, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_823 = self.Op("pd_op.matmul", 823, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.matmul_827 = self.Op("pd_op.matmul", 827, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.matmul_835 = self.Op("pd_op.matmul", 835, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_6760 = self.Op("cinn_op.generate_shape", 6760, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6761 = self.Op("pd_op.expand", 6761, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6762 = self.Op("pd_op.add", 6762, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.scale_6763 = self.Op("cinn_op.scale", 6763, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(bias=self.a_f32("0"), stop_gradient=self.a_array(self.a_bool(False)), bias_after_scale=self.a_bool(True), scale=self.a_f32("0.125")))

    self.generate_shape_6764 = self.Op("cinn_op.generate_shape", 6764, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(12), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.reshape_6765 = self.Op("pd_op.reshape", 6765, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16()), self.t_dtensor([0, -1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.transpose_6766 = self.Op("pd_op.transpose", 6766, input_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16())], output_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), perm=self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6767 = self.Op("cinn_op.generate_shape", 6767, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_array(self.a_str("Mul"), self.a_str("S0"), self.a_i64(12)), self.a_i64(-1), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_6768 = self.Op("pd_op.reshape", 6768, input_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([0, -1, 12, -1, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_6770 = self.Op("cf.yield", 6770, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6769 = self.Op("cinn_op.fusion", 6769, input_types=[], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.generate_shape_6771 = self.Op("cinn_op.generate_shape", 6771, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6772 = self.Op("pd_op.expand", 6772, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6773 = self.Op("pd_op.add", 6773, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.generate_shape_6774 = self.Op("cinn_op.generate_shape", 6774, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(-1), self.a_i64(12), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_6775 = self.Op("pd_op.reshape", 6775, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16()), self.t_dtensor([0, -1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.transpose_6776 = self.Op("pd_op.transpose", 6776, input_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16())], output_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), perm=self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6777 = self.Op("cinn_op.generate_shape", 6777, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_array(self.a_str("Mul"), self.a_str("S0"), self.a_i64(12)), self.a_i64(-1), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_6778 = self.Op("pd_op.reshape", 6778, input_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([0, -1, 12, -1, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_6780 = self.Op("cf.yield", 6780, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6779 = self.Op("cinn_op.fusion", 6779, input_types=[], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.generate_shape_6781 = self.Op("cinn_op.generate_shape", 6781, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6782 = self.Op("pd_op.expand", 6782, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6783 = self.Op("pd_op.add", 6783, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.generate_shape_6784 = self.Op("cinn_op.generate_shape", 6784, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(-1), self.a_i64(12), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_6785 = self.Op("pd_op.reshape", 6785, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16()), self.t_dtensor([0, -1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.transpose_6786 = self.Op("pd_op.transpose", 6786, input_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16())], output_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), perm=self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6787 = self.Op("cinn_op.generate_shape", 6787, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_array(self.a_str("Mul"), self.a_str("S0"), self.a_i64(12)), self.a_i64(-1), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_6788 = self.Op("pd_op.reshape", 6788, input_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([0, -1, 12, -1, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_6790 = self.Op("cf.yield", 6790, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6789 = self.Op("cinn_op.fusion", 6789, input_types=[], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_866 = self.Op("pd_op.matmul", 866, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(True)))

    self.generate_shape_6791 = self.Op("cinn_op.generate_shape", 6791, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("SS0"), self.a_i64(12), self.a_str("SS1"), self.a_str("SS1")), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS1"), self.a_i64(0), self.a_i64(1)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS1"), self.a_i64(1), self.a_i64(1)))))

    self.reshape_6792 = self.Op("pd_op.reshape", 6792, input_types=[self.t_dtensor([-1, -1, -1], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, 12, -1, -1], self.t_f16()), self.t_dtensor([0, -1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.generate_shape_6793 = self.Op("cinn_op.generate_shape", 6793, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(12), self.a_str("S1"), self.a_str("S1")), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6794 = self.Op("pd_op.expand", 6794, input_types=[self.t_dtensor([-1, -1, -1, -1], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6795 = self.Op("pd_op.add", 6795, input_types=[self.t_dtensor([-1, 12, -1, -1], self.t_f16()), self.t_dtensor([-1, -1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, 12, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.generate_shape_6796 = self.Op("cinn_op.generate_shape", 6796, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_array(self.a_str("Mul"), self.a_str("SS0"), self.a_i64(12)), self.a_str("SS1"), self.a_str("SS1")), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS1"), self.a_i64(0), self.a_i64(1)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS1"), self.a_i64(1), self.a_i64(1)))))

    self.reshape_6797 = self.Op("pd_op.reshape", 6797, input_types=[self.t_dtensor([-1, 12, -1, -1], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16()), self.t_dtensor([0, -1, 12, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_6799 = self.Op("cf.yield", 6799, input_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6798 = self.Op("cinn_op.fusion", 6798, input_types=[], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.softmax_875 = self.Op("pd_op.softmax", 875, input_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), axis=self.a_i32(-1), stop_gradient=self.a_array(self.a_bool(False))))

    self.matmul_876 = self.Op("pd_op.matmul", 876, input_types=[self.t_dtensor([-1, -1, -1], self.t_f16()), self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_6800 = self.Op("cinn_op.generate_shape", 6800, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(12), self.a_str("S1"), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.reshape_6801 = self.Op("pd_op.reshape", 6801, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16()), self.t_dtensor([0, -1, -1, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.transpose_6802 = self.Op("pd_op.transpose", 6802, input_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), perm=self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6803 = self.Op("cinn_op.generate_shape", 6803, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.reshape_6804 = self.Op("pd_op.reshape", 6804, input_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([0, -1, -1, 12, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_6806 = self.Op("cf.yield", 6806, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6805 = self.Op("cinn_op.fusion", 6805, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_885 = self.Op("pd_op.matmul", 885, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_6807 = self.Op("cinn_op.generate_shape", 6807, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6808 = self.Op("pd_op.expand", 6808, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6809 = self.Op("pd_op.add", 6809, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.add_6810 = self.Op("pd_op.add", 6810, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.yield_6812 = self.Op("cf.yield", 6812, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6811 = self.Op("cinn_op.fusion", 6811, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.cast_6813 = self.Op("pd_op.cast", 6813, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_6814 = self.Op("cinn_op.reduce_sum", 6814, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.yield_6816 = self.Op("cf.yield", 6816, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[], attrs=dict())

    self.fusion_6815 = self.Op("cinn_op.fusion", 6815, input_types=[], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.cast_6817 = self.Op("pd_op.cast", 6817, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.full_6818 = self.Op("pd_op.full", 6818, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_6819 = self.Op("cinn_op.generate_shape", 6819, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6820 = self.Op("pd_op.expand", 6820, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_6821 = self.Op("pd_op.divide", 6821, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6822 = self.Op("cinn_op.generate_shape", 6822, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6823 = self.Op("pd_op.expand", 6823, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.subtract_6824 = self.Op("pd_op.subtract", 6824, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_6825 = self.Op("pd_op.multiply", 6825, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_6826 = self.Op("cinn_op.reduce_sum", 6826, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.full_6827 = self.Op("pd_op.full", 6827, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_6828 = self.Op("cinn_op.generate_shape", 6828, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6829 = self.Op("pd_op.expand", 6829, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_6830 = self.Op("pd_op.divide", 6830, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.full_6831 = self.Op("pd_op.full", 6831, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("1e-05"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_6832 = self.Op("cinn_op.generate_shape", 6832, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6833 = self.Op("pd_op.expand", 6833, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6834 = self.Op("pd_op.add", 6834, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.rsqrt_6835 = self.Op("pd_op.rsqrt", 6835, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6836 = self.Op("cinn_op.generate_shape", 6836, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6837 = self.Op("pd_op.expand", 6837, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_6838 = self.Op("pd_op.multiply", 6838, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_6839 = self.Op("pd_op.cast", 6839, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6840 = self.Op("cinn_op.generate_shape", 6840, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6841 = self.Op("pd_op.expand", 6841, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_6842 = self.Op("pd_op.multiply", 6842, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_6843 = self.Op("pd_op.cast", 6843, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6844 = self.Op("cinn_op.generate_shape", 6844, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6845 = self.Op("pd_op.expand", 6845, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6846 = self.Op("pd_op.add", 6846, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_6847 = self.Op("pd_op.cast", 6847, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(dtype=self.a_dtype("float16"), stop_gradient=self.a_array(self.a_bool(False))))

    self.yield_6849 = self.Op("cf.yield", 6849, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6848 = self.Op("cinn_op.fusion", 6848, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_889 = self.Op("pd_op.matmul", 889, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 3072], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_6850 = self.Op("cinn_op.generate_shape", 6850, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(3072)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6851 = self.Op("pd_op.expand", 6851, input_types=[self.t_dtensor([3072], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6852 = self.Op("pd_op.add", 6852, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.scale_6853 = self.Op("cinn_op.scale", 6853, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(bias=self.a_f32("0"), stop_gradient=self.a_array(self.a_bool(False)), bias_after_scale=self.a_bool(True), scale=self.a_f32("1.702")))

    self.cast_6854 = self.Op("pd_op.cast", 6854, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.full_6855 = self.Op("pd_op.full", 6855, input_types=[], output_types=[self.t_dtensor([1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("1"), shape=self.a_intarray(1), place=self.a_place("cpu"), dtype=self.a_dtype("float32")))

    self.scale_6856 = self.Op("cinn_op.scale", 6856, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(bias=self.a_f32("0"), stop_gradient=self.a_array(self.a_bool(False)), bias_after_scale=self.a_bool(True), scale=self.a_f32("-1")))

    self.exp_6857 = self.Op("pd_op.exp", 6857, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6858 = self.Op("cinn_op.generate_shape", 6858, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(3072)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6859 = self.Op("pd_op.expand", 6859, input_types=[self.t_dtensor([1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6860 = self.Op("pd_op.add", 6860, input_types=[self.t_dtensor([-1, -1, -1], self.t_f32()), self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6861 = self.Op("cinn_op.generate_shape", 6861, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(3072)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6862 = self.Op("pd_op.expand", 6862, input_types=[self.t_dtensor([1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_6863 = self.Op("pd_op.divide", 6863, input_types=[self.t_dtensor([-1, -1, -1], self.t_f32()), self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_6864 = self.Op("pd_op.cast", 6864, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(dtype=self.a_dtype("float16"), stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_6865 = self.Op("pd_op.multiply", 6865, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16()), self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.yield_6867 = self.Op("cf.yield", 6867, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6866 = self.Op("cinn_op.fusion", 6866, input_types=[], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_895 = self.Op("pd_op.matmul", 895, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16()), self.t_dtensor([3072, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_6868 = self.Op("cinn_op.generate_shape", 6868, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6869 = self.Op("pd_op.expand", 6869, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6870 = self.Op("pd_op.add", 6870, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.add_6871 = self.Op("pd_op.add", 6871, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.yield_6873 = self.Op("cf.yield", 6873, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6872 = self.Op("cinn_op.fusion", 6872, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.cast_6874 = self.Op("pd_op.cast", 6874, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_6875 = self.Op("cinn_op.reduce_sum", 6875, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.yield_6877 = self.Op("cf.yield", 6877, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[], attrs=dict())

    self.fusion_6876 = self.Op("cinn_op.fusion", 6876, input_types=[], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.cast_6878 = self.Op("pd_op.cast", 6878, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.full_6879 = self.Op("pd_op.full", 6879, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_6880 = self.Op("cinn_op.generate_shape", 6880, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6881 = self.Op("pd_op.expand", 6881, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_6882 = self.Op("pd_op.divide", 6882, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6883 = self.Op("cinn_op.generate_shape", 6883, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6884 = self.Op("pd_op.expand", 6884, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.subtract_6885 = self.Op("pd_op.subtract", 6885, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_6886 = self.Op("pd_op.multiply", 6886, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_6887 = self.Op("cinn_op.reduce_sum", 6887, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.full_6888 = self.Op("pd_op.full", 6888, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_6889 = self.Op("cinn_op.generate_shape", 6889, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6890 = self.Op("pd_op.expand", 6890, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_6891 = self.Op("pd_op.divide", 6891, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.full_6892 = self.Op("pd_op.full", 6892, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("1e-05"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_6893 = self.Op("cinn_op.generate_shape", 6893, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6894 = self.Op("pd_op.expand", 6894, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6895 = self.Op("pd_op.add", 6895, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.rsqrt_6896 = self.Op("pd_op.rsqrt", 6896, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6897 = self.Op("cinn_op.generate_shape", 6897, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6898 = self.Op("pd_op.expand", 6898, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_6899 = self.Op("pd_op.multiply", 6899, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_6900 = self.Op("pd_op.cast", 6900, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6901 = self.Op("cinn_op.generate_shape", 6901, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6902 = self.Op("pd_op.expand", 6902, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_6903 = self.Op("pd_op.multiply", 6903, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_6904 = self.Op("pd_op.cast", 6904, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6905 = self.Op("cinn_op.generate_shape", 6905, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6906 = self.Op("pd_op.expand", 6906, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6907 = self.Op("pd_op.add", 6907, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_6908 = self.Op("pd_op.cast", 6908, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(dtype=self.a_dtype("float16"), stop_gradient=self.a_array(self.a_bool(False))))

    self.yield_6910 = self.Op("cf.yield", 6910, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6909 = self.Op("cinn_op.fusion", 6909, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_906 = self.Op("pd_op.matmul", 906, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.matmul_910 = self.Op("pd_op.matmul", 910, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.matmul_918 = self.Op("pd_op.matmul", 918, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_6911 = self.Op("cinn_op.generate_shape", 6911, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6912 = self.Op("pd_op.expand", 6912, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6913 = self.Op("pd_op.add", 6913, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.scale_6914 = self.Op("cinn_op.scale", 6914, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(bias=self.a_f32("0"), stop_gradient=self.a_array(self.a_bool(False)), bias_after_scale=self.a_bool(True), scale=self.a_f32("0.125")))

    self.generate_shape_6915 = self.Op("cinn_op.generate_shape", 6915, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(12), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.reshape_6916 = self.Op("pd_op.reshape", 6916, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16()), self.t_dtensor([0, -1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.transpose_6917 = self.Op("pd_op.transpose", 6917, input_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16())], output_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), perm=self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6918 = self.Op("cinn_op.generate_shape", 6918, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_array(self.a_str("Mul"), self.a_str("S0"), self.a_i64(12)), self.a_i64(-1), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_6919 = self.Op("pd_op.reshape", 6919, input_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([0, -1, 12, -1, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_6921 = self.Op("cf.yield", 6921, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6920 = self.Op("cinn_op.fusion", 6920, input_types=[], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.generate_shape_6922 = self.Op("cinn_op.generate_shape", 6922, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6923 = self.Op("pd_op.expand", 6923, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6924 = self.Op("pd_op.add", 6924, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.generate_shape_6925 = self.Op("cinn_op.generate_shape", 6925, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(-1), self.a_i64(12), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_6926 = self.Op("pd_op.reshape", 6926, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16()), self.t_dtensor([0, -1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.transpose_6927 = self.Op("pd_op.transpose", 6927, input_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16())], output_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), perm=self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6928 = self.Op("cinn_op.generate_shape", 6928, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_array(self.a_str("Mul"), self.a_str("S0"), self.a_i64(12)), self.a_i64(-1), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_6929 = self.Op("pd_op.reshape", 6929, input_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([0, -1, 12, -1, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_6931 = self.Op("cf.yield", 6931, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6930 = self.Op("cinn_op.fusion", 6930, input_types=[], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.generate_shape_6932 = self.Op("cinn_op.generate_shape", 6932, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6933 = self.Op("pd_op.expand", 6933, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6934 = self.Op("pd_op.add", 6934, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.generate_shape_6935 = self.Op("cinn_op.generate_shape", 6935, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(-1), self.a_i64(12), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_6936 = self.Op("pd_op.reshape", 6936, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16()), self.t_dtensor([0, -1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.transpose_6937 = self.Op("pd_op.transpose", 6937, input_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16())], output_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), perm=self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6938 = self.Op("cinn_op.generate_shape", 6938, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_array(self.a_str("Mul"), self.a_str("S0"), self.a_i64(12)), self.a_i64(-1), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_6939 = self.Op("pd_op.reshape", 6939, input_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([0, -1, 12, -1, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_6941 = self.Op("cf.yield", 6941, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6940 = self.Op("cinn_op.fusion", 6940, input_types=[], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_949 = self.Op("pd_op.matmul", 949, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(True)))

    self.generate_shape_6942 = self.Op("cinn_op.generate_shape", 6942, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("SS0"), self.a_i64(12), self.a_str("SS1"), self.a_str("SS1")), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS1"), self.a_i64(0), self.a_i64(1)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS1"), self.a_i64(1), self.a_i64(1)))))

    self.reshape_6943 = self.Op("pd_op.reshape", 6943, input_types=[self.t_dtensor([-1, -1, -1], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, 12, -1, -1], self.t_f16()), self.t_dtensor([0, -1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.generate_shape_6944 = self.Op("cinn_op.generate_shape", 6944, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(12), self.a_str("S1"), self.a_str("S1")), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6945 = self.Op("pd_op.expand", 6945, input_types=[self.t_dtensor([-1, -1, -1, -1], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6946 = self.Op("pd_op.add", 6946, input_types=[self.t_dtensor([-1, 12, -1, -1], self.t_f16()), self.t_dtensor([-1, -1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, 12, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.generate_shape_6947 = self.Op("cinn_op.generate_shape", 6947, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_array(self.a_str("Mul"), self.a_str("SS0"), self.a_i64(12)), self.a_str("SS1"), self.a_str("SS1")), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS1"), self.a_i64(0), self.a_i64(1)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS1"), self.a_i64(1), self.a_i64(1)))))

    self.reshape_6948 = self.Op("pd_op.reshape", 6948, input_types=[self.t_dtensor([-1, 12, -1, -1], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16()), self.t_dtensor([0, -1, 12, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_6950 = self.Op("cf.yield", 6950, input_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6949 = self.Op("cinn_op.fusion", 6949, input_types=[], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.softmax_958 = self.Op("pd_op.softmax", 958, input_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), axis=self.a_i32(-1), stop_gradient=self.a_array(self.a_bool(False))))

    self.matmul_959 = self.Op("pd_op.matmul", 959, input_types=[self.t_dtensor([-1, -1, -1], self.t_f16()), self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_6951 = self.Op("cinn_op.generate_shape", 6951, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(12), self.a_str("S1"), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.reshape_6952 = self.Op("pd_op.reshape", 6952, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16()), self.t_dtensor([0, -1, -1, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.transpose_6953 = self.Op("pd_op.transpose", 6953, input_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), perm=self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6954 = self.Op("cinn_op.generate_shape", 6954, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.reshape_6955 = self.Op("pd_op.reshape", 6955, input_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([0, -1, -1, 12, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_6957 = self.Op("cf.yield", 6957, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6956 = self.Op("cinn_op.fusion", 6956, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_968 = self.Op("pd_op.matmul", 968, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_6958 = self.Op("cinn_op.generate_shape", 6958, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6959 = self.Op("pd_op.expand", 6959, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6960 = self.Op("pd_op.add", 6960, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.add_6961 = self.Op("pd_op.add", 6961, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.yield_6963 = self.Op("cf.yield", 6963, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6962 = self.Op("cinn_op.fusion", 6962, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.cast_6964 = self.Op("pd_op.cast", 6964, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_6965 = self.Op("cinn_op.reduce_sum", 6965, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.yield_6967 = self.Op("cf.yield", 6967, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[], attrs=dict())

    self.fusion_6966 = self.Op("cinn_op.fusion", 6966, input_types=[], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.cast_6968 = self.Op("pd_op.cast", 6968, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.full_6969 = self.Op("pd_op.full", 6969, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_6970 = self.Op("cinn_op.generate_shape", 6970, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6971 = self.Op("pd_op.expand", 6971, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_6972 = self.Op("pd_op.divide", 6972, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6973 = self.Op("cinn_op.generate_shape", 6973, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6974 = self.Op("pd_op.expand", 6974, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.subtract_6975 = self.Op("pd_op.subtract", 6975, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_6976 = self.Op("pd_op.multiply", 6976, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_6977 = self.Op("cinn_op.reduce_sum", 6977, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.full_6978 = self.Op("pd_op.full", 6978, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_6979 = self.Op("cinn_op.generate_shape", 6979, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6980 = self.Op("pd_op.expand", 6980, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_6981 = self.Op("pd_op.divide", 6981, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.full_6982 = self.Op("pd_op.full", 6982, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("1e-05"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_6983 = self.Op("cinn_op.generate_shape", 6983, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6984 = self.Op("pd_op.expand", 6984, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6985 = self.Op("pd_op.add", 6985, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.rsqrt_6986 = self.Op("pd_op.rsqrt", 6986, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6987 = self.Op("cinn_op.generate_shape", 6987, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6988 = self.Op("pd_op.expand", 6988, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_6989 = self.Op("pd_op.multiply", 6989, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_6990 = self.Op("pd_op.cast", 6990, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6991 = self.Op("cinn_op.generate_shape", 6991, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6992 = self.Op("pd_op.expand", 6992, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_6993 = self.Op("pd_op.multiply", 6993, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_6994 = self.Op("pd_op.cast", 6994, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_6995 = self.Op("cinn_op.generate_shape", 6995, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_6996 = self.Op("pd_op.expand", 6996, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_6997 = self.Op("pd_op.add", 6997, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_6998 = self.Op("pd_op.cast", 6998, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(dtype=self.a_dtype("float16"), stop_gradient=self.a_array(self.a_bool(False))))

    self.yield_7000 = self.Op("cf.yield", 7000, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_6999 = self.Op("cinn_op.fusion", 6999, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_972 = self.Op("pd_op.matmul", 972, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 3072], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_7001 = self.Op("cinn_op.generate_shape", 7001, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(3072)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7002 = self.Op("pd_op.expand", 7002, input_types=[self.t_dtensor([3072], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_7003 = self.Op("pd_op.add", 7003, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.scale_7004 = self.Op("cinn_op.scale", 7004, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(bias=self.a_f32("0"), stop_gradient=self.a_array(self.a_bool(False)), bias_after_scale=self.a_bool(True), scale=self.a_f32("1.702")))

    self.cast_7005 = self.Op("pd_op.cast", 7005, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.full_7006 = self.Op("pd_op.full", 7006, input_types=[], output_types=[self.t_dtensor([1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("1"), shape=self.a_intarray(1), place=self.a_place("cpu"), dtype=self.a_dtype("float32")))

    self.scale_7007 = self.Op("cinn_op.scale", 7007, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(bias=self.a_f32("0"), stop_gradient=self.a_array(self.a_bool(False)), bias_after_scale=self.a_bool(True), scale=self.a_f32("-1")))

    self.exp_7008 = self.Op("pd_op.exp", 7008, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_7009 = self.Op("cinn_op.generate_shape", 7009, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(3072)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7010 = self.Op("pd_op.expand", 7010, input_types=[self.t_dtensor([1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_7011 = self.Op("pd_op.add", 7011, input_types=[self.t_dtensor([-1, -1, -1], self.t_f32()), self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_7012 = self.Op("cinn_op.generate_shape", 7012, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(3072)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7013 = self.Op("pd_op.expand", 7013, input_types=[self.t_dtensor([1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_7014 = self.Op("pd_op.divide", 7014, input_types=[self.t_dtensor([-1, -1, -1], self.t_f32()), self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_7015 = self.Op("pd_op.cast", 7015, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(dtype=self.a_dtype("float16"), stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_7016 = self.Op("pd_op.multiply", 7016, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16()), self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.yield_7018 = self.Op("cf.yield", 7018, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_7017 = self.Op("cinn_op.fusion", 7017, input_types=[], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_978 = self.Op("pd_op.matmul", 978, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16()), self.t_dtensor([3072, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_7019 = self.Op("cinn_op.generate_shape", 7019, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7020 = self.Op("pd_op.expand", 7020, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_7021 = self.Op("pd_op.add", 7021, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.add_7022 = self.Op("pd_op.add", 7022, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.yield_7024 = self.Op("cf.yield", 7024, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_7023 = self.Op("cinn_op.fusion", 7023, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.cast_7025 = self.Op("pd_op.cast", 7025, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_7026 = self.Op("cinn_op.reduce_sum", 7026, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.yield_7028 = self.Op("cf.yield", 7028, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[], attrs=dict())

    self.fusion_7027 = self.Op("cinn_op.fusion", 7027, input_types=[], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.cast_7029 = self.Op("pd_op.cast", 7029, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.full_7030 = self.Op("pd_op.full", 7030, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_7031 = self.Op("cinn_op.generate_shape", 7031, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7032 = self.Op("pd_op.expand", 7032, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_7033 = self.Op("pd_op.divide", 7033, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_7034 = self.Op("cinn_op.generate_shape", 7034, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7035 = self.Op("pd_op.expand", 7035, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.subtract_7036 = self.Op("pd_op.subtract", 7036, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_7037 = self.Op("pd_op.multiply", 7037, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_7038 = self.Op("cinn_op.reduce_sum", 7038, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.full_7039 = self.Op("pd_op.full", 7039, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_7040 = self.Op("cinn_op.generate_shape", 7040, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7041 = self.Op("pd_op.expand", 7041, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_7042 = self.Op("pd_op.divide", 7042, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.full_7043 = self.Op("pd_op.full", 7043, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("1e-05"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_7044 = self.Op("cinn_op.generate_shape", 7044, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7045 = self.Op("pd_op.expand", 7045, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_7046 = self.Op("pd_op.add", 7046, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.rsqrt_7047 = self.Op("pd_op.rsqrt", 7047, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_7048 = self.Op("cinn_op.generate_shape", 7048, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7049 = self.Op("pd_op.expand", 7049, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_7050 = self.Op("pd_op.multiply", 7050, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_7051 = self.Op("pd_op.cast", 7051, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_7052 = self.Op("cinn_op.generate_shape", 7052, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7053 = self.Op("pd_op.expand", 7053, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_7054 = self.Op("pd_op.multiply", 7054, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_7055 = self.Op("pd_op.cast", 7055, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_7056 = self.Op("cinn_op.generate_shape", 7056, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7057 = self.Op("pd_op.expand", 7057, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_7058 = self.Op("pd_op.add", 7058, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_7059 = self.Op("pd_op.cast", 7059, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(dtype=self.a_dtype("float16"), stop_gradient=self.a_array(self.a_bool(False))))

    self.yield_7061 = self.Op("cf.yield", 7061, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_7060 = self.Op("cinn_op.fusion", 7060, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_989 = self.Op("pd_op.matmul", 989, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.matmul_993 = self.Op("pd_op.matmul", 993, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.matmul_1001 = self.Op("pd_op.matmul", 1001, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_7062 = self.Op("cinn_op.generate_shape", 7062, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7063 = self.Op("pd_op.expand", 7063, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_7064 = self.Op("pd_op.add", 7064, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.scale_7065 = self.Op("cinn_op.scale", 7065, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(bias=self.a_f32("0"), stop_gradient=self.a_array(self.a_bool(False)), bias_after_scale=self.a_bool(True), scale=self.a_f32("0.125")))

    self.generate_shape_7066 = self.Op("cinn_op.generate_shape", 7066, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(12), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.reshape_7067 = self.Op("pd_op.reshape", 7067, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16()), self.t_dtensor([0, -1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.transpose_7068 = self.Op("pd_op.transpose", 7068, input_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16())], output_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), perm=self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_7069 = self.Op("cinn_op.generate_shape", 7069, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_array(self.a_str("Mul"), self.a_str("S0"), self.a_i64(12)), self.a_i64(-1), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_7070 = self.Op("pd_op.reshape", 7070, input_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([0, -1, 12, -1, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_7072 = self.Op("cf.yield", 7072, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_7071 = self.Op("cinn_op.fusion", 7071, input_types=[], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.generate_shape_7073 = self.Op("cinn_op.generate_shape", 7073, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7074 = self.Op("pd_op.expand", 7074, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_7075 = self.Op("pd_op.add", 7075, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.generate_shape_7076 = self.Op("cinn_op.generate_shape", 7076, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(-1), self.a_i64(12), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_7077 = self.Op("pd_op.reshape", 7077, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16()), self.t_dtensor([0, -1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.transpose_7078 = self.Op("pd_op.transpose", 7078, input_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16())], output_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), perm=self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_7079 = self.Op("cinn_op.generate_shape", 7079, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_array(self.a_str("Mul"), self.a_str("S0"), self.a_i64(12)), self.a_i64(-1), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_7080 = self.Op("pd_op.reshape", 7080, input_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([0, -1, 12, -1, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_7082 = self.Op("cf.yield", 7082, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_7081 = self.Op("cinn_op.fusion", 7081, input_types=[], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.generate_shape_7083 = self.Op("cinn_op.generate_shape", 7083, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7084 = self.Op("pd_op.expand", 7084, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_7085 = self.Op("pd_op.add", 7085, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.generate_shape_7086 = self.Op("cinn_op.generate_shape", 7086, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(-1), self.a_i64(12), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_7087 = self.Op("pd_op.reshape", 7087, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16()), self.t_dtensor([0, -1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.transpose_7088 = self.Op("pd_op.transpose", 7088, input_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16())], output_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), perm=self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_7089 = self.Op("cinn_op.generate_shape", 7089, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_array(self.a_str("Mul"), self.a_str("S0"), self.a_i64(12)), self.a_i64(-1), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_7090 = self.Op("pd_op.reshape", 7090, input_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([0, -1, 12, -1, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_7092 = self.Op("cf.yield", 7092, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_7091 = self.Op("cinn_op.fusion", 7091, input_types=[], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_1032 = self.Op("pd_op.matmul", 1032, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(True)))

    self.generate_shape_7093 = self.Op("cinn_op.generate_shape", 7093, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("SS0"), self.a_i64(12), self.a_str("SS1"), self.a_str("SS1")), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS1"), self.a_i64(0), self.a_i64(1)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS1"), self.a_i64(1), self.a_i64(1)))))

    self.reshape_7094 = self.Op("pd_op.reshape", 7094, input_types=[self.t_dtensor([-1, -1, -1], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, 12, -1, -1], self.t_f16()), self.t_dtensor([0, -1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.generate_shape_7095 = self.Op("cinn_op.generate_shape", 7095, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(12), self.a_str("S1"), self.a_str("S1")), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7096 = self.Op("pd_op.expand", 7096, input_types=[self.t_dtensor([-1, -1, -1, -1], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_7097 = self.Op("pd_op.add", 7097, input_types=[self.t_dtensor([-1, 12, -1, -1], self.t_f16()), self.t_dtensor([-1, -1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, 12, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.generate_shape_7098 = self.Op("cinn_op.generate_shape", 7098, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_array(self.a_str("Mul"), self.a_str("SS0"), self.a_i64(12)), self.a_str("SS1"), self.a_str("SS1")), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS1"), self.a_i64(0), self.a_i64(1)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS1"), self.a_i64(1), self.a_i64(1)))))

    self.reshape_7099 = self.Op("pd_op.reshape", 7099, input_types=[self.t_dtensor([-1, 12, -1, -1], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16()), self.t_dtensor([0, -1, 12, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_7101 = self.Op("cf.yield", 7101, input_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_7100 = self.Op("cinn_op.fusion", 7100, input_types=[], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.softmax_1041 = self.Op("pd_op.softmax", 1041, input_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), axis=self.a_i32(-1), stop_gradient=self.a_array(self.a_bool(False))))

    self.matmul_1042 = self.Op("pd_op.matmul", 1042, input_types=[self.t_dtensor([-1, -1, -1], self.t_f16()), self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_7102 = self.Op("cinn_op.generate_shape", 7102, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(12), self.a_str("S1"), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.reshape_7103 = self.Op("pd_op.reshape", 7103, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16()), self.t_dtensor([0, -1, -1, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.transpose_7104 = self.Op("pd_op.transpose", 7104, input_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), perm=self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_7105 = self.Op("cinn_op.generate_shape", 7105, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.reshape_7106 = self.Op("pd_op.reshape", 7106, input_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([0, -1, -1, 12, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_7108 = self.Op("cf.yield", 7108, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_7107 = self.Op("cinn_op.fusion", 7107, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_1051 = self.Op("pd_op.matmul", 1051, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_7109 = self.Op("cinn_op.generate_shape", 7109, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7110 = self.Op("pd_op.expand", 7110, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_7111 = self.Op("pd_op.add", 7111, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.add_7112 = self.Op("pd_op.add", 7112, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.yield_7114 = self.Op("cf.yield", 7114, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_7113 = self.Op("cinn_op.fusion", 7113, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.cast_7115 = self.Op("pd_op.cast", 7115, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_7116 = self.Op("cinn_op.reduce_sum", 7116, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.yield_7118 = self.Op("cf.yield", 7118, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[], attrs=dict())

    self.fusion_7117 = self.Op("cinn_op.fusion", 7117, input_types=[], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.cast_7119 = self.Op("pd_op.cast", 7119, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.full_7120 = self.Op("pd_op.full", 7120, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_7121 = self.Op("cinn_op.generate_shape", 7121, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7122 = self.Op("pd_op.expand", 7122, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_7123 = self.Op("pd_op.divide", 7123, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_7124 = self.Op("cinn_op.generate_shape", 7124, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7125 = self.Op("pd_op.expand", 7125, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.subtract_7126 = self.Op("pd_op.subtract", 7126, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_7127 = self.Op("pd_op.multiply", 7127, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_7128 = self.Op("cinn_op.reduce_sum", 7128, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.full_7129 = self.Op("pd_op.full", 7129, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_7130 = self.Op("cinn_op.generate_shape", 7130, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7131 = self.Op("pd_op.expand", 7131, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_7132 = self.Op("pd_op.divide", 7132, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.full_7133 = self.Op("pd_op.full", 7133, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("1e-05"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_7134 = self.Op("cinn_op.generate_shape", 7134, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7135 = self.Op("pd_op.expand", 7135, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_7136 = self.Op("pd_op.add", 7136, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.rsqrt_7137 = self.Op("pd_op.rsqrt", 7137, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_7138 = self.Op("cinn_op.generate_shape", 7138, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7139 = self.Op("pd_op.expand", 7139, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_7140 = self.Op("pd_op.multiply", 7140, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_7141 = self.Op("pd_op.cast", 7141, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_7142 = self.Op("cinn_op.generate_shape", 7142, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7143 = self.Op("pd_op.expand", 7143, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_7144 = self.Op("pd_op.multiply", 7144, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_7145 = self.Op("pd_op.cast", 7145, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_7146 = self.Op("cinn_op.generate_shape", 7146, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7147 = self.Op("pd_op.expand", 7147, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_7148 = self.Op("pd_op.add", 7148, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_7149 = self.Op("pd_op.cast", 7149, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(dtype=self.a_dtype("float16"), stop_gradient=self.a_array(self.a_bool(False))))

    self.yield_7151 = self.Op("cf.yield", 7151, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_7150 = self.Op("cinn_op.fusion", 7150, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_1055 = self.Op("pd_op.matmul", 1055, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 3072], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_7152 = self.Op("cinn_op.generate_shape", 7152, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(3072)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7153 = self.Op("pd_op.expand", 7153, input_types=[self.t_dtensor([3072], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_7154 = self.Op("pd_op.add", 7154, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.scale_7155 = self.Op("cinn_op.scale", 7155, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(bias=self.a_f32("0"), stop_gradient=self.a_array(self.a_bool(False)), bias_after_scale=self.a_bool(True), scale=self.a_f32("1.702")))

    self.cast_7156 = self.Op("pd_op.cast", 7156, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.full_7157 = self.Op("pd_op.full", 7157, input_types=[], output_types=[self.t_dtensor([1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("1"), shape=self.a_intarray(1), place=self.a_place("cpu"), dtype=self.a_dtype("float32")))

    self.scale_7158 = self.Op("cinn_op.scale", 7158, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(bias=self.a_f32("0"), stop_gradient=self.a_array(self.a_bool(False)), bias_after_scale=self.a_bool(True), scale=self.a_f32("-1")))

    self.exp_7159 = self.Op("pd_op.exp", 7159, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_7160 = self.Op("cinn_op.generate_shape", 7160, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(3072)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7161 = self.Op("pd_op.expand", 7161, input_types=[self.t_dtensor([1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_7162 = self.Op("pd_op.add", 7162, input_types=[self.t_dtensor([-1, -1, -1], self.t_f32()), self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_7163 = self.Op("cinn_op.generate_shape", 7163, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(3072)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7164 = self.Op("pd_op.expand", 7164, input_types=[self.t_dtensor([1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_7165 = self.Op("pd_op.divide", 7165, input_types=[self.t_dtensor([-1, -1, -1], self.t_f32()), self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_7166 = self.Op("pd_op.cast", 7166, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(dtype=self.a_dtype("float16"), stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_7167 = self.Op("pd_op.multiply", 7167, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16()), self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.yield_7169 = self.Op("cf.yield", 7169, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_7168 = self.Op("cinn_op.fusion", 7168, input_types=[], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_1061 = self.Op("pd_op.matmul", 1061, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16()), self.t_dtensor([3072, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_7170 = self.Op("cinn_op.generate_shape", 7170, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7171 = self.Op("pd_op.expand", 7171, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_7172 = self.Op("pd_op.add", 7172, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.add_7173 = self.Op("pd_op.add", 7173, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.yield_7175 = self.Op("cf.yield", 7175, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_7174 = self.Op("cinn_op.fusion", 7174, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.cast_7176 = self.Op("pd_op.cast", 7176, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_7177 = self.Op("cinn_op.reduce_sum", 7177, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.yield_7179 = self.Op("cf.yield", 7179, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[], attrs=dict())

    self.fusion_7178 = self.Op("cinn_op.fusion", 7178, input_types=[], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.cast_7180 = self.Op("pd_op.cast", 7180, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.full_7181 = self.Op("pd_op.full", 7181, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_7182 = self.Op("cinn_op.generate_shape", 7182, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7183 = self.Op("pd_op.expand", 7183, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_7184 = self.Op("pd_op.divide", 7184, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_7185 = self.Op("cinn_op.generate_shape", 7185, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7186 = self.Op("pd_op.expand", 7186, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.subtract_7187 = self.Op("pd_op.subtract", 7187, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_7188 = self.Op("pd_op.multiply", 7188, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_7189 = self.Op("cinn_op.reduce_sum", 7189, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.full_7190 = self.Op("pd_op.full", 7190, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_7191 = self.Op("cinn_op.generate_shape", 7191, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7192 = self.Op("pd_op.expand", 7192, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_7193 = self.Op("pd_op.divide", 7193, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.full_7194 = self.Op("pd_op.full", 7194, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("1e-05"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_7195 = self.Op("cinn_op.generate_shape", 7195, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7196 = self.Op("pd_op.expand", 7196, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_7197 = self.Op("pd_op.add", 7197, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.rsqrt_7198 = self.Op("pd_op.rsqrt", 7198, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_7199 = self.Op("cinn_op.generate_shape", 7199, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7200 = self.Op("pd_op.expand", 7200, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_7201 = self.Op("pd_op.multiply", 7201, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_7202 = self.Op("pd_op.cast", 7202, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_7203 = self.Op("cinn_op.generate_shape", 7203, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7204 = self.Op("pd_op.expand", 7204, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_7205 = self.Op("pd_op.multiply", 7205, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_7206 = self.Op("pd_op.cast", 7206, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_7207 = self.Op("cinn_op.generate_shape", 7207, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7208 = self.Op("pd_op.expand", 7208, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_7209 = self.Op("pd_op.add", 7209, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_7210 = self.Op("pd_op.cast", 7210, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(dtype=self.a_dtype("float16"), stop_gradient=self.a_array(self.a_bool(False))))

    self.yield_7212 = self.Op("cf.yield", 7212, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_7211 = self.Op("cinn_op.fusion", 7211, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_1072 = self.Op("pd_op.matmul", 1072, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.matmul_1076 = self.Op("pd_op.matmul", 1076, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.matmul_1084 = self.Op("pd_op.matmul", 1084, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_7213 = self.Op("cinn_op.generate_shape", 7213, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7214 = self.Op("pd_op.expand", 7214, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_7215 = self.Op("pd_op.add", 7215, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.scale_7216 = self.Op("cinn_op.scale", 7216, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(bias=self.a_f32("0"), stop_gradient=self.a_array(self.a_bool(False)), bias_after_scale=self.a_bool(True), scale=self.a_f32("0.125")))

    self.generate_shape_7217 = self.Op("cinn_op.generate_shape", 7217, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(12), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.reshape_7218 = self.Op("pd_op.reshape", 7218, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16()), self.t_dtensor([0, -1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.transpose_7219 = self.Op("pd_op.transpose", 7219, input_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16())], output_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), perm=self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_7220 = self.Op("cinn_op.generate_shape", 7220, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_array(self.a_str("Mul"), self.a_str("S0"), self.a_i64(12)), self.a_i64(-1), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_7221 = self.Op("pd_op.reshape", 7221, input_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([0, -1, 12, -1, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_7223 = self.Op("cf.yield", 7223, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_7222 = self.Op("cinn_op.fusion", 7222, input_types=[], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.generate_shape_7224 = self.Op("cinn_op.generate_shape", 7224, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7225 = self.Op("pd_op.expand", 7225, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_7226 = self.Op("pd_op.add", 7226, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.generate_shape_7227 = self.Op("cinn_op.generate_shape", 7227, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(-1), self.a_i64(12), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_7228 = self.Op("pd_op.reshape", 7228, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16()), self.t_dtensor([0, -1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.transpose_7229 = self.Op("pd_op.transpose", 7229, input_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16())], output_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), perm=self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_7230 = self.Op("cinn_op.generate_shape", 7230, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_array(self.a_str("Mul"), self.a_str("S0"), self.a_i64(12)), self.a_i64(-1), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_7231 = self.Op("pd_op.reshape", 7231, input_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([0, -1, 12, -1, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_7233 = self.Op("cf.yield", 7233, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_7232 = self.Op("cinn_op.fusion", 7232, input_types=[], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.generate_shape_7234 = self.Op("cinn_op.generate_shape", 7234, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7235 = self.Op("pd_op.expand", 7235, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_7236 = self.Op("pd_op.add", 7236, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.generate_shape_7237 = self.Op("cinn_op.generate_shape", 7237, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(-1), self.a_i64(12), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_7238 = self.Op("pd_op.reshape", 7238, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16()), self.t_dtensor([0, -1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.transpose_7239 = self.Op("pd_op.transpose", 7239, input_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16())], output_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), perm=self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_7240 = self.Op("cinn_op.generate_shape", 7240, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_array(self.a_str("Mul"), self.a_str("S0"), self.a_i64(12)), self.a_i64(-1), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_7241 = self.Op("pd_op.reshape", 7241, input_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([0, -1, 12, -1, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_7243 = self.Op("cf.yield", 7243, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_7242 = self.Op("cinn_op.fusion", 7242, input_types=[], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_1115 = self.Op("pd_op.matmul", 1115, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(True)))

    self.generate_shape_7244 = self.Op("cinn_op.generate_shape", 7244, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("SS0"), self.a_i64(12), self.a_str("SS1"), self.a_str("SS1")), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS1"), self.a_i64(0), self.a_i64(1)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS1"), self.a_i64(1), self.a_i64(1)))))

    self.reshape_7245 = self.Op("pd_op.reshape", 7245, input_types=[self.t_dtensor([-1, -1, -1], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, 12, -1, -1], self.t_f16()), self.t_dtensor([0, -1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.generate_shape_7246 = self.Op("cinn_op.generate_shape", 7246, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(12), self.a_str("S1"), self.a_str("S1")), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7247 = self.Op("pd_op.expand", 7247, input_types=[self.t_dtensor([-1, -1, -1, -1], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_7248 = self.Op("pd_op.add", 7248, input_types=[self.t_dtensor([-1, 12, -1, -1], self.t_f16()), self.t_dtensor([-1, -1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, 12, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.generate_shape_7249 = self.Op("cinn_op.generate_shape", 7249, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_array(self.a_str("Mul"), self.a_str("SS0"), self.a_i64(12)), self.a_str("SS1"), self.a_str("SS1")), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS1"), self.a_i64(0), self.a_i64(1)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS1"), self.a_i64(1), self.a_i64(1)))))

    self.reshape_7250 = self.Op("pd_op.reshape", 7250, input_types=[self.t_dtensor([-1, 12, -1, -1], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16()), self.t_dtensor([0, -1, 12, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_7252 = self.Op("cf.yield", 7252, input_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_7251 = self.Op("cinn_op.fusion", 7251, input_types=[], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.softmax_1124 = self.Op("pd_op.softmax", 1124, input_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), axis=self.a_i32(-1), stop_gradient=self.a_array(self.a_bool(False))))

    self.matmul_1125 = self.Op("pd_op.matmul", 1125, input_types=[self.t_dtensor([-1, -1, -1], self.t_f16()), self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_7253 = self.Op("cinn_op.generate_shape", 7253, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(12), self.a_str("S1"), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.reshape_7254 = self.Op("pd_op.reshape", 7254, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16()), self.t_dtensor([0, -1, -1, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.transpose_7255 = self.Op("pd_op.transpose", 7255, input_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), perm=self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_7256 = self.Op("cinn_op.generate_shape", 7256, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.reshape_7257 = self.Op("pd_op.reshape", 7257, input_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([0, -1, -1, 12, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_7259 = self.Op("cf.yield", 7259, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_7258 = self.Op("cinn_op.fusion", 7258, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_1134 = self.Op("pd_op.matmul", 1134, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_7260 = self.Op("cinn_op.generate_shape", 7260, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7261 = self.Op("pd_op.expand", 7261, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_7262 = self.Op("pd_op.add", 7262, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.add_7263 = self.Op("pd_op.add", 7263, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.yield_7265 = self.Op("cf.yield", 7265, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_7264 = self.Op("cinn_op.fusion", 7264, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.cast_7266 = self.Op("pd_op.cast", 7266, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_7267 = self.Op("cinn_op.reduce_sum", 7267, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.yield_7269 = self.Op("cf.yield", 7269, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[], attrs=dict())

    self.fusion_7268 = self.Op("cinn_op.fusion", 7268, input_types=[], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.cast_7270 = self.Op("pd_op.cast", 7270, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.full_7271 = self.Op("pd_op.full", 7271, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_7272 = self.Op("cinn_op.generate_shape", 7272, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7273 = self.Op("pd_op.expand", 7273, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_7274 = self.Op("pd_op.divide", 7274, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_7275 = self.Op("cinn_op.generate_shape", 7275, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7276 = self.Op("pd_op.expand", 7276, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.subtract_7277 = self.Op("pd_op.subtract", 7277, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_7278 = self.Op("pd_op.multiply", 7278, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_7279 = self.Op("cinn_op.reduce_sum", 7279, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.full_7280 = self.Op("pd_op.full", 7280, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_7281 = self.Op("cinn_op.generate_shape", 7281, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7282 = self.Op("pd_op.expand", 7282, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_7283 = self.Op("pd_op.divide", 7283, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.full_7284 = self.Op("pd_op.full", 7284, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("1e-05"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_7285 = self.Op("cinn_op.generate_shape", 7285, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7286 = self.Op("pd_op.expand", 7286, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_7287 = self.Op("pd_op.add", 7287, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.rsqrt_7288 = self.Op("pd_op.rsqrt", 7288, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_7289 = self.Op("cinn_op.generate_shape", 7289, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7290 = self.Op("pd_op.expand", 7290, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_7291 = self.Op("pd_op.multiply", 7291, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_7292 = self.Op("pd_op.cast", 7292, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_7293 = self.Op("cinn_op.generate_shape", 7293, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7294 = self.Op("pd_op.expand", 7294, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_7295 = self.Op("pd_op.multiply", 7295, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_7296 = self.Op("pd_op.cast", 7296, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_7297 = self.Op("cinn_op.generate_shape", 7297, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7298 = self.Op("pd_op.expand", 7298, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_7299 = self.Op("pd_op.add", 7299, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_7300 = self.Op("pd_op.cast", 7300, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(dtype=self.a_dtype("float16"), stop_gradient=self.a_array(self.a_bool(False))))

    self.yield_7302 = self.Op("cf.yield", 7302, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_7301 = self.Op("cinn_op.fusion", 7301, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_1138 = self.Op("pd_op.matmul", 1138, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 3072], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_7303 = self.Op("cinn_op.generate_shape", 7303, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(3072)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7304 = self.Op("pd_op.expand", 7304, input_types=[self.t_dtensor([3072], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_7305 = self.Op("pd_op.add", 7305, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.scale_7306 = self.Op("cinn_op.scale", 7306, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(bias=self.a_f32("0"), stop_gradient=self.a_array(self.a_bool(False)), bias_after_scale=self.a_bool(True), scale=self.a_f32("1.702")))

    self.cast_7307 = self.Op("pd_op.cast", 7307, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.full_7308 = self.Op("pd_op.full", 7308, input_types=[], output_types=[self.t_dtensor([1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("1"), shape=self.a_intarray(1), place=self.a_place("cpu"), dtype=self.a_dtype("float32")))

    self.scale_7309 = self.Op("cinn_op.scale", 7309, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(bias=self.a_f32("0"), stop_gradient=self.a_array(self.a_bool(False)), bias_after_scale=self.a_bool(True), scale=self.a_f32("-1")))

    self.exp_7310 = self.Op("pd_op.exp", 7310, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_7311 = self.Op("cinn_op.generate_shape", 7311, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(3072)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7312 = self.Op("pd_op.expand", 7312, input_types=[self.t_dtensor([1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_7313 = self.Op("pd_op.add", 7313, input_types=[self.t_dtensor([-1, -1, -1], self.t_f32()), self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_7314 = self.Op("cinn_op.generate_shape", 7314, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(3072)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7315 = self.Op("pd_op.expand", 7315, input_types=[self.t_dtensor([1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_7316 = self.Op("pd_op.divide", 7316, input_types=[self.t_dtensor([-1, -1, -1], self.t_f32()), self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_7317 = self.Op("pd_op.cast", 7317, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(dtype=self.a_dtype("float16"), stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_7318 = self.Op("pd_op.multiply", 7318, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16()), self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.yield_7320 = self.Op("cf.yield", 7320, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_7319 = self.Op("cinn_op.fusion", 7319, input_types=[], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_1144 = self.Op("pd_op.matmul", 1144, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16()), self.t_dtensor([3072, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_7321 = self.Op("cinn_op.generate_shape", 7321, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7322 = self.Op("pd_op.expand", 7322, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_7323 = self.Op("pd_op.add", 7323, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.add_7324 = self.Op("pd_op.add", 7324, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.yield_7326 = self.Op("cf.yield", 7326, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_7325 = self.Op("cinn_op.fusion", 7325, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.cast_7327 = self.Op("pd_op.cast", 7327, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_7328 = self.Op("cinn_op.reduce_sum", 7328, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.yield_7330 = self.Op("cf.yield", 7330, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[], attrs=dict())

    self.fusion_7329 = self.Op("cinn_op.fusion", 7329, input_types=[], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.cast_7331 = self.Op("pd_op.cast", 7331, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.full_7332 = self.Op("pd_op.full", 7332, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_7333 = self.Op("cinn_op.generate_shape", 7333, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7334 = self.Op("pd_op.expand", 7334, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_7335 = self.Op("pd_op.divide", 7335, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_7336 = self.Op("cinn_op.generate_shape", 7336, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7337 = self.Op("pd_op.expand", 7337, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.subtract_7338 = self.Op("pd_op.subtract", 7338, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_7339 = self.Op("pd_op.multiply", 7339, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_7340 = self.Op("cinn_op.reduce_sum", 7340, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.full_7341 = self.Op("pd_op.full", 7341, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_7342 = self.Op("cinn_op.generate_shape", 7342, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7343 = self.Op("pd_op.expand", 7343, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_7344 = self.Op("pd_op.divide", 7344, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.full_7345 = self.Op("pd_op.full", 7345, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("1e-05"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_7346 = self.Op("cinn_op.generate_shape", 7346, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7347 = self.Op("pd_op.expand", 7347, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_7348 = self.Op("pd_op.add", 7348, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.rsqrt_7349 = self.Op("pd_op.rsqrt", 7349, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_7350 = self.Op("cinn_op.generate_shape", 7350, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7351 = self.Op("pd_op.expand", 7351, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_7352 = self.Op("pd_op.multiply", 7352, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_7353 = self.Op("pd_op.cast", 7353, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_7354 = self.Op("cinn_op.generate_shape", 7354, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7355 = self.Op("pd_op.expand", 7355, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_7356 = self.Op("pd_op.multiply", 7356, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_7357 = self.Op("pd_op.cast", 7357, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_7358 = self.Op("cinn_op.generate_shape", 7358, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7359 = self.Op("pd_op.expand", 7359, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_7360 = self.Op("pd_op.add", 7360, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_7361 = self.Op("pd_op.cast", 7361, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(dtype=self.a_dtype("float16"), stop_gradient=self.a_array(self.a_bool(False))))

    self.yield_7363 = self.Op("cf.yield", 7363, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_7362 = self.Op("cinn_op.fusion", 7362, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_1155 = self.Op("pd_op.matmul", 1155, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.matmul_1159 = self.Op("pd_op.matmul", 1159, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.matmul_1167 = self.Op("pd_op.matmul", 1167, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_7364 = self.Op("cinn_op.generate_shape", 7364, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7365 = self.Op("pd_op.expand", 7365, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_7366 = self.Op("pd_op.add", 7366, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.scale_7367 = self.Op("cinn_op.scale", 7367, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(bias=self.a_f32("0"), stop_gradient=self.a_array(self.a_bool(False)), bias_after_scale=self.a_bool(True), scale=self.a_f32("0.125")))

    self.generate_shape_7368 = self.Op("cinn_op.generate_shape", 7368, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(12), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.reshape_7369 = self.Op("pd_op.reshape", 7369, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16()), self.t_dtensor([0, -1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.transpose_7370 = self.Op("pd_op.transpose", 7370, input_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16())], output_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), perm=self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_7371 = self.Op("cinn_op.generate_shape", 7371, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_array(self.a_str("Mul"), self.a_str("S0"), self.a_i64(12)), self.a_i64(-1), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_7372 = self.Op("pd_op.reshape", 7372, input_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([0, -1, 12, -1, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_7374 = self.Op("cf.yield", 7374, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_7373 = self.Op("cinn_op.fusion", 7373, input_types=[], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.generate_shape_7375 = self.Op("cinn_op.generate_shape", 7375, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7376 = self.Op("pd_op.expand", 7376, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_7377 = self.Op("pd_op.add", 7377, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.generate_shape_7378 = self.Op("cinn_op.generate_shape", 7378, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(-1), self.a_i64(12), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_7379 = self.Op("pd_op.reshape", 7379, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16()), self.t_dtensor([0, -1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.transpose_7380 = self.Op("pd_op.transpose", 7380, input_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16())], output_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), perm=self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_7381 = self.Op("cinn_op.generate_shape", 7381, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_array(self.a_str("Mul"), self.a_str("S0"), self.a_i64(12)), self.a_i64(-1), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_7382 = self.Op("pd_op.reshape", 7382, input_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([0, -1, 12, -1, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_7384 = self.Op("cf.yield", 7384, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_7383 = self.Op("cinn_op.fusion", 7383, input_types=[], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.generate_shape_7385 = self.Op("cinn_op.generate_shape", 7385, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7386 = self.Op("pd_op.expand", 7386, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_7387 = self.Op("pd_op.add", 7387, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.generate_shape_7388 = self.Op("cinn_op.generate_shape", 7388, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(-1), self.a_i64(12), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_7389 = self.Op("pd_op.reshape", 7389, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16()), self.t_dtensor([0, -1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.transpose_7390 = self.Op("pd_op.transpose", 7390, input_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16())], output_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), perm=self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_7391 = self.Op("cinn_op.generate_shape", 7391, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_array(self.a_str("Mul"), self.a_str("S0"), self.a_i64(12)), self.a_i64(-1), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)))))

    self.reshape_7392 = self.Op("pd_op.reshape", 7392, input_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([0, -1, 12, -1, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_7394 = self.Op("cf.yield", 7394, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_7393 = self.Op("cinn_op.fusion", 7393, input_types=[], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_1198 = self.Op("pd_op.matmul", 1198, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(True)))

    self.generate_shape_7395 = self.Op("cinn_op.generate_shape", 7395, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("SS0"), self.a_i64(12), self.a_str("SS1"), self.a_str("SS1")), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS1"), self.a_i64(0), self.a_i64(1)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS1"), self.a_i64(1), self.a_i64(1)))))

    self.reshape_7396 = self.Op("pd_op.reshape", 7396, input_types=[self.t_dtensor([-1, -1, -1], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, 12, -1, -1], self.t_f16()), self.t_dtensor([0, -1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.generate_shape_7397 = self.Op("cinn_op.generate_shape", 7397, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(12), self.a_str("S1"), self.a_str("S1")), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7398 = self.Op("pd_op.expand", 7398, input_types=[self.t_dtensor([-1, -1, -1, -1], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_7399 = self.Op("pd_op.add", 7399, input_types=[self.t_dtensor([-1, 12, -1, -1], self.t_f16()), self.t_dtensor([-1, -1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, 12, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.generate_shape_7400 = self.Op("cinn_op.generate_shape", 7400, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_array(self.a_str("Mul"), self.a_str("SS0"), self.a_i64(12)), self.a_str("SS1"), self.a_str("SS1")), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS1"), self.a_i64(0), self.a_i64(1)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("SS1"), self.a_i64(1), self.a_i64(1)))))

    self.reshape_7401 = self.Op("pd_op.reshape", 7401, input_types=[self.t_dtensor([-1, 12, -1, -1], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16()), self.t_dtensor([0, -1, 12, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_7403 = self.Op("cf.yield", 7403, input_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_7402 = self.Op("cinn_op.fusion", 7402, input_types=[], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.softmax_1207 = self.Op("pd_op.softmax", 1207, input_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), axis=self.a_i32(-1), stop_gradient=self.a_array(self.a_bool(False))))

    self.matmul_1208 = self.Op("pd_op.matmul", 1208, input_types=[self.t_dtensor([-1, -1, -1], self.t_f16()), self.t_dtensor([-1, -1, 64], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_7404 = self.Op("cinn_op.generate_shape", 7404, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([4], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(12), self.a_str("S1"), self.a_i64(64)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.reshape_7405 = self.Op("pd_op.reshape", 7405, input_types=[self.t_dtensor([-1, -1, 64], self.t_f16()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16()), self.t_dtensor([0, -1, -1, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.transpose_7406 = self.Op("pd_op.transpose", 7406, input_types=[self.t_dtensor([-1, 12, -1, 64], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), perm=self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_7407 = self.Op("cinn_op.generate_shape", 7407, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.reshape_7408 = self.Op("pd_op.reshape", 7408, input_types=[self.t_dtensor([-1, -1, 12, 64], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([0, -1, -1, 12, 64], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False)), persistable=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.yield_7410 = self.Op("cf.yield", 7410, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_7409 = self.Op("cinn_op.fusion", 7409, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_1217 = self.Op("pd_op.matmul", 1217, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_7411 = self.Op("cinn_op.generate_shape", 7411, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7412 = self.Op("pd_op.expand", 7412, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_7413 = self.Op("pd_op.add", 7413, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.add_7414 = self.Op("pd_op.add", 7414, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.yield_7416 = self.Op("cf.yield", 7416, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_7415 = self.Op("cinn_op.fusion", 7415, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.cast_7417 = self.Op("pd_op.cast", 7417, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_7418 = self.Op("cinn_op.reduce_sum", 7418, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.yield_7420 = self.Op("cf.yield", 7420, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[], attrs=dict())

    self.fusion_7419 = self.Op("cinn_op.fusion", 7419, input_types=[], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.cast_7421 = self.Op("pd_op.cast", 7421, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.full_7422 = self.Op("pd_op.full", 7422, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_7423 = self.Op("cinn_op.generate_shape", 7423, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7424 = self.Op("pd_op.expand", 7424, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_7425 = self.Op("pd_op.divide", 7425, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_7426 = self.Op("cinn_op.generate_shape", 7426, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7427 = self.Op("pd_op.expand", 7427, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.subtract_7428 = self.Op("pd_op.subtract", 7428, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_7429 = self.Op("pd_op.multiply", 7429, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_7430 = self.Op("cinn_op.reduce_sum", 7430, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.full_7431 = self.Op("pd_op.full", 7431, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_7432 = self.Op("cinn_op.generate_shape", 7432, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7433 = self.Op("pd_op.expand", 7433, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_7434 = self.Op("pd_op.divide", 7434, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.full_7435 = self.Op("pd_op.full", 7435, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("1e-05"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_7436 = self.Op("cinn_op.generate_shape", 7436, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7437 = self.Op("pd_op.expand", 7437, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_7438 = self.Op("pd_op.add", 7438, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.rsqrt_7439 = self.Op("pd_op.rsqrt", 7439, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_7440 = self.Op("cinn_op.generate_shape", 7440, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7441 = self.Op("pd_op.expand", 7441, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_7442 = self.Op("pd_op.multiply", 7442, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_7443 = self.Op("pd_op.cast", 7443, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_7444 = self.Op("cinn_op.generate_shape", 7444, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7445 = self.Op("pd_op.expand", 7445, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_7446 = self.Op("pd_op.multiply", 7446, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_7447 = self.Op("pd_op.cast", 7447, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_7448 = self.Op("cinn_op.generate_shape", 7448, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7449 = self.Op("pd_op.expand", 7449, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_7450 = self.Op("pd_op.add", 7450, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_7451 = self.Op("pd_op.cast", 7451, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(dtype=self.a_dtype("float16"), stop_gradient=self.a_array(self.a_bool(False))))

    self.yield_7453 = self.Op("cf.yield", 7453, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_7452 = self.Op("cinn_op.fusion", 7452, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_1221 = self.Op("pd_op.matmul", 1221, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([768, 3072], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_7454 = self.Op("cinn_op.generate_shape", 7454, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(3072)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7455 = self.Op("pd_op.expand", 7455, input_types=[self.t_dtensor([3072], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_7456 = self.Op("pd_op.add", 7456, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.scale_7457 = self.Op("cinn_op.scale", 7457, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(bias=self.a_f32("0"), stop_gradient=self.a_array(self.a_bool(False)), bias_after_scale=self.a_bool(True), scale=self.a_f32("1.702")))

    self.cast_7458 = self.Op("pd_op.cast", 7458, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.full_7459 = self.Op("pd_op.full", 7459, input_types=[], output_types=[self.t_dtensor([1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("1"), shape=self.a_intarray(1), place=self.a_place("cpu"), dtype=self.a_dtype("float32")))

    self.scale_7460 = self.Op("cinn_op.scale", 7460, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(bias=self.a_f32("0"), stop_gradient=self.a_array(self.a_bool(False)), bias_after_scale=self.a_bool(True), scale=self.a_f32("-1")))

    self.exp_7461 = self.Op("pd_op.exp", 7461, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_7462 = self.Op("cinn_op.generate_shape", 7462, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(3072)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7463 = self.Op("pd_op.expand", 7463, input_types=[self.t_dtensor([1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_7464 = self.Op("pd_op.add", 7464, input_types=[self.t_dtensor([-1, -1, -1], self.t_f32()), self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_7465 = self.Op("cinn_op.generate_shape", 7465, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(3072)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7466 = self.Op("pd_op.expand", 7466, input_types=[self.t_dtensor([1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_7467 = self.Op("pd_op.divide", 7467, input_types=[self.t_dtensor([-1, -1, -1], self.t_f32()), self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_7468 = self.Op("pd_op.cast", 7468, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(dtype=self.a_dtype("float16"), stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_7469 = self.Op("pd_op.multiply", 7469, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16()), self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.yield_7471 = self.Op("cf.yield", 7471, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_7470 = self.Op("cinn_op.fusion", 7470, input_types=[], output_types=[self.t_dtensor([-1, -1, 3072], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.matmul_1227 = self.Op("pd_op.matmul", 1227, input_types=[self.t_dtensor([-1, -1, 3072], self.t_f16()), self.t_dtensor([3072, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), transpose_x=self.a_bool(False), transpose_y=self.a_bool(False)))

    self.generate_shape_7472 = self.Op("cinn_op.generate_shape", 7472, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7473 = self.Op("pd_op.expand", 7473, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_7474 = self.Op("pd_op.add", 7474, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.add_7475 = self.Op("pd_op.add", 7475, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.cast_7476 = self.Op("pd_op.cast", 7476, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_7477 = self.Op("cinn_op.reduce_sum", 7477, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.yield_7479 = self.Op("cf.yield", 7479, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[], attrs=dict())

    self.fusion_7478 = self.Op("cinn_op.fusion", 7478, input_types=[], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.generate_shape_7480 = self.Op("cinn_op.generate_shape", 7480, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7481 = self.Op("pd_op.expand", 7481, input_types=[self.t_dtensor([768], self.t_f16()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_7482 = self.Op("pd_op.add", 7482, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, -1], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.add_7483 = self.Op("pd_op.add", 7483, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.cast_7484 = self.Op("pd_op.cast", 7484, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.full_7485 = self.Op("pd_op.full", 7485, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_7486 = self.Op("cinn_op.generate_shape", 7486, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7487 = self.Op("pd_op.expand", 7487, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_7488 = self.Op("pd_op.divide", 7488, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_7489 = self.Op("cinn_op.generate_shape", 7489, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7490 = self.Op("pd_op.expand", 7490, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.subtract_7491 = self.Op("pd_op.subtract", 7491, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_7492 = self.Op("pd_op.multiply", 7492, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.reduce_sum_7493 = self.Op("cinn_op.reduce_sum", 7493, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(keep_dim=self.a_bool(True), stop_gradient=self.a_array(self.a_bool(False)), dim=self.a_array(self.a_i64(2))))

    self.full_7494 = self.Op("pd_op.full", 7494, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("768"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_7495 = self.Op("cinn_op.generate_shape", 7495, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7496 = self.Op("pd_op.expand", 7496, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.divide_7497 = self.Op("pd_op.divide", 7497, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.full_7498 = self.Op("pd_op.full", 7498, input_types=[], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("1e-05"), shape=self.a_intarray(), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.generate_shape_7499 = self.Op("cinn_op.generate_shape", 7499, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7500 = self.Op("pd_op.expand", 7500, input_types=[self.t_dtensor([], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_7501 = self.Op("pd_op.add", 7501, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.rsqrt_7502 = self.Op("pd_op.rsqrt", 7502, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_7503 = self.Op("cinn_op.generate_shape", 7503, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7504 = self.Op("pd_op.expand", 7504, input_types=[self.t_dtensor([-1, -1, 1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_7505 = self.Op("pd_op.multiply", 7505, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_7506 = self.Op("pd_op.cast", 7506, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_7507 = self.Op("cinn_op.generate_shape", 7507, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7508 = self.Op("pd_op.expand", 7508, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.multiply_7509 = self.Op("pd_op.multiply", 7509, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_7510 = self.Op("pd_op.cast", 7510, input_types=[self.t_dtensor([768], self.t_f32())], output_types=[self.t_dtensor([-1], self.t_f32())], attrs=dict(dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.generate_shape_7511 = self.Op("cinn_op.generate_shape", 7511, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_str("S1"), self.a_i64(768)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S1"), self.a_i64(0), self.a_i64(1)))))

    self.expand_7512 = self.Op("pd_op.expand", 7512, input_types=[self.t_dtensor([-1], self.t_f32()), self.t_dtensor([3], self.t_i64())], output_types=[self.t_dtensor([-1, -1, -1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.add_7513 = self.Op("pd_op.add", 7513, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32()), self.t_dtensor([-1, -1, -1], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False))))

    self.cast_7514 = self.Op("pd_op.cast", 7514, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(dtype=self.a_dtype("float16"), stop_gradient=self.a_array(self.a_bool(False))))

    self.yield_7516 = self.Op("cf.yield", 7516, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[], attrs=dict())

    self.fusion_7515 = self.Op("cinn_op.fusion", 7515, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.scale_7517 = self.Op("cinn_op.scale", 7517, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], attrs=dict(bias=self.a_f32("0"), stop_gradient=self.a_array(self.a_bool(False)), bias_after_scale=self.a_bool(True), scale=self.a_f32("1")))

    self.cast_7518 = self.Op("pd_op.cast", 7518, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(False)), dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.yield_7520 = self.Op("cf.yield", 7520, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[], attrs=dict())

    self.fusion_7519 = self.Op("cinn_op.fusion", 7519, input_types=[], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.shape_1231 = self.Op("pd_op.shape", 1231, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([3], self.t_i32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.slice_7521 = self.Op("cinn_op.slice", 7521, input_types=[self.t_dtensor([3], self.t_i32())], output_types=[self.t_dtensor([], self.t_i32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), decrease_axis=self.a_array(self.a_i64(0)), ends=self.a_array(self.a_i64(1)), infer_flags=self.a_array(self.a_i64(1)), axes=self.a_array(self.a_i64(0)), starts=self.a_array(self.a_i64(0))))

    self.yield_7523 = self.Op("cf.yield", 7523, input_types=[self.t_dtensor([], self.t_i32())], output_types=[], attrs=dict())

    self.fusion_7522 = self.Op("cinn_op.fusion", 7522, input_types=[], output_types=[self.t_dtensor([], self.t_i32())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.full_1235 = self.Op("pd_op.full", 1235, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), shape=self.a_intarray(1), value=self.a_f32("0"), dtype=self.a_dtype("int32"), place=self.a_place("cpu")))

    self.full_1236 = self.Op("pd_op.full", 1236, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), shape=self.a_intarray(1), value=self.a_f32("1"), dtype=self.a_dtype("int32"), place=self.a_place("cpu")))

    self.arange_1237 = self.Op("pd_op.arange", 1237, input_types=[self.t_dtensor([1], self.t_i32()), self.t_dtensor([], self.t_i32()), self.t_dtensor([1], self.t_i32())], output_types=[self.t_dtensor([-1], self.t_i32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), dtype=self.a_dtype("int32"), persistable=self.a_array(self.a_bool(False)), place=self.a_place("undefined", 0)))

    self.full_1238 = self.Op("pd_op.full", 1238, input_types=[], output_types=[self.t_dtensor([1], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("-1"), shape=self.a_intarray(1), place=self.a_place("cpu"), dtype=self.a_dtype("int64")))

    self.argmax_1239 = self.Op("pd_op.argmax", 1239, input_types=[self.t_dtensor([-1, -1], self.t_i64()), self.t_dtensor([1], self.t_i64())], output_types=[self.t_dtensor([-1], self.t_i32())], attrs=dict(persistable=self.a_array(self.a_bool(False)), stop_gradient=self.a_array(self.a_bool(False)), dtype=self.a_dtype("int32"), keepdims=self.a_bool(False), flatten=self.a_bool(False)))

    self.fetch_1248 = self.Op("pd_op.fetch", 1248, input_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, -1, 768], self.t_f32())], attrs=dict(name=self.a_str("save_infer_model/scale_0.tmp_0_cast_auto_mixed.tmp_2"), col=self.a_i32(0)))

    self.generate_shape_7524 = self.Op("cinn_op.generate_shape", 7524, input_types=[self.t_dtensor([-1], self.t_i32()), self.t_dtensor([-1, -1, 768], self.t_f16())], output_types=[self.t_dtensor([2], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), output_dim_exprs=self.a_array(self.a_str("S0"), self.a_i64(1)), symbol_bindings=self.a_array(self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(0), self.a_i64(0)), self.a_array(self.a_str("ShapeSymbolBinding"), self.a_str("S0"), self.a_i64(1), self.a_i64(0)))))

    self.reshape_7525 = self.Op("pd_op.reshape", 7525, input_types=[self.t_dtensor([-1], self.t_i32()), self.t_dtensor([2], self.t_i64())], output_types=[self.t_dtensor([-1, -1], self.t_i32()), self.t_dtensor([0, -1], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.reshape_7526 = self.Op("pd_op.reshape", 7526, input_types=[self.t_dtensor([-1], self.t_i32()), self.t_dtensor([2], self.t_i64())], output_types=[self.t_dtensor([-1, -1], self.t_i32()), self.t_dtensor([0, -1], self.t_i64())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False), self.a_bool(False))))

    self.concat_7527 = self.Op("cinn_op.concat", 7527, input_types=[self.t_dtensor([-1, -1], self.t_i32()), self.t_dtensor([-1, -1], self.t_i32())], output_types=[self.t_dtensor([-1, -1], self.t_i32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), axis=self.a_i32(1)))

    self.gather_nd_7528 = self.Op("pd_op.gather_nd", 7528, input_types=[self.t_dtensor([-1, -1, 768], self.t_f16()), self.t_dtensor([-1, -1], self.t_i32())], output_types=[self.t_dtensor([-1, 768], self.t_f16())], attrs=dict(stop_gradient=self.a_array(self.a_bool(False)), persistable=self.a_array(self.a_bool(False))))

    self.scale_7529 = self.Op("cinn_op.scale", 7529, input_types=[self.t_dtensor([-1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, 768], self.t_f16())], attrs=dict(bias=self.a_f32("0"), stop_gradient=self.a_array(self.a_bool(False)), bias_after_scale=self.a_bool(True), scale=self.a_f32("1")))

    self.cast_7530 = self.Op("pd_op.cast", 7530, input_types=[self.t_dtensor([-1, 768], self.t_f16())], output_types=[self.t_dtensor([-1, 768], self.t_f32())], attrs=dict(persistable=self.a_array(self.a_bool(False)), dtype=self.a_dtype("float32"), stop_gradient=self.a_array(self.a_bool(False))))

    self.yield_7532 = self.Op("cf.yield", 7532, input_types=[self.t_dtensor([-1, 768], self.t_f32())], output_types=[], attrs=dict())

    self.fusion_7531 = self.Op("cinn_op.fusion", 7531, input_types=[], output_types=[self.t_dtensor([-1, 768], self.t_f32())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.fetch_1250 = self.Op("pd_op.fetch", 1250, input_types=[self.t_dtensor([-1, 768], self.t_f32())], output_types=[self.t_dtensor([-1, 768], self.t_f32())], attrs=dict(name=self.a_str("save_infer_model/scale_1.tmp_0_cast_auto_mixed.tmp_3"), col=self.a_i32(1)))

    self.module_3 = self.Op("builtin.module", 3, input_types=[], output_types=[], attrs=dict(program=self.a_pointer("0x4a5d7a10")), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    

  def fusion_5647_block00(self, call, shape_2120):

    def ret_lambda():

      slice_56460, = call(self.slice_5646, shape_2120)

      return call(self.yield_5648, slice_56460)

    return ret_lambda

    

  def fusion_5650_block00(self, call, slice_2180):

    def ret_lambda():

      cast_56490, = call(self.cast_5649, slice_2180)

      return call(self.yield_5651, cast_56490)

    return ret_lambda

    

  def fusion_5659_block00(self, call, feed_2010):

    def ret_lambda():

      full_56520, = call(self.full_5652)

      cast_56530, = call(self.cast_5653, full_56520)

      generate_shape_56540, = call(self.generate_shape_5654, feed_2010)

      expand_56550, = call(self.expand_5655, cast_56530, generate_shape_56540)

      cast_56560, = call(self.cast_5656, expand_56550)

      scale_56570, = call(self.scale_5657, cast_56560)

      cast_56580, = call(self.cast_5658, scale_56570)

      return call(self.yield_5660, cast_56580)

    return ret_lambda

    

  def fusion_5664_block00(self, call, embedding_2190, embedding_2210):

    def ret_lambda():

      generate_shape_56610, = call(self.generate_shape_5661, embedding_2190)

      expand_56620, = call(self.expand_5662, embedding_2210, generate_shape_56610)

      add_56630, = call(self.add_5663, embedding_2190, expand_56620)

      return call(self.yield_5665, add_56630)

    return ret_lambda

    

  def fusion_5668_block00(self, call, fusion_56640):

    def ret_lambda():

      cast_56660, = call(self.cast_5666, fusion_56640)

      reduce_sum_56670, = call(self.reduce_sum_5667, cast_56660)

      return call(self.yield_5669, reduce_sum_56670)

    return ret_lambda

    

  def fusion_5701_block00(self, call, fusion_56640, embedding_2190, fusion_56680, parameter_80, parameter_70):

    def ret_lambda():

      cast_56700, = call(self.cast_5670, fusion_56640)

      full_56710, = call(self.full_5671)

      generate_shape_56720, = call(self.generate_shape_5672, embedding_2190)

      expand_56730, = call(self.expand_5673, full_56710, generate_shape_56720)

      divide_56740, = call(self.divide_5674, fusion_56680, expand_56730)

      generate_shape_56750, = call(self.generate_shape_5675, embedding_2190)

      expand_56760, = call(self.expand_5676, divide_56740, generate_shape_56750)

      subtract_56770, = call(self.subtract_5677, cast_56700, expand_56760)

      multiply_56780, = call(self.multiply_5678, subtract_56770, subtract_56770)

      reduce_sum_56790, = call(self.reduce_sum_5679, multiply_56780)

      full_56800, = call(self.full_5680)

      generate_shape_56810, = call(self.generate_shape_5681, embedding_2190)

      expand_56820, = call(self.expand_5682, full_56800, generate_shape_56810)

      divide_56830, = call(self.divide_5683, reduce_sum_56790, expand_56820)

      full_56840, = call(self.full_5684)

      generate_shape_56850, = call(self.generate_shape_5685, embedding_2190)

      expand_56860, = call(self.expand_5686, full_56840, generate_shape_56850)

      add_56870, = call(self.add_5687, divide_56830, expand_56860)

      rsqrt_56880, = call(self.rsqrt_5688, add_56870)

      generate_shape_56890, = call(self.generate_shape_5689, embedding_2190)

      expand_56900, = call(self.expand_5690, rsqrt_56880, generate_shape_56890)

      multiply_56910, = call(self.multiply_5691, subtract_56770, expand_56900)

      cast_56920, = call(self.cast_5692, parameter_80)

      generate_shape_56930, = call(self.generate_shape_5693, embedding_2190)

      expand_56940, = call(self.expand_5694, cast_56920, generate_shape_56930)

      multiply_56950, = call(self.multiply_5695, multiply_56910, expand_56940)

      cast_56960, = call(self.cast_5696, parameter_70)

      generate_shape_56970, = call(self.generate_shape_5697, embedding_2190)

      expand_56980, = call(self.expand_5698, cast_56960, generate_shape_56970)

      add_56990, = call(self.add_5699, multiply_56950, expand_56980)

      cast_57000, = call(self.cast_5700, add_56990)

      return call(self.yield_5702, cast_57000)

    return ret_lambda

    

  def fusion_5712_block00(self, call, matmul_2420, parameter_100, fusion_57010):

    def ret_lambda():

      generate_shape_57030, = call(self.generate_shape_5703, matmul_2420)

      expand_57040, = call(self.expand_5704, parameter_100, generate_shape_57030)

      add_57050, = call(self.add_5705, matmul_2420, expand_57040)

      scale_57060, = call(self.scale_5706, add_57050)

      generate_shape_57070, = call(self.generate_shape_5707, fusion_57010)

      reshape_57080, reshape_57081, = call(self.reshape_5708, scale_57060, generate_shape_57070)

      transpose_57090, = call(self.transpose_5709, reshape_57080)

      generate_shape_57100, = call(self.generate_shape_5710, fusion_57010)

      reshape_57110, reshape_57111, = call(self.reshape_5711, transpose_57090, generate_shape_57100)

      return call(self.yield_5713, reshape_57110)

    return ret_lambda

    

  def fusion_5722_block00(self, call, matmul_2460, parameter_120, fusion_57010):

    def ret_lambda():

      generate_shape_57140, = call(self.generate_shape_5714, matmul_2460)

      expand_57150, = call(self.expand_5715, parameter_120, generate_shape_57140)

      add_57160, = call(self.add_5716, matmul_2460, expand_57150)

      generate_shape_57170, = call(self.generate_shape_5717, fusion_57010)

      reshape_57180, reshape_57181, = call(self.reshape_5718, add_57160, generate_shape_57170)

      transpose_57190, = call(self.transpose_5719, reshape_57180)

      generate_shape_57200, = call(self.generate_shape_5720, fusion_57010)

      reshape_57210, reshape_57211, = call(self.reshape_5721, transpose_57190, generate_shape_57200)

      return call(self.yield_5723, reshape_57210)

    return ret_lambda

    

  def fusion_5732_block00(self, call, matmul_2540, parameter_140, fusion_57010):

    def ret_lambda():

      generate_shape_57240, = call(self.generate_shape_5724, matmul_2540)

      expand_57250, = call(self.expand_5725, parameter_140, generate_shape_57240)

      add_57260, = call(self.add_5726, matmul_2540, expand_57250)

      generate_shape_57270, = call(self.generate_shape_5727, fusion_57010)

      reshape_57280, reshape_57281, = call(self.reshape_5728, add_57260, generate_shape_57270)

      transpose_57290, = call(self.transpose_5729, reshape_57280)

      generate_shape_57300, = call(self.generate_shape_5730, fusion_57010)

      reshape_57310, reshape_57311, = call(self.reshape_5731, transpose_57290, generate_shape_57300)

      return call(self.yield_5733, reshape_57310)

    return ret_lambda

    

  def fusion_5741_block00(self, call, fusion_57010, fusion_57220, matmul_2850, triu_2330):

    def ret_lambda():

      generate_shape_57340, = call(self.generate_shape_5734, fusion_57010, fusion_57220)

      reshape_57350, reshape_57351, = call(self.reshape_5735, matmul_2850, generate_shape_57340)

      generate_shape_57360, = call(self.generate_shape_5736, fusion_57010)

      expand_57370, = call(self.expand_5737, triu_2330, generate_shape_57360)

      add_57380, = call(self.add_5738, reshape_57350, expand_57370)

      generate_shape_57390, = call(self.generate_shape_5739, fusion_57010, fusion_57220)

      reshape_57400, reshape_57401, = call(self.reshape_5740, add_57380, generate_shape_57390)

      return call(self.yield_5742, reshape_57400)

    return ret_lambda

    

  def fusion_5748_block00(self, call, fusion_57010, matmul_2950):

    def ret_lambda():

      generate_shape_57430, = call(self.generate_shape_5743, fusion_57010)

      reshape_57440, reshape_57441, = call(self.reshape_5744, matmul_2950, generate_shape_57430)

      transpose_57450, = call(self.transpose_5745, reshape_57440)

      generate_shape_57460, = call(self.generate_shape_5746, fusion_57010)

      reshape_57470, reshape_57471, = call(self.reshape_5747, transpose_57450, generate_shape_57460)

      return call(self.yield_5749, reshape_57470)

    return ret_lambda

    

  def fusion_5754_block00(self, call, matmul_3040, parameter_160, fusion_56640):

    def ret_lambda():

      generate_shape_57500, = call(self.generate_shape_5750, matmul_3040)

      expand_57510, = call(self.expand_5751, parameter_160, generate_shape_57500)

      add_57520, = call(self.add_5752, matmul_3040, expand_57510)

      add_57530, = call(self.add_5753, fusion_56640, add_57520)

      return call(self.yield_5755, add_57530)

    return ret_lambda

    

  def fusion_5758_block00(self, call, fusion_57540):

    def ret_lambda():

      cast_57560, = call(self.cast_5756, fusion_57540)

      reduce_sum_57570, = call(self.reduce_sum_5757, cast_57560)

      return call(self.yield_5759, reduce_sum_57570)

    return ret_lambda

    

  def fusion_5791_block00(self, call, fusion_57540, matmul_3040, fusion_57580, parameter_180, parameter_170):

    def ret_lambda():

      cast_57600, = call(self.cast_5760, fusion_57540)

      full_57610, = call(self.full_5761)

      generate_shape_57620, = call(self.generate_shape_5762, matmul_3040)

      expand_57630, = call(self.expand_5763, full_57610, generate_shape_57620)

      divide_57640, = call(self.divide_5764, fusion_57580, expand_57630)

      generate_shape_57650, = call(self.generate_shape_5765, matmul_3040)

      expand_57660, = call(self.expand_5766, divide_57640, generate_shape_57650)

      subtract_57670, = call(self.subtract_5767, cast_57600, expand_57660)

      multiply_57680, = call(self.multiply_5768, subtract_57670, subtract_57670)

      reduce_sum_57690, = call(self.reduce_sum_5769, multiply_57680)

      full_57700, = call(self.full_5770)

      generate_shape_57710, = call(self.generate_shape_5771, matmul_3040)

      expand_57720, = call(self.expand_5772, full_57700, generate_shape_57710)

      divide_57730, = call(self.divide_5773, reduce_sum_57690, expand_57720)

      full_57740, = call(self.full_5774)

      generate_shape_57750, = call(self.generate_shape_5775, matmul_3040)

      expand_57760, = call(self.expand_5776, full_57740, generate_shape_57750)

      add_57770, = call(self.add_5777, divide_57730, expand_57760)

      rsqrt_57780, = call(self.rsqrt_5778, add_57770)

      generate_shape_57790, = call(self.generate_shape_5779, matmul_3040)

      expand_57800, = call(self.expand_5780, rsqrt_57780, generate_shape_57790)

      multiply_57810, = call(self.multiply_5781, subtract_57670, expand_57800)

      cast_57820, = call(self.cast_5782, parameter_180)

      generate_shape_57830, = call(self.generate_shape_5783, matmul_3040)

      expand_57840, = call(self.expand_5784, cast_57820, generate_shape_57830)

      multiply_57850, = call(self.multiply_5785, multiply_57810, expand_57840)

      cast_57860, = call(self.cast_5786, parameter_170)

      generate_shape_57870, = call(self.generate_shape_5787, matmul_3040)

      expand_57880, = call(self.expand_5788, cast_57860, generate_shape_57870)

      add_57890, = call(self.add_5789, multiply_57850, expand_57880)

      cast_57900, = call(self.cast_5790, add_57890)

      return call(self.yield_5792, cast_57900)

    return ret_lambda

    

  def fusion_5809_block00(self, call, matmul_3080, parameter_200):

    def ret_lambda():

      generate_shape_57930, = call(self.generate_shape_5793, matmul_3080)

      expand_57940, = call(self.expand_5794, parameter_200, generate_shape_57930)

      add_57950, = call(self.add_5795, matmul_3080, expand_57940)

      scale_57960, = call(self.scale_5796, add_57950)

      cast_57970, = call(self.cast_5797, scale_57960)

      full_57980, = call(self.full_5798)

      scale_57990, = call(self.scale_5799, cast_57970)

      exp_58000, = call(self.exp_5800, scale_57990)

      generate_shape_58010, = call(self.generate_shape_5801, matmul_3080)

      expand_58020, = call(self.expand_5802, full_57980, generate_shape_58010)

      add_58030, = call(self.add_5803, expand_58020, exp_58000)

      generate_shape_58040, = call(self.generate_shape_5804, matmul_3080)

      expand_58050, = call(self.expand_5805, full_57980, generate_shape_58040)

      divide_58060, = call(self.divide_5806, expand_58050, add_58030)

      cast_58070, = call(self.cast_5807, divide_58060)

      multiply_58080, = call(self.multiply_5808, add_57950, cast_58070)

      return call(self.yield_5810, multiply_58080)

    return ret_lambda

    

  def fusion_5815_block00(self, call, matmul_3140, parameter_220, fusion_57540):

    def ret_lambda():

      generate_shape_58110, = call(self.generate_shape_5811, matmul_3140)

      expand_58120, = call(self.expand_5812, parameter_220, generate_shape_58110)

      add_58130, = call(self.add_5813, matmul_3140, expand_58120)

      add_58140, = call(self.add_5814, fusion_57540, add_58130)

      return call(self.yield_5816, add_58140)

    return ret_lambda

    

  def fusion_5819_block00(self, call, fusion_58150):

    def ret_lambda():

      cast_58170, = call(self.cast_5817, fusion_58150)

      reduce_sum_58180, = call(self.reduce_sum_5818, cast_58170)

      return call(self.yield_5820, reduce_sum_58180)

    return ret_lambda

    

  def fusion_5852_block00(self, call, fusion_58150, matmul_3140, fusion_58190, parameter_240, parameter_230):

    def ret_lambda():

      cast_58210, = call(self.cast_5821, fusion_58150)

      full_58220, = call(self.full_5822)

      generate_shape_58230, = call(self.generate_shape_5823, matmul_3140)

      expand_58240, = call(self.expand_5824, full_58220, generate_shape_58230)

      divide_58250, = call(self.divide_5825, fusion_58190, expand_58240)

      generate_shape_58260, = call(self.generate_shape_5826, matmul_3140)

      expand_58270, = call(self.expand_5827, divide_58250, generate_shape_58260)

      subtract_58280, = call(self.subtract_5828, cast_58210, expand_58270)

      multiply_58290, = call(self.multiply_5829, subtract_58280, subtract_58280)

      reduce_sum_58300, = call(self.reduce_sum_5830, multiply_58290)

      full_58310, = call(self.full_5831)

      generate_shape_58320, = call(self.generate_shape_5832, matmul_3140)

      expand_58330, = call(self.expand_5833, full_58310, generate_shape_58320)

      divide_58340, = call(self.divide_5834, reduce_sum_58300, expand_58330)

      full_58350, = call(self.full_5835)

      generate_shape_58360, = call(self.generate_shape_5836, matmul_3140)

      expand_58370, = call(self.expand_5837, full_58350, generate_shape_58360)

      add_58380, = call(self.add_5838, divide_58340, expand_58370)

      rsqrt_58390, = call(self.rsqrt_5839, add_58380)

      generate_shape_58400, = call(self.generate_shape_5840, matmul_3140)

      expand_58410, = call(self.expand_5841, rsqrt_58390, generate_shape_58400)

      multiply_58420, = call(self.multiply_5842, subtract_58280, expand_58410)

      cast_58430, = call(self.cast_5843, parameter_240)

      generate_shape_58440, = call(self.generate_shape_5844, matmul_3140)

      expand_58450, = call(self.expand_5845, cast_58430, generate_shape_58440)

      multiply_58460, = call(self.multiply_5846, multiply_58420, expand_58450)

      cast_58470, = call(self.cast_5847, parameter_230)

      generate_shape_58480, = call(self.generate_shape_5848, matmul_3140)

      expand_58490, = call(self.expand_5849, cast_58470, generate_shape_58480)

      add_58500, = call(self.add_5850, multiply_58460, expand_58490)

      cast_58510, = call(self.cast_5851, add_58500)

      return call(self.yield_5853, cast_58510)

    return ret_lambda

    

  def fusion_5863_block00(self, call, matmul_3250, parameter_260, fusion_58520):

    def ret_lambda():

      generate_shape_58540, = call(self.generate_shape_5854, matmul_3250)

      expand_58550, = call(self.expand_5855, parameter_260, generate_shape_58540)

      add_58560, = call(self.add_5856, matmul_3250, expand_58550)

      scale_58570, = call(self.scale_5857, add_58560)

      generate_shape_58580, = call(self.generate_shape_5858, fusion_58520)

      reshape_58590, reshape_58591, = call(self.reshape_5859, scale_58570, generate_shape_58580)

      transpose_58600, = call(self.transpose_5860, reshape_58590)

      generate_shape_58610, = call(self.generate_shape_5861, fusion_58520)

      reshape_58620, reshape_58621, = call(self.reshape_5862, transpose_58600, generate_shape_58610)

      return call(self.yield_5864, reshape_58620)

    return ret_lambda

    

  def fusion_5873_block00(self, call, matmul_3290, parameter_280, fusion_58520):

    def ret_lambda():

      generate_shape_58650, = call(self.generate_shape_5865, matmul_3290)

      expand_58660, = call(self.expand_5866, parameter_280, generate_shape_58650)

      add_58670, = call(self.add_5867, matmul_3290, expand_58660)

      generate_shape_58680, = call(self.generate_shape_5868, fusion_58520)

      reshape_58690, reshape_58691, = call(self.reshape_5869, add_58670, generate_shape_58680)

      transpose_58700, = call(self.transpose_5870, reshape_58690)

      generate_shape_58710, = call(self.generate_shape_5871, fusion_58520)

      reshape_58720, reshape_58721, = call(self.reshape_5872, transpose_58700, generate_shape_58710)

      return call(self.yield_5874, reshape_58720)

    return ret_lambda

    

  def fusion_5883_block00(self, call, matmul_3370, parameter_300, fusion_58520):

    def ret_lambda():

      generate_shape_58750, = call(self.generate_shape_5875, matmul_3370)

      expand_58760, = call(self.expand_5876, parameter_300, generate_shape_58750)

      add_58770, = call(self.add_5877, matmul_3370, expand_58760)

      generate_shape_58780, = call(self.generate_shape_5878, fusion_58520)

      reshape_58790, reshape_58791, = call(self.reshape_5879, add_58770, generate_shape_58780)

      transpose_58800, = call(self.transpose_5880, reshape_58790)

      generate_shape_58810, = call(self.generate_shape_5881, fusion_58520)

      reshape_58820, reshape_58821, = call(self.reshape_5882, transpose_58800, generate_shape_58810)

      return call(self.yield_5884, reshape_58820)

    return ret_lambda

    

  def fusion_5892_block00(self, call, fusion_58520, fusion_58730, matmul_3680, triu_2330):

    def ret_lambda():

      generate_shape_58850, = call(self.generate_shape_5885, fusion_58520, fusion_58730)

      reshape_58860, reshape_58861, = call(self.reshape_5886, matmul_3680, generate_shape_58850)

      generate_shape_58870, = call(self.generate_shape_5887, fusion_58520)

      expand_58880, = call(self.expand_5888, triu_2330, generate_shape_58870)

      add_58890, = call(self.add_5889, reshape_58860, expand_58880)

      generate_shape_58900, = call(self.generate_shape_5890, fusion_58520, fusion_58730)

      reshape_58910, reshape_58911, = call(self.reshape_5891, add_58890, generate_shape_58900)

      return call(self.yield_5893, reshape_58910)

    return ret_lambda

    

  def fusion_5899_block00(self, call, fusion_58520, matmul_3780):

    def ret_lambda():

      generate_shape_58940, = call(self.generate_shape_5894, fusion_58520)

      reshape_58950, reshape_58951, = call(self.reshape_5895, matmul_3780, generate_shape_58940)

      transpose_58960, = call(self.transpose_5896, reshape_58950)

      generate_shape_58970, = call(self.generate_shape_5897, fusion_58520)

      reshape_58980, reshape_58981, = call(self.reshape_5898, transpose_58960, generate_shape_58970)

      return call(self.yield_5900, reshape_58980)

    return ret_lambda

    

  def fusion_5905_block00(self, call, matmul_3870, parameter_320, fusion_58150):

    def ret_lambda():

      generate_shape_59010, = call(self.generate_shape_5901, matmul_3870)

      expand_59020, = call(self.expand_5902, parameter_320, generate_shape_59010)

      add_59030, = call(self.add_5903, matmul_3870, expand_59020)

      add_59040, = call(self.add_5904, fusion_58150, add_59030)

      return call(self.yield_5906, add_59040)

    return ret_lambda

    

  def fusion_5909_block00(self, call, fusion_59050):

    def ret_lambda():

      cast_59070, = call(self.cast_5907, fusion_59050)

      reduce_sum_59080, = call(self.reduce_sum_5908, cast_59070)

      return call(self.yield_5910, reduce_sum_59080)

    return ret_lambda

    

  def fusion_5942_block00(self, call, fusion_59050, matmul_3870, fusion_59090, parameter_340, parameter_330):

    def ret_lambda():

      cast_59110, = call(self.cast_5911, fusion_59050)

      full_59120, = call(self.full_5912)

      generate_shape_59130, = call(self.generate_shape_5913, matmul_3870)

      expand_59140, = call(self.expand_5914, full_59120, generate_shape_59130)

      divide_59150, = call(self.divide_5915, fusion_59090, expand_59140)

      generate_shape_59160, = call(self.generate_shape_5916, matmul_3870)

      expand_59170, = call(self.expand_5917, divide_59150, generate_shape_59160)

      subtract_59180, = call(self.subtract_5918, cast_59110, expand_59170)

      multiply_59190, = call(self.multiply_5919, subtract_59180, subtract_59180)

      reduce_sum_59200, = call(self.reduce_sum_5920, multiply_59190)

      full_59210, = call(self.full_5921)

      generate_shape_59220, = call(self.generate_shape_5922, matmul_3870)

      expand_59230, = call(self.expand_5923, full_59210, generate_shape_59220)

      divide_59240, = call(self.divide_5924, reduce_sum_59200, expand_59230)

      full_59250, = call(self.full_5925)

      generate_shape_59260, = call(self.generate_shape_5926, matmul_3870)

      expand_59270, = call(self.expand_5927, full_59250, generate_shape_59260)

      add_59280, = call(self.add_5928, divide_59240, expand_59270)

      rsqrt_59290, = call(self.rsqrt_5929, add_59280)

      generate_shape_59300, = call(self.generate_shape_5930, matmul_3870)

      expand_59310, = call(self.expand_5931, rsqrt_59290, generate_shape_59300)

      multiply_59320, = call(self.multiply_5932, subtract_59180, expand_59310)

      cast_59330, = call(self.cast_5933, parameter_340)

      generate_shape_59340, = call(self.generate_shape_5934, matmul_3870)

      expand_59350, = call(self.expand_5935, cast_59330, generate_shape_59340)

      multiply_59360, = call(self.multiply_5936, multiply_59320, expand_59350)

      cast_59370, = call(self.cast_5937, parameter_330)

      generate_shape_59380, = call(self.generate_shape_5938, matmul_3870)

      expand_59390, = call(self.expand_5939, cast_59370, generate_shape_59380)

      add_59400, = call(self.add_5940, multiply_59360, expand_59390)

      cast_59410, = call(self.cast_5941, add_59400)

      return call(self.yield_5943, cast_59410)

    return ret_lambda

    

  def fusion_5960_block00(self, call, matmul_3910, parameter_360):

    def ret_lambda():

      generate_shape_59440, = call(self.generate_shape_5944, matmul_3910)

      expand_59450, = call(self.expand_5945, parameter_360, generate_shape_59440)

      add_59460, = call(self.add_5946, matmul_3910, expand_59450)

      scale_59470, = call(self.scale_5947, add_59460)

      cast_59480, = call(self.cast_5948, scale_59470)

      full_59490, = call(self.full_5949)

      scale_59500, = call(self.scale_5950, cast_59480)

      exp_59510, = call(self.exp_5951, scale_59500)

      generate_shape_59520, = call(self.generate_shape_5952, matmul_3910)

      expand_59530, = call(self.expand_5953, full_59490, generate_shape_59520)

      add_59540, = call(self.add_5954, expand_59530, exp_59510)

      generate_shape_59550, = call(self.generate_shape_5955, matmul_3910)

      expand_59560, = call(self.expand_5956, full_59490, generate_shape_59550)

      divide_59570, = call(self.divide_5957, expand_59560, add_59540)

      cast_59580, = call(self.cast_5958, divide_59570)

      multiply_59590, = call(self.multiply_5959, add_59460, cast_59580)

      return call(self.yield_5961, multiply_59590)

    return ret_lambda

    

  def fusion_5966_block00(self, call, matmul_3970, parameter_380, fusion_59050):

    def ret_lambda():

      generate_shape_59620, = call(self.generate_shape_5962, matmul_3970)

      expand_59630, = call(self.expand_5963, parameter_380, generate_shape_59620)

      add_59640, = call(self.add_5964, matmul_3970, expand_59630)

      add_59650, = call(self.add_5965, fusion_59050, add_59640)

      return call(self.yield_5967, add_59650)

    return ret_lambda

    

  def fusion_5970_block00(self, call, fusion_59660):

    def ret_lambda():

      cast_59680, = call(self.cast_5968, fusion_59660)

      reduce_sum_59690, = call(self.reduce_sum_5969, cast_59680)

      return call(self.yield_5971, reduce_sum_59690)

    return ret_lambda

    

  def fusion_6003_block00(self, call, fusion_59660, matmul_3970, fusion_59700, parameter_400, parameter_390):

    def ret_lambda():

      cast_59720, = call(self.cast_5972, fusion_59660)

      full_59730, = call(self.full_5973)

      generate_shape_59740, = call(self.generate_shape_5974, matmul_3970)

      expand_59750, = call(self.expand_5975, full_59730, generate_shape_59740)

      divide_59760, = call(self.divide_5976, fusion_59700, expand_59750)

      generate_shape_59770, = call(self.generate_shape_5977, matmul_3970)

      expand_59780, = call(self.expand_5978, divide_59760, generate_shape_59770)

      subtract_59790, = call(self.subtract_5979, cast_59720, expand_59780)

      multiply_59800, = call(self.multiply_5980, subtract_59790, subtract_59790)

      reduce_sum_59810, = call(self.reduce_sum_5981, multiply_59800)

      full_59820, = call(self.full_5982)

      generate_shape_59830, = call(self.generate_shape_5983, matmul_3970)

      expand_59840, = call(self.expand_5984, full_59820, generate_shape_59830)

      divide_59850, = call(self.divide_5985, reduce_sum_59810, expand_59840)

      full_59860, = call(self.full_5986)

      generate_shape_59870, = call(self.generate_shape_5987, matmul_3970)

      expand_59880, = call(self.expand_5988, full_59860, generate_shape_59870)

      add_59890, = call(self.add_5989, divide_59850, expand_59880)

      rsqrt_59900, = call(self.rsqrt_5990, add_59890)

      generate_shape_59910, = call(self.generate_shape_5991, matmul_3970)

      expand_59920, = call(self.expand_5992, rsqrt_59900, generate_shape_59910)

      multiply_59930, = call(self.multiply_5993, subtract_59790, expand_59920)

      cast_59940, = call(self.cast_5994, parameter_400)

      generate_shape_59950, = call(self.generate_shape_5995, matmul_3970)

      expand_59960, = call(self.expand_5996, cast_59940, generate_shape_59950)

      multiply_59970, = call(self.multiply_5997, multiply_59930, expand_59960)

      cast_59980, = call(self.cast_5998, parameter_390)

      generate_shape_59990, = call(self.generate_shape_5999, matmul_3970)

      expand_60000, = call(self.expand_6000, cast_59980, generate_shape_59990)

      add_60010, = call(self.add_6001, multiply_59970, expand_60000)

      cast_60020, = call(self.cast_6002, add_60010)

      return call(self.yield_6004, cast_60020)

    return ret_lambda

    

  def fusion_6014_block00(self, call, matmul_4080, parameter_420, fusion_60030):

    def ret_lambda():

      generate_shape_60050, = call(self.generate_shape_6005, matmul_4080)

      expand_60060, = call(self.expand_6006, parameter_420, generate_shape_60050)

      add_60070, = call(self.add_6007, matmul_4080, expand_60060)

      scale_60080, = call(self.scale_6008, add_60070)

      generate_shape_60090, = call(self.generate_shape_6009, fusion_60030)

      reshape_60100, reshape_60101, = call(self.reshape_6010, scale_60080, generate_shape_60090)

      transpose_60110, = call(self.transpose_6011, reshape_60100)

      generate_shape_60120, = call(self.generate_shape_6012, fusion_60030)

      reshape_60130, reshape_60131, = call(self.reshape_6013, transpose_60110, generate_shape_60120)

      return call(self.yield_6015, reshape_60130)

    return ret_lambda

    

  def fusion_6024_block00(self, call, matmul_4120, parameter_440, fusion_60030):

    def ret_lambda():

      generate_shape_60160, = call(self.generate_shape_6016, matmul_4120)

      expand_60170, = call(self.expand_6017, parameter_440, generate_shape_60160)

      add_60180, = call(self.add_6018, matmul_4120, expand_60170)

      generate_shape_60190, = call(self.generate_shape_6019, fusion_60030)

      reshape_60200, reshape_60201, = call(self.reshape_6020, add_60180, generate_shape_60190)

      transpose_60210, = call(self.transpose_6021, reshape_60200)

      generate_shape_60220, = call(self.generate_shape_6022, fusion_60030)

      reshape_60230, reshape_60231, = call(self.reshape_6023, transpose_60210, generate_shape_60220)

      return call(self.yield_6025, reshape_60230)

    return ret_lambda

    

  def fusion_6034_block00(self, call, matmul_4200, parameter_460, fusion_60030):

    def ret_lambda():

      generate_shape_60260, = call(self.generate_shape_6026, matmul_4200)

      expand_60270, = call(self.expand_6027, parameter_460, generate_shape_60260)

      add_60280, = call(self.add_6028, matmul_4200, expand_60270)

      generate_shape_60290, = call(self.generate_shape_6029, fusion_60030)

      reshape_60300, reshape_60301, = call(self.reshape_6030, add_60280, generate_shape_60290)

      transpose_60310, = call(self.transpose_6031, reshape_60300)

      generate_shape_60320, = call(self.generate_shape_6032, fusion_60030)

      reshape_60330, reshape_60331, = call(self.reshape_6033, transpose_60310, generate_shape_60320)

      return call(self.yield_6035, reshape_60330)

    return ret_lambda

    

  def fusion_6043_block00(self, call, fusion_60030, fusion_60240, matmul_4510, triu_2330):

    def ret_lambda():

      generate_shape_60360, = call(self.generate_shape_6036, fusion_60030, fusion_60240)

      reshape_60370, reshape_60371, = call(self.reshape_6037, matmul_4510, generate_shape_60360)

      generate_shape_60380, = call(self.generate_shape_6038, fusion_60030)

      expand_60390, = call(self.expand_6039, triu_2330, generate_shape_60380)

      add_60400, = call(self.add_6040, reshape_60370, expand_60390)

      generate_shape_60410, = call(self.generate_shape_6041, fusion_60030, fusion_60240)

      reshape_60420, reshape_60421, = call(self.reshape_6042, add_60400, generate_shape_60410)

      return call(self.yield_6044, reshape_60420)

    return ret_lambda

    

  def fusion_6050_block00(self, call, fusion_60030, matmul_4610):

    def ret_lambda():

      generate_shape_60450, = call(self.generate_shape_6045, fusion_60030)

      reshape_60460, reshape_60461, = call(self.reshape_6046, matmul_4610, generate_shape_60450)

      transpose_60470, = call(self.transpose_6047, reshape_60460)

      generate_shape_60480, = call(self.generate_shape_6048, fusion_60030)

      reshape_60490, reshape_60491, = call(self.reshape_6049, transpose_60470, generate_shape_60480)

      return call(self.yield_6051, reshape_60490)

    return ret_lambda

    

  def fusion_6056_block00(self, call, matmul_4700, parameter_480, fusion_59660):

    def ret_lambda():

      generate_shape_60520, = call(self.generate_shape_6052, matmul_4700)

      expand_60530, = call(self.expand_6053, parameter_480, generate_shape_60520)

      add_60540, = call(self.add_6054, matmul_4700, expand_60530)

      add_60550, = call(self.add_6055, fusion_59660, add_60540)

      return call(self.yield_6057, add_60550)

    return ret_lambda

    

  def fusion_6060_block00(self, call, fusion_60560):

    def ret_lambda():

      cast_60580, = call(self.cast_6058, fusion_60560)

      reduce_sum_60590, = call(self.reduce_sum_6059, cast_60580)

      return call(self.yield_6061, reduce_sum_60590)

    return ret_lambda

    

  def fusion_6093_block00(self, call, fusion_60560, matmul_4700, fusion_60600, parameter_500, parameter_490):

    def ret_lambda():

      cast_60620, = call(self.cast_6062, fusion_60560)

      full_60630, = call(self.full_6063)

      generate_shape_60640, = call(self.generate_shape_6064, matmul_4700)

      expand_60650, = call(self.expand_6065, full_60630, generate_shape_60640)

      divide_60660, = call(self.divide_6066, fusion_60600, expand_60650)

      generate_shape_60670, = call(self.generate_shape_6067, matmul_4700)

      expand_60680, = call(self.expand_6068, divide_60660, generate_shape_60670)

      subtract_60690, = call(self.subtract_6069, cast_60620, expand_60680)

      multiply_60700, = call(self.multiply_6070, subtract_60690, subtract_60690)

      reduce_sum_60710, = call(self.reduce_sum_6071, multiply_60700)

      full_60720, = call(self.full_6072)

      generate_shape_60730, = call(self.generate_shape_6073, matmul_4700)

      expand_60740, = call(self.expand_6074, full_60720, generate_shape_60730)

      divide_60750, = call(self.divide_6075, reduce_sum_60710, expand_60740)

      full_60760, = call(self.full_6076)

      generate_shape_60770, = call(self.generate_shape_6077, matmul_4700)

      expand_60780, = call(self.expand_6078, full_60760, generate_shape_60770)

      add_60790, = call(self.add_6079, divide_60750, expand_60780)

      rsqrt_60800, = call(self.rsqrt_6080, add_60790)

      generate_shape_60810, = call(self.generate_shape_6081, matmul_4700)

      expand_60820, = call(self.expand_6082, rsqrt_60800, generate_shape_60810)

      multiply_60830, = call(self.multiply_6083, subtract_60690, expand_60820)

      cast_60840, = call(self.cast_6084, parameter_500)

      generate_shape_60850, = call(self.generate_shape_6085, matmul_4700)

      expand_60860, = call(self.expand_6086, cast_60840, generate_shape_60850)

      multiply_60870, = call(self.multiply_6087, multiply_60830, expand_60860)

      cast_60880, = call(self.cast_6088, parameter_490)

      generate_shape_60890, = call(self.generate_shape_6089, matmul_4700)

      expand_60900, = call(self.expand_6090, cast_60880, generate_shape_60890)

      add_60910, = call(self.add_6091, multiply_60870, expand_60900)

      cast_60920, = call(self.cast_6092, add_60910)

      return call(self.yield_6094, cast_60920)

    return ret_lambda

    

  def fusion_6111_block00(self, call, matmul_4740, parameter_520):

    def ret_lambda():

      generate_shape_60950, = call(self.generate_shape_6095, matmul_4740)

      expand_60960, = call(self.expand_6096, parameter_520, generate_shape_60950)

      add_60970, = call(self.add_6097, matmul_4740, expand_60960)

      scale_60980, = call(self.scale_6098, add_60970)

      cast_60990, = call(self.cast_6099, scale_60980)

      full_61000, = call(self.full_6100)

      scale_61010, = call(self.scale_6101, cast_60990)

      exp_61020, = call(self.exp_6102, scale_61010)

      generate_shape_61030, = call(self.generate_shape_6103, matmul_4740)

      expand_61040, = call(self.expand_6104, full_61000, generate_shape_61030)

      add_61050, = call(self.add_6105, expand_61040, exp_61020)

      generate_shape_61060, = call(self.generate_shape_6106, matmul_4740)

      expand_61070, = call(self.expand_6107, full_61000, generate_shape_61060)

      divide_61080, = call(self.divide_6108, expand_61070, add_61050)

      cast_61090, = call(self.cast_6109, divide_61080)

      multiply_61100, = call(self.multiply_6110, add_60970, cast_61090)

      return call(self.yield_6112, multiply_61100)

    return ret_lambda

    

  def fusion_6117_block00(self, call, matmul_4800, parameter_540, fusion_60560):

    def ret_lambda():

      generate_shape_61130, = call(self.generate_shape_6113, matmul_4800)

      expand_61140, = call(self.expand_6114, parameter_540, generate_shape_61130)

      add_61150, = call(self.add_6115, matmul_4800, expand_61140)

      add_61160, = call(self.add_6116, fusion_60560, add_61150)

      return call(self.yield_6118, add_61160)

    return ret_lambda

    

  def fusion_6121_block00(self, call, fusion_61170):

    def ret_lambda():

      cast_61190, = call(self.cast_6119, fusion_61170)

      reduce_sum_61200, = call(self.reduce_sum_6120, cast_61190)

      return call(self.yield_6122, reduce_sum_61200)

    return ret_lambda

    

  def fusion_6154_block00(self, call, fusion_61170, matmul_4800, fusion_61210, parameter_560, parameter_550):

    def ret_lambda():

      cast_61230, = call(self.cast_6123, fusion_61170)

      full_61240, = call(self.full_6124)

      generate_shape_61250, = call(self.generate_shape_6125, matmul_4800)

      expand_61260, = call(self.expand_6126, full_61240, generate_shape_61250)

      divide_61270, = call(self.divide_6127, fusion_61210, expand_61260)

      generate_shape_61280, = call(self.generate_shape_6128, matmul_4800)

      expand_61290, = call(self.expand_6129, divide_61270, generate_shape_61280)

      subtract_61300, = call(self.subtract_6130, cast_61230, expand_61290)

      multiply_61310, = call(self.multiply_6131, subtract_61300, subtract_61300)

      reduce_sum_61320, = call(self.reduce_sum_6132, multiply_61310)

      full_61330, = call(self.full_6133)

      generate_shape_61340, = call(self.generate_shape_6134, matmul_4800)

      expand_61350, = call(self.expand_6135, full_61330, generate_shape_61340)

      divide_61360, = call(self.divide_6136, reduce_sum_61320, expand_61350)

      full_61370, = call(self.full_6137)

      generate_shape_61380, = call(self.generate_shape_6138, matmul_4800)

      expand_61390, = call(self.expand_6139, full_61370, generate_shape_61380)

      add_61400, = call(self.add_6140, divide_61360, expand_61390)

      rsqrt_61410, = call(self.rsqrt_6141, add_61400)

      generate_shape_61420, = call(self.generate_shape_6142, matmul_4800)

      expand_61430, = call(self.expand_6143, rsqrt_61410, generate_shape_61420)

      multiply_61440, = call(self.multiply_6144, subtract_61300, expand_61430)

      cast_61450, = call(self.cast_6145, parameter_560)

      generate_shape_61460, = call(self.generate_shape_6146, matmul_4800)

      expand_61470, = call(self.expand_6147, cast_61450, generate_shape_61460)

      multiply_61480, = call(self.multiply_6148, multiply_61440, expand_61470)

      cast_61490, = call(self.cast_6149, parameter_550)

      generate_shape_61500, = call(self.generate_shape_6150, matmul_4800)

      expand_61510, = call(self.expand_6151, cast_61490, generate_shape_61500)

      add_61520, = call(self.add_6152, multiply_61480, expand_61510)

      cast_61530, = call(self.cast_6153, add_61520)

      return call(self.yield_6155, cast_61530)

    return ret_lambda

    

  def fusion_6165_block00(self, call, matmul_4910, parameter_580, fusion_61540):

    def ret_lambda():

      generate_shape_61560, = call(self.generate_shape_6156, matmul_4910)

      expand_61570, = call(self.expand_6157, parameter_580, generate_shape_61560)

      add_61580, = call(self.add_6158, matmul_4910, expand_61570)

      scale_61590, = call(self.scale_6159, add_61580)

      generate_shape_61600, = call(self.generate_shape_6160, fusion_61540)

      reshape_61610, reshape_61611, = call(self.reshape_6161, scale_61590, generate_shape_61600)

      transpose_61620, = call(self.transpose_6162, reshape_61610)

      generate_shape_61630, = call(self.generate_shape_6163, fusion_61540)

      reshape_61640, reshape_61641, = call(self.reshape_6164, transpose_61620, generate_shape_61630)

      return call(self.yield_6166, reshape_61640)

    return ret_lambda

    

  def fusion_6175_block00(self, call, matmul_4950, parameter_600, fusion_61540):

    def ret_lambda():

      generate_shape_61670, = call(self.generate_shape_6167, matmul_4950)

      expand_61680, = call(self.expand_6168, parameter_600, generate_shape_61670)

      add_61690, = call(self.add_6169, matmul_4950, expand_61680)

      generate_shape_61700, = call(self.generate_shape_6170, fusion_61540)

      reshape_61710, reshape_61711, = call(self.reshape_6171, add_61690, generate_shape_61700)

      transpose_61720, = call(self.transpose_6172, reshape_61710)

      generate_shape_61730, = call(self.generate_shape_6173, fusion_61540)

      reshape_61740, reshape_61741, = call(self.reshape_6174, transpose_61720, generate_shape_61730)

      return call(self.yield_6176, reshape_61740)

    return ret_lambda

    

  def fusion_6185_block00(self, call, matmul_5030, parameter_620, fusion_61540):

    def ret_lambda():

      generate_shape_61770, = call(self.generate_shape_6177, matmul_5030)

      expand_61780, = call(self.expand_6178, parameter_620, generate_shape_61770)

      add_61790, = call(self.add_6179, matmul_5030, expand_61780)

      generate_shape_61800, = call(self.generate_shape_6180, fusion_61540)

      reshape_61810, reshape_61811, = call(self.reshape_6181, add_61790, generate_shape_61800)

      transpose_61820, = call(self.transpose_6182, reshape_61810)

      generate_shape_61830, = call(self.generate_shape_6183, fusion_61540)

      reshape_61840, reshape_61841, = call(self.reshape_6184, transpose_61820, generate_shape_61830)

      return call(self.yield_6186, reshape_61840)

    return ret_lambda

    

  def fusion_6194_block00(self, call, fusion_61540, fusion_61750, matmul_5340, triu_2330):

    def ret_lambda():

      generate_shape_61870, = call(self.generate_shape_6187, fusion_61540, fusion_61750)

      reshape_61880, reshape_61881, = call(self.reshape_6188, matmul_5340, generate_shape_61870)

      generate_shape_61890, = call(self.generate_shape_6189, fusion_61540)

      expand_61900, = call(self.expand_6190, triu_2330, generate_shape_61890)

      add_61910, = call(self.add_6191, reshape_61880, expand_61900)

      generate_shape_61920, = call(self.generate_shape_6192, fusion_61540, fusion_61750)

      reshape_61930, reshape_61931, = call(self.reshape_6193, add_61910, generate_shape_61920)

      return call(self.yield_6195, reshape_61930)

    return ret_lambda

    

  def fusion_6201_block00(self, call, fusion_61540, matmul_5440):

    def ret_lambda():

      generate_shape_61960, = call(self.generate_shape_6196, fusion_61540)

      reshape_61970, reshape_61971, = call(self.reshape_6197, matmul_5440, generate_shape_61960)

      transpose_61980, = call(self.transpose_6198, reshape_61970)

      generate_shape_61990, = call(self.generate_shape_6199, fusion_61540)

      reshape_62000, reshape_62001, = call(self.reshape_6200, transpose_61980, generate_shape_61990)

      return call(self.yield_6202, reshape_62000)

    return ret_lambda

    

  def fusion_6207_block00(self, call, matmul_5530, parameter_640, fusion_61170):

    def ret_lambda():

      generate_shape_62030, = call(self.generate_shape_6203, matmul_5530)

      expand_62040, = call(self.expand_6204, parameter_640, generate_shape_62030)

      add_62050, = call(self.add_6205, matmul_5530, expand_62040)

      add_62060, = call(self.add_6206, fusion_61170, add_62050)

      return call(self.yield_6208, add_62060)

    return ret_lambda

    

  def fusion_6211_block00(self, call, fusion_62070):

    def ret_lambda():

      cast_62090, = call(self.cast_6209, fusion_62070)

      reduce_sum_62100, = call(self.reduce_sum_6210, cast_62090)

      return call(self.yield_6212, reduce_sum_62100)

    return ret_lambda

    

  def fusion_6244_block00(self, call, fusion_62070, matmul_5530, fusion_62110, parameter_660, parameter_650):

    def ret_lambda():

      cast_62130, = call(self.cast_6213, fusion_62070)

      full_62140, = call(self.full_6214)

      generate_shape_62150, = call(self.generate_shape_6215, matmul_5530)

      expand_62160, = call(self.expand_6216, full_62140, generate_shape_62150)

      divide_62170, = call(self.divide_6217, fusion_62110, expand_62160)

      generate_shape_62180, = call(self.generate_shape_6218, matmul_5530)

      expand_62190, = call(self.expand_6219, divide_62170, generate_shape_62180)

      subtract_62200, = call(self.subtract_6220, cast_62130, expand_62190)

      multiply_62210, = call(self.multiply_6221, subtract_62200, subtract_62200)

      reduce_sum_62220, = call(self.reduce_sum_6222, multiply_62210)

      full_62230, = call(self.full_6223)

      generate_shape_62240, = call(self.generate_shape_6224, matmul_5530)

      expand_62250, = call(self.expand_6225, full_62230, generate_shape_62240)

      divide_62260, = call(self.divide_6226, reduce_sum_62220, expand_62250)

      full_62270, = call(self.full_6227)

      generate_shape_62280, = call(self.generate_shape_6228, matmul_5530)

      expand_62290, = call(self.expand_6229, full_62270, generate_shape_62280)

      add_62300, = call(self.add_6230, divide_62260, expand_62290)

      rsqrt_62310, = call(self.rsqrt_6231, add_62300)

      generate_shape_62320, = call(self.generate_shape_6232, matmul_5530)

      expand_62330, = call(self.expand_6233, rsqrt_62310, generate_shape_62320)

      multiply_62340, = call(self.multiply_6234, subtract_62200, expand_62330)

      cast_62350, = call(self.cast_6235, parameter_660)

      generate_shape_62360, = call(self.generate_shape_6236, matmul_5530)

      expand_62370, = call(self.expand_6237, cast_62350, generate_shape_62360)

      multiply_62380, = call(self.multiply_6238, multiply_62340, expand_62370)

      cast_62390, = call(self.cast_6239, parameter_650)

      generate_shape_62400, = call(self.generate_shape_6240, matmul_5530)

      expand_62410, = call(self.expand_6241, cast_62390, generate_shape_62400)

      add_62420, = call(self.add_6242, multiply_62380, expand_62410)

      cast_62430, = call(self.cast_6243, add_62420)

      return call(self.yield_6245, cast_62430)

    return ret_lambda

    

  def fusion_6262_block00(self, call, matmul_5570, parameter_680):

    def ret_lambda():

      generate_shape_62460, = call(self.generate_shape_6246, matmul_5570)

      expand_62470, = call(self.expand_6247, parameter_680, generate_shape_62460)

      add_62480, = call(self.add_6248, matmul_5570, expand_62470)

      scale_62490, = call(self.scale_6249, add_62480)

      cast_62500, = call(self.cast_6250, scale_62490)

      full_62510, = call(self.full_6251)

      scale_62520, = call(self.scale_6252, cast_62500)

      exp_62530, = call(self.exp_6253, scale_62520)

      generate_shape_62540, = call(self.generate_shape_6254, matmul_5570)

      expand_62550, = call(self.expand_6255, full_62510, generate_shape_62540)

      add_62560, = call(self.add_6256, expand_62550, exp_62530)

      generate_shape_62570, = call(self.generate_shape_6257, matmul_5570)

      expand_62580, = call(self.expand_6258, full_62510, generate_shape_62570)

      divide_62590, = call(self.divide_6259, expand_62580, add_62560)

      cast_62600, = call(self.cast_6260, divide_62590)

      multiply_62610, = call(self.multiply_6261, add_62480, cast_62600)

      return call(self.yield_6263, multiply_62610)

    return ret_lambda

    

  def fusion_6268_block00(self, call, matmul_5630, parameter_700, fusion_62070):

    def ret_lambda():

      generate_shape_62640, = call(self.generate_shape_6264, matmul_5630)

      expand_62650, = call(self.expand_6265, parameter_700, generate_shape_62640)

      add_62660, = call(self.add_6266, matmul_5630, expand_62650)

      add_62670, = call(self.add_6267, fusion_62070, add_62660)

      return call(self.yield_6269, add_62670)

    return ret_lambda

    

  def fusion_6272_block00(self, call, fusion_62680):

    def ret_lambda():

      cast_62700, = call(self.cast_6270, fusion_62680)

      reduce_sum_62710, = call(self.reduce_sum_6271, cast_62700)

      return call(self.yield_6273, reduce_sum_62710)

    return ret_lambda

    

  def fusion_6305_block00(self, call, fusion_62680, matmul_5630, fusion_62720, parameter_720, parameter_710):

    def ret_lambda():

      cast_62740, = call(self.cast_6274, fusion_62680)

      full_62750, = call(self.full_6275)

      generate_shape_62760, = call(self.generate_shape_6276, matmul_5630)

      expand_62770, = call(self.expand_6277, full_62750, generate_shape_62760)

      divide_62780, = call(self.divide_6278, fusion_62720, expand_62770)

      generate_shape_62790, = call(self.generate_shape_6279, matmul_5630)

      expand_62800, = call(self.expand_6280, divide_62780, generate_shape_62790)

      subtract_62810, = call(self.subtract_6281, cast_62740, expand_62800)

      multiply_62820, = call(self.multiply_6282, subtract_62810, subtract_62810)

      reduce_sum_62830, = call(self.reduce_sum_6283, multiply_62820)

      full_62840, = call(self.full_6284)

      generate_shape_62850, = call(self.generate_shape_6285, matmul_5630)

      expand_62860, = call(self.expand_6286, full_62840, generate_shape_62850)

      divide_62870, = call(self.divide_6287, reduce_sum_62830, expand_62860)

      full_62880, = call(self.full_6288)

      generate_shape_62890, = call(self.generate_shape_6289, matmul_5630)

      expand_62900, = call(self.expand_6290, full_62880, generate_shape_62890)

      add_62910, = call(self.add_6291, divide_62870, expand_62900)

      rsqrt_62920, = call(self.rsqrt_6292, add_62910)

      generate_shape_62930, = call(self.generate_shape_6293, matmul_5630)

      expand_62940, = call(self.expand_6294, rsqrt_62920, generate_shape_62930)

      multiply_62950, = call(self.multiply_6295, subtract_62810, expand_62940)

      cast_62960, = call(self.cast_6296, parameter_720)

      generate_shape_62970, = call(self.generate_shape_6297, matmul_5630)

      expand_62980, = call(self.expand_6298, cast_62960, generate_shape_62970)

      multiply_62990, = call(self.multiply_6299, multiply_62950, expand_62980)

      cast_63000, = call(self.cast_6300, parameter_710)

      generate_shape_63010, = call(self.generate_shape_6301, matmul_5630)

      expand_63020, = call(self.expand_6302, cast_63000, generate_shape_63010)

      add_63030, = call(self.add_6303, multiply_62990, expand_63020)

      cast_63040, = call(self.cast_6304, add_63030)

      return call(self.yield_6306, cast_63040)

    return ret_lambda

    

  def fusion_6316_block00(self, call, matmul_5740, parameter_740, fusion_63050):

    def ret_lambda():

      generate_shape_63070, = call(self.generate_shape_6307, matmul_5740)

      expand_63080, = call(self.expand_6308, parameter_740, generate_shape_63070)

      add_63090, = call(self.add_6309, matmul_5740, expand_63080)

      scale_63100, = call(self.scale_6310, add_63090)

      generate_shape_63110, = call(self.generate_shape_6311, fusion_63050)

      reshape_63120, reshape_63121, = call(self.reshape_6312, scale_63100, generate_shape_63110)

      transpose_63130, = call(self.transpose_6313, reshape_63120)

      generate_shape_63140, = call(self.generate_shape_6314, fusion_63050)

      reshape_63150, reshape_63151, = call(self.reshape_6315, transpose_63130, generate_shape_63140)

      return call(self.yield_6317, reshape_63150)

    return ret_lambda

    

  def fusion_6326_block00(self, call, matmul_5780, parameter_760, fusion_63050):

    def ret_lambda():

      generate_shape_63180, = call(self.generate_shape_6318, matmul_5780)

      expand_63190, = call(self.expand_6319, parameter_760, generate_shape_63180)

      add_63200, = call(self.add_6320, matmul_5780, expand_63190)

      generate_shape_63210, = call(self.generate_shape_6321, fusion_63050)

      reshape_63220, reshape_63221, = call(self.reshape_6322, add_63200, generate_shape_63210)

      transpose_63230, = call(self.transpose_6323, reshape_63220)

      generate_shape_63240, = call(self.generate_shape_6324, fusion_63050)

      reshape_63250, reshape_63251, = call(self.reshape_6325, transpose_63230, generate_shape_63240)

      return call(self.yield_6327, reshape_63250)

    return ret_lambda

    

  def fusion_6336_block00(self, call, matmul_5860, parameter_780, fusion_63050):

    def ret_lambda():

      generate_shape_63280, = call(self.generate_shape_6328, matmul_5860)

      expand_63290, = call(self.expand_6329, parameter_780, generate_shape_63280)

      add_63300, = call(self.add_6330, matmul_5860, expand_63290)

      generate_shape_63310, = call(self.generate_shape_6331, fusion_63050)

      reshape_63320, reshape_63321, = call(self.reshape_6332, add_63300, generate_shape_63310)

      transpose_63330, = call(self.transpose_6333, reshape_63320)

      generate_shape_63340, = call(self.generate_shape_6334, fusion_63050)

      reshape_63350, reshape_63351, = call(self.reshape_6335, transpose_63330, generate_shape_63340)

      return call(self.yield_6337, reshape_63350)

    return ret_lambda

    

  def fusion_6345_block00(self, call, fusion_63050, fusion_63260, matmul_6170, triu_2330):

    def ret_lambda():

      generate_shape_63380, = call(self.generate_shape_6338, fusion_63050, fusion_63260)

      reshape_63390, reshape_63391, = call(self.reshape_6339, matmul_6170, generate_shape_63380)

      generate_shape_63400, = call(self.generate_shape_6340, fusion_63050)

      expand_63410, = call(self.expand_6341, triu_2330, generate_shape_63400)

      add_63420, = call(self.add_6342, reshape_63390, expand_63410)

      generate_shape_63430, = call(self.generate_shape_6343, fusion_63050, fusion_63260)

      reshape_63440, reshape_63441, = call(self.reshape_6344, add_63420, generate_shape_63430)

      return call(self.yield_6346, reshape_63440)

    return ret_lambda

    

  def fusion_6352_block00(self, call, fusion_63050, matmul_6270):

    def ret_lambda():

      generate_shape_63470, = call(self.generate_shape_6347, fusion_63050)

      reshape_63480, reshape_63481, = call(self.reshape_6348, matmul_6270, generate_shape_63470)

      transpose_63490, = call(self.transpose_6349, reshape_63480)

      generate_shape_63500, = call(self.generate_shape_6350, fusion_63050)

      reshape_63510, reshape_63511, = call(self.reshape_6351, transpose_63490, generate_shape_63500)

      return call(self.yield_6353, reshape_63510)

    return ret_lambda

    

  def fusion_6358_block00(self, call, matmul_6360, parameter_800, fusion_62680):

    def ret_lambda():

      generate_shape_63540, = call(self.generate_shape_6354, matmul_6360)

      expand_63550, = call(self.expand_6355, parameter_800, generate_shape_63540)

      add_63560, = call(self.add_6356, matmul_6360, expand_63550)

      add_63570, = call(self.add_6357, fusion_62680, add_63560)

      return call(self.yield_6359, add_63570)

    return ret_lambda

    

  def fusion_6362_block00(self, call, fusion_63580):

    def ret_lambda():

      cast_63600, = call(self.cast_6360, fusion_63580)

      reduce_sum_63610, = call(self.reduce_sum_6361, cast_63600)

      return call(self.yield_6363, reduce_sum_63610)

    return ret_lambda

    

  def fusion_6395_block00(self, call, fusion_63580, matmul_6360, fusion_63620, parameter_820, parameter_810):

    def ret_lambda():

      cast_63640, = call(self.cast_6364, fusion_63580)

      full_63650, = call(self.full_6365)

      generate_shape_63660, = call(self.generate_shape_6366, matmul_6360)

      expand_63670, = call(self.expand_6367, full_63650, generate_shape_63660)

      divide_63680, = call(self.divide_6368, fusion_63620, expand_63670)

      generate_shape_63690, = call(self.generate_shape_6369, matmul_6360)

      expand_63700, = call(self.expand_6370, divide_63680, generate_shape_63690)

      subtract_63710, = call(self.subtract_6371, cast_63640, expand_63700)

      multiply_63720, = call(self.multiply_6372, subtract_63710, subtract_63710)

      reduce_sum_63730, = call(self.reduce_sum_6373, multiply_63720)

      full_63740, = call(self.full_6374)

      generate_shape_63750, = call(self.generate_shape_6375, matmul_6360)

      expand_63760, = call(self.expand_6376, full_63740, generate_shape_63750)

      divide_63770, = call(self.divide_6377, reduce_sum_63730, expand_63760)

      full_63780, = call(self.full_6378)

      generate_shape_63790, = call(self.generate_shape_6379, matmul_6360)

      expand_63800, = call(self.expand_6380, full_63780, generate_shape_63790)

      add_63810, = call(self.add_6381, divide_63770, expand_63800)

      rsqrt_63820, = call(self.rsqrt_6382, add_63810)

      generate_shape_63830, = call(self.generate_shape_6383, matmul_6360)

      expand_63840, = call(self.expand_6384, rsqrt_63820, generate_shape_63830)

      multiply_63850, = call(self.multiply_6385, subtract_63710, expand_63840)

      cast_63860, = call(self.cast_6386, parameter_820)

      generate_shape_63870, = call(self.generate_shape_6387, matmul_6360)

      expand_63880, = call(self.expand_6388, cast_63860, generate_shape_63870)

      multiply_63890, = call(self.multiply_6389, multiply_63850, expand_63880)

      cast_63900, = call(self.cast_6390, parameter_810)

      generate_shape_63910, = call(self.generate_shape_6391, matmul_6360)

      expand_63920, = call(self.expand_6392, cast_63900, generate_shape_63910)

      add_63930, = call(self.add_6393, multiply_63890, expand_63920)

      cast_63940, = call(self.cast_6394, add_63930)

      return call(self.yield_6396, cast_63940)

    return ret_lambda

    

  def fusion_6413_block00(self, call, matmul_6400, parameter_840):

    def ret_lambda():

      generate_shape_63970, = call(self.generate_shape_6397, matmul_6400)

      expand_63980, = call(self.expand_6398, parameter_840, generate_shape_63970)

      add_63990, = call(self.add_6399, matmul_6400, expand_63980)

      scale_64000, = call(self.scale_6400, add_63990)

      cast_64010, = call(self.cast_6401, scale_64000)

      full_64020, = call(self.full_6402)

      scale_64030, = call(self.scale_6403, cast_64010)

      exp_64040, = call(self.exp_6404, scale_64030)

      generate_shape_64050, = call(self.generate_shape_6405, matmul_6400)

      expand_64060, = call(self.expand_6406, full_64020, generate_shape_64050)

      add_64070, = call(self.add_6407, expand_64060, exp_64040)

      generate_shape_64080, = call(self.generate_shape_6408, matmul_6400)

      expand_64090, = call(self.expand_6409, full_64020, generate_shape_64080)

      divide_64100, = call(self.divide_6410, expand_64090, add_64070)

      cast_64110, = call(self.cast_6411, divide_64100)

      multiply_64120, = call(self.multiply_6412, add_63990, cast_64110)

      return call(self.yield_6414, multiply_64120)

    return ret_lambda

    

  def fusion_6419_block00(self, call, matmul_6460, parameter_860, fusion_63580):

    def ret_lambda():

      generate_shape_64150, = call(self.generate_shape_6415, matmul_6460)

      expand_64160, = call(self.expand_6416, parameter_860, generate_shape_64150)

      add_64170, = call(self.add_6417, matmul_6460, expand_64160)

      add_64180, = call(self.add_6418, fusion_63580, add_64170)

      return call(self.yield_6420, add_64180)

    return ret_lambda

    

  def fusion_6423_block00(self, call, fusion_64190):

    def ret_lambda():

      cast_64210, = call(self.cast_6421, fusion_64190)

      reduce_sum_64220, = call(self.reduce_sum_6422, cast_64210)

      return call(self.yield_6424, reduce_sum_64220)

    return ret_lambda

    

  def fusion_6456_block00(self, call, fusion_64190, matmul_6460, fusion_64230, parameter_880, parameter_870):

    def ret_lambda():

      cast_64250, = call(self.cast_6425, fusion_64190)

      full_64260, = call(self.full_6426)

      generate_shape_64270, = call(self.generate_shape_6427, matmul_6460)

      expand_64280, = call(self.expand_6428, full_64260, generate_shape_64270)

      divide_64290, = call(self.divide_6429, fusion_64230, expand_64280)

      generate_shape_64300, = call(self.generate_shape_6430, matmul_6460)

      expand_64310, = call(self.expand_6431, divide_64290, generate_shape_64300)

      subtract_64320, = call(self.subtract_6432, cast_64250, expand_64310)

      multiply_64330, = call(self.multiply_6433, subtract_64320, subtract_64320)

      reduce_sum_64340, = call(self.reduce_sum_6434, multiply_64330)

      full_64350, = call(self.full_6435)

      generate_shape_64360, = call(self.generate_shape_6436, matmul_6460)

      expand_64370, = call(self.expand_6437, full_64350, generate_shape_64360)

      divide_64380, = call(self.divide_6438, reduce_sum_64340, expand_64370)

      full_64390, = call(self.full_6439)

      generate_shape_64400, = call(self.generate_shape_6440, matmul_6460)

      expand_64410, = call(self.expand_6441, full_64390, generate_shape_64400)

      add_64420, = call(self.add_6442, divide_64380, expand_64410)

      rsqrt_64430, = call(self.rsqrt_6443, add_64420)

      generate_shape_64440, = call(self.generate_shape_6444, matmul_6460)

      expand_64450, = call(self.expand_6445, rsqrt_64430, generate_shape_64440)

      multiply_64460, = call(self.multiply_6446, subtract_64320, expand_64450)

      cast_64470, = call(self.cast_6447, parameter_880)

      generate_shape_64480, = call(self.generate_shape_6448, matmul_6460)

      expand_64490, = call(self.expand_6449, cast_64470, generate_shape_64480)

      multiply_64500, = call(self.multiply_6450, multiply_64460, expand_64490)

      cast_64510, = call(self.cast_6451, parameter_870)

      generate_shape_64520, = call(self.generate_shape_6452, matmul_6460)

      expand_64530, = call(self.expand_6453, cast_64510, generate_shape_64520)

      add_64540, = call(self.add_6454, multiply_64500, expand_64530)

      cast_64550, = call(self.cast_6455, add_64540)

      return call(self.yield_6457, cast_64550)

    return ret_lambda

    

  def fusion_6467_block00(self, call, matmul_6570, parameter_900, fusion_64560):

    def ret_lambda():

      generate_shape_64580, = call(self.generate_shape_6458, matmul_6570)

      expand_64590, = call(self.expand_6459, parameter_900, generate_shape_64580)

      add_64600, = call(self.add_6460, matmul_6570, expand_64590)

      scale_64610, = call(self.scale_6461, add_64600)

      generate_shape_64620, = call(self.generate_shape_6462, fusion_64560)

      reshape_64630, reshape_64631, = call(self.reshape_6463, scale_64610, generate_shape_64620)

      transpose_64640, = call(self.transpose_6464, reshape_64630)

      generate_shape_64650, = call(self.generate_shape_6465, fusion_64560)

      reshape_64660, reshape_64661, = call(self.reshape_6466, transpose_64640, generate_shape_64650)

      return call(self.yield_6468, reshape_64660)

    return ret_lambda

    

  def fusion_6477_block00(self, call, matmul_6610, parameter_920, fusion_64560):

    def ret_lambda():

      generate_shape_64690, = call(self.generate_shape_6469, matmul_6610)

      expand_64700, = call(self.expand_6470, parameter_920, generate_shape_64690)

      add_64710, = call(self.add_6471, matmul_6610, expand_64700)

      generate_shape_64720, = call(self.generate_shape_6472, fusion_64560)

      reshape_64730, reshape_64731, = call(self.reshape_6473, add_64710, generate_shape_64720)

      transpose_64740, = call(self.transpose_6474, reshape_64730)

      generate_shape_64750, = call(self.generate_shape_6475, fusion_64560)

      reshape_64760, reshape_64761, = call(self.reshape_6476, transpose_64740, generate_shape_64750)

      return call(self.yield_6478, reshape_64760)

    return ret_lambda

    

  def fusion_6487_block00(self, call, matmul_6690, parameter_940, fusion_64560):

    def ret_lambda():

      generate_shape_64790, = call(self.generate_shape_6479, matmul_6690)

      expand_64800, = call(self.expand_6480, parameter_940, generate_shape_64790)

      add_64810, = call(self.add_6481, matmul_6690, expand_64800)

      generate_shape_64820, = call(self.generate_shape_6482, fusion_64560)

      reshape_64830, reshape_64831, = call(self.reshape_6483, add_64810, generate_shape_64820)

      transpose_64840, = call(self.transpose_6484, reshape_64830)

      generate_shape_64850, = call(self.generate_shape_6485, fusion_64560)

      reshape_64860, reshape_64861, = call(self.reshape_6486, transpose_64840, generate_shape_64850)

      return call(self.yield_6488, reshape_64860)

    return ret_lambda

    

  def fusion_6496_block00(self, call, fusion_64560, fusion_64770, matmul_7000, triu_2330):

    def ret_lambda():

      generate_shape_64890, = call(self.generate_shape_6489, fusion_64560, fusion_64770)

      reshape_64900, reshape_64901, = call(self.reshape_6490, matmul_7000, generate_shape_64890)

      generate_shape_64910, = call(self.generate_shape_6491, fusion_64560)

      expand_64920, = call(self.expand_6492, triu_2330, generate_shape_64910)

      add_64930, = call(self.add_6493, reshape_64900, expand_64920)

      generate_shape_64940, = call(self.generate_shape_6494, fusion_64560, fusion_64770)

      reshape_64950, reshape_64951, = call(self.reshape_6495, add_64930, generate_shape_64940)

      return call(self.yield_6497, reshape_64950)

    return ret_lambda

    

  def fusion_6503_block00(self, call, fusion_64560, matmul_7100):

    def ret_lambda():

      generate_shape_64980, = call(self.generate_shape_6498, fusion_64560)

      reshape_64990, reshape_64991, = call(self.reshape_6499, matmul_7100, generate_shape_64980)

      transpose_65000, = call(self.transpose_6500, reshape_64990)

      generate_shape_65010, = call(self.generate_shape_6501, fusion_64560)

      reshape_65020, reshape_65021, = call(self.reshape_6502, transpose_65000, generate_shape_65010)

      return call(self.yield_6504, reshape_65020)

    return ret_lambda

    

  def fusion_6509_block00(self, call, matmul_7190, parameter_960, fusion_64190):

    def ret_lambda():

      generate_shape_65050, = call(self.generate_shape_6505, matmul_7190)

      expand_65060, = call(self.expand_6506, parameter_960, generate_shape_65050)

      add_65070, = call(self.add_6507, matmul_7190, expand_65060)

      add_65080, = call(self.add_6508, fusion_64190, add_65070)

      return call(self.yield_6510, add_65080)

    return ret_lambda

    

  def fusion_6513_block00(self, call, fusion_65090):

    def ret_lambda():

      cast_65110, = call(self.cast_6511, fusion_65090)

      reduce_sum_65120, = call(self.reduce_sum_6512, cast_65110)

      return call(self.yield_6514, reduce_sum_65120)

    return ret_lambda

    

  def fusion_6546_block00(self, call, fusion_65090, matmul_7190, fusion_65130, parameter_980, parameter_970):

    def ret_lambda():

      cast_65150, = call(self.cast_6515, fusion_65090)

      full_65160, = call(self.full_6516)

      generate_shape_65170, = call(self.generate_shape_6517, matmul_7190)

      expand_65180, = call(self.expand_6518, full_65160, generate_shape_65170)

      divide_65190, = call(self.divide_6519, fusion_65130, expand_65180)

      generate_shape_65200, = call(self.generate_shape_6520, matmul_7190)

      expand_65210, = call(self.expand_6521, divide_65190, generate_shape_65200)

      subtract_65220, = call(self.subtract_6522, cast_65150, expand_65210)

      multiply_65230, = call(self.multiply_6523, subtract_65220, subtract_65220)

      reduce_sum_65240, = call(self.reduce_sum_6524, multiply_65230)

      full_65250, = call(self.full_6525)

      generate_shape_65260, = call(self.generate_shape_6526, matmul_7190)

      expand_65270, = call(self.expand_6527, full_65250, generate_shape_65260)

      divide_65280, = call(self.divide_6528, reduce_sum_65240, expand_65270)

      full_65290, = call(self.full_6529)

      generate_shape_65300, = call(self.generate_shape_6530, matmul_7190)

      expand_65310, = call(self.expand_6531, full_65290, generate_shape_65300)

      add_65320, = call(self.add_6532, divide_65280, expand_65310)

      rsqrt_65330, = call(self.rsqrt_6533, add_65320)

      generate_shape_65340, = call(self.generate_shape_6534, matmul_7190)

      expand_65350, = call(self.expand_6535, rsqrt_65330, generate_shape_65340)

      multiply_65360, = call(self.multiply_6536, subtract_65220, expand_65350)

      cast_65370, = call(self.cast_6537, parameter_980)

      generate_shape_65380, = call(self.generate_shape_6538, matmul_7190)

      expand_65390, = call(self.expand_6539, cast_65370, generate_shape_65380)

      multiply_65400, = call(self.multiply_6540, multiply_65360, expand_65390)

      cast_65410, = call(self.cast_6541, parameter_970)

      generate_shape_65420, = call(self.generate_shape_6542, matmul_7190)

      expand_65430, = call(self.expand_6543, cast_65410, generate_shape_65420)

      add_65440, = call(self.add_6544, multiply_65400, expand_65430)

      cast_65450, = call(self.cast_6545, add_65440)

      return call(self.yield_6547, cast_65450)

    return ret_lambda

    

  def fusion_6564_block00(self, call, matmul_7230, parameter_1000):

    def ret_lambda():

      generate_shape_65480, = call(self.generate_shape_6548, matmul_7230)

      expand_65490, = call(self.expand_6549, parameter_1000, generate_shape_65480)

      add_65500, = call(self.add_6550, matmul_7230, expand_65490)

      scale_65510, = call(self.scale_6551, add_65500)

      cast_65520, = call(self.cast_6552, scale_65510)

      full_65530, = call(self.full_6553)

      scale_65540, = call(self.scale_6554, cast_65520)

      exp_65550, = call(self.exp_6555, scale_65540)

      generate_shape_65560, = call(self.generate_shape_6556, matmul_7230)

      expand_65570, = call(self.expand_6557, full_65530, generate_shape_65560)

      add_65580, = call(self.add_6558, expand_65570, exp_65550)

      generate_shape_65590, = call(self.generate_shape_6559, matmul_7230)

      expand_65600, = call(self.expand_6560, full_65530, generate_shape_65590)

      divide_65610, = call(self.divide_6561, expand_65600, add_65580)

      cast_65620, = call(self.cast_6562, divide_65610)

      multiply_65630, = call(self.multiply_6563, add_65500, cast_65620)

      return call(self.yield_6565, multiply_65630)

    return ret_lambda

    

  def fusion_6570_block00(self, call, matmul_7290, parameter_1020, fusion_65090):

    def ret_lambda():

      generate_shape_65660, = call(self.generate_shape_6566, matmul_7290)

      expand_65670, = call(self.expand_6567, parameter_1020, generate_shape_65660)

      add_65680, = call(self.add_6568, matmul_7290, expand_65670)

      add_65690, = call(self.add_6569, fusion_65090, add_65680)

      return call(self.yield_6571, add_65690)

    return ret_lambda

    

  def fusion_6574_block00(self, call, fusion_65700):

    def ret_lambda():

      cast_65720, = call(self.cast_6572, fusion_65700)

      reduce_sum_65730, = call(self.reduce_sum_6573, cast_65720)

      return call(self.yield_6575, reduce_sum_65730)

    return ret_lambda

    

  def fusion_6607_block00(self, call, fusion_65700, matmul_7290, fusion_65740, parameter_1040, parameter_1030):

    def ret_lambda():

      cast_65760, = call(self.cast_6576, fusion_65700)

      full_65770, = call(self.full_6577)

      generate_shape_65780, = call(self.generate_shape_6578, matmul_7290)

      expand_65790, = call(self.expand_6579, full_65770, generate_shape_65780)

      divide_65800, = call(self.divide_6580, fusion_65740, expand_65790)

      generate_shape_65810, = call(self.generate_shape_6581, matmul_7290)

      expand_65820, = call(self.expand_6582, divide_65800, generate_shape_65810)

      subtract_65830, = call(self.subtract_6583, cast_65760, expand_65820)

      multiply_65840, = call(self.multiply_6584, subtract_65830, subtract_65830)

      reduce_sum_65850, = call(self.reduce_sum_6585, multiply_65840)

      full_65860, = call(self.full_6586)

      generate_shape_65870, = call(self.generate_shape_6587, matmul_7290)

      expand_65880, = call(self.expand_6588, full_65860, generate_shape_65870)

      divide_65890, = call(self.divide_6589, reduce_sum_65850, expand_65880)

      full_65900, = call(self.full_6590)

      generate_shape_65910, = call(self.generate_shape_6591, matmul_7290)

      expand_65920, = call(self.expand_6592, full_65900, generate_shape_65910)

      add_65930, = call(self.add_6593, divide_65890, expand_65920)

      rsqrt_65940, = call(self.rsqrt_6594, add_65930)

      generate_shape_65950, = call(self.generate_shape_6595, matmul_7290)

      expand_65960, = call(self.expand_6596, rsqrt_65940, generate_shape_65950)

      multiply_65970, = call(self.multiply_6597, subtract_65830, expand_65960)

      cast_65980, = call(self.cast_6598, parameter_1040)

      generate_shape_65990, = call(self.generate_shape_6599, matmul_7290)

      expand_66000, = call(self.expand_6600, cast_65980, generate_shape_65990)

      multiply_66010, = call(self.multiply_6601, multiply_65970, expand_66000)

      cast_66020, = call(self.cast_6602, parameter_1030)

      generate_shape_66030, = call(self.generate_shape_6603, matmul_7290)

      expand_66040, = call(self.expand_6604, cast_66020, generate_shape_66030)

      add_66050, = call(self.add_6605, multiply_66010, expand_66040)

      cast_66060, = call(self.cast_6606, add_66050)

      return call(self.yield_6608, cast_66060)

    return ret_lambda

    

  def fusion_6618_block00(self, call, matmul_7400, parameter_1060, fusion_66070):

    def ret_lambda():

      generate_shape_66090, = call(self.generate_shape_6609, matmul_7400)

      expand_66100, = call(self.expand_6610, parameter_1060, generate_shape_66090)

      add_66110, = call(self.add_6611, matmul_7400, expand_66100)

      scale_66120, = call(self.scale_6612, add_66110)

      generate_shape_66130, = call(self.generate_shape_6613, fusion_66070)

      reshape_66140, reshape_66141, = call(self.reshape_6614, scale_66120, generate_shape_66130)

      transpose_66150, = call(self.transpose_6615, reshape_66140)

      generate_shape_66160, = call(self.generate_shape_6616, fusion_66070)

      reshape_66170, reshape_66171, = call(self.reshape_6617, transpose_66150, generate_shape_66160)

      return call(self.yield_6619, reshape_66170)

    return ret_lambda

    

  def fusion_6628_block00(self, call, matmul_7440, parameter_1080, fusion_66070):

    def ret_lambda():

      generate_shape_66200, = call(self.generate_shape_6620, matmul_7440)

      expand_66210, = call(self.expand_6621, parameter_1080, generate_shape_66200)

      add_66220, = call(self.add_6622, matmul_7440, expand_66210)

      generate_shape_66230, = call(self.generate_shape_6623, fusion_66070)

      reshape_66240, reshape_66241, = call(self.reshape_6624, add_66220, generate_shape_66230)

      transpose_66250, = call(self.transpose_6625, reshape_66240)

      generate_shape_66260, = call(self.generate_shape_6626, fusion_66070)

      reshape_66270, reshape_66271, = call(self.reshape_6627, transpose_66250, generate_shape_66260)

      return call(self.yield_6629, reshape_66270)

    return ret_lambda

    

  def fusion_6638_block00(self, call, matmul_7520, parameter_1100, fusion_66070):

    def ret_lambda():

      generate_shape_66300, = call(self.generate_shape_6630, matmul_7520)

      expand_66310, = call(self.expand_6631, parameter_1100, generate_shape_66300)

      add_66320, = call(self.add_6632, matmul_7520, expand_66310)

      generate_shape_66330, = call(self.generate_shape_6633, fusion_66070)

      reshape_66340, reshape_66341, = call(self.reshape_6634, add_66320, generate_shape_66330)

      transpose_66350, = call(self.transpose_6635, reshape_66340)

      generate_shape_66360, = call(self.generate_shape_6636, fusion_66070)

      reshape_66370, reshape_66371, = call(self.reshape_6637, transpose_66350, generate_shape_66360)

      return call(self.yield_6639, reshape_66370)

    return ret_lambda

    

  def fusion_6647_block00(self, call, fusion_66070, fusion_66280, matmul_7830, triu_2330):

    def ret_lambda():

      generate_shape_66400, = call(self.generate_shape_6640, fusion_66070, fusion_66280)

      reshape_66410, reshape_66411, = call(self.reshape_6641, matmul_7830, generate_shape_66400)

      generate_shape_66420, = call(self.generate_shape_6642, fusion_66070)

      expand_66430, = call(self.expand_6643, triu_2330, generate_shape_66420)

      add_66440, = call(self.add_6644, reshape_66410, expand_66430)

      generate_shape_66450, = call(self.generate_shape_6645, fusion_66070, fusion_66280)

      reshape_66460, reshape_66461, = call(self.reshape_6646, add_66440, generate_shape_66450)

      return call(self.yield_6648, reshape_66460)

    return ret_lambda

    

  def fusion_6654_block00(self, call, fusion_66070, matmul_7930):

    def ret_lambda():

      generate_shape_66490, = call(self.generate_shape_6649, fusion_66070)

      reshape_66500, reshape_66501, = call(self.reshape_6650, matmul_7930, generate_shape_66490)

      transpose_66510, = call(self.transpose_6651, reshape_66500)

      generate_shape_66520, = call(self.generate_shape_6652, fusion_66070)

      reshape_66530, reshape_66531, = call(self.reshape_6653, transpose_66510, generate_shape_66520)

      return call(self.yield_6655, reshape_66530)

    return ret_lambda

    

  def fusion_6660_block00(self, call, matmul_8020, parameter_1120, fusion_65700):

    def ret_lambda():

      generate_shape_66560, = call(self.generate_shape_6656, matmul_8020)

      expand_66570, = call(self.expand_6657, parameter_1120, generate_shape_66560)

      add_66580, = call(self.add_6658, matmul_8020, expand_66570)

      add_66590, = call(self.add_6659, fusion_65700, add_66580)

      return call(self.yield_6661, add_66590)

    return ret_lambda

    

  def fusion_6664_block00(self, call, fusion_66600):

    def ret_lambda():

      cast_66620, = call(self.cast_6662, fusion_66600)

      reduce_sum_66630, = call(self.reduce_sum_6663, cast_66620)

      return call(self.yield_6665, reduce_sum_66630)

    return ret_lambda

    

  def fusion_6697_block00(self, call, fusion_66600, matmul_8020, fusion_66640, parameter_1140, parameter_1130):

    def ret_lambda():

      cast_66660, = call(self.cast_6666, fusion_66600)

      full_66670, = call(self.full_6667)

      generate_shape_66680, = call(self.generate_shape_6668, matmul_8020)

      expand_66690, = call(self.expand_6669, full_66670, generate_shape_66680)

      divide_66700, = call(self.divide_6670, fusion_66640, expand_66690)

      generate_shape_66710, = call(self.generate_shape_6671, matmul_8020)

      expand_66720, = call(self.expand_6672, divide_66700, generate_shape_66710)

      subtract_66730, = call(self.subtract_6673, cast_66660, expand_66720)

      multiply_66740, = call(self.multiply_6674, subtract_66730, subtract_66730)

      reduce_sum_66750, = call(self.reduce_sum_6675, multiply_66740)

      full_66760, = call(self.full_6676)

      generate_shape_66770, = call(self.generate_shape_6677, matmul_8020)

      expand_66780, = call(self.expand_6678, full_66760, generate_shape_66770)

      divide_66790, = call(self.divide_6679, reduce_sum_66750, expand_66780)

      full_66800, = call(self.full_6680)

      generate_shape_66810, = call(self.generate_shape_6681, matmul_8020)

      expand_66820, = call(self.expand_6682, full_66800, generate_shape_66810)

      add_66830, = call(self.add_6683, divide_66790, expand_66820)

      rsqrt_66840, = call(self.rsqrt_6684, add_66830)

      generate_shape_66850, = call(self.generate_shape_6685, matmul_8020)

      expand_66860, = call(self.expand_6686, rsqrt_66840, generate_shape_66850)

      multiply_66870, = call(self.multiply_6687, subtract_66730, expand_66860)

      cast_66880, = call(self.cast_6688, parameter_1140)

      generate_shape_66890, = call(self.generate_shape_6689, matmul_8020)

      expand_66900, = call(self.expand_6690, cast_66880, generate_shape_66890)

      multiply_66910, = call(self.multiply_6691, multiply_66870, expand_66900)

      cast_66920, = call(self.cast_6692, parameter_1130)

      generate_shape_66930, = call(self.generate_shape_6693, matmul_8020)

      expand_66940, = call(self.expand_6694, cast_66920, generate_shape_66930)

      add_66950, = call(self.add_6695, multiply_66910, expand_66940)

      cast_66960, = call(self.cast_6696, add_66950)

      return call(self.yield_6698, cast_66960)

    return ret_lambda

    

  def fusion_6715_block00(self, call, matmul_8060, parameter_1160):

    def ret_lambda():

      generate_shape_66990, = call(self.generate_shape_6699, matmul_8060)

      expand_67000, = call(self.expand_6700, parameter_1160, generate_shape_66990)

      add_67010, = call(self.add_6701, matmul_8060, expand_67000)

      scale_67020, = call(self.scale_6702, add_67010)

      cast_67030, = call(self.cast_6703, scale_67020)

      full_67040, = call(self.full_6704)

      scale_67050, = call(self.scale_6705, cast_67030)

      exp_67060, = call(self.exp_6706, scale_67050)

      generate_shape_67070, = call(self.generate_shape_6707, matmul_8060)

      expand_67080, = call(self.expand_6708, full_67040, generate_shape_67070)

      add_67090, = call(self.add_6709, expand_67080, exp_67060)

      generate_shape_67100, = call(self.generate_shape_6710, matmul_8060)

      expand_67110, = call(self.expand_6711, full_67040, generate_shape_67100)

      divide_67120, = call(self.divide_6712, expand_67110, add_67090)

      cast_67130, = call(self.cast_6713, divide_67120)

      multiply_67140, = call(self.multiply_6714, add_67010, cast_67130)

      return call(self.yield_6716, multiply_67140)

    return ret_lambda

    

  def fusion_6721_block00(self, call, matmul_8120, parameter_1180, fusion_66600):

    def ret_lambda():

      generate_shape_67170, = call(self.generate_shape_6717, matmul_8120)

      expand_67180, = call(self.expand_6718, parameter_1180, generate_shape_67170)

      add_67190, = call(self.add_6719, matmul_8120, expand_67180)

      add_67200, = call(self.add_6720, fusion_66600, add_67190)

      return call(self.yield_6722, add_67200)

    return ret_lambda

    

  def fusion_6725_block00(self, call, fusion_67210):

    def ret_lambda():

      cast_67230, = call(self.cast_6723, fusion_67210)

      reduce_sum_67240, = call(self.reduce_sum_6724, cast_67230)

      return call(self.yield_6726, reduce_sum_67240)

    return ret_lambda

    

  def fusion_6758_block00(self, call, fusion_67210, matmul_8120, fusion_67250, parameter_1200, parameter_1190):

    def ret_lambda():

      cast_67270, = call(self.cast_6727, fusion_67210)

      full_67280, = call(self.full_6728)

      generate_shape_67290, = call(self.generate_shape_6729, matmul_8120)

      expand_67300, = call(self.expand_6730, full_67280, generate_shape_67290)

      divide_67310, = call(self.divide_6731, fusion_67250, expand_67300)

      generate_shape_67320, = call(self.generate_shape_6732, matmul_8120)

      expand_67330, = call(self.expand_6733, divide_67310, generate_shape_67320)

      subtract_67340, = call(self.subtract_6734, cast_67270, expand_67330)

      multiply_67350, = call(self.multiply_6735, subtract_67340, subtract_67340)

      reduce_sum_67360, = call(self.reduce_sum_6736, multiply_67350)

      full_67370, = call(self.full_6737)

      generate_shape_67380, = call(self.generate_shape_6738, matmul_8120)

      expand_67390, = call(self.expand_6739, full_67370, generate_shape_67380)

      divide_67400, = call(self.divide_6740, reduce_sum_67360, expand_67390)

      full_67410, = call(self.full_6741)

      generate_shape_67420, = call(self.generate_shape_6742, matmul_8120)

      expand_67430, = call(self.expand_6743, full_67410, generate_shape_67420)

      add_67440, = call(self.add_6744, divide_67400, expand_67430)

      rsqrt_67450, = call(self.rsqrt_6745, add_67440)

      generate_shape_67460, = call(self.generate_shape_6746, matmul_8120)

      expand_67470, = call(self.expand_6747, rsqrt_67450, generate_shape_67460)

      multiply_67480, = call(self.multiply_6748, subtract_67340, expand_67470)

      cast_67490, = call(self.cast_6749, parameter_1200)

      generate_shape_67500, = call(self.generate_shape_6750, matmul_8120)

      expand_67510, = call(self.expand_6751, cast_67490, generate_shape_67500)

      multiply_67520, = call(self.multiply_6752, multiply_67480, expand_67510)

      cast_67530, = call(self.cast_6753, parameter_1190)

      generate_shape_67540, = call(self.generate_shape_6754, matmul_8120)

      expand_67550, = call(self.expand_6755, cast_67530, generate_shape_67540)

      add_67560, = call(self.add_6756, multiply_67520, expand_67550)

      cast_67570, = call(self.cast_6757, add_67560)

      return call(self.yield_6759, cast_67570)

    return ret_lambda

    

  def fusion_6769_block00(self, call, matmul_8230, parameter_1220, fusion_67580):

    def ret_lambda():

      generate_shape_67600, = call(self.generate_shape_6760, matmul_8230)

      expand_67610, = call(self.expand_6761, parameter_1220, generate_shape_67600)

      add_67620, = call(self.add_6762, matmul_8230, expand_67610)

      scale_67630, = call(self.scale_6763, add_67620)

      generate_shape_67640, = call(self.generate_shape_6764, fusion_67580)

      reshape_67650, reshape_67651, = call(self.reshape_6765, scale_67630, generate_shape_67640)

      transpose_67660, = call(self.transpose_6766, reshape_67650)

      generate_shape_67670, = call(self.generate_shape_6767, fusion_67580)

      reshape_67680, reshape_67681, = call(self.reshape_6768, transpose_67660, generate_shape_67670)

      return call(self.yield_6770, reshape_67680)

    return ret_lambda

    

  def fusion_6779_block00(self, call, matmul_8270, parameter_1240, fusion_67580):

    def ret_lambda():

      generate_shape_67710, = call(self.generate_shape_6771, matmul_8270)

      expand_67720, = call(self.expand_6772, parameter_1240, generate_shape_67710)

      add_67730, = call(self.add_6773, matmul_8270, expand_67720)

      generate_shape_67740, = call(self.generate_shape_6774, fusion_67580)

      reshape_67750, reshape_67751, = call(self.reshape_6775, add_67730, generate_shape_67740)

      transpose_67760, = call(self.transpose_6776, reshape_67750)

      generate_shape_67770, = call(self.generate_shape_6777, fusion_67580)

      reshape_67780, reshape_67781, = call(self.reshape_6778, transpose_67760, generate_shape_67770)

      return call(self.yield_6780, reshape_67780)

    return ret_lambda

    

  def fusion_6789_block00(self, call, matmul_8350, parameter_1260, fusion_67580):

    def ret_lambda():

      generate_shape_67810, = call(self.generate_shape_6781, matmul_8350)

      expand_67820, = call(self.expand_6782, parameter_1260, generate_shape_67810)

      add_67830, = call(self.add_6783, matmul_8350, expand_67820)

      generate_shape_67840, = call(self.generate_shape_6784, fusion_67580)

      reshape_67850, reshape_67851, = call(self.reshape_6785, add_67830, generate_shape_67840)

      transpose_67860, = call(self.transpose_6786, reshape_67850)

      generate_shape_67870, = call(self.generate_shape_6787, fusion_67580)

      reshape_67880, reshape_67881, = call(self.reshape_6788, transpose_67860, generate_shape_67870)

      return call(self.yield_6790, reshape_67880)

    return ret_lambda

    

  def fusion_6798_block00(self, call, fusion_67580, fusion_67790, matmul_8660, triu_2330):

    def ret_lambda():

      generate_shape_67910, = call(self.generate_shape_6791, fusion_67580, fusion_67790)

      reshape_67920, reshape_67921, = call(self.reshape_6792, matmul_8660, generate_shape_67910)

      generate_shape_67930, = call(self.generate_shape_6793, fusion_67580)

      expand_67940, = call(self.expand_6794, triu_2330, generate_shape_67930)

      add_67950, = call(self.add_6795, reshape_67920, expand_67940)

      generate_shape_67960, = call(self.generate_shape_6796, fusion_67580, fusion_67790)

      reshape_67970, reshape_67971, = call(self.reshape_6797, add_67950, generate_shape_67960)

      return call(self.yield_6799, reshape_67970)

    return ret_lambda

    

  def fusion_6805_block00(self, call, fusion_67580, matmul_8760):

    def ret_lambda():

      generate_shape_68000, = call(self.generate_shape_6800, fusion_67580)

      reshape_68010, reshape_68011, = call(self.reshape_6801, matmul_8760, generate_shape_68000)

      transpose_68020, = call(self.transpose_6802, reshape_68010)

      generate_shape_68030, = call(self.generate_shape_6803, fusion_67580)

      reshape_68040, reshape_68041, = call(self.reshape_6804, transpose_68020, generate_shape_68030)

      return call(self.yield_6806, reshape_68040)

    return ret_lambda

    

  def fusion_6811_block00(self, call, matmul_8850, parameter_1280, fusion_67210):

    def ret_lambda():

      generate_shape_68070, = call(self.generate_shape_6807, matmul_8850)

      expand_68080, = call(self.expand_6808, parameter_1280, generate_shape_68070)

      add_68090, = call(self.add_6809, matmul_8850, expand_68080)

      add_68100, = call(self.add_6810, fusion_67210, add_68090)

      return call(self.yield_6812, add_68100)

    return ret_lambda

    

  def fusion_6815_block00(self, call, fusion_68110):

    def ret_lambda():

      cast_68130, = call(self.cast_6813, fusion_68110)

      reduce_sum_68140, = call(self.reduce_sum_6814, cast_68130)

      return call(self.yield_6816, reduce_sum_68140)

    return ret_lambda

    

  def fusion_6848_block00(self, call, fusion_68110, matmul_8850, fusion_68150, parameter_1300, parameter_1290):

    def ret_lambda():

      cast_68170, = call(self.cast_6817, fusion_68110)

      full_68180, = call(self.full_6818)

      generate_shape_68190, = call(self.generate_shape_6819, matmul_8850)

      expand_68200, = call(self.expand_6820, full_68180, generate_shape_68190)

      divide_68210, = call(self.divide_6821, fusion_68150, expand_68200)

      generate_shape_68220, = call(self.generate_shape_6822, matmul_8850)

      expand_68230, = call(self.expand_6823, divide_68210, generate_shape_68220)

      subtract_68240, = call(self.subtract_6824, cast_68170, expand_68230)

      multiply_68250, = call(self.multiply_6825, subtract_68240, subtract_68240)

      reduce_sum_68260, = call(self.reduce_sum_6826, multiply_68250)

      full_68270, = call(self.full_6827)

      generate_shape_68280, = call(self.generate_shape_6828, matmul_8850)

      expand_68290, = call(self.expand_6829, full_68270, generate_shape_68280)

      divide_68300, = call(self.divide_6830, reduce_sum_68260, expand_68290)

      full_68310, = call(self.full_6831)

      generate_shape_68320, = call(self.generate_shape_6832, matmul_8850)

      expand_68330, = call(self.expand_6833, full_68310, generate_shape_68320)

      add_68340, = call(self.add_6834, divide_68300, expand_68330)

      rsqrt_68350, = call(self.rsqrt_6835, add_68340)

      generate_shape_68360, = call(self.generate_shape_6836, matmul_8850)

      expand_68370, = call(self.expand_6837, rsqrt_68350, generate_shape_68360)

      multiply_68380, = call(self.multiply_6838, subtract_68240, expand_68370)

      cast_68390, = call(self.cast_6839, parameter_1300)

      generate_shape_68400, = call(self.generate_shape_6840, matmul_8850)

      expand_68410, = call(self.expand_6841, cast_68390, generate_shape_68400)

      multiply_68420, = call(self.multiply_6842, multiply_68380, expand_68410)

      cast_68430, = call(self.cast_6843, parameter_1290)

      generate_shape_68440, = call(self.generate_shape_6844, matmul_8850)

      expand_68450, = call(self.expand_6845, cast_68430, generate_shape_68440)

      add_68460, = call(self.add_6846, multiply_68420, expand_68450)

      cast_68470, = call(self.cast_6847, add_68460)

      return call(self.yield_6849, cast_68470)

    return ret_lambda

    

  def fusion_6866_block00(self, call, matmul_8890, parameter_1320):

    def ret_lambda():

      generate_shape_68500, = call(self.generate_shape_6850, matmul_8890)

      expand_68510, = call(self.expand_6851, parameter_1320, generate_shape_68500)

      add_68520, = call(self.add_6852, matmul_8890, expand_68510)

      scale_68530, = call(self.scale_6853, add_68520)

      cast_68540, = call(self.cast_6854, scale_68530)

      full_68550, = call(self.full_6855)

      scale_68560, = call(self.scale_6856, cast_68540)

      exp_68570, = call(self.exp_6857, scale_68560)

      generate_shape_68580, = call(self.generate_shape_6858, matmul_8890)

      expand_68590, = call(self.expand_6859, full_68550, generate_shape_68580)

      add_68600, = call(self.add_6860, expand_68590, exp_68570)

      generate_shape_68610, = call(self.generate_shape_6861, matmul_8890)

      expand_68620, = call(self.expand_6862, full_68550, generate_shape_68610)

      divide_68630, = call(self.divide_6863, expand_68620, add_68600)

      cast_68640, = call(self.cast_6864, divide_68630)

      multiply_68650, = call(self.multiply_6865, add_68520, cast_68640)

      return call(self.yield_6867, multiply_68650)

    return ret_lambda

    

  def fusion_6872_block00(self, call, matmul_8950, parameter_1340, fusion_68110):

    def ret_lambda():

      generate_shape_68680, = call(self.generate_shape_6868, matmul_8950)

      expand_68690, = call(self.expand_6869, parameter_1340, generate_shape_68680)

      add_68700, = call(self.add_6870, matmul_8950, expand_68690)

      add_68710, = call(self.add_6871, fusion_68110, add_68700)

      return call(self.yield_6873, add_68710)

    return ret_lambda

    

  def fusion_6876_block00(self, call, fusion_68720):

    def ret_lambda():

      cast_68740, = call(self.cast_6874, fusion_68720)

      reduce_sum_68750, = call(self.reduce_sum_6875, cast_68740)

      return call(self.yield_6877, reduce_sum_68750)

    return ret_lambda

    

  def fusion_6909_block00(self, call, fusion_68720, matmul_8950, fusion_68760, parameter_1360, parameter_1350):

    def ret_lambda():

      cast_68780, = call(self.cast_6878, fusion_68720)

      full_68790, = call(self.full_6879)

      generate_shape_68800, = call(self.generate_shape_6880, matmul_8950)

      expand_68810, = call(self.expand_6881, full_68790, generate_shape_68800)

      divide_68820, = call(self.divide_6882, fusion_68760, expand_68810)

      generate_shape_68830, = call(self.generate_shape_6883, matmul_8950)

      expand_68840, = call(self.expand_6884, divide_68820, generate_shape_68830)

      subtract_68850, = call(self.subtract_6885, cast_68780, expand_68840)

      multiply_68860, = call(self.multiply_6886, subtract_68850, subtract_68850)

      reduce_sum_68870, = call(self.reduce_sum_6887, multiply_68860)

      full_68880, = call(self.full_6888)

      generate_shape_68890, = call(self.generate_shape_6889, matmul_8950)

      expand_68900, = call(self.expand_6890, full_68880, generate_shape_68890)

      divide_68910, = call(self.divide_6891, reduce_sum_68870, expand_68900)

      full_68920, = call(self.full_6892)

      generate_shape_68930, = call(self.generate_shape_6893, matmul_8950)

      expand_68940, = call(self.expand_6894, full_68920, generate_shape_68930)

      add_68950, = call(self.add_6895, divide_68910, expand_68940)

      rsqrt_68960, = call(self.rsqrt_6896, add_68950)

      generate_shape_68970, = call(self.generate_shape_6897, matmul_8950)

      expand_68980, = call(self.expand_6898, rsqrt_68960, generate_shape_68970)

      multiply_68990, = call(self.multiply_6899, subtract_68850, expand_68980)

      cast_69000, = call(self.cast_6900, parameter_1360)

      generate_shape_69010, = call(self.generate_shape_6901, matmul_8950)

      expand_69020, = call(self.expand_6902, cast_69000, generate_shape_69010)

      multiply_69030, = call(self.multiply_6903, multiply_68990, expand_69020)

      cast_69040, = call(self.cast_6904, parameter_1350)

      generate_shape_69050, = call(self.generate_shape_6905, matmul_8950)

      expand_69060, = call(self.expand_6906, cast_69040, generate_shape_69050)

      add_69070, = call(self.add_6907, multiply_69030, expand_69060)

      cast_69080, = call(self.cast_6908, add_69070)

      return call(self.yield_6910, cast_69080)

    return ret_lambda

    

  def fusion_6920_block00(self, call, matmul_9060, parameter_1380, fusion_69090):

    def ret_lambda():

      generate_shape_69110, = call(self.generate_shape_6911, matmul_9060)

      expand_69120, = call(self.expand_6912, parameter_1380, generate_shape_69110)

      add_69130, = call(self.add_6913, matmul_9060, expand_69120)

      scale_69140, = call(self.scale_6914, add_69130)

      generate_shape_69150, = call(self.generate_shape_6915, fusion_69090)

      reshape_69160, reshape_69161, = call(self.reshape_6916, scale_69140, generate_shape_69150)

      transpose_69170, = call(self.transpose_6917, reshape_69160)

      generate_shape_69180, = call(self.generate_shape_6918, fusion_69090)

      reshape_69190, reshape_69191, = call(self.reshape_6919, transpose_69170, generate_shape_69180)

      return call(self.yield_6921, reshape_69190)

    return ret_lambda

    

  def fusion_6930_block00(self, call, matmul_9100, parameter_1400, fusion_69090):

    def ret_lambda():

      generate_shape_69220, = call(self.generate_shape_6922, matmul_9100)

      expand_69230, = call(self.expand_6923, parameter_1400, generate_shape_69220)

      add_69240, = call(self.add_6924, matmul_9100, expand_69230)

      generate_shape_69250, = call(self.generate_shape_6925, fusion_69090)

      reshape_69260, reshape_69261, = call(self.reshape_6926, add_69240, generate_shape_69250)

      transpose_69270, = call(self.transpose_6927, reshape_69260)

      generate_shape_69280, = call(self.generate_shape_6928, fusion_69090)

      reshape_69290, reshape_69291, = call(self.reshape_6929, transpose_69270, generate_shape_69280)

      return call(self.yield_6931, reshape_69290)

    return ret_lambda

    

  def fusion_6940_block00(self, call, matmul_9180, parameter_1420, fusion_69090):

    def ret_lambda():

      generate_shape_69320, = call(self.generate_shape_6932, matmul_9180)

      expand_69330, = call(self.expand_6933, parameter_1420, generate_shape_69320)

      add_69340, = call(self.add_6934, matmul_9180, expand_69330)

      generate_shape_69350, = call(self.generate_shape_6935, fusion_69090)

      reshape_69360, reshape_69361, = call(self.reshape_6936, add_69340, generate_shape_69350)

      transpose_69370, = call(self.transpose_6937, reshape_69360)

      generate_shape_69380, = call(self.generate_shape_6938, fusion_69090)

      reshape_69390, reshape_69391, = call(self.reshape_6939, transpose_69370, generate_shape_69380)

      return call(self.yield_6941, reshape_69390)

    return ret_lambda

    

  def fusion_6949_block00(self, call, fusion_69090, fusion_69300, matmul_9490, triu_2330):

    def ret_lambda():

      generate_shape_69420, = call(self.generate_shape_6942, fusion_69090, fusion_69300)

      reshape_69430, reshape_69431, = call(self.reshape_6943, matmul_9490, generate_shape_69420)

      generate_shape_69440, = call(self.generate_shape_6944, fusion_69090)

      expand_69450, = call(self.expand_6945, triu_2330, generate_shape_69440)

      add_69460, = call(self.add_6946, reshape_69430, expand_69450)

      generate_shape_69470, = call(self.generate_shape_6947, fusion_69090, fusion_69300)

      reshape_69480, reshape_69481, = call(self.reshape_6948, add_69460, generate_shape_69470)

      return call(self.yield_6950, reshape_69480)

    return ret_lambda

    

  def fusion_6956_block00(self, call, fusion_69090, matmul_9590):

    def ret_lambda():

      generate_shape_69510, = call(self.generate_shape_6951, fusion_69090)

      reshape_69520, reshape_69521, = call(self.reshape_6952, matmul_9590, generate_shape_69510)

      transpose_69530, = call(self.transpose_6953, reshape_69520)

      generate_shape_69540, = call(self.generate_shape_6954, fusion_69090)

      reshape_69550, reshape_69551, = call(self.reshape_6955, transpose_69530, generate_shape_69540)

      return call(self.yield_6957, reshape_69550)

    return ret_lambda

    

  def fusion_6962_block00(self, call, matmul_9680, parameter_1440, fusion_68720):

    def ret_lambda():

      generate_shape_69580, = call(self.generate_shape_6958, matmul_9680)

      expand_69590, = call(self.expand_6959, parameter_1440, generate_shape_69580)

      add_69600, = call(self.add_6960, matmul_9680, expand_69590)

      add_69610, = call(self.add_6961, fusion_68720, add_69600)

      return call(self.yield_6963, add_69610)

    return ret_lambda

    

  def fusion_6966_block00(self, call, fusion_69620):

    def ret_lambda():

      cast_69640, = call(self.cast_6964, fusion_69620)

      reduce_sum_69650, = call(self.reduce_sum_6965, cast_69640)

      return call(self.yield_6967, reduce_sum_69650)

    return ret_lambda

    

  def fusion_6999_block00(self, call, fusion_69620, matmul_9680, fusion_69660, parameter_1460, parameter_1450):

    def ret_lambda():

      cast_69680, = call(self.cast_6968, fusion_69620)

      full_69690, = call(self.full_6969)

      generate_shape_69700, = call(self.generate_shape_6970, matmul_9680)

      expand_69710, = call(self.expand_6971, full_69690, generate_shape_69700)

      divide_69720, = call(self.divide_6972, fusion_69660, expand_69710)

      generate_shape_69730, = call(self.generate_shape_6973, matmul_9680)

      expand_69740, = call(self.expand_6974, divide_69720, generate_shape_69730)

      subtract_69750, = call(self.subtract_6975, cast_69680, expand_69740)

      multiply_69760, = call(self.multiply_6976, subtract_69750, subtract_69750)

      reduce_sum_69770, = call(self.reduce_sum_6977, multiply_69760)

      full_69780, = call(self.full_6978)

      generate_shape_69790, = call(self.generate_shape_6979, matmul_9680)

      expand_69800, = call(self.expand_6980, full_69780, generate_shape_69790)

      divide_69810, = call(self.divide_6981, reduce_sum_69770, expand_69800)

      full_69820, = call(self.full_6982)

      generate_shape_69830, = call(self.generate_shape_6983, matmul_9680)

      expand_69840, = call(self.expand_6984, full_69820, generate_shape_69830)

      add_69850, = call(self.add_6985, divide_69810, expand_69840)

      rsqrt_69860, = call(self.rsqrt_6986, add_69850)

      generate_shape_69870, = call(self.generate_shape_6987, matmul_9680)

      expand_69880, = call(self.expand_6988, rsqrt_69860, generate_shape_69870)

      multiply_69890, = call(self.multiply_6989, subtract_69750, expand_69880)

      cast_69900, = call(self.cast_6990, parameter_1460)

      generate_shape_69910, = call(self.generate_shape_6991, matmul_9680)

      expand_69920, = call(self.expand_6992, cast_69900, generate_shape_69910)

      multiply_69930, = call(self.multiply_6993, multiply_69890, expand_69920)

      cast_69940, = call(self.cast_6994, parameter_1450)

      generate_shape_69950, = call(self.generate_shape_6995, matmul_9680)

      expand_69960, = call(self.expand_6996, cast_69940, generate_shape_69950)

      add_69970, = call(self.add_6997, multiply_69930, expand_69960)

      cast_69980, = call(self.cast_6998, add_69970)

      return call(self.yield_7000, cast_69980)

    return ret_lambda

    

  def fusion_7017_block00(self, call, matmul_9720, parameter_1480):

    def ret_lambda():

      generate_shape_70010, = call(self.generate_shape_7001, matmul_9720)

      expand_70020, = call(self.expand_7002, parameter_1480, generate_shape_70010)

      add_70030, = call(self.add_7003, matmul_9720, expand_70020)

      scale_70040, = call(self.scale_7004, add_70030)

      cast_70050, = call(self.cast_7005, scale_70040)

      full_70060, = call(self.full_7006)

      scale_70070, = call(self.scale_7007, cast_70050)

      exp_70080, = call(self.exp_7008, scale_70070)

      generate_shape_70090, = call(self.generate_shape_7009, matmul_9720)

      expand_70100, = call(self.expand_7010, full_70060, generate_shape_70090)

      add_70110, = call(self.add_7011, expand_70100, exp_70080)

      generate_shape_70120, = call(self.generate_shape_7012, matmul_9720)

      expand_70130, = call(self.expand_7013, full_70060, generate_shape_70120)

      divide_70140, = call(self.divide_7014, expand_70130, add_70110)

      cast_70150, = call(self.cast_7015, divide_70140)

      multiply_70160, = call(self.multiply_7016, add_70030, cast_70150)

      return call(self.yield_7018, multiply_70160)

    return ret_lambda

    

  def fusion_7023_block00(self, call, matmul_9780, parameter_1500, fusion_69620):

    def ret_lambda():

      generate_shape_70190, = call(self.generate_shape_7019, matmul_9780)

      expand_70200, = call(self.expand_7020, parameter_1500, generate_shape_70190)

      add_70210, = call(self.add_7021, matmul_9780, expand_70200)

      add_70220, = call(self.add_7022, fusion_69620, add_70210)

      return call(self.yield_7024, add_70220)

    return ret_lambda

    

  def fusion_7027_block00(self, call, fusion_70230):

    def ret_lambda():

      cast_70250, = call(self.cast_7025, fusion_70230)

      reduce_sum_70260, = call(self.reduce_sum_7026, cast_70250)

      return call(self.yield_7028, reduce_sum_70260)

    return ret_lambda

    

  def fusion_7060_block00(self, call, fusion_70230, matmul_9780, fusion_70270, parameter_1520, parameter_1510):

    def ret_lambda():

      cast_70290, = call(self.cast_7029, fusion_70230)

      full_70300, = call(self.full_7030)

      generate_shape_70310, = call(self.generate_shape_7031, matmul_9780)

      expand_70320, = call(self.expand_7032, full_70300, generate_shape_70310)

      divide_70330, = call(self.divide_7033, fusion_70270, expand_70320)

      generate_shape_70340, = call(self.generate_shape_7034, matmul_9780)

      expand_70350, = call(self.expand_7035, divide_70330, generate_shape_70340)

      subtract_70360, = call(self.subtract_7036, cast_70290, expand_70350)

      multiply_70370, = call(self.multiply_7037, subtract_70360, subtract_70360)

      reduce_sum_70380, = call(self.reduce_sum_7038, multiply_70370)

      full_70390, = call(self.full_7039)

      generate_shape_70400, = call(self.generate_shape_7040, matmul_9780)

      expand_70410, = call(self.expand_7041, full_70390, generate_shape_70400)

      divide_70420, = call(self.divide_7042, reduce_sum_70380, expand_70410)

      full_70430, = call(self.full_7043)

      generate_shape_70440, = call(self.generate_shape_7044, matmul_9780)

      expand_70450, = call(self.expand_7045, full_70430, generate_shape_70440)

      add_70460, = call(self.add_7046, divide_70420, expand_70450)

      rsqrt_70470, = call(self.rsqrt_7047, add_70460)

      generate_shape_70480, = call(self.generate_shape_7048, matmul_9780)

      expand_70490, = call(self.expand_7049, rsqrt_70470, generate_shape_70480)

      multiply_70500, = call(self.multiply_7050, subtract_70360, expand_70490)

      cast_70510, = call(self.cast_7051, parameter_1520)

      generate_shape_70520, = call(self.generate_shape_7052, matmul_9780)

      expand_70530, = call(self.expand_7053, cast_70510, generate_shape_70520)

      multiply_70540, = call(self.multiply_7054, multiply_70500, expand_70530)

      cast_70550, = call(self.cast_7055, parameter_1510)

      generate_shape_70560, = call(self.generate_shape_7056, matmul_9780)

      expand_70570, = call(self.expand_7057, cast_70550, generate_shape_70560)

      add_70580, = call(self.add_7058, multiply_70540, expand_70570)

      cast_70590, = call(self.cast_7059, add_70580)

      return call(self.yield_7061, cast_70590)

    return ret_lambda

    

  def fusion_7071_block00(self, call, matmul_9890, parameter_1540, fusion_70600):

    def ret_lambda():

      generate_shape_70620, = call(self.generate_shape_7062, matmul_9890)

      expand_70630, = call(self.expand_7063, parameter_1540, generate_shape_70620)

      add_70640, = call(self.add_7064, matmul_9890, expand_70630)

      scale_70650, = call(self.scale_7065, add_70640)

      generate_shape_70660, = call(self.generate_shape_7066, fusion_70600)

      reshape_70670, reshape_70671, = call(self.reshape_7067, scale_70650, generate_shape_70660)

      transpose_70680, = call(self.transpose_7068, reshape_70670)

      generate_shape_70690, = call(self.generate_shape_7069, fusion_70600)

      reshape_70700, reshape_70701, = call(self.reshape_7070, transpose_70680, generate_shape_70690)

      return call(self.yield_7072, reshape_70700)

    return ret_lambda

    

  def fusion_7081_block00(self, call, matmul_9930, parameter_1560, fusion_70600):

    def ret_lambda():

      generate_shape_70730, = call(self.generate_shape_7073, matmul_9930)

      expand_70740, = call(self.expand_7074, parameter_1560, generate_shape_70730)

      add_70750, = call(self.add_7075, matmul_9930, expand_70740)

      generate_shape_70760, = call(self.generate_shape_7076, fusion_70600)

      reshape_70770, reshape_70771, = call(self.reshape_7077, add_70750, generate_shape_70760)

      transpose_70780, = call(self.transpose_7078, reshape_70770)

      generate_shape_70790, = call(self.generate_shape_7079, fusion_70600)

      reshape_70800, reshape_70801, = call(self.reshape_7080, transpose_70780, generate_shape_70790)

      return call(self.yield_7082, reshape_70800)

    return ret_lambda

    

  def fusion_7091_block00(self, call, matmul_10010, parameter_1580, fusion_70600):

    def ret_lambda():

      generate_shape_70830, = call(self.generate_shape_7083, matmul_10010)

      expand_70840, = call(self.expand_7084, parameter_1580, generate_shape_70830)

      add_70850, = call(self.add_7085, matmul_10010, expand_70840)

      generate_shape_70860, = call(self.generate_shape_7086, fusion_70600)

      reshape_70870, reshape_70871, = call(self.reshape_7087, add_70850, generate_shape_70860)

      transpose_70880, = call(self.transpose_7088, reshape_70870)

      generate_shape_70890, = call(self.generate_shape_7089, fusion_70600)

      reshape_70900, reshape_70901, = call(self.reshape_7090, transpose_70880, generate_shape_70890)

      return call(self.yield_7092, reshape_70900)

    return ret_lambda

    

  def fusion_7100_block00(self, call, fusion_70600, fusion_70810, matmul_10320, triu_2330):

    def ret_lambda():

      generate_shape_70930, = call(self.generate_shape_7093, fusion_70600, fusion_70810)

      reshape_70940, reshape_70941, = call(self.reshape_7094, matmul_10320, generate_shape_70930)

      generate_shape_70950, = call(self.generate_shape_7095, fusion_70600)

      expand_70960, = call(self.expand_7096, triu_2330, generate_shape_70950)

      add_70970, = call(self.add_7097, reshape_70940, expand_70960)

      generate_shape_70980, = call(self.generate_shape_7098, fusion_70600, fusion_70810)

      reshape_70990, reshape_70991, = call(self.reshape_7099, add_70970, generate_shape_70980)

      return call(self.yield_7101, reshape_70990)

    return ret_lambda

    

  def fusion_7107_block00(self, call, fusion_70600, matmul_10420):

    def ret_lambda():

      generate_shape_71020, = call(self.generate_shape_7102, fusion_70600)

      reshape_71030, reshape_71031, = call(self.reshape_7103, matmul_10420, generate_shape_71020)

      transpose_71040, = call(self.transpose_7104, reshape_71030)

      generate_shape_71050, = call(self.generate_shape_7105, fusion_70600)

      reshape_71060, reshape_71061, = call(self.reshape_7106, transpose_71040, generate_shape_71050)

      return call(self.yield_7108, reshape_71060)

    return ret_lambda

    

  def fusion_7113_block00(self, call, matmul_10510, parameter_1600, fusion_70230):

    def ret_lambda():

      generate_shape_71090, = call(self.generate_shape_7109, matmul_10510)

      expand_71100, = call(self.expand_7110, parameter_1600, generate_shape_71090)

      add_71110, = call(self.add_7111, matmul_10510, expand_71100)

      add_71120, = call(self.add_7112, fusion_70230, add_71110)

      return call(self.yield_7114, add_71120)

    return ret_lambda

    

  def fusion_7117_block00(self, call, fusion_71130):

    def ret_lambda():

      cast_71150, = call(self.cast_7115, fusion_71130)

      reduce_sum_71160, = call(self.reduce_sum_7116, cast_71150)

      return call(self.yield_7118, reduce_sum_71160)

    return ret_lambda

    

  def fusion_7150_block00(self, call, fusion_71130, matmul_10510, fusion_71170, parameter_1620, parameter_1610):

    def ret_lambda():

      cast_71190, = call(self.cast_7119, fusion_71130)

      full_71200, = call(self.full_7120)

      generate_shape_71210, = call(self.generate_shape_7121, matmul_10510)

      expand_71220, = call(self.expand_7122, full_71200, generate_shape_71210)

      divide_71230, = call(self.divide_7123, fusion_71170, expand_71220)

      generate_shape_71240, = call(self.generate_shape_7124, matmul_10510)

      expand_71250, = call(self.expand_7125, divide_71230, generate_shape_71240)

      subtract_71260, = call(self.subtract_7126, cast_71190, expand_71250)

      multiply_71270, = call(self.multiply_7127, subtract_71260, subtract_71260)

      reduce_sum_71280, = call(self.reduce_sum_7128, multiply_71270)

      full_71290, = call(self.full_7129)

      generate_shape_71300, = call(self.generate_shape_7130, matmul_10510)

      expand_71310, = call(self.expand_7131, full_71290, generate_shape_71300)

      divide_71320, = call(self.divide_7132, reduce_sum_71280, expand_71310)

      full_71330, = call(self.full_7133)

      generate_shape_71340, = call(self.generate_shape_7134, matmul_10510)

      expand_71350, = call(self.expand_7135, full_71330, generate_shape_71340)

      add_71360, = call(self.add_7136, divide_71320, expand_71350)

      rsqrt_71370, = call(self.rsqrt_7137, add_71360)

      generate_shape_71380, = call(self.generate_shape_7138, matmul_10510)

      expand_71390, = call(self.expand_7139, rsqrt_71370, generate_shape_71380)

      multiply_71400, = call(self.multiply_7140, subtract_71260, expand_71390)

      cast_71410, = call(self.cast_7141, parameter_1620)

      generate_shape_71420, = call(self.generate_shape_7142, matmul_10510)

      expand_71430, = call(self.expand_7143, cast_71410, generate_shape_71420)

      multiply_71440, = call(self.multiply_7144, multiply_71400, expand_71430)

      cast_71450, = call(self.cast_7145, parameter_1610)

      generate_shape_71460, = call(self.generate_shape_7146, matmul_10510)

      expand_71470, = call(self.expand_7147, cast_71450, generate_shape_71460)

      add_71480, = call(self.add_7148, multiply_71440, expand_71470)

      cast_71490, = call(self.cast_7149, add_71480)

      return call(self.yield_7151, cast_71490)

    return ret_lambda

    

  def fusion_7168_block00(self, call, matmul_10550, parameter_1640):

    def ret_lambda():

      generate_shape_71520, = call(self.generate_shape_7152, matmul_10550)

      expand_71530, = call(self.expand_7153, parameter_1640, generate_shape_71520)

      add_71540, = call(self.add_7154, matmul_10550, expand_71530)

      scale_71550, = call(self.scale_7155, add_71540)

      cast_71560, = call(self.cast_7156, scale_71550)

      full_71570, = call(self.full_7157)

      scale_71580, = call(self.scale_7158, cast_71560)

      exp_71590, = call(self.exp_7159, scale_71580)

      generate_shape_71600, = call(self.generate_shape_7160, matmul_10550)

      expand_71610, = call(self.expand_7161, full_71570, generate_shape_71600)

      add_71620, = call(self.add_7162, expand_71610, exp_71590)

      generate_shape_71630, = call(self.generate_shape_7163, matmul_10550)

      expand_71640, = call(self.expand_7164, full_71570, generate_shape_71630)

      divide_71650, = call(self.divide_7165, expand_71640, add_71620)

      cast_71660, = call(self.cast_7166, divide_71650)

      multiply_71670, = call(self.multiply_7167, add_71540, cast_71660)

      return call(self.yield_7169, multiply_71670)

    return ret_lambda

    

  def fusion_7174_block00(self, call, matmul_10610, parameter_1660, fusion_71130):

    def ret_lambda():

      generate_shape_71700, = call(self.generate_shape_7170, matmul_10610)

      expand_71710, = call(self.expand_7171, parameter_1660, generate_shape_71700)

      add_71720, = call(self.add_7172, matmul_10610, expand_71710)

      add_71730, = call(self.add_7173, fusion_71130, add_71720)

      return call(self.yield_7175, add_71730)

    return ret_lambda

    

  def fusion_7178_block00(self, call, fusion_71740):

    def ret_lambda():

      cast_71760, = call(self.cast_7176, fusion_71740)

      reduce_sum_71770, = call(self.reduce_sum_7177, cast_71760)

      return call(self.yield_7179, reduce_sum_71770)

    return ret_lambda

    

  def fusion_7211_block00(self, call, fusion_71740, matmul_10610, fusion_71780, parameter_1680, parameter_1670):

    def ret_lambda():

      cast_71800, = call(self.cast_7180, fusion_71740)

      full_71810, = call(self.full_7181)

      generate_shape_71820, = call(self.generate_shape_7182, matmul_10610)

      expand_71830, = call(self.expand_7183, full_71810, generate_shape_71820)

      divide_71840, = call(self.divide_7184, fusion_71780, expand_71830)

      generate_shape_71850, = call(self.generate_shape_7185, matmul_10610)

      expand_71860, = call(self.expand_7186, divide_71840, generate_shape_71850)

      subtract_71870, = call(self.subtract_7187, cast_71800, expand_71860)

      multiply_71880, = call(self.multiply_7188, subtract_71870, subtract_71870)

      reduce_sum_71890, = call(self.reduce_sum_7189, multiply_71880)

      full_71900, = call(self.full_7190)

      generate_shape_71910, = call(self.generate_shape_7191, matmul_10610)

      expand_71920, = call(self.expand_7192, full_71900, generate_shape_71910)

      divide_71930, = call(self.divide_7193, reduce_sum_71890, expand_71920)

      full_71940, = call(self.full_7194)

      generate_shape_71950, = call(self.generate_shape_7195, matmul_10610)

      expand_71960, = call(self.expand_7196, full_71940, generate_shape_71950)

      add_71970, = call(self.add_7197, divide_71930, expand_71960)

      rsqrt_71980, = call(self.rsqrt_7198, add_71970)

      generate_shape_71990, = call(self.generate_shape_7199, matmul_10610)

      expand_72000, = call(self.expand_7200, rsqrt_71980, generate_shape_71990)

      multiply_72010, = call(self.multiply_7201, subtract_71870, expand_72000)

      cast_72020, = call(self.cast_7202, parameter_1680)

      generate_shape_72030, = call(self.generate_shape_7203, matmul_10610)

      expand_72040, = call(self.expand_7204, cast_72020, generate_shape_72030)

      multiply_72050, = call(self.multiply_7205, multiply_72010, expand_72040)

      cast_72060, = call(self.cast_7206, parameter_1670)

      generate_shape_72070, = call(self.generate_shape_7207, matmul_10610)

      expand_72080, = call(self.expand_7208, cast_72060, generate_shape_72070)

      add_72090, = call(self.add_7209, multiply_72050, expand_72080)

      cast_72100, = call(self.cast_7210, add_72090)

      return call(self.yield_7212, cast_72100)

    return ret_lambda

    

  def fusion_7222_block00(self, call, matmul_10720, parameter_1700, fusion_72110):

    def ret_lambda():

      generate_shape_72130, = call(self.generate_shape_7213, matmul_10720)

      expand_72140, = call(self.expand_7214, parameter_1700, generate_shape_72130)

      add_72150, = call(self.add_7215, matmul_10720, expand_72140)

      scale_72160, = call(self.scale_7216, add_72150)

      generate_shape_72170, = call(self.generate_shape_7217, fusion_72110)

      reshape_72180, reshape_72181, = call(self.reshape_7218, scale_72160, generate_shape_72170)

      transpose_72190, = call(self.transpose_7219, reshape_72180)

      generate_shape_72200, = call(self.generate_shape_7220, fusion_72110)

      reshape_72210, reshape_72211, = call(self.reshape_7221, transpose_72190, generate_shape_72200)

      return call(self.yield_7223, reshape_72210)

    return ret_lambda

    

  def fusion_7232_block00(self, call, matmul_10760, parameter_1720, fusion_72110):

    def ret_lambda():

      generate_shape_72240, = call(self.generate_shape_7224, matmul_10760)

      expand_72250, = call(self.expand_7225, parameter_1720, generate_shape_72240)

      add_72260, = call(self.add_7226, matmul_10760, expand_72250)

      generate_shape_72270, = call(self.generate_shape_7227, fusion_72110)

      reshape_72280, reshape_72281, = call(self.reshape_7228, add_72260, generate_shape_72270)

      transpose_72290, = call(self.transpose_7229, reshape_72280)

      generate_shape_72300, = call(self.generate_shape_7230, fusion_72110)

      reshape_72310, reshape_72311, = call(self.reshape_7231, transpose_72290, generate_shape_72300)

      return call(self.yield_7233, reshape_72310)

    return ret_lambda

    

  def fusion_7242_block00(self, call, matmul_10840, parameter_1740, fusion_72110):

    def ret_lambda():

      generate_shape_72340, = call(self.generate_shape_7234, matmul_10840)

      expand_72350, = call(self.expand_7235, parameter_1740, generate_shape_72340)

      add_72360, = call(self.add_7236, matmul_10840, expand_72350)

      generate_shape_72370, = call(self.generate_shape_7237, fusion_72110)

      reshape_72380, reshape_72381, = call(self.reshape_7238, add_72360, generate_shape_72370)

      transpose_72390, = call(self.transpose_7239, reshape_72380)

      generate_shape_72400, = call(self.generate_shape_7240, fusion_72110)

      reshape_72410, reshape_72411, = call(self.reshape_7241, transpose_72390, generate_shape_72400)

      return call(self.yield_7243, reshape_72410)

    return ret_lambda

    

  def fusion_7251_block00(self, call, fusion_72110, fusion_72320, matmul_11150, triu_2330):

    def ret_lambda():

      generate_shape_72440, = call(self.generate_shape_7244, fusion_72110, fusion_72320)

      reshape_72450, reshape_72451, = call(self.reshape_7245, matmul_11150, generate_shape_72440)

      generate_shape_72460, = call(self.generate_shape_7246, fusion_72110)

      expand_72470, = call(self.expand_7247, triu_2330, generate_shape_72460)

      add_72480, = call(self.add_7248, reshape_72450, expand_72470)

      generate_shape_72490, = call(self.generate_shape_7249, fusion_72110, fusion_72320)

      reshape_72500, reshape_72501, = call(self.reshape_7250, add_72480, generate_shape_72490)

      return call(self.yield_7252, reshape_72500)

    return ret_lambda

    

  def fusion_7258_block00(self, call, fusion_72110, matmul_11250):

    def ret_lambda():

      generate_shape_72530, = call(self.generate_shape_7253, fusion_72110)

      reshape_72540, reshape_72541, = call(self.reshape_7254, matmul_11250, generate_shape_72530)

      transpose_72550, = call(self.transpose_7255, reshape_72540)

      generate_shape_72560, = call(self.generate_shape_7256, fusion_72110)

      reshape_72570, reshape_72571, = call(self.reshape_7257, transpose_72550, generate_shape_72560)

      return call(self.yield_7259, reshape_72570)

    return ret_lambda

    

  def fusion_7264_block00(self, call, matmul_11340, parameter_1760, fusion_71740):

    def ret_lambda():

      generate_shape_72600, = call(self.generate_shape_7260, matmul_11340)

      expand_72610, = call(self.expand_7261, parameter_1760, generate_shape_72600)

      add_72620, = call(self.add_7262, matmul_11340, expand_72610)

      add_72630, = call(self.add_7263, fusion_71740, add_72620)

      return call(self.yield_7265, add_72630)

    return ret_lambda

    

  def fusion_7268_block00(self, call, fusion_72640):

    def ret_lambda():

      cast_72660, = call(self.cast_7266, fusion_72640)

      reduce_sum_72670, = call(self.reduce_sum_7267, cast_72660)

      return call(self.yield_7269, reduce_sum_72670)

    return ret_lambda

    

  def fusion_7301_block00(self, call, fusion_72640, matmul_11340, fusion_72680, parameter_1780, parameter_1770):

    def ret_lambda():

      cast_72700, = call(self.cast_7270, fusion_72640)

      full_72710, = call(self.full_7271)

      generate_shape_72720, = call(self.generate_shape_7272, matmul_11340)

      expand_72730, = call(self.expand_7273, full_72710, generate_shape_72720)

      divide_72740, = call(self.divide_7274, fusion_72680, expand_72730)

      generate_shape_72750, = call(self.generate_shape_7275, matmul_11340)

      expand_72760, = call(self.expand_7276, divide_72740, generate_shape_72750)

      subtract_72770, = call(self.subtract_7277, cast_72700, expand_72760)

      multiply_72780, = call(self.multiply_7278, subtract_72770, subtract_72770)

      reduce_sum_72790, = call(self.reduce_sum_7279, multiply_72780)

      full_72800, = call(self.full_7280)

      generate_shape_72810, = call(self.generate_shape_7281, matmul_11340)

      expand_72820, = call(self.expand_7282, full_72800, generate_shape_72810)

      divide_72830, = call(self.divide_7283, reduce_sum_72790, expand_72820)

      full_72840, = call(self.full_7284)

      generate_shape_72850, = call(self.generate_shape_7285, matmul_11340)

      expand_72860, = call(self.expand_7286, full_72840, generate_shape_72850)

      add_72870, = call(self.add_7287, divide_72830, expand_72860)

      rsqrt_72880, = call(self.rsqrt_7288, add_72870)

      generate_shape_72890, = call(self.generate_shape_7289, matmul_11340)

      expand_72900, = call(self.expand_7290, rsqrt_72880, generate_shape_72890)

      multiply_72910, = call(self.multiply_7291, subtract_72770, expand_72900)

      cast_72920, = call(self.cast_7292, parameter_1780)

      generate_shape_72930, = call(self.generate_shape_7293, matmul_11340)

      expand_72940, = call(self.expand_7294, cast_72920, generate_shape_72930)

      multiply_72950, = call(self.multiply_7295, multiply_72910, expand_72940)

      cast_72960, = call(self.cast_7296, parameter_1770)

      generate_shape_72970, = call(self.generate_shape_7297, matmul_11340)

      expand_72980, = call(self.expand_7298, cast_72960, generate_shape_72970)

      add_72990, = call(self.add_7299, multiply_72950, expand_72980)

      cast_73000, = call(self.cast_7300, add_72990)

      return call(self.yield_7302, cast_73000)

    return ret_lambda

    

  def fusion_7319_block00(self, call, matmul_11380, parameter_1800):

    def ret_lambda():

      generate_shape_73030, = call(self.generate_shape_7303, matmul_11380)

      expand_73040, = call(self.expand_7304, parameter_1800, generate_shape_73030)

      add_73050, = call(self.add_7305, matmul_11380, expand_73040)

      scale_73060, = call(self.scale_7306, add_73050)

      cast_73070, = call(self.cast_7307, scale_73060)

      full_73080, = call(self.full_7308)

      scale_73090, = call(self.scale_7309, cast_73070)

      exp_73100, = call(self.exp_7310, scale_73090)

      generate_shape_73110, = call(self.generate_shape_7311, matmul_11380)

      expand_73120, = call(self.expand_7312, full_73080, generate_shape_73110)

      add_73130, = call(self.add_7313, expand_73120, exp_73100)

      generate_shape_73140, = call(self.generate_shape_7314, matmul_11380)

      expand_73150, = call(self.expand_7315, full_73080, generate_shape_73140)

      divide_73160, = call(self.divide_7316, expand_73150, add_73130)

      cast_73170, = call(self.cast_7317, divide_73160)

      multiply_73180, = call(self.multiply_7318, add_73050, cast_73170)

      return call(self.yield_7320, multiply_73180)

    return ret_lambda

    

  def fusion_7325_block00(self, call, matmul_11440, parameter_1820, fusion_72640):

    def ret_lambda():

      generate_shape_73210, = call(self.generate_shape_7321, matmul_11440)

      expand_73220, = call(self.expand_7322, parameter_1820, generate_shape_73210)

      add_73230, = call(self.add_7323, matmul_11440, expand_73220)

      add_73240, = call(self.add_7324, fusion_72640, add_73230)

      return call(self.yield_7326, add_73240)

    return ret_lambda

    

  def fusion_7329_block00(self, call, fusion_73250):

    def ret_lambda():

      cast_73270, = call(self.cast_7327, fusion_73250)

      reduce_sum_73280, = call(self.reduce_sum_7328, cast_73270)

      return call(self.yield_7330, reduce_sum_73280)

    return ret_lambda

    

  def fusion_7362_block00(self, call, fusion_73250, matmul_11440, fusion_73290, parameter_1840, parameter_1830):

    def ret_lambda():

      cast_73310, = call(self.cast_7331, fusion_73250)

      full_73320, = call(self.full_7332)

      generate_shape_73330, = call(self.generate_shape_7333, matmul_11440)

      expand_73340, = call(self.expand_7334, full_73320, generate_shape_73330)

      divide_73350, = call(self.divide_7335, fusion_73290, expand_73340)

      generate_shape_73360, = call(self.generate_shape_7336, matmul_11440)

      expand_73370, = call(self.expand_7337, divide_73350, generate_shape_73360)

      subtract_73380, = call(self.subtract_7338, cast_73310, expand_73370)

      multiply_73390, = call(self.multiply_7339, subtract_73380, subtract_73380)

      reduce_sum_73400, = call(self.reduce_sum_7340, multiply_73390)

      full_73410, = call(self.full_7341)

      generate_shape_73420, = call(self.generate_shape_7342, matmul_11440)

      expand_73430, = call(self.expand_7343, full_73410, generate_shape_73420)

      divide_73440, = call(self.divide_7344, reduce_sum_73400, expand_73430)

      full_73450, = call(self.full_7345)

      generate_shape_73460, = call(self.generate_shape_7346, matmul_11440)

      expand_73470, = call(self.expand_7347, full_73450, generate_shape_73460)

      add_73480, = call(self.add_7348, divide_73440, expand_73470)

      rsqrt_73490, = call(self.rsqrt_7349, add_73480)

      generate_shape_73500, = call(self.generate_shape_7350, matmul_11440)

      expand_73510, = call(self.expand_7351, rsqrt_73490, generate_shape_73500)

      multiply_73520, = call(self.multiply_7352, subtract_73380, expand_73510)

      cast_73530, = call(self.cast_7353, parameter_1840)

      generate_shape_73540, = call(self.generate_shape_7354, matmul_11440)

      expand_73550, = call(self.expand_7355, cast_73530, generate_shape_73540)

      multiply_73560, = call(self.multiply_7356, multiply_73520, expand_73550)

      cast_73570, = call(self.cast_7357, parameter_1830)

      generate_shape_73580, = call(self.generate_shape_7358, matmul_11440)

      expand_73590, = call(self.expand_7359, cast_73570, generate_shape_73580)

      add_73600, = call(self.add_7360, multiply_73560, expand_73590)

      cast_73610, = call(self.cast_7361, add_73600)

      return call(self.yield_7363, cast_73610)

    return ret_lambda

    

  def fusion_7373_block00(self, call, matmul_11550, parameter_1860, fusion_73620):

    def ret_lambda():

      generate_shape_73640, = call(self.generate_shape_7364, matmul_11550)

      expand_73650, = call(self.expand_7365, parameter_1860, generate_shape_73640)

      add_73660, = call(self.add_7366, matmul_11550, expand_73650)

      scale_73670, = call(self.scale_7367, add_73660)

      generate_shape_73680, = call(self.generate_shape_7368, fusion_73620)

      reshape_73690, reshape_73691, = call(self.reshape_7369, scale_73670, generate_shape_73680)

      transpose_73700, = call(self.transpose_7370, reshape_73690)

      generate_shape_73710, = call(self.generate_shape_7371, fusion_73620)

      reshape_73720, reshape_73721, = call(self.reshape_7372, transpose_73700, generate_shape_73710)

      return call(self.yield_7374, reshape_73720)

    return ret_lambda

    

  def fusion_7383_block00(self, call, matmul_11590, parameter_1880, fusion_73620):

    def ret_lambda():

      generate_shape_73750, = call(self.generate_shape_7375, matmul_11590)

      expand_73760, = call(self.expand_7376, parameter_1880, generate_shape_73750)

      add_73770, = call(self.add_7377, matmul_11590, expand_73760)

      generate_shape_73780, = call(self.generate_shape_7378, fusion_73620)

      reshape_73790, reshape_73791, = call(self.reshape_7379, add_73770, generate_shape_73780)

      transpose_73800, = call(self.transpose_7380, reshape_73790)

      generate_shape_73810, = call(self.generate_shape_7381, fusion_73620)

      reshape_73820, reshape_73821, = call(self.reshape_7382, transpose_73800, generate_shape_73810)

      return call(self.yield_7384, reshape_73820)

    return ret_lambda

    

  def fusion_7393_block00(self, call, matmul_11670, parameter_1900, fusion_73620):

    def ret_lambda():

      generate_shape_73850, = call(self.generate_shape_7385, matmul_11670)

      expand_73860, = call(self.expand_7386, parameter_1900, generate_shape_73850)

      add_73870, = call(self.add_7387, matmul_11670, expand_73860)

      generate_shape_73880, = call(self.generate_shape_7388, fusion_73620)

      reshape_73890, reshape_73891, = call(self.reshape_7389, add_73870, generate_shape_73880)

      transpose_73900, = call(self.transpose_7390, reshape_73890)

      generate_shape_73910, = call(self.generate_shape_7391, fusion_73620)

      reshape_73920, reshape_73921, = call(self.reshape_7392, transpose_73900, generate_shape_73910)

      return call(self.yield_7394, reshape_73920)

    return ret_lambda

    

  def fusion_7402_block00(self, call, fusion_73620, fusion_73830, matmul_11980, triu_2330):

    def ret_lambda():

      generate_shape_73950, = call(self.generate_shape_7395, fusion_73620, fusion_73830)

      reshape_73960, reshape_73961, = call(self.reshape_7396, matmul_11980, generate_shape_73950)

      generate_shape_73970, = call(self.generate_shape_7397, fusion_73620)

      expand_73980, = call(self.expand_7398, triu_2330, generate_shape_73970)

      add_73990, = call(self.add_7399, reshape_73960, expand_73980)

      generate_shape_74000, = call(self.generate_shape_7400, fusion_73620, fusion_73830)

      reshape_74010, reshape_74011, = call(self.reshape_7401, add_73990, generate_shape_74000)

      return call(self.yield_7403, reshape_74010)

    return ret_lambda

    

  def fusion_7409_block00(self, call, fusion_73620, matmul_12080):

    def ret_lambda():

      generate_shape_74040, = call(self.generate_shape_7404, fusion_73620)

      reshape_74050, reshape_74051, = call(self.reshape_7405, matmul_12080, generate_shape_74040)

      transpose_74060, = call(self.transpose_7406, reshape_74050)

      generate_shape_74070, = call(self.generate_shape_7407, fusion_73620)

      reshape_74080, reshape_74081, = call(self.reshape_7408, transpose_74060, generate_shape_74070)

      return call(self.yield_7410, reshape_74080)

    return ret_lambda

    

  def fusion_7415_block00(self, call, matmul_12170, parameter_1920, fusion_73250):

    def ret_lambda():

      generate_shape_74110, = call(self.generate_shape_7411, matmul_12170)

      expand_74120, = call(self.expand_7412, parameter_1920, generate_shape_74110)

      add_74130, = call(self.add_7413, matmul_12170, expand_74120)

      add_74140, = call(self.add_7414, fusion_73250, add_74130)

      return call(self.yield_7416, add_74140)

    return ret_lambda

    

  def fusion_7419_block00(self, call, fusion_74150):

    def ret_lambda():

      cast_74170, = call(self.cast_7417, fusion_74150)

      reduce_sum_74180, = call(self.reduce_sum_7418, cast_74170)

      return call(self.yield_7420, reduce_sum_74180)

    return ret_lambda

    

  def fusion_7452_block00(self, call, fusion_74150, matmul_12170, fusion_74190, parameter_1940, parameter_1930):

    def ret_lambda():

      cast_74210, = call(self.cast_7421, fusion_74150)

      full_74220, = call(self.full_7422)

      generate_shape_74230, = call(self.generate_shape_7423, matmul_12170)

      expand_74240, = call(self.expand_7424, full_74220, generate_shape_74230)

      divide_74250, = call(self.divide_7425, fusion_74190, expand_74240)

      generate_shape_74260, = call(self.generate_shape_7426, matmul_12170)

      expand_74270, = call(self.expand_7427, divide_74250, generate_shape_74260)

      subtract_74280, = call(self.subtract_7428, cast_74210, expand_74270)

      multiply_74290, = call(self.multiply_7429, subtract_74280, subtract_74280)

      reduce_sum_74300, = call(self.reduce_sum_7430, multiply_74290)

      full_74310, = call(self.full_7431)

      generate_shape_74320, = call(self.generate_shape_7432, matmul_12170)

      expand_74330, = call(self.expand_7433, full_74310, generate_shape_74320)

      divide_74340, = call(self.divide_7434, reduce_sum_74300, expand_74330)

      full_74350, = call(self.full_7435)

      generate_shape_74360, = call(self.generate_shape_7436, matmul_12170)

      expand_74370, = call(self.expand_7437, full_74350, generate_shape_74360)

      add_74380, = call(self.add_7438, divide_74340, expand_74370)

      rsqrt_74390, = call(self.rsqrt_7439, add_74380)

      generate_shape_74400, = call(self.generate_shape_7440, matmul_12170)

      expand_74410, = call(self.expand_7441, rsqrt_74390, generate_shape_74400)

      multiply_74420, = call(self.multiply_7442, subtract_74280, expand_74410)

      cast_74430, = call(self.cast_7443, parameter_1940)

      generate_shape_74440, = call(self.generate_shape_7444, matmul_12170)

      expand_74450, = call(self.expand_7445, cast_74430, generate_shape_74440)

      multiply_74460, = call(self.multiply_7446, multiply_74420, expand_74450)

      cast_74470, = call(self.cast_7447, parameter_1930)

      generate_shape_74480, = call(self.generate_shape_7448, matmul_12170)

      expand_74490, = call(self.expand_7449, cast_74470, generate_shape_74480)

      add_74500, = call(self.add_7450, multiply_74460, expand_74490)

      cast_74510, = call(self.cast_7451, add_74500)

      return call(self.yield_7453, cast_74510)

    return ret_lambda

    

  def fusion_7470_block00(self, call, matmul_12210, parameter_1960):

    def ret_lambda():

      generate_shape_74540, = call(self.generate_shape_7454, matmul_12210)

      expand_74550, = call(self.expand_7455, parameter_1960, generate_shape_74540)

      add_74560, = call(self.add_7456, matmul_12210, expand_74550)

      scale_74570, = call(self.scale_7457, add_74560)

      cast_74580, = call(self.cast_7458, scale_74570)

      full_74590, = call(self.full_7459)

      scale_74600, = call(self.scale_7460, cast_74580)

      exp_74610, = call(self.exp_7461, scale_74600)

      generate_shape_74620, = call(self.generate_shape_7462, matmul_12210)

      expand_74630, = call(self.expand_7463, full_74590, generate_shape_74620)

      add_74640, = call(self.add_7464, expand_74630, exp_74610)

      generate_shape_74650, = call(self.generate_shape_7465, matmul_12210)

      expand_74660, = call(self.expand_7466, full_74590, generate_shape_74650)

      divide_74670, = call(self.divide_7467, expand_74660, add_74640)

      cast_74680, = call(self.cast_7468, divide_74670)

      multiply_74690, = call(self.multiply_7469, add_74560, cast_74680)

      return call(self.yield_7471, multiply_74690)

    return ret_lambda

    

  def fusion_7478_block00(self, call, matmul_12270, parameter_1980, fusion_74150):

    def ret_lambda():

      generate_shape_74720, = call(self.generate_shape_7472, matmul_12270)

      expand_74730, = call(self.expand_7473, parameter_1980, generate_shape_74720)

      add_74740, = call(self.add_7474, matmul_12270, expand_74730)

      add_74750, = call(self.add_7475, fusion_74150, add_74740)

      cast_74760, = call(self.cast_7476, add_74750)

      reduce_sum_74770, = call(self.reduce_sum_7477, cast_74760)

      return call(self.yield_7479, reduce_sum_74770)

    return ret_lambda

    

  def fusion_7515_block00(self, call, matmul_12270, parameter_1980, fusion_74150, fusion_74780, parameter_2000, parameter_1990):

    def ret_lambda():

      generate_shape_74800, = call(self.generate_shape_7480, matmul_12270)

      expand_74810, = call(self.expand_7481, parameter_1980, generate_shape_74800)

      add_74820, = call(self.add_7482, matmul_12270, expand_74810)

      add_74830, = call(self.add_7483, fusion_74150, add_74820)

      cast_74840, = call(self.cast_7484, add_74830)

      full_74850, = call(self.full_7485)

      generate_shape_74860, = call(self.generate_shape_7486, matmul_12270)

      expand_74870, = call(self.expand_7487, full_74850, generate_shape_74860)

      divide_74880, = call(self.divide_7488, fusion_74780, expand_74870)

      generate_shape_74890, = call(self.generate_shape_7489, matmul_12270)

      expand_74900, = call(self.expand_7490, divide_74880, generate_shape_74890)

      subtract_74910, = call(self.subtract_7491, cast_74840, expand_74900)

      multiply_74920, = call(self.multiply_7492, subtract_74910, subtract_74910)

      reduce_sum_74930, = call(self.reduce_sum_7493, multiply_74920)

      full_74940, = call(self.full_7494)

      generate_shape_74950, = call(self.generate_shape_7495, matmul_12270)

      expand_74960, = call(self.expand_7496, full_74940, generate_shape_74950)

      divide_74970, = call(self.divide_7497, reduce_sum_74930, expand_74960)

      full_74980, = call(self.full_7498)

      generate_shape_74990, = call(self.generate_shape_7499, matmul_12270)

      expand_75000, = call(self.expand_7500, full_74980, generate_shape_74990)

      add_75010, = call(self.add_7501, divide_74970, expand_75000)

      rsqrt_75020, = call(self.rsqrt_7502, add_75010)

      generate_shape_75030, = call(self.generate_shape_7503, matmul_12270)

      expand_75040, = call(self.expand_7504, rsqrt_75020, generate_shape_75030)

      multiply_75050, = call(self.multiply_7505, subtract_74910, expand_75040)

      cast_75060, = call(self.cast_7506, parameter_2000)

      generate_shape_75070, = call(self.generate_shape_7507, matmul_12270)

      expand_75080, = call(self.expand_7508, cast_75060, generate_shape_75070)

      multiply_75090, = call(self.multiply_7509, multiply_75050, expand_75080)

      cast_75100, = call(self.cast_7510, parameter_1990)

      generate_shape_75110, = call(self.generate_shape_7511, matmul_12270)

      expand_75120, = call(self.expand_7512, cast_75100, generate_shape_75110)

      add_75130, = call(self.add_7513, multiply_75090, expand_75120)

      cast_75140, = call(self.cast_7514, add_75130)

      return call(self.yield_7516, cast_75140)

    return ret_lambda

    

  def fusion_7519_block00(self, call, fusion_75150):

    def ret_lambda():

      scale_75170, = call(self.scale_7517, fusion_75150)

      cast_75180, = call(self.cast_7518, scale_75170)

      return call(self.yield_7520, cast_75180)

    return ret_lambda

    

  def fusion_7522_block00(self, call, shape_12310):

    def ret_lambda():

      slice_75210, = call(self.slice_7521, shape_12310)

      return call(self.yield_7523, slice_75210)

    return ret_lambda

    

  def fusion_7531_block00(self, call, arange_12370, fusion_75150, argmax_12390):

    def ret_lambda():

      generate_shape_75240, = call(self.generate_shape_7524, arange_12370, fusion_75150)

      reshape_75250, reshape_75251, = call(self.reshape_7525, arange_12370, generate_shape_75240)

      reshape_75260, reshape_75261, = call(self.reshape_7526, argmax_12390, generate_shape_75240)

      concat_75270, = call(self.concat_7527, reshape_75250, reshape_75260)

      gather_nd_75280, = call(self.gather_nd_7528, fusion_75150, concat_75270)

      scale_75290, = call(self.scale_7529, gather_nd_75280)

      cast_75300, = call(self.cast_7530, scale_75290)

      return call(self.yield_7532, cast_75300)

    return ret_lambda

    

  def module_3_block00(self, call):

    def ret_lambda():

      parameter_40, = call(self.parameter_4)

      parameter_50, = call(self.parameter_5)

      parameter_60, = call(self.parameter_6)

      parameter_70, = call(self.parameter_7)

      parameter_80, = call(self.parameter_8)

      parameter_90, = call(self.parameter_9)

      parameter_100, = call(self.parameter_10)

      parameter_110, = call(self.parameter_11)

      parameter_120, = call(self.parameter_12)

      parameter_130, = call(self.parameter_13)

      parameter_140, = call(self.parameter_14)

      parameter_150, = call(self.parameter_15)

      parameter_160, = call(self.parameter_16)

      parameter_170, = call(self.parameter_17)

      parameter_180, = call(self.parameter_18)

      parameter_190, = call(self.parameter_19)

      parameter_200, = call(self.parameter_20)

      parameter_210, = call(self.parameter_21)

      parameter_220, = call(self.parameter_22)

      parameter_230, = call(self.parameter_23)

      parameter_240, = call(self.parameter_24)

      parameter_250, = call(self.parameter_25)

      parameter_260, = call(self.parameter_26)

      parameter_270, = call(self.parameter_27)

      parameter_280, = call(self.parameter_28)

      parameter_290, = call(self.parameter_29)

      parameter_300, = call(self.parameter_30)

      parameter_310, = call(self.parameter_31)

      parameter_320, = call(self.parameter_32)

      parameter_330, = call(self.parameter_33)

      parameter_340, = call(self.parameter_34)

      parameter_350, = call(self.parameter_35)

      parameter_360, = call(self.parameter_36)

      parameter_370, = call(self.parameter_37)

      parameter_380, = call(self.parameter_38)

      parameter_390, = call(self.parameter_39)

      parameter_400, = call(self.parameter_40)

      parameter_410, = call(self.parameter_41)

      parameter_420, = call(self.parameter_42)

      parameter_430, = call(self.parameter_43)

      parameter_440, = call(self.parameter_44)

      parameter_450, = call(self.parameter_45)

      parameter_460, = call(self.parameter_46)

      parameter_470, = call(self.parameter_47)

      parameter_480, = call(self.parameter_48)

      parameter_490, = call(self.parameter_49)

      parameter_500, = call(self.parameter_50)

      parameter_510, = call(self.parameter_51)

      parameter_520, = call(self.parameter_52)

      parameter_530, = call(self.parameter_53)

      parameter_540, = call(self.parameter_54)

      parameter_550, = call(self.parameter_55)

      parameter_560, = call(self.parameter_56)

      parameter_570, = call(self.parameter_57)

      parameter_580, = call(self.parameter_58)

      parameter_590, = call(self.parameter_59)

      parameter_600, = call(self.parameter_60)

      parameter_610, = call(self.parameter_61)

      parameter_620, = call(self.parameter_62)

      parameter_630, = call(self.parameter_63)

      parameter_640, = call(self.parameter_64)

      parameter_650, = call(self.parameter_65)

      parameter_660, = call(self.parameter_66)

      parameter_670, = call(self.parameter_67)

      parameter_680, = call(self.parameter_68)

      parameter_690, = call(self.parameter_69)

      parameter_700, = call(self.parameter_70)

      parameter_710, = call(self.parameter_71)

      parameter_720, = call(self.parameter_72)

      parameter_730, = call(self.parameter_73)

      parameter_740, = call(self.parameter_74)

      parameter_750, = call(self.parameter_75)

      parameter_760, = call(self.parameter_76)

      parameter_770, = call(self.parameter_77)

      parameter_780, = call(self.parameter_78)

      parameter_790, = call(self.parameter_79)

      parameter_800, = call(self.parameter_80)

      parameter_810, = call(self.parameter_81)

      parameter_820, = call(self.parameter_82)

      parameter_830, = call(self.parameter_83)

      parameter_840, = call(self.parameter_84)

      parameter_850, = call(self.parameter_85)

      parameter_860, = call(self.parameter_86)

      parameter_870, = call(self.parameter_87)

      parameter_880, = call(self.parameter_88)

      parameter_890, = call(self.parameter_89)

      parameter_900, = call(self.parameter_90)

      parameter_910, = call(self.parameter_91)

      parameter_920, = call(self.parameter_92)

      parameter_930, = call(self.parameter_93)

      parameter_940, = call(self.parameter_94)

      parameter_950, = call(self.parameter_95)

      parameter_960, = call(self.parameter_96)

      parameter_970, = call(self.parameter_97)

      parameter_980, = call(self.parameter_98)

      parameter_990, = call(self.parameter_99)

      parameter_1000, = call(self.parameter_100)

      parameter_1010, = call(self.parameter_101)

      parameter_1020, = call(self.parameter_102)

      parameter_1030, = call(self.parameter_103)

      parameter_1040, = call(self.parameter_104)

      parameter_1050, = call(self.parameter_105)

      parameter_1060, = call(self.parameter_106)

      parameter_1070, = call(self.parameter_107)

      parameter_1080, = call(self.parameter_108)

      parameter_1090, = call(self.parameter_109)

      parameter_1100, = call(self.parameter_110)

      parameter_1110, = call(self.parameter_111)

      parameter_1120, = call(self.parameter_112)

      parameter_1130, = call(self.parameter_113)

      parameter_1140, = call(self.parameter_114)

      parameter_1150, = call(self.parameter_115)

      parameter_1160, = call(self.parameter_116)

      parameter_1170, = call(self.parameter_117)

      parameter_1180, = call(self.parameter_118)

      parameter_1190, = call(self.parameter_119)

      parameter_1200, = call(self.parameter_120)

      parameter_1210, = call(self.parameter_121)

      parameter_1220, = call(self.parameter_122)

      parameter_1230, = call(self.parameter_123)

      parameter_1240, = call(self.parameter_124)

      parameter_1250, = call(self.parameter_125)

      parameter_1260, = call(self.parameter_126)

      parameter_1270, = call(self.parameter_127)

      parameter_1280, = call(self.parameter_128)

      parameter_1290, = call(self.parameter_129)

      parameter_1300, = call(self.parameter_130)

      parameter_1310, = call(self.parameter_131)

      parameter_1320, = call(self.parameter_132)

      parameter_1330, = call(self.parameter_133)

      parameter_1340, = call(self.parameter_134)

      parameter_1350, = call(self.parameter_135)

      parameter_1360, = call(self.parameter_136)

      parameter_1370, = call(self.parameter_137)

      parameter_1380, = call(self.parameter_138)

      parameter_1390, = call(self.parameter_139)

      parameter_1400, = call(self.parameter_140)

      parameter_1410, = call(self.parameter_141)

      parameter_1420, = call(self.parameter_142)

      parameter_1430, = call(self.parameter_143)

      parameter_1440, = call(self.parameter_144)

      parameter_1450, = call(self.parameter_145)

      parameter_1460, = call(self.parameter_146)

      parameter_1470, = call(self.parameter_147)

      parameter_1480, = call(self.parameter_148)

      parameter_1490, = call(self.parameter_149)

      parameter_1500, = call(self.parameter_150)

      parameter_1510, = call(self.parameter_151)

      parameter_1520, = call(self.parameter_152)

      parameter_1530, = call(self.parameter_153)

      parameter_1540, = call(self.parameter_154)

      parameter_1550, = call(self.parameter_155)

      parameter_1560, = call(self.parameter_156)

      parameter_1570, = call(self.parameter_157)

      parameter_1580, = call(self.parameter_158)

      parameter_1590, = call(self.parameter_159)

      parameter_1600, = call(self.parameter_160)

      parameter_1610, = call(self.parameter_161)

      parameter_1620, = call(self.parameter_162)

      parameter_1630, = call(self.parameter_163)

      parameter_1640, = call(self.parameter_164)

      parameter_1650, = call(self.parameter_165)

      parameter_1660, = call(self.parameter_166)

      parameter_1670, = call(self.parameter_167)

      parameter_1680, = call(self.parameter_168)

      parameter_1690, = call(self.parameter_169)

      parameter_1700, = call(self.parameter_170)

      parameter_1710, = call(self.parameter_171)

      parameter_1720, = call(self.parameter_172)

      parameter_1730, = call(self.parameter_173)

      parameter_1740, = call(self.parameter_174)

      parameter_1750, = call(self.parameter_175)

      parameter_1760, = call(self.parameter_176)

      parameter_1770, = call(self.parameter_177)

      parameter_1780, = call(self.parameter_178)

      parameter_1790, = call(self.parameter_179)

      parameter_1800, = call(self.parameter_180)

      parameter_1810, = call(self.parameter_181)

      parameter_1820, = call(self.parameter_182)

      parameter_1830, = call(self.parameter_183)

      parameter_1840, = call(self.parameter_184)

      parameter_1850, = call(self.parameter_185)

      parameter_1860, = call(self.parameter_186)

      parameter_1870, = call(self.parameter_187)

      parameter_1880, = call(self.parameter_188)

      parameter_1890, = call(self.parameter_189)

      parameter_1900, = call(self.parameter_190)

      parameter_1910, = call(self.parameter_191)

      parameter_1920, = call(self.parameter_192)

      parameter_1930, = call(self.parameter_193)

      parameter_1940, = call(self.parameter_194)

      parameter_1950, = call(self.parameter_195)

      parameter_1960, = call(self.parameter_196)

      parameter_1970, = call(self.parameter_197)

      parameter_1980, = call(self.parameter_198)

      parameter_1990, = call(self.parameter_199)

      parameter_2000, = call(self.parameter_200)

      feed_2010, = call(self.feed_201)

      shape_2120, = call(self.shape_212, feed_2010)

      fusion_56470, = call(self.fusion_5647, blocks=[[(self.fusion_5647_block00, shape_2120)]])

      full_int_array_2160, = call(self.full_int_array_216)

      combine_40120, = call(self.combine_4012, fusion_56470)

      slice_2180, = call(self.slice_218, parameter_40, full_int_array_2160, combine_40120)

      embedding_2190, = call(self.embedding_219, feed_2010, parameter_50)

      fusion_56500, = call(self.fusion_5650, blocks=[[(self.fusion_5650_block00, slice_2180)]])

      embedding_2210, = call(self.embedding_221, fusion_56500, parameter_60)

      fusion_56590, = call(self.fusion_5659, blocks=[[(self.fusion_5659_block00, feed_2010)]])

      triu_2330, = call(self.triu_233, fusion_56590)

      fusion_56640, = call(self.fusion_5664, blocks=[[(self.fusion_5664_block00, embedding_2190, embedding_2210)]])

      fusion_56680, = call(self.fusion_5668, blocks=[[(self.fusion_5668_block00, fusion_56640)]])

      fusion_57010, = call(self.fusion_5701, blocks=[[(self.fusion_5701_block00, fusion_56640, embedding_2190, fusion_56680, parameter_80, parameter_70)]])

      matmul_2420, = call(self.matmul_242, fusion_57010, parameter_90)

      matmul_2460, = call(self.matmul_246, fusion_57010, parameter_110)

      matmul_2540, = call(self.matmul_254, fusion_57010, parameter_130)

      fusion_57120, = call(self.fusion_5712, blocks=[[(self.fusion_5712_block00, matmul_2420, parameter_100, fusion_57010)]])

      fusion_57220, = call(self.fusion_5722, blocks=[[(self.fusion_5722_block00, matmul_2460, parameter_120, fusion_57010)]])

      fusion_57320, = call(self.fusion_5732, blocks=[[(self.fusion_5732_block00, matmul_2540, parameter_140, fusion_57010)]])

      matmul_2850, = call(self.matmul_285, fusion_57120, fusion_57220)

      fusion_57410, = call(self.fusion_5741, blocks=[[(self.fusion_5741_block00, fusion_57010, fusion_57220, matmul_2850, triu_2330)]])

      softmax_2940, = call(self.softmax_294, fusion_57410)

      matmul_2950, = call(self.matmul_295, softmax_2940, fusion_57320)

      fusion_57480, = call(self.fusion_5748, blocks=[[(self.fusion_5748_block00, fusion_57010, matmul_2950)]])

      matmul_3040, = call(self.matmul_304, fusion_57480, parameter_150)

      fusion_57540, = call(self.fusion_5754, blocks=[[(self.fusion_5754_block00, matmul_3040, parameter_160, fusion_56640)]])

      fusion_57580, = call(self.fusion_5758, blocks=[[(self.fusion_5758_block00, fusion_57540)]])

      fusion_57910, = call(self.fusion_5791, blocks=[[(self.fusion_5791_block00, fusion_57540, matmul_3040, fusion_57580, parameter_180, parameter_170)]])

      matmul_3080, = call(self.matmul_308, fusion_57910, parameter_190)

      fusion_58090, = call(self.fusion_5809, blocks=[[(self.fusion_5809_block00, matmul_3080, parameter_200)]])

      matmul_3140, = call(self.matmul_314, fusion_58090, parameter_210)

      fusion_58150, = call(self.fusion_5815, blocks=[[(self.fusion_5815_block00, matmul_3140, parameter_220, fusion_57540)]])

      fusion_58190, = call(self.fusion_5819, blocks=[[(self.fusion_5819_block00, fusion_58150)]])

      fusion_58520, = call(self.fusion_5852, blocks=[[(self.fusion_5852_block00, fusion_58150, matmul_3140, fusion_58190, parameter_240, parameter_230)]])

      matmul_3250, = call(self.matmul_325, fusion_58520, parameter_250)

      matmul_3290, = call(self.matmul_329, fusion_58520, parameter_270)

      matmul_3370, = call(self.matmul_337, fusion_58520, parameter_290)

      fusion_58630, = call(self.fusion_5863, blocks=[[(self.fusion_5863_block00, matmul_3250, parameter_260, fusion_58520)]])

      fusion_58730, = call(self.fusion_5873, blocks=[[(self.fusion_5873_block00, matmul_3290, parameter_280, fusion_58520)]])

      fusion_58830, = call(self.fusion_5883, blocks=[[(self.fusion_5883_block00, matmul_3370, parameter_300, fusion_58520)]])

      matmul_3680, = call(self.matmul_368, fusion_58630, fusion_58730)

      fusion_58920, = call(self.fusion_5892, blocks=[[(self.fusion_5892_block00, fusion_58520, fusion_58730, matmul_3680, triu_2330)]])

      softmax_3770, = call(self.softmax_377, fusion_58920)

      matmul_3780, = call(self.matmul_378, softmax_3770, fusion_58830)

      fusion_58990, = call(self.fusion_5899, blocks=[[(self.fusion_5899_block00, fusion_58520, matmul_3780)]])

      matmul_3870, = call(self.matmul_387, fusion_58990, parameter_310)

      fusion_59050, = call(self.fusion_5905, blocks=[[(self.fusion_5905_block00, matmul_3870, parameter_320, fusion_58150)]])

      fusion_59090, = call(self.fusion_5909, blocks=[[(self.fusion_5909_block00, fusion_59050)]])

      fusion_59420, = call(self.fusion_5942, blocks=[[(self.fusion_5942_block00, fusion_59050, matmul_3870, fusion_59090, parameter_340, parameter_330)]])

      matmul_3910, = call(self.matmul_391, fusion_59420, parameter_350)

      fusion_59600, = call(self.fusion_5960, blocks=[[(self.fusion_5960_block00, matmul_3910, parameter_360)]])

      matmul_3970, = call(self.matmul_397, fusion_59600, parameter_370)

      fusion_59660, = call(self.fusion_5966, blocks=[[(self.fusion_5966_block00, matmul_3970, parameter_380, fusion_59050)]])

      fusion_59700, = call(self.fusion_5970, blocks=[[(self.fusion_5970_block00, fusion_59660)]])

      fusion_60030, = call(self.fusion_6003, blocks=[[(self.fusion_6003_block00, fusion_59660, matmul_3970, fusion_59700, parameter_400, parameter_390)]])

      matmul_4080, = call(self.matmul_408, fusion_60030, parameter_410)

      matmul_4120, = call(self.matmul_412, fusion_60030, parameter_430)

      matmul_4200, = call(self.matmul_420, fusion_60030, parameter_450)

      fusion_60140, = call(self.fusion_6014, blocks=[[(self.fusion_6014_block00, matmul_4080, parameter_420, fusion_60030)]])

      fusion_60240, = call(self.fusion_6024, blocks=[[(self.fusion_6024_block00, matmul_4120, parameter_440, fusion_60030)]])

      fusion_60340, = call(self.fusion_6034, blocks=[[(self.fusion_6034_block00, matmul_4200, parameter_460, fusion_60030)]])

      matmul_4510, = call(self.matmul_451, fusion_60140, fusion_60240)

      fusion_60430, = call(self.fusion_6043, blocks=[[(self.fusion_6043_block00, fusion_60030, fusion_60240, matmul_4510, triu_2330)]])

      softmax_4600, = call(self.softmax_460, fusion_60430)

      matmul_4610, = call(self.matmul_461, softmax_4600, fusion_60340)

      fusion_60500, = call(self.fusion_6050, blocks=[[(self.fusion_6050_block00, fusion_60030, matmul_4610)]])

      matmul_4700, = call(self.matmul_470, fusion_60500, parameter_470)

      fusion_60560, = call(self.fusion_6056, blocks=[[(self.fusion_6056_block00, matmul_4700, parameter_480, fusion_59660)]])

      fusion_60600, = call(self.fusion_6060, blocks=[[(self.fusion_6060_block00, fusion_60560)]])

      fusion_60930, = call(self.fusion_6093, blocks=[[(self.fusion_6093_block00, fusion_60560, matmul_4700, fusion_60600, parameter_500, parameter_490)]])

      matmul_4740, = call(self.matmul_474, fusion_60930, parameter_510)

      fusion_61110, = call(self.fusion_6111, blocks=[[(self.fusion_6111_block00, matmul_4740, parameter_520)]])

      matmul_4800, = call(self.matmul_480, fusion_61110, parameter_530)

      fusion_61170, = call(self.fusion_6117, blocks=[[(self.fusion_6117_block00, matmul_4800, parameter_540, fusion_60560)]])

      fusion_61210, = call(self.fusion_6121, blocks=[[(self.fusion_6121_block00, fusion_61170)]])

      fusion_61540, = call(self.fusion_6154, blocks=[[(self.fusion_6154_block00, fusion_61170, matmul_4800, fusion_61210, parameter_560, parameter_550)]])

      matmul_4910, = call(self.matmul_491, fusion_61540, parameter_570)

      matmul_4950, = call(self.matmul_495, fusion_61540, parameter_590)

      matmul_5030, = call(self.matmul_503, fusion_61540, parameter_610)

      fusion_61650, = call(self.fusion_6165, blocks=[[(self.fusion_6165_block00, matmul_4910, parameter_580, fusion_61540)]])

      fusion_61750, = call(self.fusion_6175, blocks=[[(self.fusion_6175_block00, matmul_4950, parameter_600, fusion_61540)]])

      fusion_61850, = call(self.fusion_6185, blocks=[[(self.fusion_6185_block00, matmul_5030, parameter_620, fusion_61540)]])

      matmul_5340, = call(self.matmul_534, fusion_61650, fusion_61750)

      fusion_61940, = call(self.fusion_6194, blocks=[[(self.fusion_6194_block00, fusion_61540, fusion_61750, matmul_5340, triu_2330)]])

      softmax_5430, = call(self.softmax_543, fusion_61940)

      matmul_5440, = call(self.matmul_544, softmax_5430, fusion_61850)

      fusion_62010, = call(self.fusion_6201, blocks=[[(self.fusion_6201_block00, fusion_61540, matmul_5440)]])

      matmul_5530, = call(self.matmul_553, fusion_62010, parameter_630)

      fusion_62070, = call(self.fusion_6207, blocks=[[(self.fusion_6207_block00, matmul_5530, parameter_640, fusion_61170)]])

      fusion_62110, = call(self.fusion_6211, blocks=[[(self.fusion_6211_block00, fusion_62070)]])

      fusion_62440, = call(self.fusion_6244, blocks=[[(self.fusion_6244_block00, fusion_62070, matmul_5530, fusion_62110, parameter_660, parameter_650)]])

      matmul_5570, = call(self.matmul_557, fusion_62440, parameter_670)

      fusion_62620, = call(self.fusion_6262, blocks=[[(self.fusion_6262_block00, matmul_5570, parameter_680)]])

      matmul_5630, = call(self.matmul_563, fusion_62620, parameter_690)

      fusion_62680, = call(self.fusion_6268, blocks=[[(self.fusion_6268_block00, matmul_5630, parameter_700, fusion_62070)]])

      fusion_62720, = call(self.fusion_6272, blocks=[[(self.fusion_6272_block00, fusion_62680)]])

      fusion_63050, = call(self.fusion_6305, blocks=[[(self.fusion_6305_block00, fusion_62680, matmul_5630, fusion_62720, parameter_720, parameter_710)]])

      matmul_5740, = call(self.matmul_574, fusion_63050, parameter_730)

      matmul_5780, = call(self.matmul_578, fusion_63050, parameter_750)

      matmul_5860, = call(self.matmul_586, fusion_63050, parameter_770)

      fusion_63160, = call(self.fusion_6316, blocks=[[(self.fusion_6316_block00, matmul_5740, parameter_740, fusion_63050)]])

      fusion_63260, = call(self.fusion_6326, blocks=[[(self.fusion_6326_block00, matmul_5780, parameter_760, fusion_63050)]])

      fusion_63360, = call(self.fusion_6336, blocks=[[(self.fusion_6336_block00, matmul_5860, parameter_780, fusion_63050)]])

      matmul_6170, = call(self.matmul_617, fusion_63160, fusion_63260)

      fusion_63450, = call(self.fusion_6345, blocks=[[(self.fusion_6345_block00, fusion_63050, fusion_63260, matmul_6170, triu_2330)]])

      softmax_6260, = call(self.softmax_626, fusion_63450)

      matmul_6270, = call(self.matmul_627, softmax_6260, fusion_63360)

      fusion_63520, = call(self.fusion_6352, blocks=[[(self.fusion_6352_block00, fusion_63050, matmul_6270)]])

      matmul_6360, = call(self.matmul_636, fusion_63520, parameter_790)

      fusion_63580, = call(self.fusion_6358, blocks=[[(self.fusion_6358_block00, matmul_6360, parameter_800, fusion_62680)]])

      fusion_63620, = call(self.fusion_6362, blocks=[[(self.fusion_6362_block00, fusion_63580)]])

      fusion_63950, = call(self.fusion_6395, blocks=[[(self.fusion_6395_block00, fusion_63580, matmul_6360, fusion_63620, parameter_820, parameter_810)]])

      matmul_6400, = call(self.matmul_640, fusion_63950, parameter_830)

      fusion_64130, = call(self.fusion_6413, blocks=[[(self.fusion_6413_block00, matmul_6400, parameter_840)]])

      matmul_6460, = call(self.matmul_646, fusion_64130, parameter_850)

      fusion_64190, = call(self.fusion_6419, blocks=[[(self.fusion_6419_block00, matmul_6460, parameter_860, fusion_63580)]])

      fusion_64230, = call(self.fusion_6423, blocks=[[(self.fusion_6423_block00, fusion_64190)]])

      fusion_64560, = call(self.fusion_6456, blocks=[[(self.fusion_6456_block00, fusion_64190, matmul_6460, fusion_64230, parameter_880, parameter_870)]])

      matmul_6570, = call(self.matmul_657, fusion_64560, parameter_890)

      matmul_6610, = call(self.matmul_661, fusion_64560, parameter_910)

      matmul_6690, = call(self.matmul_669, fusion_64560, parameter_930)

      fusion_64670, = call(self.fusion_6467, blocks=[[(self.fusion_6467_block00, matmul_6570, parameter_900, fusion_64560)]])

      fusion_64770, = call(self.fusion_6477, blocks=[[(self.fusion_6477_block00, matmul_6610, parameter_920, fusion_64560)]])

      fusion_64870, = call(self.fusion_6487, blocks=[[(self.fusion_6487_block00, matmul_6690, parameter_940, fusion_64560)]])

      matmul_7000, = call(self.matmul_700, fusion_64670, fusion_64770)

      fusion_64960, = call(self.fusion_6496, blocks=[[(self.fusion_6496_block00, fusion_64560, fusion_64770, matmul_7000, triu_2330)]])

      softmax_7090, = call(self.softmax_709, fusion_64960)

      matmul_7100, = call(self.matmul_710, softmax_7090, fusion_64870)

      fusion_65030, = call(self.fusion_6503, blocks=[[(self.fusion_6503_block00, fusion_64560, matmul_7100)]])

      matmul_7190, = call(self.matmul_719, fusion_65030, parameter_950)

      fusion_65090, = call(self.fusion_6509, blocks=[[(self.fusion_6509_block00, matmul_7190, parameter_960, fusion_64190)]])

      fusion_65130, = call(self.fusion_6513, blocks=[[(self.fusion_6513_block00, fusion_65090)]])

      fusion_65460, = call(self.fusion_6546, blocks=[[(self.fusion_6546_block00, fusion_65090, matmul_7190, fusion_65130, parameter_980, parameter_970)]])

      matmul_7230, = call(self.matmul_723, fusion_65460, parameter_990)

      fusion_65640, = call(self.fusion_6564, blocks=[[(self.fusion_6564_block00, matmul_7230, parameter_1000)]])

      matmul_7290, = call(self.matmul_729, fusion_65640, parameter_1010)

      fusion_65700, = call(self.fusion_6570, blocks=[[(self.fusion_6570_block00, matmul_7290, parameter_1020, fusion_65090)]])

      fusion_65740, = call(self.fusion_6574, blocks=[[(self.fusion_6574_block00, fusion_65700)]])

      fusion_66070, = call(self.fusion_6607, blocks=[[(self.fusion_6607_block00, fusion_65700, matmul_7290, fusion_65740, parameter_1040, parameter_1030)]])

      matmul_7400, = call(self.matmul_740, fusion_66070, parameter_1050)

      matmul_7440, = call(self.matmul_744, fusion_66070, parameter_1070)

      matmul_7520, = call(self.matmul_752, fusion_66070, parameter_1090)

      fusion_66180, = call(self.fusion_6618, blocks=[[(self.fusion_6618_block00, matmul_7400, parameter_1060, fusion_66070)]])

      fusion_66280, = call(self.fusion_6628, blocks=[[(self.fusion_6628_block00, matmul_7440, parameter_1080, fusion_66070)]])

      fusion_66380, = call(self.fusion_6638, blocks=[[(self.fusion_6638_block00, matmul_7520, parameter_1100, fusion_66070)]])

      matmul_7830, = call(self.matmul_783, fusion_66180, fusion_66280)

      fusion_66470, = call(self.fusion_6647, blocks=[[(self.fusion_6647_block00, fusion_66070, fusion_66280, matmul_7830, triu_2330)]])

      softmax_7920, = call(self.softmax_792, fusion_66470)

      matmul_7930, = call(self.matmul_793, softmax_7920, fusion_66380)

      fusion_66540, = call(self.fusion_6654, blocks=[[(self.fusion_6654_block00, fusion_66070, matmul_7930)]])

      matmul_8020, = call(self.matmul_802, fusion_66540, parameter_1110)

      fusion_66600, = call(self.fusion_6660, blocks=[[(self.fusion_6660_block00, matmul_8020, parameter_1120, fusion_65700)]])

      fusion_66640, = call(self.fusion_6664, blocks=[[(self.fusion_6664_block00, fusion_66600)]])

      fusion_66970, = call(self.fusion_6697, blocks=[[(self.fusion_6697_block00, fusion_66600, matmul_8020, fusion_66640, parameter_1140, parameter_1130)]])

      matmul_8060, = call(self.matmul_806, fusion_66970, parameter_1150)

      fusion_67150, = call(self.fusion_6715, blocks=[[(self.fusion_6715_block00, matmul_8060, parameter_1160)]])

      matmul_8120, = call(self.matmul_812, fusion_67150, parameter_1170)

      fusion_67210, = call(self.fusion_6721, blocks=[[(self.fusion_6721_block00, matmul_8120, parameter_1180, fusion_66600)]])

      fusion_67250, = call(self.fusion_6725, blocks=[[(self.fusion_6725_block00, fusion_67210)]])

      fusion_67580, = call(self.fusion_6758, blocks=[[(self.fusion_6758_block00, fusion_67210, matmul_8120, fusion_67250, parameter_1200, parameter_1190)]])

      matmul_8230, = call(self.matmul_823, fusion_67580, parameter_1210)

      matmul_8270, = call(self.matmul_827, fusion_67580, parameter_1230)

      matmul_8350, = call(self.matmul_835, fusion_67580, parameter_1250)

      fusion_67690, = call(self.fusion_6769, blocks=[[(self.fusion_6769_block00, matmul_8230, parameter_1220, fusion_67580)]])

      fusion_67790, = call(self.fusion_6779, blocks=[[(self.fusion_6779_block00, matmul_8270, parameter_1240, fusion_67580)]])

      fusion_67890, = call(self.fusion_6789, blocks=[[(self.fusion_6789_block00, matmul_8350, parameter_1260, fusion_67580)]])

      matmul_8660, = call(self.matmul_866, fusion_67690, fusion_67790)

      fusion_67980, = call(self.fusion_6798, blocks=[[(self.fusion_6798_block00, fusion_67580, fusion_67790, matmul_8660, triu_2330)]])

      softmax_8750, = call(self.softmax_875, fusion_67980)

      matmul_8760, = call(self.matmul_876, softmax_8750, fusion_67890)

      fusion_68050, = call(self.fusion_6805, blocks=[[(self.fusion_6805_block00, fusion_67580, matmul_8760)]])

      matmul_8850, = call(self.matmul_885, fusion_68050, parameter_1270)

      fusion_68110, = call(self.fusion_6811, blocks=[[(self.fusion_6811_block00, matmul_8850, parameter_1280, fusion_67210)]])

      fusion_68150, = call(self.fusion_6815, blocks=[[(self.fusion_6815_block00, fusion_68110)]])

      fusion_68480, = call(self.fusion_6848, blocks=[[(self.fusion_6848_block00, fusion_68110, matmul_8850, fusion_68150, parameter_1300, parameter_1290)]])

      matmul_8890, = call(self.matmul_889, fusion_68480, parameter_1310)

      fusion_68660, = call(self.fusion_6866, blocks=[[(self.fusion_6866_block00, matmul_8890, parameter_1320)]])

      matmul_8950, = call(self.matmul_895, fusion_68660, parameter_1330)

      fusion_68720, = call(self.fusion_6872, blocks=[[(self.fusion_6872_block00, matmul_8950, parameter_1340, fusion_68110)]])

      fusion_68760, = call(self.fusion_6876, blocks=[[(self.fusion_6876_block00, fusion_68720)]])

      fusion_69090, = call(self.fusion_6909, blocks=[[(self.fusion_6909_block00, fusion_68720, matmul_8950, fusion_68760, parameter_1360, parameter_1350)]])

      matmul_9060, = call(self.matmul_906, fusion_69090, parameter_1370)

      matmul_9100, = call(self.matmul_910, fusion_69090, parameter_1390)

      matmul_9180, = call(self.matmul_918, fusion_69090, parameter_1410)

      fusion_69200, = call(self.fusion_6920, blocks=[[(self.fusion_6920_block00, matmul_9060, parameter_1380, fusion_69090)]])

      fusion_69300, = call(self.fusion_6930, blocks=[[(self.fusion_6930_block00, matmul_9100, parameter_1400, fusion_69090)]])

      fusion_69400, = call(self.fusion_6940, blocks=[[(self.fusion_6940_block00, matmul_9180, parameter_1420, fusion_69090)]])

      matmul_9490, = call(self.matmul_949, fusion_69200, fusion_69300)

      fusion_69490, = call(self.fusion_6949, blocks=[[(self.fusion_6949_block00, fusion_69090, fusion_69300, matmul_9490, triu_2330)]])

      softmax_9580, = call(self.softmax_958, fusion_69490)

      matmul_9590, = call(self.matmul_959, softmax_9580, fusion_69400)

      fusion_69560, = call(self.fusion_6956, blocks=[[(self.fusion_6956_block00, fusion_69090, matmul_9590)]])

      matmul_9680, = call(self.matmul_968, fusion_69560, parameter_1430)

      fusion_69620, = call(self.fusion_6962, blocks=[[(self.fusion_6962_block00, matmul_9680, parameter_1440, fusion_68720)]])

      fusion_69660, = call(self.fusion_6966, blocks=[[(self.fusion_6966_block00, fusion_69620)]])

      fusion_69990, = call(self.fusion_6999, blocks=[[(self.fusion_6999_block00, fusion_69620, matmul_9680, fusion_69660, parameter_1460, parameter_1450)]])

      matmul_9720, = call(self.matmul_972, fusion_69990, parameter_1470)

      fusion_70170, = call(self.fusion_7017, blocks=[[(self.fusion_7017_block00, matmul_9720, parameter_1480)]])

      matmul_9780, = call(self.matmul_978, fusion_70170, parameter_1490)

      fusion_70230, = call(self.fusion_7023, blocks=[[(self.fusion_7023_block00, matmul_9780, parameter_1500, fusion_69620)]])

      fusion_70270, = call(self.fusion_7027, blocks=[[(self.fusion_7027_block00, fusion_70230)]])

      fusion_70600, = call(self.fusion_7060, blocks=[[(self.fusion_7060_block00, fusion_70230, matmul_9780, fusion_70270, parameter_1520, parameter_1510)]])

      matmul_9890, = call(self.matmul_989, fusion_70600, parameter_1530)

      matmul_9930, = call(self.matmul_993, fusion_70600, parameter_1550)

      matmul_10010, = call(self.matmul_1001, fusion_70600, parameter_1570)

      fusion_70710, = call(self.fusion_7071, blocks=[[(self.fusion_7071_block00, matmul_9890, parameter_1540, fusion_70600)]])

      fusion_70810, = call(self.fusion_7081, blocks=[[(self.fusion_7081_block00, matmul_9930, parameter_1560, fusion_70600)]])

      fusion_70910, = call(self.fusion_7091, blocks=[[(self.fusion_7091_block00, matmul_10010, parameter_1580, fusion_70600)]])

      matmul_10320, = call(self.matmul_1032, fusion_70710, fusion_70810)

      fusion_71000, = call(self.fusion_7100, blocks=[[(self.fusion_7100_block00, fusion_70600, fusion_70810, matmul_10320, triu_2330)]])

      softmax_10410, = call(self.softmax_1041, fusion_71000)

      matmul_10420, = call(self.matmul_1042, softmax_10410, fusion_70910)

      fusion_71070, = call(self.fusion_7107, blocks=[[(self.fusion_7107_block00, fusion_70600, matmul_10420)]])

      matmul_10510, = call(self.matmul_1051, fusion_71070, parameter_1590)

      fusion_71130, = call(self.fusion_7113, blocks=[[(self.fusion_7113_block00, matmul_10510, parameter_1600, fusion_70230)]])

      fusion_71170, = call(self.fusion_7117, blocks=[[(self.fusion_7117_block00, fusion_71130)]])

      fusion_71500, = call(self.fusion_7150, blocks=[[(self.fusion_7150_block00, fusion_71130, matmul_10510, fusion_71170, parameter_1620, parameter_1610)]])

      matmul_10550, = call(self.matmul_1055, fusion_71500, parameter_1630)

      fusion_71680, = call(self.fusion_7168, blocks=[[(self.fusion_7168_block00, matmul_10550, parameter_1640)]])

      matmul_10610, = call(self.matmul_1061, fusion_71680, parameter_1650)

      fusion_71740, = call(self.fusion_7174, blocks=[[(self.fusion_7174_block00, matmul_10610, parameter_1660, fusion_71130)]])

      fusion_71780, = call(self.fusion_7178, blocks=[[(self.fusion_7178_block00, fusion_71740)]])

      fusion_72110, = call(self.fusion_7211, blocks=[[(self.fusion_7211_block00, fusion_71740, matmul_10610, fusion_71780, parameter_1680, parameter_1670)]])

      matmul_10720, = call(self.matmul_1072, fusion_72110, parameter_1690)

      matmul_10760, = call(self.matmul_1076, fusion_72110, parameter_1710)

      matmul_10840, = call(self.matmul_1084, fusion_72110, parameter_1730)

      fusion_72220, = call(self.fusion_7222, blocks=[[(self.fusion_7222_block00, matmul_10720, parameter_1700, fusion_72110)]])

      fusion_72320, = call(self.fusion_7232, blocks=[[(self.fusion_7232_block00, matmul_10760, parameter_1720, fusion_72110)]])

      fusion_72420, = call(self.fusion_7242, blocks=[[(self.fusion_7242_block00, matmul_10840, parameter_1740, fusion_72110)]])

      matmul_11150, = call(self.matmul_1115, fusion_72220, fusion_72320)

      fusion_72510, = call(self.fusion_7251, blocks=[[(self.fusion_7251_block00, fusion_72110, fusion_72320, matmul_11150, triu_2330)]])

      softmax_11240, = call(self.softmax_1124, fusion_72510)

      matmul_11250, = call(self.matmul_1125, softmax_11240, fusion_72420)

      fusion_72580, = call(self.fusion_7258, blocks=[[(self.fusion_7258_block00, fusion_72110, matmul_11250)]])

      matmul_11340, = call(self.matmul_1134, fusion_72580, parameter_1750)

      fusion_72640, = call(self.fusion_7264, blocks=[[(self.fusion_7264_block00, matmul_11340, parameter_1760, fusion_71740)]])

      fusion_72680, = call(self.fusion_7268, blocks=[[(self.fusion_7268_block00, fusion_72640)]])

      fusion_73010, = call(self.fusion_7301, blocks=[[(self.fusion_7301_block00, fusion_72640, matmul_11340, fusion_72680, parameter_1780, parameter_1770)]])

      matmul_11380, = call(self.matmul_1138, fusion_73010, parameter_1790)

      fusion_73190, = call(self.fusion_7319, blocks=[[(self.fusion_7319_block00, matmul_11380, parameter_1800)]])

      matmul_11440, = call(self.matmul_1144, fusion_73190, parameter_1810)

      fusion_73250, = call(self.fusion_7325, blocks=[[(self.fusion_7325_block00, matmul_11440, parameter_1820, fusion_72640)]])

      fusion_73290, = call(self.fusion_7329, blocks=[[(self.fusion_7329_block00, fusion_73250)]])

      fusion_73620, = call(self.fusion_7362, blocks=[[(self.fusion_7362_block00, fusion_73250, matmul_11440, fusion_73290, parameter_1840, parameter_1830)]])

      matmul_11550, = call(self.matmul_1155, fusion_73620, parameter_1850)

      matmul_11590, = call(self.matmul_1159, fusion_73620, parameter_1870)

      matmul_11670, = call(self.matmul_1167, fusion_73620, parameter_1890)

      fusion_73730, = call(self.fusion_7373, blocks=[[(self.fusion_7373_block00, matmul_11550, parameter_1860, fusion_73620)]])

      fusion_73830, = call(self.fusion_7383, blocks=[[(self.fusion_7383_block00, matmul_11590, parameter_1880, fusion_73620)]])

      fusion_73930, = call(self.fusion_7393, blocks=[[(self.fusion_7393_block00, matmul_11670, parameter_1900, fusion_73620)]])

      matmul_11980, = call(self.matmul_1198, fusion_73730, fusion_73830)

      fusion_74020, = call(self.fusion_7402, blocks=[[(self.fusion_7402_block00, fusion_73620, fusion_73830, matmul_11980, triu_2330)]])

      softmax_12070, = call(self.softmax_1207, fusion_74020)

      matmul_12080, = call(self.matmul_1208, softmax_12070, fusion_73930)

      fusion_74090, = call(self.fusion_7409, blocks=[[(self.fusion_7409_block00, fusion_73620, matmul_12080)]])

      matmul_12170, = call(self.matmul_1217, fusion_74090, parameter_1910)

      fusion_74150, = call(self.fusion_7415, blocks=[[(self.fusion_7415_block00, matmul_12170, parameter_1920, fusion_73250)]])

      fusion_74190, = call(self.fusion_7419, blocks=[[(self.fusion_7419_block00, fusion_74150)]])

      fusion_74520, = call(self.fusion_7452, blocks=[[(self.fusion_7452_block00, fusion_74150, matmul_12170, fusion_74190, parameter_1940, parameter_1930)]])

      matmul_12210, = call(self.matmul_1221, fusion_74520, parameter_1950)

      fusion_74700, = call(self.fusion_7470, blocks=[[(self.fusion_7470_block00, matmul_12210, parameter_1960)]])

      matmul_12270, = call(self.matmul_1227, fusion_74700, parameter_1970)

      fusion_74780, = call(self.fusion_7478, blocks=[[(self.fusion_7478_block00, matmul_12270, parameter_1980, fusion_74150)]])

      fusion_75150, = call(self.fusion_7515, blocks=[[(self.fusion_7515_block00, matmul_12270, parameter_1980, fusion_74150, fusion_74780, parameter_2000, parameter_1990)]])

      fusion_75190, = call(self.fusion_7519, blocks=[[(self.fusion_7519_block00, fusion_75150)]])

      shape_12310, = call(self.shape_1231, fusion_75150)

      fusion_75220, = call(self.fusion_7522, blocks=[[(self.fusion_7522_block00, shape_12310)]])

      full_12350, = call(self.full_1235)

      full_12360, = call(self.full_1236)

      arange_12370, = call(self.arange_1237, full_12350, fusion_75220, full_12360)

      full_12380, = call(self.full_1238)

      argmax_12390, = call(self.argmax_1239, feed_2010, full_12380)

      fetch_12480, = call(self.fetch_1248, fusion_75190)

      fusion_75310, = call(self.fusion_7531, blocks=[[(self.fusion_7531_block00, arange_12370, fusion_75150, argmax_12390)]])

      fetch_12500, = call(self.fetch_1250, fusion_75310)

    return ret_lambda

    

  def __call__(self, call, *args, **kwargs):

    self.SetArgs(args)

    self.SetKeywordArgs(kwargs)

    return call(self.module_3, blocks=[[(self.module_3_block00,)]])
