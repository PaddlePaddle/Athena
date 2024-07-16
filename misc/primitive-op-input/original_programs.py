class PirProgram_5645888679101557789:

    def __init__(self):

        self.data_193 = self.Op(
            "pd_op.data",
            193,
            input_types=[],
            output_types=[self.t_dtensor([1, -1, 768], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                shape=self.a_intarray(1, -1, 768),
                name=self.a_str("x"),
                place=self.a_place("undefined", 0),
                dtype=self.a_dtype("float32"),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.full_194 = self.Op(
            "pd_op.full",
            194,
            input_types=[],
            output_types=[self.t_dtensor([1], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                value=self.a_f32("0"),
                shape=self.a_intarray(1),
                place=self.a_place("undefined", 0),
                dtype=self.a_dtype("float32"),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.full_int_array_195 = self.Op(
            "pd_op.full_int_array",
            195,
            input_types=[],
            output_types=[self.t_dtensor([0], self.t_i64())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                dtype=self.a_dtype("int64"),
                place=self.a_place("cpu"),
                value=self.a_array(),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.sum_196 = self.Op(
            "pd_op.sum",
            196,
            input_types=[
                self.t_dtensor([1, -1, 768], self.t_f32()),
                self.t_dtensor([0], self.t_i64()),
            ],
            output_types=[self.t_dtensor([], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                keepdim=self.a_bool(False),
                dtype=self.a_dtype("Undefined"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.full_197 = self.Op(
            "pd_op.full",
            197,
            input_types=[],
            output_types=[self.t_dtensor([1], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                value=self.a_f32("0"),
                shape=self.a_intarray(1),
                place=self.a_place("undefined", 0),
                dtype=self.a_dtype("float32"),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.greater_than_198 = self.Op(
            "pd_op.greater_than",
            198,
            input_types=[
                self.t_dtensor([], self.t_f32()),
                self.t_dtensor([1], self.t_f32()),
            ],
            output_types=[self.t_dtensor([1], self.t_bool())],
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

        self.full_199 = self.Op(
            "pd_op.full",
            199,
            input_types=[],
            output_types=[self.t_dtensor([1], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True)),
                value=self.a_f32("1"),
                shape=self.a_intarray(1),
                place=self.a_place("undefined", 0),
                dtype=self.a_dtype("float32"),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.less_than_200 = self.Op(
            "pd_op.less_than",
            200,
            input_types=[
                self.t_dtensor([1], self.t_f32()),
                self.t_dtensor([1], self.t_f32()),
            ],
            output_types=[self.t_dtensor([1], self.t_bool())],
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

        self.logical_and_201 = self.Op(
            "pd_op.logical_and",
            201,
            input_types=[
                self.t_dtensor([1], self.t_bool()),
                self.t_dtensor([1], self.t_bool()),
            ],
            output_types=[self.t_dtensor([1], self.t_bool())],
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

        self.less_than_207 = self.Op(
            "pd_op.less_than",
            207,
            input_types=[
                self.t_dtensor([1], self.t_f32()),
                self.t_dtensor([1], self.t_f32()),
            ],
            output_types=[self.t_dtensor([1], self.t_bool())],
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

        self.logical_and_208 = self.Op(
            "pd_op.logical_and",
            208,
            input_types=[
                self.t_dtensor([1], self.t_bool()),
                self.t_dtensor([1], self.t_bool()),
            ],
            output_types=[self.t_dtensor([1], self.t_bool())],
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

        self.exp_210 = self.Op(
            "pd_op.exp",
            210,
            input_types=[self.t_dtensor([1, -1, 768], self.t_f32())],
            output_types=[self.t_dtensor([1, -1, 768], self.t_f32())],
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

        self.subtract_211 = self.Op(
            "pd_op.subtract",
            211,
            input_types=[
                self.t_dtensor([1, -1, 768], self.t_f32()),
                self.t_dtensor([1, -1, 768], self.t_f32()),
            ],
            output_types=[self.t_dtensor([1, -1, 768], self.t_f32())],
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

        self.full_212 = self.Op(
            "pd_op.full",
            212,
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

        self.scale_213 = self.Op(
            "pd_op.scale",
            213,
            input_types=[
                self.t_dtensor([1], self.t_f32()),
                self.t_dtensor([1], self.t_f32()),
            ],
            output_types=[self.t_dtensor([1], self.t_f32())],
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

        self.sum_215 = self.Op(
            "pd_op.sum",
            215,
            input_types=[
                self.t_dtensor([1, -1, 768], self.t_f32()),
                self.t_dtensor([0], self.t_i64()),
            ],
            output_types=[self.t_dtensor([], self.t_f32())],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(False)),
                keepdim=self.a_bool(False),
                dtype=self.a_dtype("Undefined"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
            ),
        )

        self.greater_than_217 = self.Op(
            "pd_op.greater_than",
            217,
            input_types=[
                self.t_dtensor([], self.t_f32()),
                self.t_dtensor([1], self.t_f32()),
            ],
            output_types=[self.t_dtensor([1], self.t_bool())],
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

        self.less_than_219 = self.Op(
            "pd_op.less_than",
            219,
            input_types=[
                self.t_dtensor([1], self.t_f32()),
                self.t_dtensor([1], self.t_f32()),
            ],
            output_types=[self.t_dtensor([1], self.t_bool())],
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

        self.logical_and_220 = self.Op(
            "pd_op.logical_and",
            220,
            input_types=[
                self.t_dtensor([1], self.t_bool()),
                self.t_dtensor([1], self.t_bool()),
            ],
            output_types=[self.t_dtensor([1], self.t_bool())],
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

        self.yield_221 = self.Op(
            "cf.yield",
            221,
            input_types=[
                self.t_dtensor([1], self.t_bool()),
                self.t_dtensor([1], self.t_f32()),
                self.t_dtensor([1, -1, 768], self.t_f32()),
            ],
            output_types=[],
            attrs=dict(
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()),
                    self.a_symbol(self.s_null()),
                    self.a_symbol(self.s_null()),
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.while_209 = self.Op(
            "pd_op.while",
            209,
            input_types=[
                self.t_dtensor([1], self.t_bool()),
                self.t_dtensor([1], self.t_f32()),
                self.t_dtensor([1, -1, 768], self.t_f32()),
            ],
            output_types=[
                self.t_dtensor([1], self.t_f32()),
                self.t_dtensor([1, -1, 768], self.t_f32()),
            ],
            attrs=dict(
                stop_gradient=self.a_array(self.a_bool(True), self.a_bool(False)),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()),
                    self.a_symbol(self.s_null()),
                    self.a_symbol(self.s_null()),
                ),
                __results_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null()), self.a_symbol(self.s_null())
                ),
            ),
            block_positional_arg_names=[[["arg_1117666928", "arg_1117663664"]]],
            block_keyword_arg_names=[[{}]],
            block_positional_arg_types=[
                [
                    [
                        self.t_dtensor([1], self.t_f32()),
                        self.t_dtensor([1, -1, 768], self.t_f32()),
                    ]
                ]
            ],
            block_keyword_arg_types=[[[]]],
        )

        self.exp_222 = self.Op(
            "pd_op.exp",
            222,
            input_types=[self.t_dtensor([1, -1, 768], self.t_f32())],
            output_types=[self.t_dtensor([1, -1, 768], self.t_f32())],
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

        self.shadow_output_223 = self.Op(
            "builtin.shadow_output",
            223,
            input_types=[self.t_dtensor([1, -1, 768], self.t_f32())],
            output_types=[],
            attrs=dict(
                output_name=self.a_str("output_0"),
                __operands_symbols_signature__=self.a_array(
                    self.a_symbol(self.s_null())
                ),
                __results_symbols_signature__=self.a_array(),
            ),
        )

        self.module_191 = self.Op(
            "builtin.module",
            191,
            input_types=[],
            output_types=[],
            attrs=dict(
                program=self.a_pointer("0x47319ad0"),
                __operands_symbols_signature__=self.a_array(),
                __results_symbols_signature__=self.a_array(),
            ),
            block_positional_arg_names=[[[]]],
            block_keyword_arg_names=[[{}]],
            block_positional_arg_types=[[[]]],
            block_keyword_arg_types=[[[]]],
        )

    def while_209_block00(self, call, full_int_array_1950, full_1970, full_1990):

        def ret_lambda_while_209_block00(arg_1117666928, arg_1117663664):

            (exp_2100,) = call(self.exp_210, arg_1117663664)

            (subtract_2110,) = call(self.subtract_211, exp_2100, arg_1117663664)

            (full_2120,) = call(self.full_212)

            (scale_2130,) = call(self.scale_213, arg_1117666928, full_2120)

            (sum_2150,) = call(self.sum_215, subtract_2110, full_int_array_1950)

            (greater_than_2170,) = call(self.greater_than_217, sum_2150, full_1970)

            (less_than_2190,) = call(self.less_than_219, scale_2130, full_1990)

            (logical_and_2200,) = call(
                self.logical_and_220, greater_than_2170, less_than_2190
            )

            return call(self.yield_221, logical_and_2200, scale_2130, subtract_2110)

        return ret_lambda_while_209_block00

    def module_191_block00(self, call):

        def ret_lambda_module_191_block00():

            (data_1930,) = call(self.data_193)

            (full_1940,) = call(self.full_194)

            (full_int_array_1950,) = call(self.full_int_array_195)

            (sum_1960,) = call(self.sum_196, data_1930, full_int_array_1950)

            (full_1970,) = call(self.full_197)

            (greater_than_1980,) = call(self.greater_than_198, sum_1960, full_1970)

            (full_1990,) = call(self.full_199)

            (less_than_2000,) = call(self.less_than_200, full_1940, full_1990)

            (logical_and_2010,) = call(
                self.logical_and_201, greater_than_1980, less_than_2000
            )

            (less_than_2070,) = call(self.less_than_207, full_1940, full_1990)

            (logical_and_2080,) = call(
                self.logical_and_208, greater_than_1980, less_than_2070
            )

            (
                while_2090,
                while_2091,
            ) = call(
                self.while_209,
                logical_and_2080,
                full_1940,
                data_1930,
                blocks=[
                    [
                        (
                            self.while_209_block00,
                            full_int_array_1950,
                            full_1970,
                            full_1990,
                        )
                    ]
                ],
            )

            (exp_2220,) = call(self.exp_222, while_2091)

            call(self.shadow_output_223, exp_2220)

        return ret_lambda_module_191_block00

    def __call__(self, call, *args, **kwargs):

        self.SetArgs(args)

        self.SetKeywordArgs(kwargs)

        return call(self.module_191, blocks=[[(self.module_191_block00,)]])
