import os
os.environ['FLAGS_cinn_new_group_scheduler'] = '1'
os.environ['FLAGS_group_schedule_tiling_first'] = '1'
os.environ['FLAGS_prim_all'] = 'true'
os.environ['FLAGS_prim_enable_dynamic'] = '1'
os.environ['FLAGS_enable_pir_api'] = '1'
os.environ['FLAGS_cinn_bucket_compile'] = '1'

import unittest
import numpy as np
import paddle

def GetEnvVarEnableJit():
    enable_jit = os.getenv('PADDLE_DEBUG_ENABLE_JIT')
    return enable_jit not in {
        "0",
        "False",
        "false",
        "OFF",
    }

def GetEnvVarEnableCinn():
    enable_cinn = os.getenv('PADDLE_DEBUG_ENABLE_CINN')
    return enable_cinn not in {
        "0",
        "False",
        "false",
        "OFF",
    }


def GetTolerance(dtype):
    if dtype == np.float16:
        return GetFloat16Tolerance()
    if dtype == np.float32:
        return GetFloat32Tolerance()
    return 1e-6

def GetFloat16Tolerance():
    try:
        return float(os.getenv('PADDLE_DEBUG_FLOAT16_TOL'))
    except:
        return 1e-3

def GetFloat32Tolerance():
    try:
        return float(os.getenv('PADDLE_DEBUG_FLOAT32_TOL'))
    except:
        return 1e-6

def IsInteger(dtype):
    return np.dtype(dtype).char in np.typecodes['AllInteger']


class CinnTestBase:
    def setUp(self):
        paddle.seed(2024)
        self.prepare_data()

    def test_train(self):
        dy_outs = self.train(use_cinn=False)
        cinn_outs = self.train(use_cinn=GetEnvVarEnableCinn())

        for cinn_out, dy_out in zip(cinn_outs, dy_outs):
          if type(cinn_out) is list and type(dy_out) is list:
            for x, y in zip(cinn_out, dy_out):
              self.assert_all_close(x, y)
          else:
            self.assert_all_close(cinn_out, dy_out)

    def assert_all_close(self, x, y):
        if (hasattr(x, "numpy") and hasattr(y, "numpy")):
            x_numpy = x.numpy()
            y_numpy = y.numpy()
            assert x_numpy.dtype == y_numpy.dtype
            if IsInteger(x_numpy.dtype):
                np.testing.assert_equal(x_numpy, y_numpy)
            else:
                tol = GetTolerance(x_numpy.dtype)
                np.testing.assert_allclose(x_numpy, y_numpy, atol=tol, rtol=tol)
        else:
            assert x == y

{% macro get_input_tensor_instance(tensor_meta) -%}
{%- set shape = tensor_meta.shape -%}
{%- set dtype = tensor_meta.dtype -%}
{%- set big_dtype = tensor_meta.big_dtype -%}
{%- set data = tensor_meta.data -%}
{%- set min = tensor_meta.min -%}
{%- set max = tensor_meta.max -%}
{%- if data != None -%}
    paddle.to_tensor({{data}}, dtype='{{dtype}}').reshape({{shape}})
{%- elif big_dtype == "bool" -%}
    paddle.cast(paddle.randint(low=0, high=2, shape={{shape}}, dtype='int32'), 'bool')
{%- elif big_dtype == "int64" -%}
    paddle.randint(low={{min}}, high={{max}}, shape={{shape}}, dtype='{{dtype}}')
{%- elif big_dtype == "float64" -%}
    paddle.uniform({{shape}}, dtype='{{dtype}}', min={{min}}, max={{max}})
{%- endif -%}
{%- endmacro %}

{%- for op in ops %}
{%- set op_idx = loop.index0 %}

class PrimitiveOp{{op_idx}}(paddle.nn.Layer):
    def __init__(self):
        super().__init__()

    def forward(self, {{ op.input_tensor_names | join(", ") }}):
        return {{ op.op_expr }}

class TestPrimitiveOp{{op_idx}}(CinnTestBase, unittest.TestCase):
    def prepare_data(self):
        self.inputs = [
        {%- for example_tensor_meta in op.example_inputs_meta %}
            {{get_input_tensor_instance(example_tensor_meta)}},
        {%- endfor %}
        ]
        for input in self.inputs:
            input.stop_gradient = True

    def apply_to_static(self, net, use_cinn):
        build_strategy = paddle.static.BuildStrategy()
        input_spec = [
        {%- for shape, dtype in op.input_spec_shape_dtypes %}
        {%- set input_idx = loop.index0 %}
            paddle.static.InputSpec(shape={{shape}}, dtype='{{dtype}}'),
        {%- endfor %}
        ]
        build_strategy.build_cinn_pass = use_cinn
        return paddle.jit.to_static(
            net,
            input_spec=input_spec,
            build_strategy=build_strategy,
            full_graph=True,
        )

    def train(self, use_cinn):
        net = PrimitiveOp{{op_idx}}()
        if GetEnvVarEnableJit():
            net = self.apply_to_static(net, use_cinn)
        out = net(*self.inputs)
        return out

{%- endfor %}

if __name__ == '__main__':
    unittest.main()
