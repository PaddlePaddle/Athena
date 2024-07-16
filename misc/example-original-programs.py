class PirProgram_0:

    def __init__(self):

        self.parameter_931 = self.Op(
            "builtin.parameter",
            931,
            input_types=[],
            output_types=[self.t_dtensor([2, 128], self.t_f32())],
            attrs=dict(
                is_distributed=self.a_array(self.a_bool(False)),
                stop_gradient=self.a_array(self.a_bool(True)),
                parameter_name=self.a_str("eager_tmp_0"),
                is_parameter=self.a_array(self.a_bool(True)),
                persistable=self.a_array(self.a_bool(True)),
                trainable=self.a_array(self.a_bool(False)),
                need_clip=self.a_array(self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.parameter_932 = self.Op(
            "builtin.parameter",
            932,
            input_types=[],
            output_types=[self.t_dtensor([2], self.t_i64())],
            attrs=dict(
                is_distributed=self.a_array(self.a_bool(False)),
                stop_gradient=self.a_array(self.a_bool(True)),
                parameter_name=self.a_str("generated_tensor_7"),
                is_parameter=self.a_array(self.a_bool(True)),
                persistable=self.a_array(self.a_bool(True)),
                trainable=self.a_array(self.a_bool(False)),
                need_clip=self.a_array(self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.parameter_933 = self.Op(
            "builtin.parameter",
            933,
            input_types=[],
            output_types=[self.t_dtensor([1], self.t_f32())],
            attrs=dict(
                is_distributed=self.a_array(self.a_bool(False)),
                stop_gradient=self.a_array(self.a_bool(False)),
                parameter_name=self.a_str("linear_2.b_0"),
                is_parameter=self.a_array(self.a_bool(True)),
                persistable=self.a_array(self.a_bool(True)),
                trainable=self.a_array(self.a_bool(True)),
                need_clip=self.a_array(self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.parameter_934 = self.Op(
            "builtin.parameter",
            934,
            input_types=[],
            output_types=[self.t_dtensor([256, 1], self.t_f32())],
            attrs=dict(
                is_distributed=self.a_array(self.a_bool(False)),
                stop_gradient=self.a_array(self.a_bool(False)),
                parameter_name=self.a_str("linear_2.w_0"),
                is_parameter=self.a_array(self.a_bool(True)),
                persistable=self.a_array(self.a_bool(True)),
                trainable=self.a_array(self.a_bool(True)),
                need_clip=self.a_array(self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.parameter_935 = self.Op(
            "builtin.parameter",
            935,
            input_types=[],
            output_types=[self.t_dtensor([256], self.t_f32())],
            attrs=dict(
                is_distributed=self.a_array(self.a_bool(False)),
                stop_gradient=self.a_array(self.a_bool(False)),
                parameter_name=self.a_str("create_parameter_65.w_0"),
                is_parameter=self.a_array(self.a_bool(True)),
                persistable=self.a_array(self.a_bool(True)),
                trainable=self.a_array(self.a_bool(True)),
                need_clip=self.a_array(self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.parameter_936 = self.Op(
            "builtin.parameter",
            936,
            input_types=[],
            output_types=[self.t_dtensor([256, 1], self.t_f32())],
            attrs=dict(
                is_distributed=self.a_array(self.a_bool(False)),
                stop_gradient=self.a_array(self.a_bool(False)),
                parameter_name=self.a_str("create_parameter_64.w_0"),
                is_parameter=self.a_array(self.a_bool(True)),
                persistable=self.a_array(self.a_bool(True)),
                trainable=self.a_array(self.a_bool(True)),
                need_clip=self.a_array(self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.parameter_937 = self.Op(
            "builtin.parameter",
            937,
            input_types=[],
            output_types=[self.t_dtensor([256, 256], self.t_f32())],
            attrs=dict(
                is_distributed=self.a_array(self.a_bool(False)),
                stop_gradient=self.a_array(self.a_bool(False)),
                parameter_name=self.a_str("create_parameter_63.w_0"),
                is_parameter=self.a_array(self.a_bool(True)),
                persistable=self.a_array(self.a_bool(True)),
                trainable=self.a_array(self.a_bool(True)),
                need_clip=self.a_array(self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.parameter_938 = self.Op(
            "builtin.parameter",
            938,
            input_types=[],
            output_types=[self.t_dtensor([256], self.t_f32())],
            attrs=dict(
                is_distributed=self.a_array(self.a_bool(False)),
                stop_gradient=self.a_array(self.a_bool(False)),
                parameter_name=self.a_str("create_parameter_62.w_0"),
                is_parameter=self.a_array(self.a_bool(True)),
                persistable=self.a_array(self.a_bool(True)),
                trainable=self.a_array(self.a_bool(True)),
                need_clip=self.a_array(self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.parameter_939 = self.Op(
            "builtin.parameter",
            939,
            input_types=[],
            output_types=[self.t_dtensor([256, 1], self.t_f32())],
            attrs=dict(
                is_distributed=self.a_array(self.a_bool(False)),
                stop_gradient=self.a_array(self.a_bool(False)),
                parameter_name=self.a_str("create_parameter_61.w_0"),
                is_parameter=self.a_array(self.a_bool(True)),
                persistable=self.a_array(self.a_bool(True)),
                trainable=self.a_array(self.a_bool(True)),
                need_clip=self.a_array(self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.parameter_940 = self.Op(
            "builtin.parameter",
            940,
            input_types=[],
            output_types=[self.t_dtensor([256, 256], self.t_f32())],
            attrs=dict(
                is_distributed=self.a_array(self.a_bool(False)),
                stop_gradient=self.a_array(self.a_bool(False)),
                parameter_name=self.a_str("create_parameter_60.w_0"),
                is_parameter=self.a_array(self.a_bool(True)),
                persistable=self.a_array(self.a_bool(True)),
                trainable=self.a_array(self.a_bool(True)),
                need_clip=self.a_array(self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.parameter_941 = self.Op(
            "builtin.parameter",
            941,
            input_types=[],
            output_types=[self.t_dtensor([256], self.t_f32())],
            attrs=dict(
                is_distributed=self.a_array(self.a_bool(False)),
                stop_gradient=self.a_array(self.a_bool(False)),
                parameter_name=self.a_str("create_parameter_59.w_0"),
                is_parameter=self.a_array(self.a_bool(True)),
                persistable=self.a_array(self.a_bool(True)),
                trainable=self.a_array(self.a_bool(True)),
                need_clip=self.a_array(self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.parameter_942 = self.Op(
            "builtin.parameter",
            942,
            input_types=[],
            output_types=[self.t_dtensor([256, 1], self.t_f32())],
            attrs=dict(
                is_distributed=self.a_array(self.a_bool(False)),
                stop_gradient=self.a_array(self.a_bool(False)),
                parameter_name=self.a_str("create_parameter_58.w_0"),
                is_parameter=self.a_array(self.a_bool(True)),
                persistable=self.a_array(self.a_bool(True)),
                trainable=self.a_array(self.a_bool(True)),
                need_clip=self.a_array(self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.parameter_943 = self.Op(
            "builtin.parameter",
            943,
            input_types=[],
            output_types=[self.t_dtensor([256, 256], self.t_f32())],
            attrs=dict(
                is_distributed=self.a_array(self.a_bool(False)),
                stop_gradient=self.a_array(self.a_bool(False)),
                parameter_name=self.a_str("create_parameter_57.w_0"),
                is_parameter=self.a_array(self.a_bool(True)),
                persistable=self.a_array(self.a_bool(True)),
                trainable=self.a_array(self.a_bool(True)),
                need_clip=self.a_array(self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.parameter_944 = self.Op(
            "builtin.parameter",
            944,
            input_types=[],
            output_types=[self.t_dtensor([256], self.t_f32())],
            attrs=dict(
                is_distributed=self.a_array(self.a_bool(False)),
                stop_gradient=self.a_array(self.a_bool(False)),
                parameter_name=self.a_str("create_parameter_56.w_0"),
                is_parameter=self.a_array(self.a_bool(True)),
                persistable=self.a_array(self.a_bool(True)),
                trainable=self.a_array(self.a_bool(True)),
                need_clip=self.a_array(self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.parameter_945 = self.Op(
            "builtin.parameter",
            945,
            input_types=[],
            output_types=[self.t_dtensor([256, 1], self.t_f32())],
            attrs=dict(
                is_distributed=self.a_array(self.a_bool(False)),
                stop_gradient=self.a_array(self.a_bool(False)),
                parameter_name=self.a_str("create_parameter_55.w_0"),
                is_parameter=self.a_array(self.a_bool(True)),
                persistable=self.a_array(self.a_bool(True)),
                trainable=self.a_array(self.a_bool(True)),
                need_clip=self.a_array(self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.parameter_946 = self.Op(
            "builtin.parameter",
            946,
            input_types=[],
            output_types=[self.t_dtensor([256, 256], self.t_f32())],
            attrs=dict(
                is_distributed=self.a_array(self.a_bool(False)),
                stop_gradient=self.a_array(self.a_bool(False)),
                parameter_name=self.a_str("create_parameter_54.w_0"),
                is_parameter=self.a_array(self.a_bool(True)),
                persistable=self.a_array(self.a_bool(True)),
                trainable=self.a_array(self.a_bool(True)),
                need_clip=self.a_array(self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.parameter_947 = self.Op(
            "builtin.parameter",
            947,
            input_types=[],
            output_types=[self.t_dtensor([256], self.t_f32())],
            attrs=dict(
                is_distributed=self.a_array(self.a_bool(False)),
                stop_gradient=self.a_array(self.a_bool(False)),
                parameter_name=self.a_str("create_parameter_53.w_0"),
                is_parameter=self.a_array(self.a_bool(True)),
                persistable=self.a_array(self.a_bool(True)),
                trainable=self.a_array(self.a_bool(True)),
                need_clip=self.a_array(self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.parameter_948 = self.Op(
            "builtin.parameter",
            948,
            input_types=[],
            output_types=[self.t_dtensor([256, 1], self.t_f32())],
            attrs=dict(
                is_distributed=self.a_array(self.a_bool(False)),
                stop_gradient=self.a_array(self.a_bool(False)),
                parameter_name=self.a_str("create_parameter_52.w_0"),
                is_parameter=self.a_array(self.a_bool(True)),
                persistable=self.a_array(self.a_bool(True)),
                trainable=self.a_array(self.a_bool(True)),
                need_clip=self.a_array(self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.parameter_949 = self.Op(
            "builtin.parameter",
            949,
            input_types=[],
            output_types=[self.t_dtensor([256, 256], self.t_f32())],
            attrs=dict(
                is_distributed=self.a_array(self.a_bool(False)),
                stop_gradient=self.a_array(self.a_bool(False)),
                parameter_name=self.a_str("create_parameter_51.w_0"),
                is_parameter=self.a_array(self.a_bool(True)),
                persistable=self.a_array(self.a_bool(True)),
                trainable=self.a_array(self.a_bool(True)),
                need_clip=self.a_array(self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.parameter_950 = self.Op(
            "builtin.parameter",
            950,
            input_types=[],
            output_types=[self.t_dtensor([256], self.t_f32())],
            attrs=dict(
                is_distributed=self.a_array(self.a_bool(False)),
                stop_gradient=self.a_array(self.a_bool(False)),
                parameter_name=self.a_str("create_parameter_50.w_0"),
                is_parameter=self.a_array(self.a_bool(True)),
                persistable=self.a_array(self.a_bool(True)),
                trainable=self.a_array(self.a_bool(True)),
                need_clip=self.a_array(self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.parameter_951 = self.Op(
            "builtin.parameter",
            951,
            input_types=[],
            output_types=[self.t_dtensor([256, 1], self.t_f32())],
            attrs=dict(
                is_distributed=self.a_array(self.a_bool(False)),
                stop_gradient=self.a_array(self.a_bool(False)),
                parameter_name=self.a_str("create_parameter_49.w_0"),
                is_parameter=self.a_array(self.a_bool(True)),
                persistable=self.a_array(self.a_bool(True)),
                trainable=self.a_array(self.a_bool(True)),
                need_clip=self.a_array(self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.parameter_952 = self.Op(
            "builtin.parameter",
            952,
            input_types=[],
            output_types=[self.t_dtensor([256, 258], self.t_f32())],
            attrs=dict(
                is_distributed=self.a_array(self.a_bool(False)),
                stop_gradient=self.a_array(self.a_bool(False)),
                parameter_name=self.a_str("create_parameter_48.w_0"),
                is_parameter=self.a_array(self.a_bool(True)),
                persistable=self.a_array(self.a_bool(True)),
                trainable=self.a_array(self.a_bool(True)),
                need_clip=self.a_array(self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.parameter_953 = self.Op(
            "builtin.parameter",
            953,
            input_types=[],
            output_types=[self.t_dtensor([256], self.t_f32())],
            attrs=dict(
                is_distributed=self.a_array(self.a_bool(False)),
                stop_gradient=self.a_array(self.a_bool(False)),
                parameter_name=self.a_str("create_parameter_47.w_0"),
                is_parameter=self.a_array(self.a_bool(True)),
                persistable=self.a_array(self.a_bool(True)),
                trainable=self.a_array(self.a_bool(True)),
                need_clip=self.a_array(self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.parameter_954 = self.Op(
            "builtin.parameter",
            954,
            input_types=[],
            output_types=[self.t_dtensor([256, 1], self.t_f32())],
            attrs=dict(
                is_distributed=self.a_array(self.a_bool(False)),
                stop_gradient=self.a_array(self.a_bool(False)),
                parameter_name=self.a_str("create_parameter_46.w_0"),
                is_parameter=self.a_array(self.a_bool(True)),
                persistable=self.a_array(self.a_bool(True)),
                trainable=self.a_array(self.a_bool(True)),
                need_clip=self.a_array(self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.parameter_955 = self.Op(
            "builtin.parameter",
            955,
            input_types=[],
            output_types=[self.t_dtensor([256, 258], self.t_f32())],
            attrs=dict(
                is_distributed=self.a_array(self.a_bool(False)),
                stop_gradient=self.a_array(self.a_bool(False)),
                parameter_name=self.a_str("create_parameter_45.w_0"),
                is_parameter=self.a_array(self.a_bool(True)),
                persistable=self.a_array(self.a_bool(True)),
                trainable=self.a_array(self.a_bool(True)),
                need_clip=self.a_array(self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.parameter_956 = self.Op(
            "builtin.parameter",
            956,
            input_types=[],
            output_types=[self.t_dtensor([256], self.t_f32())],
            attrs=dict(
                is_distributed=self.a_array(self.a_bool(False)),
                stop_gradient=self.a_array(self.a_bool(False)),
                parameter_name=self.a_str("create_parameter_44.w_0"),
                is_parameter=self.a_array(self.a_bool(True)),
                persistable=self.a_array(self.a_bool(True)),
                trainable=self.a_array(self.a_bool(True)),
                need_clip=self.a_array(self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.parameter_957 = self.Op(
            "builtin.parameter",
            957,
            input_types=[],
            output_types=[self.t_dtensor([256, 1], self.t_f32())],
            attrs=dict(
                is_distributed=self.a_array(self.a_bool(False)),
                stop_gradient=self.a_array(self.a_bool(False)),
                parameter_name=self.a_str("create_parameter_43.w_0"),
                is_parameter=self.a_array(self.a_bool(True)),
                persistable=self.a_array(self.a_bool(True)),
                trainable=self.a_array(self.a_bool(True)),
                need_clip=self.a_array(self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.parameter_958 = self.Op(
            "builtin.parameter",
            958,
            input_types=[],
            output_types=[self.t_dtensor([256, 258], self.t_f32())],
            attrs=dict(
                is_distributed=self.a_array(self.a_bool(False)),
                stop_gradient=self.a_array(self.a_bool(False)),
                parameter_name=self.a_str("create_parameter_42.w_0"),
                is_parameter=self.a_array(self.a_bool(True)),
                persistable=self.a_array(self.a_bool(True)),
                trainable=self.a_array(self.a_bool(True)),
                need_clip=self.a_array(self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.data_959 = self.Op(
            "pd_op.data",
            959,
            input_types=[],
            output_types=[self.t_dtensor([200, 1], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                shape=self.a_intarray(200, 1),
                name=self.a_str("_jst.0.invar.0"),
                place=self.a_place("undefined", 0),
                dtype=self.a_dtype("float32"),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.data_960 = self.Op(
            "pd_op.data",
            960,
            input_types=[],
            output_types=[self.t_dtensor([200, 1], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                shape=self.a_intarray(200, 1),
                name=self.a_str("_jst.0.invar.1"),
                place=self.a_place("undefined", 0),
                dtype=self.a_dtype("float32"),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.data_961 = self.Op(
            "pd_op.data",
            961,
            input_types=[],
            output_types=[self.t_dtensor([200, 1], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                shape=self.a_intarray(200, 1),
                name=self.a_str("_jst.0.invar.2"),
                place=self.a_place("undefined", 0),
                dtype=self.a_dtype("float32"),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.data_962 = self.Op(
            "pd_op.data",
            962,
            input_types=[],
            output_types=[self.t_dtensor([200, 1], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                shape=self.a_intarray(200, 1),
                name=self.a_str("_jst.0.invar.3"),
                place=self.a_place("undefined", 0),
                dtype=self.a_dtype("float32"),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.data_963 = self.Op(
            "pd_op.data",
            963,
            input_types=[],
            output_types=[self.t_dtensor([200, 1], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                shape=self.a_intarray(200, 1),
                name=self.a_str("_jst.0.invar.4"),
                place=self.a_place("undefined", 0),
                dtype=self.a_dtype("float32"),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.full_964 = self.Op(
            "pd_op.full",
            964,
            input_types=[],
            output_types=[self.t_dtensor([1], self.t_i32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                value=self.a_f32("-1"),
                shape=self.a_intarray(1),
                place=self.a_place("cpu"),
                dtype=self.a_dtype("int32"),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.combine_965 = self.Op(
            "builtin.combine",
            965,
            input_types=[
                self.t_dtensor([200, 1], self.t_f32()),
                self.t_dtensor([200, 1], self.t_f32()),
            ],
            output_types=[
                self.t_vec(
                    self.t_dtensor([200, 1], self.t_f32()),
                    self.t_dtensor([200, 1], self.t_f32()),
                )
            ],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.concat_966 = self.Op(
            "pd_op.concat",
            966,
            input_types=[
                self.t_vec(
                    self.t_dtensor([200, 1], self.t_f32()),
                    self.t_dtensor([200, 1], self.t_f32()),
                ),
                self.t_dtensor([1], self.t_i32()),
            ],
            output_types=[self.t_dtensor([200, 2], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.full_967 = self.Op(
            "pd_op.full",
            967,
            input_types=[],
            output_types=[self.t_dtensor([2, 2], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                value=self.a_f32("0"),
                shape=self.a_intarray(2, 2),
                place=self.a_place("undefined", 0),
                dtype=self.a_dtype("float32"),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.full_int_array_968 = self.Op(
            "pd_op.full_int_array",
            968,
            input_types=[],
            output_types=[self.t_dtensor([1], self.t_i64())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                dtype=self.a_dtype("int64"),
                place=self.a_place("cpu"),
                value=self.a_array(self.a_i64(0)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.full_int_array_969 = self.Op(
            "pd_op.full_int_array",
            969,
            input_types=[],
            output_types=[self.t_dtensor([1], self.t_i64())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                dtype=self.a_dtype("int64"),
                place=self.a_place("cpu"),
                value=self.a_array(self.a_i64(1)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.slice_970 = self.Op(
            "pd_op.slice",
            970,
            input_types=[
                self.t_dtensor([2], self.t_i64()),
                self.t_dtensor([1], self.t_i64()),
                self.t_dtensor([1], self.t_i64()),
            ],
            output_types=[self.t_dtensor([], self.t_i64())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                decrease_axis=self.a_array(self.a_i64(0)),
                infer_flags=self.a_array(self.a_i64(1)),
                axes=self.a_array(self.a_i64(0)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()),
                    self.a_symbol(self.s_null()),
                    self.a_symbol(self.s_null()),
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.full_971 = self.Op(
            "pd_op.full",
            971,
            input_types=[],
            output_types=[self.t_dtensor([1], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                value=self.a_f32("1"),
                shape=self.a_intarray(1),
                place=self.a_place("cpu"),
                dtype=self.a_dtype("float32"),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.scale_972 = self.Op(
            "pd_op.scale",
            972,
            input_types=[
                self.t_dtensor([], self.t_i64()),
                self.t_dtensor([1], self.t_f32()),
            ],
            output_types=[self.t_dtensor([], self.t_i64())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                bias_after_scale=self.a_bool(True),
                bias=self.a_f32("1"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.full_973 = self.Op(
            "pd_op.full",
            973,
            input_types=[],
            output_types=[self.t_dtensor([1], self.t_i32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                value=self.a_f32("0"),
                shape=self.a_intarray(1),
                place=self.a_place("cpu"),
                dtype=self.a_dtype("int32"),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.full_974 = self.Op(
            "pd_op.full",
            974,
            input_types=[],
            output_types=[self.t_dtensor([1], self.t_i32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                value=self.a_f32("1"),
                shape=self.a_intarray(1),
                place=self.a_place("cpu"),
                dtype=self.a_dtype("int32"),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.full_975 = self.Op(
            "pd_op.full",
            975,
            input_types=[],
            output_types=[self.t_dtensor([], self.t_i64())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                value=self.a_f32("0"),
                shape=self.a_intarray(),
                place=self.a_place("cpu"),
                dtype=self.a_dtype("int64"),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.full_976 = self.Op(
            "pd_op.full",
            976,
            input_types=[],
            output_types=[self.t_dtensor([], self.t_i64())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                value=self.a_f32("1"),
                shape=self.a_intarray(),
                place=self.a_place("cpu"),
                dtype=self.a_dtype("int64"),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.combine_977 = self.Op(
            "builtin.combine",
            977,
            input_types=[
                self.t_dtensor([], self.t_i64()),
                self.t_dtensor([], self.t_i64()),
            ],
            output_types=[
                self.t_vec(
                    self.t_dtensor([], self.t_i64()), self.t_dtensor([], self.t_i64())
                )
            ],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.full_int_array_978 = self.Op(
            "pd_op.full_int_array",
            978,
            input_types=[],
            output_types=[self.t_dtensor([1], self.t_i64())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                dtype=self.a_dtype("int64"),
                place=self.a_place("cpu"),
                value=self.a_array(self.a_i64(1)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.reshape_979 = self.Op(
            "pd_op.reshape",
            979,
            input_types=[
                self.t_dtensor([], self.t_i64()),
                self.t_dtensor([1], self.t_i64()),
            ],
            output_types=[
                self.t_dtensor([1], self.t_i64()),
                self.t_dtensor([0], self.t_i64()),
            ],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True), self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
            ),
        )

        self.full_int_array_980 = self.Op(
            "pd_op.full_int_array",
            980,
            input_types=[],
            output_types=[self.t_dtensor([1], self.t_i64())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                dtype=self.a_dtype("int64"),
                place=self.a_place("cpu"),
                value=self.a_array(self.a_i64(1)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.reshape_981 = self.Op(
            "pd_op.reshape",
            981,
            input_types=[
                self.t_dtensor([], self.t_i64()),
                self.t_dtensor([1], self.t_i64()),
            ],
            output_types=[
                self.t_dtensor([1], self.t_i64()),
                self.t_dtensor([0], self.t_i64()),
            ],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True), self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
            ),
        )

        self.combine_982 = self.Op(
            "builtin.combine",
            982,
            input_types=[
                self.t_dtensor([1], self.t_i64()),
                self.t_dtensor([1], self.t_i64()),
            ],
            output_types=[
                self.t_vec(
                    self.t_dtensor([1], self.t_i64()), self.t_dtensor([1], self.t_i64())
                )
            ],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.full_983 = self.Op(
            "pd_op.full",
            983,
            input_types=[],
            output_types=[self.t_dtensor([1], self.t_i32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                value=self.a_f32("0"),
                shape=self.a_intarray(1),
                place=self.a_place("cpu"),
                dtype=self.a_dtype("int32"),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.concat_984 = self.Op(
            "pd_op.concat",
            984,
            input_types=[
                self.t_vec(
                    self.t_dtensor([1], self.t_i64()), self.t_dtensor([1], self.t_i64())
                ),
                self.t_dtensor([1], self.t_i32()),
            ],
            output_types=[self.t_dtensor([2], self.t_i64())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.combine_985 = self.Op(
            "builtin.combine",
            985,
            input_types=[
                self.t_dtensor([], self.t_i64()),
                self.t_dtensor([], self.t_i64()),
            ],
            output_types=[
                self.t_vec(
                    self.t_dtensor([], self.t_i64()), self.t_dtensor([], self.t_i64())
                )
            ],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.full_int_array_986 = self.Op(
            "pd_op.full_int_array",
            986,
            input_types=[],
            output_types=[self.t_dtensor([1], self.t_i64())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                dtype=self.a_dtype("int64"),
                place=self.a_place("cpu"),
                value=self.a_array(self.a_i64(1)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.reshape_987 = self.Op(
            "pd_op.reshape",
            987,
            input_types=[
                self.t_dtensor([], self.t_i64()),
                self.t_dtensor([1], self.t_i64()),
            ],
            output_types=[
                self.t_dtensor([1], self.t_i64()),
                self.t_dtensor([0], self.t_i64()),
            ],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True), self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
            ),
        )

        self.full_int_array_988 = self.Op(
            "pd_op.full_int_array",
            988,
            input_types=[],
            output_types=[self.t_dtensor([1], self.t_i64())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                dtype=self.a_dtype("int64"),
                place=self.a_place("cpu"),
                value=self.a_array(self.a_i64(1)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.reshape_989 = self.Op(
            "pd_op.reshape",
            989,
            input_types=[
                self.t_dtensor([], self.t_i64()),
                self.t_dtensor([1], self.t_i64()),
            ],
            output_types=[
                self.t_dtensor([1], self.t_i64()),
                self.t_dtensor([0], self.t_i64()),
            ],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True), self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
            ),
        )

        self.combine_990 = self.Op(
            "builtin.combine",
            990,
            input_types=[
                self.t_dtensor([1], self.t_i64()),
                self.t_dtensor([1], self.t_i64()),
            ],
            output_types=[
                self.t_vec(
                    self.t_dtensor([1], self.t_i64()), self.t_dtensor([1], self.t_i64())
                )
            ],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.full_991 = self.Op(
            "pd_op.full",
            991,
            input_types=[],
            output_types=[self.t_dtensor([1], self.t_i32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                value=self.a_f32("0"),
                shape=self.a_intarray(1),
                place=self.a_place("cpu"),
                dtype=self.a_dtype("int32"),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.concat_992 = self.Op(
            "pd_op.concat",
            992,
            input_types=[
                self.t_vec(
                    self.t_dtensor([1], self.t_i64()), self.t_dtensor([1], self.t_i64())
                ),
                self.t_dtensor([1], self.t_i32()),
            ],
            output_types=[self.t_dtensor([2], self.t_i64())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.full_int_array_993 = self.Op(
            "pd_op.full_int_array",
            993,
            input_types=[],
            output_types=[self.t_dtensor([2], self.t_i64())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                dtype=self.a_dtype("int64"),
                place=self.a_place("cpu"),
                value=self.a_array(self.a_i64(1), self.a_i64(1)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.set_value__994 = self.Op(
            "pd_op.set_value_",
            994,
            input_types=[
                self.t_dtensor([2, 2], self.t_f32()),
                self.t_dtensor([2], self.t_i64()),
                self.t_dtensor([2], self.t_i64()),
                self.t_dtensor([2], self.t_i64()),
            ],
            output_types=[self.t_dtensor([2, 2], self.t_f32())],
            attrs=dict(
                none_axes=self.a_array(),
                shape=self.a_array(self.a_i64(1)),
                values=self.a_array(self.a_f64("1")),
                axes=self.a_array(self.a_i64(0), self.a_i64(1)),
                decrease_axes=self.a_array(self.a_i64(0), self.a_i64(1)),
                stop_gradient=self.a_array(self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()),
                    self.a_symbol(self.s_null()),
                    self.a_symbol(self.s_null()),
                    self.a_symbol(self.s_null()),
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.full_int_array_995 = self.Op(
            "pd_op.full_int_array",
            995,
            input_types=[],
            output_types=[self.t_dtensor([1], self.t_i64())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                dtype=self.a_dtype("int64"),
                place=self.a_place("cpu"),
                value=self.a_array(self.a_i64(1)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.full_int_array_996 = self.Op(
            "pd_op.full_int_array",
            996,
            input_types=[],
            output_types=[self.t_dtensor([1], self.t_i64())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                dtype=self.a_dtype("int64"),
                place=self.a_place("cpu"),
                value=self.a_array(self.a_i64(2)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.slice_997 = self.Op(
            "pd_op.slice",
            997,
            input_types=[
                self.t_dtensor([2], self.t_i64()),
                self.t_dtensor([1], self.t_i64()),
                self.t_dtensor([1], self.t_i64()),
            ],
            output_types=[self.t_dtensor([], self.t_i64())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                decrease_axis=self.a_array(self.a_i64(0)),
                infer_flags=self.a_array(self.a_i64(1)),
                axes=self.a_array(self.a_i64(0)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()),
                    self.a_symbol(self.s_null()),
                    self.a_symbol(self.s_null()),
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.full_998 = self.Op(
            "pd_op.full",
            998,
            input_types=[],
            output_types=[self.t_dtensor([1], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                value=self.a_f32("1"),
                shape=self.a_intarray(1),
                place=self.a_place("cpu"),
                dtype=self.a_dtype("float32"),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.scale_999 = self.Op(
            "pd_op.scale",
            999,
            input_types=[
                self.t_dtensor([], self.t_i64()),
                self.t_dtensor([1], self.t_f32()),
            ],
            output_types=[self.t_dtensor([], self.t_i64())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                bias_after_scale=self.a_bool(True),
                bias=self.a_f32("1"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.full_1000 = self.Op(
            "pd_op.full",
            1000,
            input_types=[],
            output_types=[self.t_dtensor([1], self.t_i32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                value=self.a_f32("1"),
                shape=self.a_intarray(1),
                place=self.a_place("cpu"),
                dtype=self.a_dtype("int32"),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.full_1001 = self.Op(
            "pd_op.full",
            1001,
            input_types=[],
            output_types=[self.t_dtensor([1], self.t_i32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                value=self.a_f32("2"),
                shape=self.a_intarray(1),
                place=self.a_place("cpu"),
                dtype=self.a_dtype("int32"),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.full_1002 = self.Op(
            "pd_op.full",
            1002,
            input_types=[],
            output_types=[self.t_dtensor([], self.t_i64())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                value=self.a_f32("1"),
                shape=self.a_intarray(),
                place=self.a_place("cpu"),
                dtype=self.a_dtype("int64"),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.full_1003 = self.Op(
            "pd_op.full",
            1003,
            input_types=[],
            output_types=[self.t_dtensor([], self.t_i64())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                value=self.a_f32("2"),
                shape=self.a_intarray(),
                place=self.a_place("cpu"),
                dtype=self.a_dtype("int64"),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.combine_1004 = self.Op(
            "builtin.combine",
            1004,
            input_types=[
                self.t_dtensor([], self.t_i64()),
                self.t_dtensor([], self.t_i64()),
            ],
            output_types=[
                self.t_vec(
                    self.t_dtensor([], self.t_i64()), self.t_dtensor([], self.t_i64())
                )
            ],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.full_int_array_1005 = self.Op(
            "pd_op.full_int_array",
            1005,
            input_types=[],
            output_types=[self.t_dtensor([1], self.t_i64())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                dtype=self.a_dtype("int64"),
                place=self.a_place("cpu"),
                value=self.a_array(self.a_i64(1)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.reshape_1006 = self.Op(
            "pd_op.reshape",
            1006,
            input_types=[
                self.t_dtensor([], self.t_i64()),
                self.t_dtensor([1], self.t_i64()),
            ],
            output_types=[
                self.t_dtensor([1], self.t_i64()),
                self.t_dtensor([0], self.t_i64()),
            ],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True), self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
            ),
        )

        self.full_int_array_1007 = self.Op(
            "pd_op.full_int_array",
            1007,
            input_types=[],
            output_types=[self.t_dtensor([1], self.t_i64())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                dtype=self.a_dtype("int64"),
                place=self.a_place("cpu"),
                value=self.a_array(self.a_i64(1)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.reshape_1008 = self.Op(
            "pd_op.reshape",
            1008,
            input_types=[
                self.t_dtensor([], self.t_i64()),
                self.t_dtensor([1], self.t_i64()),
            ],
            output_types=[
                self.t_dtensor([1], self.t_i64()),
                self.t_dtensor([0], self.t_i64()),
            ],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True), self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
            ),
        )

        self.combine_1009 = self.Op(
            "builtin.combine",
            1009,
            input_types=[
                self.t_dtensor([1], self.t_i64()),
                self.t_dtensor([1], self.t_i64()),
            ],
            output_types=[
                self.t_vec(
                    self.t_dtensor([1], self.t_i64()), self.t_dtensor([1], self.t_i64())
                )
            ],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.full_1010 = self.Op(
            "pd_op.full",
            1010,
            input_types=[],
            output_types=[self.t_dtensor([1], self.t_i32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                value=self.a_f32("0"),
                shape=self.a_intarray(1),
                place=self.a_place("cpu"),
                dtype=self.a_dtype("int32"),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.concat_1011 = self.Op(
            "pd_op.concat",
            1011,
            input_types=[
                self.t_vec(
                    self.t_dtensor([1], self.t_i64()), self.t_dtensor([1], self.t_i64())
                ),
                self.t_dtensor([1], self.t_i32()),
            ],
            output_types=[self.t_dtensor([2], self.t_i64())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.combine_1012 = self.Op(
            "builtin.combine",
            1012,
            input_types=[
                self.t_dtensor([], self.t_i64()),
                self.t_dtensor([], self.t_i64()),
            ],
            output_types=[
                self.t_vec(
                    self.t_dtensor([], self.t_i64()), self.t_dtensor([], self.t_i64())
                )
            ],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.full_int_array_1013 = self.Op(
            "pd_op.full_int_array",
            1013,
            input_types=[],
            output_types=[self.t_dtensor([1], self.t_i64())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                dtype=self.a_dtype("int64"),
                place=self.a_place("cpu"),
                value=self.a_array(self.a_i64(1)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.reshape_1014 = self.Op(
            "pd_op.reshape",
            1014,
            input_types=[
                self.t_dtensor([], self.t_i64()),
                self.t_dtensor([1], self.t_i64()),
            ],
            output_types=[
                self.t_dtensor([1], self.t_i64()),
                self.t_dtensor([0], self.t_i64()),
            ],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True), self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
            ),
        )

        self.full_int_array_1015 = self.Op(
            "pd_op.full_int_array",
            1015,
            input_types=[],
            output_types=[self.t_dtensor([1], self.t_i64())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                dtype=self.a_dtype("int64"),
                place=self.a_place("cpu"),
                value=self.a_array(self.a_i64(1)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.reshape_1016 = self.Op(
            "pd_op.reshape",
            1016,
            input_types=[
                self.t_dtensor([], self.t_i64()),
                self.t_dtensor([1], self.t_i64()),
            ],
            output_types=[
                self.t_dtensor([1], self.t_i64()),
                self.t_dtensor([0], self.t_i64()),
            ],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True), self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
            ),
        )

        self.combine_1017 = self.Op(
            "builtin.combine",
            1017,
            input_types=[
                self.t_dtensor([1], self.t_i64()),
                self.t_dtensor([1], self.t_i64()),
            ],
            output_types=[
                self.t_vec(
                    self.t_dtensor([1], self.t_i64()), self.t_dtensor([1], self.t_i64())
                )
            ],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.full_1018 = self.Op(
            "pd_op.full",
            1018,
            input_types=[],
            output_types=[self.t_dtensor([1], self.t_i32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                value=self.a_f32("0"),
                shape=self.a_intarray(1),
                place=self.a_place("cpu"),
                dtype=self.a_dtype("int32"),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.concat_1019 = self.Op(
            "pd_op.concat",
            1019,
            input_types=[
                self.t_vec(
                    self.t_dtensor([1], self.t_i64()), self.t_dtensor([1], self.t_i64())
                ),
                self.t_dtensor([1], self.t_i32()),
            ],
            output_types=[self.t_dtensor([2], self.t_i64())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.full_int_array_1020 = self.Op(
            "pd_op.full_int_array",
            1020,
            input_types=[],
            output_types=[self.t_dtensor([2], self.t_i64())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                dtype=self.a_dtype("int64"),
                place=self.a_place("cpu"),
                value=self.a_array(self.a_i64(1), self.a_i64(1)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.set_value__1021 = self.Op(
            "pd_op.set_value_",
            1021,
            input_types=[
                self.t_dtensor([2, 2], self.t_f32()),
                self.t_dtensor([2], self.t_i64()),
                self.t_dtensor([2], self.t_i64()),
                self.t_dtensor([2], self.t_i64()),
            ],
            output_types=[self.t_dtensor([2, 2], self.t_f32())],
            attrs=dict(
                none_axes=self.a_array(),
                shape=self.a_array(self.a_i64(1)),
                values=self.a_array(self.a_f64("1")),
                axes=self.a_array(self.a_i64(0), self.a_i64(1)),
                decrease_axes=self.a_array(self.a_i64(0), self.a_i64(1)),
                stop_gradient=self.a_array(self.a_bool(True)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()),
                    self.a_symbol(self.s_null()),
                    self.a_symbol(self.s_null()),
                    self.a_symbol(self.s_null()),
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.matmul_1022 = self.Op(
            "pd_op.matmul",
            1022,
            input_types=[
                self.t_dtensor([200, 2], self.t_f32()),
                self.t_dtensor([2, 2], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 2], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                transpose_y=self.a_bool(False),
                transpose_x=self.a_bool(False),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.matmul_1023 = self.Op(
            "pd_op.matmul",
            1023,
            input_types=[
                self.t_dtensor([200, 2], self.t_f32()),
                self.t_dtensor([2, 128], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 128], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                transpose_y=self.a_bool(False),
                transpose_x=self.a_bool(False),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.full_1024 = self.Op(
            "pd_op.full",
            1024,
            input_types=[],
            output_types=[self.t_dtensor([1], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                value=self.a_f32("6.28319"),
                shape=self.a_intarray(1),
                place=self.a_place("cpu"),
                dtype=self.a_dtype("float32"),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.scale_1025 = self.Op(
            "pd_op.scale",
            1025,
            input_types=[
                self.t_dtensor([200, 128], self.t_f32()),
                self.t_dtensor([1], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 128], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                bias_after_scale=self.a_bool(True),
                bias=self.a_f32("0"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.sin_1026 = self.Op(
            "pd_op.sin",
            1026,
            input_types=[self.t_dtensor([200, 128], self.t_f32())],
            output_types=[self.t_dtensor([200, 128], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.full_1027 = self.Op(
            "pd_op.full",
            1027,
            input_types=[],
            output_types=[self.t_dtensor([1], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                value=self.a_f32("6.28319"),
                shape=self.a_intarray(1),
                place=self.a_place("cpu"),
                dtype=self.a_dtype("float32"),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.scale_1028 = self.Op(
            "pd_op.scale",
            1028,
            input_types=[
                self.t_dtensor([200, 128], self.t_f32()),
                self.t_dtensor([1], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 128], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                bias_after_scale=self.a_bool(True),
                bias=self.a_f32("0"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.cos_1029 = self.Op(
            "pd_op.cos",
            1029,
            input_types=[self.t_dtensor([200, 128], self.t_f32())],
            output_types=[self.t_dtensor([200, 128], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.full_1030 = self.Op(
            "pd_op.full",
            1030,
            input_types=[],
            output_types=[self.t_dtensor([1], self.t_i32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                value=self.a_f32("-1"),
                shape=self.a_intarray(1),
                place=self.a_place("cpu"),
                dtype=self.a_dtype("int32"),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.combine_1031 = self.Op(
            "builtin.combine",
            1031,
            input_types=[
                self.t_dtensor([200, 128], self.t_f32()),
                self.t_dtensor([200, 128], self.t_f32()),
            ],
            output_types=[
                self.t_vec(
                    self.t_dtensor([200, 128], self.t_f32()),
                    self.t_dtensor([200, 128], self.t_f32()),
                )
            ],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.concat_1032 = self.Op(
            "pd_op.concat",
            1032,
            input_types=[
                self.t_vec(
                    self.t_dtensor([200, 128], self.t_f32()),
                    self.t_dtensor([200, 128], self.t_f32()),
                ),
                self.t_dtensor([1], self.t_i32()),
            ],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.full_1033 = self.Op(
            "pd_op.full",
            1033,
            input_types=[],
            output_types=[self.t_dtensor([1], self.t_i32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                value=self.a_f32("-1"),
                shape=self.a_intarray(1),
                place=self.a_place("cpu"),
                dtype=self.a_dtype("int32"),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.combine_1034 = self.Op(
            "builtin.combine",
            1034,
            input_types=[
                self.t_dtensor([200, 2], self.t_f32()),
                self.t_dtensor([200, 256], self.t_f32()),
            ],
            output_types=[
                self.t_vec(
                    self.t_dtensor([200, 2], self.t_f32()),
                    self.t_dtensor([200, 256], self.t_f32()),
                )
            ],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.concat_1035 = self.Op(
            "pd_op.concat",
            1035,
            input_types=[
                self.t_vec(
                    self.t_dtensor([200, 2], self.t_f32()),
                    self.t_dtensor([200, 256], self.t_f32()),
                ),
                self.t_dtensor([1], self.t_i32()),
            ],
            output_types=[self.t_dtensor([200, 258], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.multiply_1036 = self.Op(
            "pd_op.multiply",
            1036,
            input_types=[
                self.t_dtensor([256, 258], self.t_f32()),
                self.t_dtensor([256, 258], self.t_f32()),
            ],
            output_types=[self.t_dtensor([256, 258], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.full_int_array_1037 = self.Op(
            "pd_op.full_int_array",
            1037,
            input_types=[],
            output_types=[self.t_dtensor([1], self.t_i64())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                dtype=self.a_dtype("int64"),
                place=self.a_place("cpu"),
                value=self.a_array(self.a_i64(1)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.sum_1038 = self.Op(
            "pd_op.sum",
            1038,
            input_types=[
                self.t_dtensor([256, 258], self.t_f32()),
                self.t_dtensor([1], self.t_i64()),
            ],
            output_types=[self.t_dtensor([256, 1], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                keepdim=self.a_bool(True),
                dtype=self.a_dtype("float32"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.sqrt_1039 = self.Op(
            "pd_op.sqrt",
            1039,
            input_types=[self.t_dtensor([256, 1], self.t_f32())],
            output_types=[self.t_dtensor([256, 1], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.multiply_1040 = self.Op(
            "pd_op.multiply",
            1040,
            input_types=[
                self.t_dtensor([256, 1], self.t_f32()),
                self.t_dtensor([256, 258], self.t_f32()),
            ],
            output_types=[self.t_dtensor([256, 258], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.divide_1041 = self.Op(
            "pd_op.divide",
            1041,
            input_types=[
                self.t_dtensor([256, 258], self.t_f32()),
                self.t_dtensor([256, 1], self.t_f32()),
            ],
            output_types=[self.t_dtensor([256, 258], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.transpose_1042 = self.Op(
            "pd_op.transpose",
            1042,
            input_types=[self.t_dtensor([256, 258], self.t_f32())],
            output_types=[self.t_dtensor([258, 256], self.t_f32())],
            attrs=dict(
                perm=self.a_array(self.a_i32(1), self.a_i32(0)),
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.matmul_1043 = self.Op(
            "pd_op.matmul",
            1043,
            input_types=[
                self.t_dtensor([200, 258], self.t_f32()),
                self.t_dtensor([258, 256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                transpose_y=self.a_bool(False),
                transpose_x=self.a_bool(False),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.add_1044 = self.Op(
            "pd_op.add",
            1044,
            input_types=[
                self.t_dtensor([200, 256], self.t_f32()),
                self.t_dtensor([256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.sigmoid_1045 = self.Op(
            "pd_op.sigmoid",
            1045,
            input_types=[self.t_dtensor([200, 256], self.t_f32())],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.multiply_1046 = self.Op(
            "pd_op.multiply",
            1046,
            input_types=[
                self.t_dtensor([200, 256], self.t_f32()),
                self.t_dtensor([200, 256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.multiply_1047 = self.Op(
            "pd_op.multiply",
            1047,
            input_types=[
                self.t_dtensor([256, 258], self.t_f32()),
                self.t_dtensor([256, 258], self.t_f32()),
            ],
            output_types=[self.t_dtensor([256, 258], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.full_int_array_1048 = self.Op(
            "pd_op.full_int_array",
            1048,
            input_types=[],
            output_types=[self.t_dtensor([1], self.t_i64())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                dtype=self.a_dtype("int64"),
                place=self.a_place("cpu"),
                value=self.a_array(self.a_i64(1)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.sum_1049 = self.Op(
            "pd_op.sum",
            1049,
            input_types=[
                self.t_dtensor([256, 258], self.t_f32()),
                self.t_dtensor([1], self.t_i64()),
            ],
            output_types=[self.t_dtensor([256, 1], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                keepdim=self.a_bool(True),
                dtype=self.a_dtype("float32"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.sqrt_1050 = self.Op(
            "pd_op.sqrt",
            1050,
            input_types=[self.t_dtensor([256, 1], self.t_f32())],
            output_types=[self.t_dtensor([256, 1], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.multiply_1051 = self.Op(
            "pd_op.multiply",
            1051,
            input_types=[
                self.t_dtensor([256, 1], self.t_f32()),
                self.t_dtensor([256, 258], self.t_f32()),
            ],
            output_types=[self.t_dtensor([256, 258], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.divide_1052 = self.Op(
            "pd_op.divide",
            1052,
            input_types=[
                self.t_dtensor([256, 258], self.t_f32()),
                self.t_dtensor([256, 1], self.t_f32()),
            ],
            output_types=[self.t_dtensor([256, 258], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.transpose_1053 = self.Op(
            "pd_op.transpose",
            1053,
            input_types=[self.t_dtensor([256, 258], self.t_f32())],
            output_types=[self.t_dtensor([258, 256], self.t_f32())],
            attrs=dict(
                perm=self.a_array(self.a_i32(1), self.a_i32(0)),
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.matmul_1054 = self.Op(
            "pd_op.matmul",
            1054,
            input_types=[
                self.t_dtensor([200, 258], self.t_f32()),
                self.t_dtensor([258, 256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                transpose_y=self.a_bool(False),
                transpose_x=self.a_bool(False),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.add_1055 = self.Op(
            "pd_op.add",
            1055,
            input_types=[
                self.t_dtensor([200, 256], self.t_f32()),
                self.t_dtensor([256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.sigmoid_1056 = self.Op(
            "pd_op.sigmoid",
            1056,
            input_types=[self.t_dtensor([200, 256], self.t_f32())],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.multiply_1057 = self.Op(
            "pd_op.multiply",
            1057,
            input_types=[
                self.t_dtensor([200, 256], self.t_f32()),
                self.t_dtensor([200, 256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.multiply_1058 = self.Op(
            "pd_op.multiply",
            1058,
            input_types=[
                self.t_dtensor([256, 258], self.t_f32()),
                self.t_dtensor([256, 258], self.t_f32()),
            ],
            output_types=[self.t_dtensor([256, 258], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.full_int_array_1059 = self.Op(
            "pd_op.full_int_array",
            1059,
            input_types=[],
            output_types=[self.t_dtensor([1], self.t_i64())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                dtype=self.a_dtype("int64"),
                place=self.a_place("cpu"),
                value=self.a_array(self.a_i64(1)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.sum_1060 = self.Op(
            "pd_op.sum",
            1060,
            input_types=[
                self.t_dtensor([256, 258], self.t_f32()),
                self.t_dtensor([1], self.t_i64()),
            ],
            output_types=[self.t_dtensor([256, 1], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                keepdim=self.a_bool(True),
                dtype=self.a_dtype("float32"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.sqrt_1061 = self.Op(
            "pd_op.sqrt",
            1061,
            input_types=[self.t_dtensor([256, 1], self.t_f32())],
            output_types=[self.t_dtensor([256, 1], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.multiply_1062 = self.Op(
            "pd_op.multiply",
            1062,
            input_types=[
                self.t_dtensor([256, 1], self.t_f32()),
                self.t_dtensor([256, 258], self.t_f32()),
            ],
            output_types=[self.t_dtensor([256, 258], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.divide_1063 = self.Op(
            "pd_op.divide",
            1063,
            input_types=[
                self.t_dtensor([256, 258], self.t_f32()),
                self.t_dtensor([256, 1], self.t_f32()),
            ],
            output_types=[self.t_dtensor([256, 258], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.transpose_1064 = self.Op(
            "pd_op.transpose",
            1064,
            input_types=[self.t_dtensor([256, 258], self.t_f32())],
            output_types=[self.t_dtensor([258, 256], self.t_f32())],
            attrs=dict(
                perm=self.a_array(self.a_i32(1), self.a_i32(0)),
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.matmul_1065 = self.Op(
            "pd_op.matmul",
            1065,
            input_types=[
                self.t_dtensor([200, 258], self.t_f32()),
                self.t_dtensor([258, 256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                transpose_y=self.a_bool(False),
                transpose_x=self.a_bool(False),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.add_1066 = self.Op(
            "pd_op.add",
            1066,
            input_types=[
                self.t_dtensor([200, 256], self.t_f32()),
                self.t_dtensor([256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.sigmoid_1067 = self.Op(
            "pd_op.sigmoid",
            1067,
            input_types=[self.t_dtensor([200, 256], self.t_f32())],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.multiply_1068 = self.Op(
            "pd_op.multiply",
            1068,
            input_types=[
                self.t_dtensor([200, 256], self.t_f32()),
                self.t_dtensor([200, 256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.multiply_1069 = self.Op(
            "pd_op.multiply",
            1069,
            input_types=[
                self.t_dtensor([256, 256], self.t_f32()),
                self.t_dtensor([256, 256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([256, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.full_int_array_1070 = self.Op(
            "pd_op.full_int_array",
            1070,
            input_types=[],
            output_types=[self.t_dtensor([1], self.t_i64())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                dtype=self.a_dtype("int64"),
                place=self.a_place("cpu"),
                value=self.a_array(self.a_i64(1)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.sum_1071 = self.Op(
            "pd_op.sum",
            1071,
            input_types=[
                self.t_dtensor([256, 256], self.t_f32()),
                self.t_dtensor([1], self.t_i64()),
            ],
            output_types=[self.t_dtensor([256, 1], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                keepdim=self.a_bool(True),
                dtype=self.a_dtype("float32"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.sqrt_1072 = self.Op(
            "pd_op.sqrt",
            1072,
            input_types=[self.t_dtensor([256, 1], self.t_f32())],
            output_types=[self.t_dtensor([256, 1], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.multiply_1073 = self.Op(
            "pd_op.multiply",
            1073,
            input_types=[
                self.t_dtensor([256, 1], self.t_f32()),
                self.t_dtensor([256, 256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([256, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.divide_1074 = self.Op(
            "pd_op.divide",
            1074,
            input_types=[
                self.t_dtensor([256, 256], self.t_f32()),
                self.t_dtensor([256, 1], self.t_f32()),
            ],
            output_types=[self.t_dtensor([256, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.transpose_1075 = self.Op(
            "pd_op.transpose",
            1075,
            input_types=[self.t_dtensor([256, 256], self.t_f32())],
            output_types=[self.t_dtensor([256, 256], self.t_f32())],
            attrs=dict(
                perm=self.a_array(self.a_i32(1), self.a_i32(0)),
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.matmul_1076 = self.Op(
            "pd_op.matmul",
            1076,
            input_types=[
                self.t_dtensor([200, 256], self.t_f32()),
                self.t_dtensor([256, 256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                transpose_y=self.a_bool(False),
                transpose_x=self.a_bool(False),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.add_1077 = self.Op(
            "pd_op.add",
            1077,
            input_types=[
                self.t_dtensor([200, 256], self.t_f32()),
                self.t_dtensor([256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.sigmoid_1078 = self.Op(
            "pd_op.sigmoid",
            1078,
            input_types=[self.t_dtensor([200, 256], self.t_f32())],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.multiply_1079 = self.Op(
            "pd_op.multiply",
            1079,
            input_types=[
                self.t_dtensor([200, 256], self.t_f32()),
                self.t_dtensor([200, 256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.multiply_1080 = self.Op(
            "pd_op.multiply",
            1080,
            input_types=[
                self.t_dtensor([200, 256], self.t_f32()),
                self.t_dtensor([200, 256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.subtract_1081 = self.Op(
            "pd_op.subtract",
            1081,
            input_types=[
                self.t_dtensor([200, 256], self.t_f32()),
                self.t_dtensor([200, 256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.multiply_1082 = self.Op(
            "pd_op.multiply",
            1082,
            input_types=[
                self.t_dtensor([200, 256], self.t_f32()),
                self.t_dtensor([200, 256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.add_1083 = self.Op(
            "pd_op.add",
            1083,
            input_types=[
                self.t_dtensor([200, 256], self.t_f32()),
                self.t_dtensor([200, 256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.multiply_1084 = self.Op(
            "pd_op.multiply",
            1084,
            input_types=[
                self.t_dtensor([256, 256], self.t_f32()),
                self.t_dtensor([256, 256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([256, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.full_int_array_1085 = self.Op(
            "pd_op.full_int_array",
            1085,
            input_types=[],
            output_types=[self.t_dtensor([1], self.t_i64())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                dtype=self.a_dtype("int64"),
                place=self.a_place("cpu"),
                value=self.a_array(self.a_i64(1)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.sum_1086 = self.Op(
            "pd_op.sum",
            1086,
            input_types=[
                self.t_dtensor([256, 256], self.t_f32()),
                self.t_dtensor([1], self.t_i64()),
            ],
            output_types=[self.t_dtensor([256, 1], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                keepdim=self.a_bool(True),
                dtype=self.a_dtype("float32"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.sqrt_1087 = self.Op(
            "pd_op.sqrt",
            1087,
            input_types=[self.t_dtensor([256, 1], self.t_f32())],
            output_types=[self.t_dtensor([256, 1], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.multiply_1088 = self.Op(
            "pd_op.multiply",
            1088,
            input_types=[
                self.t_dtensor([256, 1], self.t_f32()),
                self.t_dtensor([256, 256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([256, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.divide_1089 = self.Op(
            "pd_op.divide",
            1089,
            input_types=[
                self.t_dtensor([256, 256], self.t_f32()),
                self.t_dtensor([256, 1], self.t_f32()),
            ],
            output_types=[self.t_dtensor([256, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.transpose_1090 = self.Op(
            "pd_op.transpose",
            1090,
            input_types=[self.t_dtensor([256, 256], self.t_f32())],
            output_types=[self.t_dtensor([256, 256], self.t_f32())],
            attrs=dict(
                perm=self.a_array(self.a_i32(1), self.a_i32(0)),
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.matmul_1091 = self.Op(
            "pd_op.matmul",
            1091,
            input_types=[
                self.t_dtensor([200, 256], self.t_f32()),
                self.t_dtensor([256, 256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                transpose_y=self.a_bool(False),
                transpose_x=self.a_bool(False),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.add_1092 = self.Op(
            "pd_op.add",
            1092,
            input_types=[
                self.t_dtensor([200, 256], self.t_f32()),
                self.t_dtensor([256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.sigmoid_1093 = self.Op(
            "pd_op.sigmoid",
            1093,
            input_types=[self.t_dtensor([200, 256], self.t_f32())],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.multiply_1094 = self.Op(
            "pd_op.multiply",
            1094,
            input_types=[
                self.t_dtensor([200, 256], self.t_f32()),
                self.t_dtensor([200, 256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.multiply_1095 = self.Op(
            "pd_op.multiply",
            1095,
            input_types=[
                self.t_dtensor([200, 256], self.t_f32()),
                self.t_dtensor([200, 256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.subtract_1096 = self.Op(
            "pd_op.subtract",
            1096,
            input_types=[
                self.t_dtensor([200, 256], self.t_f32()),
                self.t_dtensor([200, 256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.multiply_1097 = self.Op(
            "pd_op.multiply",
            1097,
            input_types=[
                self.t_dtensor([200, 256], self.t_f32()),
                self.t_dtensor([200, 256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.add_1098 = self.Op(
            "pd_op.add",
            1098,
            input_types=[
                self.t_dtensor([200, 256], self.t_f32()),
                self.t_dtensor([200, 256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.multiply_1099 = self.Op(
            "pd_op.multiply",
            1099,
            input_types=[
                self.t_dtensor([256, 256], self.t_f32()),
                self.t_dtensor([256, 256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([256, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.full_int_array_1100 = self.Op(
            "pd_op.full_int_array",
            1100,
            input_types=[],
            output_types=[self.t_dtensor([1], self.t_i64())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                dtype=self.a_dtype("int64"),
                place=self.a_place("cpu"),
                value=self.a_array(self.a_i64(1)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.sum_1101 = self.Op(
            "pd_op.sum",
            1101,
            input_types=[
                self.t_dtensor([256, 256], self.t_f32()),
                self.t_dtensor([1], self.t_i64()),
            ],
            output_types=[self.t_dtensor([256, 1], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                keepdim=self.a_bool(True),
                dtype=self.a_dtype("float32"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.sqrt_1102 = self.Op(
            "pd_op.sqrt",
            1102,
            input_types=[self.t_dtensor([256, 1], self.t_f32())],
            output_types=[self.t_dtensor([256, 1], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.multiply_1103 = self.Op(
            "pd_op.multiply",
            1103,
            input_types=[
                self.t_dtensor([256, 1], self.t_f32()),
                self.t_dtensor([256, 256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([256, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.divide_1104 = self.Op(
            "pd_op.divide",
            1104,
            input_types=[
                self.t_dtensor([256, 256], self.t_f32()),
                self.t_dtensor([256, 1], self.t_f32()),
            ],
            output_types=[self.t_dtensor([256, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.transpose_1105 = self.Op(
            "pd_op.transpose",
            1105,
            input_types=[self.t_dtensor([256, 256], self.t_f32())],
            output_types=[self.t_dtensor([256, 256], self.t_f32())],
            attrs=dict(
                perm=self.a_array(self.a_i32(1), self.a_i32(0)),
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.matmul_1106 = self.Op(
            "pd_op.matmul",
            1106,
            input_types=[
                self.t_dtensor([200, 256], self.t_f32()),
                self.t_dtensor([256, 256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                transpose_y=self.a_bool(False),
                transpose_x=self.a_bool(False),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.add_1107 = self.Op(
            "pd_op.add",
            1107,
            input_types=[
                self.t_dtensor([200, 256], self.t_f32()),
                self.t_dtensor([256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.sigmoid_1108 = self.Op(
            "pd_op.sigmoid",
            1108,
            input_types=[self.t_dtensor([200, 256], self.t_f32())],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.multiply_1109 = self.Op(
            "pd_op.multiply",
            1109,
            input_types=[
                self.t_dtensor([200, 256], self.t_f32()),
                self.t_dtensor([200, 256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.multiply_1110 = self.Op(
            "pd_op.multiply",
            1110,
            input_types=[
                self.t_dtensor([200, 256], self.t_f32()),
                self.t_dtensor([200, 256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.subtract_1111 = self.Op(
            "pd_op.subtract",
            1111,
            input_types=[
                self.t_dtensor([200, 256], self.t_f32()),
                self.t_dtensor([200, 256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.multiply_1112 = self.Op(
            "pd_op.multiply",
            1112,
            input_types=[
                self.t_dtensor([200, 256], self.t_f32()),
                self.t_dtensor([200, 256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.add_1113 = self.Op(
            "pd_op.add",
            1113,
            input_types=[
                self.t_dtensor([200, 256], self.t_f32()),
                self.t_dtensor([200, 256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.multiply_1114 = self.Op(
            "pd_op.multiply",
            1114,
            input_types=[
                self.t_dtensor([256, 256], self.t_f32()),
                self.t_dtensor([256, 256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([256, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.full_int_array_1115 = self.Op(
            "pd_op.full_int_array",
            1115,
            input_types=[],
            output_types=[self.t_dtensor([1], self.t_i64())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                dtype=self.a_dtype("int64"),
                place=self.a_place("cpu"),
                value=self.a_array(self.a_i64(1)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.sum_1116 = self.Op(
            "pd_op.sum",
            1116,
            input_types=[
                self.t_dtensor([256, 256], self.t_f32()),
                self.t_dtensor([1], self.t_i64()),
            ],
            output_types=[self.t_dtensor([256, 1], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                keepdim=self.a_bool(True),
                dtype=self.a_dtype("float32"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.sqrt_1117 = self.Op(
            "pd_op.sqrt",
            1117,
            input_types=[self.t_dtensor([256, 1], self.t_f32())],
            output_types=[self.t_dtensor([256, 1], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.multiply_1118 = self.Op(
            "pd_op.multiply",
            1118,
            input_types=[
                self.t_dtensor([256, 1], self.t_f32()),
                self.t_dtensor([256, 256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([256, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.divide_1119 = self.Op(
            "pd_op.divide",
            1119,
            input_types=[
                self.t_dtensor([256, 256], self.t_f32()),
                self.t_dtensor([256, 1], self.t_f32()),
            ],
            output_types=[self.t_dtensor([256, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.transpose_1120 = self.Op(
            "pd_op.transpose",
            1120,
            input_types=[self.t_dtensor([256, 256], self.t_f32())],
            output_types=[self.t_dtensor([256, 256], self.t_f32())],
            attrs=dict(
                perm=self.a_array(self.a_i32(1), self.a_i32(0)),
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.matmul_1121 = self.Op(
            "pd_op.matmul",
            1121,
            input_types=[
                self.t_dtensor([200, 256], self.t_f32()),
                self.t_dtensor([256, 256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                transpose_y=self.a_bool(False),
                transpose_x=self.a_bool(False),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.add_1122 = self.Op(
            "pd_op.add",
            1122,
            input_types=[
                self.t_dtensor([200, 256], self.t_f32()),
                self.t_dtensor([256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.sigmoid_1123 = self.Op(
            "pd_op.sigmoid",
            1123,
            input_types=[self.t_dtensor([200, 256], self.t_f32())],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.multiply_1124 = self.Op(
            "pd_op.multiply",
            1124,
            input_types=[
                self.t_dtensor([200, 256], self.t_f32()),
                self.t_dtensor([200, 256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.multiply_1125 = self.Op(
            "pd_op.multiply",
            1125,
            input_types=[
                self.t_dtensor([200, 256], self.t_f32()),
                self.t_dtensor([200, 256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.subtract_1126 = self.Op(
            "pd_op.subtract",
            1126,
            input_types=[
                self.t_dtensor([200, 256], self.t_f32()),
                self.t_dtensor([200, 256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.multiply_1127 = self.Op(
            "pd_op.multiply",
            1127,
            input_types=[
                self.t_dtensor([200, 256], self.t_f32()),
                self.t_dtensor([200, 256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.add_1128 = self.Op(
            "pd_op.add",
            1128,
            input_types=[
                self.t_dtensor([200, 256], self.t_f32()),
                self.t_dtensor([200, 256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.multiply_1129 = self.Op(
            "pd_op.multiply",
            1129,
            input_types=[
                self.t_dtensor([256, 256], self.t_f32()),
                self.t_dtensor([256, 256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([256, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.full_int_array_1130 = self.Op(
            "pd_op.full_int_array",
            1130,
            input_types=[],
            output_types=[self.t_dtensor([1], self.t_i64())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                dtype=self.a_dtype("int64"),
                place=self.a_place("cpu"),
                value=self.a_array(self.a_i64(1)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.sum_1131 = self.Op(
            "pd_op.sum",
            1131,
            input_types=[
                self.t_dtensor([256, 256], self.t_f32()),
                self.t_dtensor([1], self.t_i64()),
            ],
            output_types=[self.t_dtensor([256, 1], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                keepdim=self.a_bool(True),
                dtype=self.a_dtype("float32"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.sqrt_1132 = self.Op(
            "pd_op.sqrt",
            1132,
            input_types=[self.t_dtensor([256, 1], self.t_f32())],
            output_types=[self.t_dtensor([256, 1], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.multiply_1133 = self.Op(
            "pd_op.multiply",
            1133,
            input_types=[
                self.t_dtensor([256, 1], self.t_f32()),
                self.t_dtensor([256, 256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([256, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.divide_1134 = self.Op(
            "pd_op.divide",
            1134,
            input_types=[
                self.t_dtensor([256, 256], self.t_f32()),
                self.t_dtensor([256, 1], self.t_f32()),
            ],
            output_types=[self.t_dtensor([256, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.transpose_1135 = self.Op(
            "pd_op.transpose",
            1135,
            input_types=[self.t_dtensor([256, 256], self.t_f32())],
            output_types=[self.t_dtensor([256, 256], self.t_f32())],
            attrs=dict(
                perm=self.a_array(self.a_i32(1), self.a_i32(0)),
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.matmul_1136 = self.Op(
            "pd_op.matmul",
            1136,
            input_types=[
                self.t_dtensor([200, 256], self.t_f32()),
                self.t_dtensor([256, 256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                transpose_y=self.a_bool(False),
                transpose_x=self.a_bool(False),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.add_1137 = self.Op(
            "pd_op.add",
            1137,
            input_types=[
                self.t_dtensor([200, 256], self.t_f32()),
                self.t_dtensor([256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.sigmoid_1138 = self.Op(
            "pd_op.sigmoid",
            1138,
            input_types=[self.t_dtensor([200, 256], self.t_f32())],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.multiply_1139 = self.Op(
            "pd_op.multiply",
            1139,
            input_types=[
                self.t_dtensor([200, 256], self.t_f32()),
                self.t_dtensor([200, 256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.multiply_1140 = self.Op(
            "pd_op.multiply",
            1140,
            input_types=[
                self.t_dtensor([200, 256], self.t_f32()),
                self.t_dtensor([200, 256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.subtract_1141 = self.Op(
            "pd_op.subtract",
            1141,
            input_types=[
                self.t_dtensor([200, 256], self.t_f32()),
                self.t_dtensor([200, 256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.multiply_1142 = self.Op(
            "pd_op.multiply",
            1142,
            input_types=[
                self.t_dtensor([200, 256], self.t_f32()),
                self.t_dtensor([200, 256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.add_1143 = self.Op(
            "pd_op.add",
            1143,
            input_types=[
                self.t_dtensor([200, 256], self.t_f32()),
                self.t_dtensor([200, 256], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 256], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.matmul_1144 = self.Op(
            "pd_op.matmul",
            1144,
            input_types=[
                self.t_dtensor([200, 256], self.t_f32()),
                self.t_dtensor([256, 1], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 1], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                transpose_y=self.a_bool(False),
                transpose_x=self.a_bool(False),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.add_1145 = self.Op(
            "pd_op.add",
            1145,
            input_types=[
                self.t_dtensor([200, 1], self.t_f32()),
                self.t_dtensor([1], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 1], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.full_int_array_1146 = self.Op(
            "pd_op.full_int_array",
            1146,
            input_types=[],
            output_types=[self.t_dtensor([1], self.t_i64())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                dtype=self.a_dtype("int64"),
                place=self.a_place("cpu"),
                value=self.a_array(self.a_i64(1)),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.full_1147 = self.Op(
            "pd_op.full",
            1147,
            input_types=[],
            output_types=[self.t_dtensor([1], self.t_i32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                value=self.a_f32("1"),
                shape=self.a_intarray(1),
                place=self.a_place("cpu"),
                dtype=self.a_dtype("int32"),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.split_1148 = self.Op(
            "pd_op.split",
            1148,
            input_types=[
                self.t_dtensor([200, 1], self.t_f32()),
                self.t_dtensor([1], self.t_i64()),
                self.t_dtensor([1], self.t_i32()),
            ],
            output_types=[self.t_vec(self.t_dtensor([200, 1], self.t_f32()))],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()),
                    self.a_symbol(self.s_null()),
                    self.a_symbol(self.s_null()),
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.split_1149 = self.Op(
            "builtin.split",
            1149,
            input_types=[self.t_vec(self.t_dtensor([200, 1], self.t_f32()))],
            output_types=[self.t_dtensor([200, 1], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.full_1150 = self.Op(
            "pd_op.full",
            1150,
            input_types=[],
            output_types=[self.t_dtensor([1], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                value=self.a_f32("1"),
                shape=self.a_intarray(1),
                place=self.a_place("cpu"),
                dtype=self.a_dtype("float32"),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.scale_1151 = self.Op(
            "pd_op.scale",
            1151,
            input_types=[
                self.t_dtensor([200, 1], self.t_f32()),
                self.t_dtensor([1], self.t_f32()),
            ],
            output_types=[self.t_dtensor([200, 1], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                bias_after_scale=self.a_bool(True),
                bias=self.a_f32("70"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.shadow_output_1152 = self.Op(
            "builtin.shadow_output",
            1152,
            input_types=[self.t_dtensor([200, 2], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_1"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1153 = self.Op(
            "builtin.shadow_output",
            1153,
            input_types=[self.t_dtensor([2, 2], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_2"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1154 = self.Op(
            "builtin.shadow_output",
            1154,
            input_types=[self.t_dtensor([200, 2], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_3"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1155 = self.Op(
            "builtin.shadow_output",
            1155,
            input_types=[self.t_dtensor([200, 128], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_4"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1156 = self.Op(
            "builtin.shadow_output",
            1156,
            input_types=[self.t_dtensor([200, 128], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_5"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1157 = self.Op(
            "builtin.shadow_output",
            1157,
            input_types=[self.t_dtensor([200, 258], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_6"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1158 = self.Op(
            "builtin.shadow_output",
            1158,
            input_types=[self.t_dtensor([256, 1], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_7"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1159 = self.Op(
            "builtin.shadow_output",
            1159,
            input_types=[self.t_dtensor([256, 258], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_8"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1160 = self.Op(
            "builtin.shadow_output",
            1160,
            input_types=[self.t_dtensor([258, 256], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_9"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1161 = self.Op(
            "builtin.shadow_output",
            1161,
            input_types=[self.t_dtensor([200, 256], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_10"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1162 = self.Op(
            "builtin.shadow_output",
            1162,
            input_types=[self.t_dtensor([200, 256], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_11"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1163 = self.Op(
            "builtin.shadow_output",
            1163,
            input_types=[self.t_dtensor([256, 1], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_12"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1164 = self.Op(
            "builtin.shadow_output",
            1164,
            input_types=[self.t_dtensor([256, 258], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_13"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1165 = self.Op(
            "builtin.shadow_output",
            1165,
            input_types=[self.t_dtensor([258, 256], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_14"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1166 = self.Op(
            "builtin.shadow_output",
            1166,
            input_types=[self.t_dtensor([200, 256], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_15"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1167 = self.Op(
            "builtin.shadow_output",
            1167,
            input_types=[self.t_dtensor([200, 256], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_16"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1168 = self.Op(
            "builtin.shadow_output",
            1168,
            input_types=[self.t_dtensor([256, 1], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_17"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1169 = self.Op(
            "builtin.shadow_output",
            1169,
            input_types=[self.t_dtensor([256, 258], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_18"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1170 = self.Op(
            "builtin.shadow_output",
            1170,
            input_types=[self.t_dtensor([258, 256], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_19"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1171 = self.Op(
            "builtin.shadow_output",
            1171,
            input_types=[self.t_dtensor([200, 256], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_20"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1172 = self.Op(
            "builtin.shadow_output",
            1172,
            input_types=[self.t_dtensor([200, 256], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_21"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1173 = self.Op(
            "builtin.shadow_output",
            1173,
            input_types=[self.t_dtensor([256, 1], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_22"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1174 = self.Op(
            "builtin.shadow_output",
            1174,
            input_types=[self.t_dtensor([256, 256], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_23"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1175 = self.Op(
            "builtin.shadow_output",
            1175,
            input_types=[self.t_dtensor([256, 256], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_24"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1176 = self.Op(
            "builtin.shadow_output",
            1176,
            input_types=[self.t_dtensor([200, 256], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_25"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1177 = self.Op(
            "builtin.shadow_output",
            1177,
            input_types=[self.t_dtensor([200, 256], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_26"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1178 = self.Op(
            "builtin.shadow_output",
            1178,
            input_types=[self.t_dtensor([200, 256], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_27"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1179 = self.Op(
            "builtin.shadow_output",
            1179,
            input_types=[self.t_dtensor([256, 1], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_28"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1180 = self.Op(
            "builtin.shadow_output",
            1180,
            input_types=[self.t_dtensor([256, 256], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_29"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1181 = self.Op(
            "builtin.shadow_output",
            1181,
            input_types=[self.t_dtensor([256, 256], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_30"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1182 = self.Op(
            "builtin.shadow_output",
            1182,
            input_types=[self.t_dtensor([200, 256], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_31"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1183 = self.Op(
            "builtin.shadow_output",
            1183,
            input_types=[self.t_dtensor([200, 256], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_32"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1184 = self.Op(
            "builtin.shadow_output",
            1184,
            input_types=[self.t_dtensor([200, 256], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_33"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1185 = self.Op(
            "builtin.shadow_output",
            1185,
            input_types=[self.t_dtensor([256, 1], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_34"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1186 = self.Op(
            "builtin.shadow_output",
            1186,
            input_types=[self.t_dtensor([256, 256], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_35"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1187 = self.Op(
            "builtin.shadow_output",
            1187,
            input_types=[self.t_dtensor([256, 256], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_36"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1188 = self.Op(
            "builtin.shadow_output",
            1188,
            input_types=[self.t_dtensor([200, 256], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_37"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1189 = self.Op(
            "builtin.shadow_output",
            1189,
            input_types=[self.t_dtensor([200, 256], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_38"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1190 = self.Op(
            "builtin.shadow_output",
            1190,
            input_types=[self.t_dtensor([200, 256], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_39"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1191 = self.Op(
            "builtin.shadow_output",
            1191,
            input_types=[self.t_dtensor([256, 1], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_40"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1192 = self.Op(
            "builtin.shadow_output",
            1192,
            input_types=[self.t_dtensor([256, 256], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_41"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1193 = self.Op(
            "builtin.shadow_output",
            1193,
            input_types=[self.t_dtensor([256, 256], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_42"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1194 = self.Op(
            "builtin.shadow_output",
            1194,
            input_types=[self.t_dtensor([200, 256], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_43"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1195 = self.Op(
            "builtin.shadow_output",
            1195,
            input_types=[self.t_dtensor([200, 256], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_44"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1196 = self.Op(
            "builtin.shadow_output",
            1196,
            input_types=[self.t_dtensor([200, 256], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_45"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1197 = self.Op(
            "builtin.shadow_output",
            1197,
            input_types=[self.t_dtensor([256, 1], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_46"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1198 = self.Op(
            "builtin.shadow_output",
            1198,
            input_types=[self.t_dtensor([256, 256], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_47"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1199 = self.Op(
            "builtin.shadow_output",
            1199,
            input_types=[self.t_dtensor([256, 256], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_48"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1200 = self.Op(
            "builtin.shadow_output",
            1200,
            input_types=[self.t_dtensor([200, 256], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_49"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1201 = self.Op(
            "builtin.shadow_output",
            1201,
            input_types=[self.t_dtensor([200, 256], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_50"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1202 = self.Op(
            "builtin.shadow_output",
            1202,
            input_types=[self.t_dtensor([200, 256], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_51"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.shadow_output_1203 = self.Op(
            "builtin.shadow_output",
            1203,
            input_types=[self.t_dtensor([200, 1], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_52"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.module_929 = self.Op(
            "builtin.module",
            929,
            input_types=[],
            output_types=[],
            attrs=dict(
                program=self.a_pointer("0x91eb9610"),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(),
            ),
            block_positional_arg_names=[[[]]],
            block_keyword_arg_names=[[{}]],
        )

    def module_929_block00(self, call):

        def ret_lambda():

            (parameter_9310,) = call(self.parameter_931)

            (parameter_9320,) = call(self.parameter_932)

            (parameter_9330,) = call(self.parameter_933)

            (parameter_9340,) = call(self.parameter_934)

            (parameter_9350,) = call(self.parameter_935)

            (parameter_9360,) = call(self.parameter_936)

            (parameter_9370,) = call(self.parameter_937)

            (parameter_9380,) = call(self.parameter_938)

            (parameter_9390,) = call(self.parameter_939)

            (parameter_9400,) = call(self.parameter_940)

            (parameter_9410,) = call(self.parameter_941)

            (parameter_9420,) = call(self.parameter_942)

            (parameter_9430,) = call(self.parameter_943)

            (parameter_9440,) = call(self.parameter_944)

            (parameter_9450,) = call(self.parameter_945)

            (parameter_9460,) = call(self.parameter_946)

            (parameter_9470,) = call(self.parameter_947)

            (parameter_9480,) = call(self.parameter_948)

            (parameter_9490,) = call(self.parameter_949)

            (parameter_9500,) = call(self.parameter_950)

            (parameter_9510,) = call(self.parameter_951)

            (parameter_9520,) = call(self.parameter_952)

            (parameter_9530,) = call(self.parameter_953)

            (parameter_9540,) = call(self.parameter_954)

            (parameter_9550,) = call(self.parameter_955)

            (parameter_9560,) = call(self.parameter_956)

            (parameter_9570,) = call(self.parameter_957)

            (parameter_9580,) = call(self.parameter_958)

            (data_9590,) = call(self.data_959)

            (data_9600,) = call(self.data_960)

            (data_9610,) = call(self.data_961)

            (data_9620,) = call(self.data_962)

            (data_9630,) = call(self.data_963)

            (full_9640,) = call(self.full_964)

            (combine_9650,) = call(self.combine_965, data_9590, data_9600)

            (concat_9660,) = call(self.concat_966, combine_9650, full_9640)

            (full_9670,) = call(self.full_967)

            (full_int_array_9680,) = call(self.full_int_array_968)

            (full_int_array_9690,) = call(self.full_int_array_969)

            (slice_9700,) = call(
                self.slice_970, parameter_9320, full_int_array_9680, full_int_array_9690
            )

            (full_9710,) = call(self.full_971)

            (scale_9720,) = call(self.scale_972, slice_9700, full_9710)

            (full_9730,) = call(self.full_973)

            (full_9740,) = call(self.full_974)

            (full_9750,) = call(self.full_975)

            (full_9760,) = call(self.full_976)

            (combine_9770,) = call(self.combine_977, slice_9700, full_9750)

            (full_int_array_9780,) = call(self.full_int_array_978)

            (
                reshape_9790,
                reshape_9791,
            ) = call(self.reshape_979, slice_9700, full_int_array_9780)

            (full_int_array_9800,) = call(self.full_int_array_980)

            (
                reshape_9810,
                reshape_9811,
            ) = call(self.reshape_981, full_9750, full_int_array_9800)

            (combine_9820,) = call(self.combine_982, reshape_9790, reshape_9810)

            (full_9830,) = call(self.full_983)

            (concat_9840,) = call(self.concat_984, combine_9820, full_9830)

            (combine_9850,) = call(self.combine_985, scale_9720, full_9760)

            (full_int_array_9860,) = call(self.full_int_array_986)

            (
                reshape_9870,
                reshape_9871,
            ) = call(self.reshape_987, scale_9720, full_int_array_9860)

            (full_int_array_9880,) = call(self.full_int_array_988)

            (
                reshape_9890,
                reshape_9891,
            ) = call(self.reshape_989, full_9760, full_int_array_9880)

            (combine_9900,) = call(self.combine_990, reshape_9870, reshape_9890)

            (full_9910,) = call(self.full_991)

            (concat_9920,) = call(self.concat_992, combine_9900, full_9910)

            (full_int_array_9930,) = call(self.full_int_array_993)

            (set_value__9940,) = call(
                self.set_value__994,
                full_9670,
                concat_9840,
                concat_9920,
                full_int_array_9930,
            )

            (full_int_array_9950,) = call(self.full_int_array_995)

            (full_int_array_9960,) = call(self.full_int_array_996)

            (slice_9970,) = call(
                self.slice_997, parameter_9320, full_int_array_9950, full_int_array_9960
            )

            (full_9980,) = call(self.full_998)

            (scale_9990,) = call(self.scale_999, slice_9970, full_9980)

            (full_10000,) = call(self.full_1000)

            (full_10010,) = call(self.full_1001)

            (full_10020,) = call(self.full_1002)

            (full_10030,) = call(self.full_1003)

            (combine_10040,) = call(self.combine_1004, slice_9970, full_10020)

            (full_int_array_10050,) = call(self.full_int_array_1005)

            (
                reshape_10060,
                reshape_10061,
            ) = call(self.reshape_1006, slice_9970, full_int_array_10050)

            (full_int_array_10070,) = call(self.full_int_array_1007)

            (
                reshape_10080,
                reshape_10081,
            ) = call(self.reshape_1008, full_10020, full_int_array_10070)

            (combine_10090,) = call(self.combine_1009, reshape_10060, reshape_10080)

            (full_10100,) = call(self.full_1010)

            (concat_10110,) = call(self.concat_1011, combine_10090, full_10100)

            (combine_10120,) = call(self.combine_1012, scale_9990, full_10030)

            (full_int_array_10130,) = call(self.full_int_array_1013)

            (
                reshape_10140,
                reshape_10141,
            ) = call(self.reshape_1014, scale_9990, full_int_array_10130)

            (full_int_array_10150,) = call(self.full_int_array_1015)

            (
                reshape_10160,
                reshape_10161,
            ) = call(self.reshape_1016, full_10030, full_int_array_10150)

            (combine_10170,) = call(self.combine_1017, reshape_10140, reshape_10160)

            (full_10180,) = call(self.full_1018)

            (concat_10190,) = call(self.concat_1019, combine_10170, full_10180)

            (full_int_array_10200,) = call(self.full_int_array_1020)

            (set_value__10210,) = call(
                self.set_value__1021,
                set_value__9940,
                concat_10110,
                concat_10190,
                full_int_array_10200,
            )

            (matmul_10220,) = call(self.matmul_1022, concat_9660, set_value__10210)

            (matmul_10230,) = call(self.matmul_1023, matmul_10220, parameter_9310)

            (full_10240,) = call(self.full_1024)

            (scale_10250,) = call(self.scale_1025, matmul_10230, full_10240)

            (sin_10260,) = call(self.sin_1026, scale_10250)

            (full_10270,) = call(self.full_1027)

            (scale_10280,) = call(self.scale_1028, matmul_10230, full_10270)

            (cos_10290,) = call(self.cos_1029, scale_10280)

            (full_10300,) = call(self.full_1030)

            (combine_10310,) = call(self.combine_1031, sin_10260, cos_10290)

            (concat_10320,) = call(self.concat_1032, combine_10310, full_10300)

            (full_10330,) = call(self.full_1033)

            (combine_10340,) = call(self.combine_1034, concat_9660, concat_10320)

            (concat_10350,) = call(self.concat_1035, combine_10340, full_10330)

            (multiply_10360,) = call(self.multiply_1036, parameter_9580, parameter_9580)

            (full_int_array_10370,) = call(self.full_int_array_1037)

            (sum_10380,) = call(self.sum_1038, multiply_10360, full_int_array_10370)

            (sqrt_10390,) = call(self.sqrt_1039, sum_10380)

            (multiply_10400,) = call(self.multiply_1040, parameter_9570, parameter_9580)

            (divide_10410,) = call(self.divide_1041, multiply_10400, sqrt_10390)

            (transpose_10420,) = call(self.transpose_1042, divide_10410)

            (matmul_10430,) = call(self.matmul_1043, concat_10350, transpose_10420)

            (add_10440,) = call(self.add_1044, matmul_10430, parameter_9560)

            (sigmoid_10450,) = call(self.sigmoid_1045, add_10440)

            (multiply_10460,) = call(self.multiply_1046, add_10440, sigmoid_10450)

            (multiply_10470,) = call(self.multiply_1047, parameter_9550, parameter_9550)

            (full_int_array_10480,) = call(self.full_int_array_1048)

            (sum_10490,) = call(self.sum_1049, multiply_10470, full_int_array_10480)

            (sqrt_10500,) = call(self.sqrt_1050, sum_10490)

            (multiply_10510,) = call(self.multiply_1051, parameter_9540, parameter_9550)

            (divide_10520,) = call(self.divide_1052, multiply_10510, sqrt_10500)

            (transpose_10530,) = call(self.transpose_1053, divide_10520)

            (matmul_10540,) = call(self.matmul_1054, concat_10350, transpose_10530)

            (add_10550,) = call(self.add_1055, matmul_10540, parameter_9530)

            (sigmoid_10560,) = call(self.sigmoid_1056, add_10550)

            (multiply_10570,) = call(self.multiply_1057, add_10550, sigmoid_10560)

            (multiply_10580,) = call(self.multiply_1058, parameter_9520, parameter_9520)

            (full_int_array_10590,) = call(self.full_int_array_1059)

            (sum_10600,) = call(self.sum_1060, multiply_10580, full_int_array_10590)

            (sqrt_10610,) = call(self.sqrt_1061, sum_10600)

            (multiply_10620,) = call(self.multiply_1062, parameter_9510, parameter_9520)

            (divide_10630,) = call(self.divide_1063, multiply_10620, sqrt_10610)

            (transpose_10640,) = call(self.transpose_1064, divide_10630)

            (matmul_10650,) = call(self.matmul_1065, concat_10350, transpose_10640)

            (add_10660,) = call(self.add_1066, matmul_10650, parameter_9500)

            (sigmoid_10670,) = call(self.sigmoid_1067, add_10660)

            (multiply_10680,) = call(self.multiply_1068, add_10660, sigmoid_10670)

            (multiply_10690,) = call(self.multiply_1069, parameter_9490, parameter_9490)

            (full_int_array_10700,) = call(self.full_int_array_1070)

            (sum_10710,) = call(self.sum_1071, multiply_10690, full_int_array_10700)

            (sqrt_10720,) = call(self.sqrt_1072, sum_10710)

            (multiply_10730,) = call(self.multiply_1073, parameter_9480, parameter_9490)

            (divide_10740,) = call(self.divide_1074, multiply_10730, sqrt_10720)

            (transpose_10750,) = call(self.transpose_1075, divide_10740)

            (matmul_10760,) = call(self.matmul_1076, multiply_10680, transpose_10750)

            (add_10770,) = call(self.add_1077, matmul_10760, parameter_9470)

            (sigmoid_10780,) = call(self.sigmoid_1078, add_10770)

            (multiply_10790,) = call(self.multiply_1079, add_10770, sigmoid_10780)

            (multiply_10800,) = call(self.multiply_1080, multiply_10790, multiply_10460)

            (subtract_10810,) = call(self.subtract_1081, multiply_10460, multiply_10800)

            (multiply_10820,) = call(self.multiply_1082, multiply_10790, multiply_10570)

            (add_10830,) = call(self.add_1083, subtract_10810, multiply_10820)

            (multiply_10840,) = call(self.multiply_1084, parameter_9460, parameter_9460)

            (full_int_array_10850,) = call(self.full_int_array_1085)

            (sum_10860,) = call(self.sum_1086, multiply_10840, full_int_array_10850)

            (sqrt_10870,) = call(self.sqrt_1087, sum_10860)

            (multiply_10880,) = call(self.multiply_1088, parameter_9450, parameter_9460)

            (divide_10890,) = call(self.divide_1089, multiply_10880, sqrt_10870)

            (transpose_10900,) = call(self.transpose_1090, divide_10890)

            (matmul_10910,) = call(self.matmul_1091, add_10830, transpose_10900)

            (add_10920,) = call(self.add_1092, matmul_10910, parameter_9440)

            (sigmoid_10930,) = call(self.sigmoid_1093, add_10920)

            (multiply_10940,) = call(self.multiply_1094, add_10920, sigmoid_10930)

            (multiply_10950,) = call(self.multiply_1095, multiply_10940, multiply_10460)

            (subtract_10960,) = call(self.subtract_1096, multiply_10460, multiply_10950)

            (multiply_10970,) = call(self.multiply_1097, multiply_10940, multiply_10570)

            (add_10980,) = call(self.add_1098, subtract_10960, multiply_10970)

            (multiply_10990,) = call(self.multiply_1099, parameter_9430, parameter_9430)

            (full_int_array_11000,) = call(self.full_int_array_1100)

            (sum_11010,) = call(self.sum_1101, multiply_10990, full_int_array_11000)

            (sqrt_11020,) = call(self.sqrt_1102, sum_11010)

            (multiply_11030,) = call(self.multiply_1103, parameter_9420, parameter_9430)

            (divide_11040,) = call(self.divide_1104, multiply_11030, sqrt_11020)

            (transpose_11050,) = call(self.transpose_1105, divide_11040)

            (matmul_11060,) = call(self.matmul_1106, add_10980, transpose_11050)

            (add_11070,) = call(self.add_1107, matmul_11060, parameter_9410)

            (sigmoid_11080,) = call(self.sigmoid_1108, add_11070)

            (multiply_11090,) = call(self.multiply_1109, add_11070, sigmoid_11080)

            (multiply_11100,) = call(self.multiply_1110, multiply_11090, multiply_10460)

            (subtract_11110,) = call(self.subtract_1111, multiply_10460, multiply_11100)

            (multiply_11120,) = call(self.multiply_1112, multiply_11090, multiply_10570)

            (add_11130,) = call(self.add_1113, subtract_11110, multiply_11120)

            (multiply_11140,) = call(self.multiply_1114, parameter_9400, parameter_9400)

            (full_int_array_11150,) = call(self.full_int_array_1115)

            (sum_11160,) = call(self.sum_1116, multiply_11140, full_int_array_11150)

            (sqrt_11170,) = call(self.sqrt_1117, sum_11160)

            (multiply_11180,) = call(self.multiply_1118, parameter_9390, parameter_9400)

            (divide_11190,) = call(self.divide_1119, multiply_11180, sqrt_11170)

            (transpose_11200,) = call(self.transpose_1120, divide_11190)

            (matmul_11210,) = call(self.matmul_1121, add_11130, transpose_11200)

            (add_11220,) = call(self.add_1122, matmul_11210, parameter_9380)

            (sigmoid_11230,) = call(self.sigmoid_1123, add_11220)

            (multiply_11240,) = call(self.multiply_1124, add_11220, sigmoid_11230)

            (multiply_11250,) = call(self.multiply_1125, multiply_11240, multiply_10460)

            (subtract_11260,) = call(self.subtract_1126, multiply_10460, multiply_11250)

            (multiply_11270,) = call(self.multiply_1127, multiply_11240, multiply_10570)

            (add_11280,) = call(self.add_1128, subtract_11260, multiply_11270)

            (multiply_11290,) = call(self.multiply_1129, parameter_9370, parameter_9370)

            (full_int_array_11300,) = call(self.full_int_array_1130)

            (sum_11310,) = call(self.sum_1131, multiply_11290, full_int_array_11300)

            (sqrt_11320,) = call(self.sqrt_1132, sum_11310)

            (multiply_11330,) = call(self.multiply_1133, parameter_9360, parameter_9370)

            (divide_11340,) = call(self.divide_1134, multiply_11330, sqrt_11320)

            (transpose_11350,) = call(self.transpose_1135, divide_11340)

            (matmul_11360,) = call(self.matmul_1136, add_11280, transpose_11350)

            (add_11370,) = call(self.add_1137, matmul_11360, parameter_9350)

            (sigmoid_11380,) = call(self.sigmoid_1138, add_11370)

            (multiply_11390,) = call(self.multiply_1139, add_11370, sigmoid_11380)

            (multiply_11400,) = call(self.multiply_1140, multiply_11390, multiply_10460)

            (subtract_11410,) = call(self.subtract_1141, multiply_10460, multiply_11400)

            (multiply_11420,) = call(self.multiply_1142, multiply_11390, multiply_10570)

            (add_11430,) = call(self.add_1143, subtract_11410, multiply_11420)

            (matmul_11440,) = call(self.matmul_1144, add_11430, parameter_9340)

            (add_11450,) = call(self.add_1145, matmul_11440, parameter_9330)

            (full_int_array_11460,) = call(self.full_int_array_1146)

            (full_11470,) = call(self.full_1147)

            (split_11480,) = call(
                self.split_1148, add_11450, full_int_array_11460, full_11470
            )

            (split_11490,) = call(self.split_1149, split_11480)

            (full_11500,) = call(self.full_1150)

            (scale_11510,) = call(self.scale_1151, split_11490, full_11500)

            call(self.shadow_output_1152, concat_9660)

            call(self.shadow_output_1153, set_value__10210)

            call(self.shadow_output_1154, matmul_10220)

            call(self.shadow_output_1155, scale_10250)

            call(self.shadow_output_1156, scale_10280)

            call(self.shadow_output_1157, concat_10350)

            call(self.shadow_output_1158, sqrt_10390)

            call(self.shadow_output_1159, multiply_10400)

            call(self.shadow_output_1160, transpose_10420)

            call(self.shadow_output_1161, add_10440)

            call(self.shadow_output_1162, multiply_10460)

            call(self.shadow_output_1163, sqrt_10500)

            call(self.shadow_output_1164, multiply_10510)

            call(self.shadow_output_1165, transpose_10530)

            call(self.shadow_output_1166, add_10550)

            call(self.shadow_output_1167, multiply_10570)

            call(self.shadow_output_1168, sqrt_10610)

            call(self.shadow_output_1169, multiply_10620)

            call(self.shadow_output_1170, transpose_10640)

            call(self.shadow_output_1171, add_10660)

            call(self.shadow_output_1172, multiply_10680)

            call(self.shadow_output_1173, sqrt_10720)

            call(self.shadow_output_1174, multiply_10730)

            call(self.shadow_output_1175, transpose_10750)

            call(self.shadow_output_1176, add_10770)

            call(self.shadow_output_1177, multiply_10790)

            call(self.shadow_output_1178, add_10830)

            call(self.shadow_output_1179, sqrt_10870)

            call(self.shadow_output_1180, multiply_10880)

            call(self.shadow_output_1181, transpose_10900)

            call(self.shadow_output_1182, add_10920)

            call(self.shadow_output_1183, multiply_10940)

            call(self.shadow_output_1184, add_10980)

            call(self.shadow_output_1185, sqrt_11020)

            call(self.shadow_output_1186, multiply_11030)

            call(self.shadow_output_1187, transpose_11050)

            call(self.shadow_output_1188, add_11070)

            call(self.shadow_output_1189, multiply_11090)

            call(self.shadow_output_1190, add_11130)

            call(self.shadow_output_1191, sqrt_11170)

            call(self.shadow_output_1192, multiply_11180)

            call(self.shadow_output_1193, transpose_11200)

            call(self.shadow_output_1194, add_11220)

            call(self.shadow_output_1195, multiply_11240)

            call(self.shadow_output_1196, add_11280)

            call(self.shadow_output_1197, sqrt_11320)

            call(self.shadow_output_1198, multiply_11330)

            call(self.shadow_output_1199, transpose_11350)

            call(self.shadow_output_1200, add_11370)

            call(self.shadow_output_1201, multiply_11390)

            call(self.shadow_output_1202, add_11430)

            call(self.shadow_output_1203, scale_11510)

        return ret_lambda

    def __call__(self, call, *args, **kwargs):

        self.SetArgs(args)

        self.SetKeywordArgs(kwargs)

        return call(self.module_929, blocks=[[(self.module_929_block00,)]])
