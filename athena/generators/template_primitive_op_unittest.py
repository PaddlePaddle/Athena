import os
if os.getenv('FLAGS_cinn_new_group_scheduler') is None:
    os.environ['FLAGS_cinn_new_group_scheduler'] = '1'
if os.getenv('FLAGS_group_schedule_tiling_first') is None:
    os.environ['FLAGS_group_schedule_tiling_first'] = '1'
if os.getenv('FLAGS_prim_all') is None:
    os.environ['FLAGS_prim_all'] = 'true'
if os.getenv('FLAGS_prim_enable_dynamic') is None:
    os.environ['FLAGS_prim_enable_dynamic'] = '1'
if os.getenv('FLAGS_enable_pir_api') is None:
    os.environ['FLAGS_enable_pir_api'] = '1'
if os.getenv('FLAGS_cinn_bucket_compile') is None:
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
    if enable_cinn is None:
        return {{PADDLE_DEBUG_ENABLE_CINN}}
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

def ApplyToStatic(net, use_cinn):
    build_strategy = paddle.static.BuildStrategy()
    build_strategy.build_cinn_pass = use_cinn
    return paddle.jit.to_static(
        net,
        input_spec=net.get_input_spec(),
        build_strategy=build_strategy,
        full_graph=True,
    )

class InstanceTrait:

    @classmethod
    def instance(cls):
        if cls.instance_ is None:
            cls.instance_ = cls()
        return cls.instance_

    @classmethod
    def static_instance_with_cinn(cls):
        if cls.static_instance_with_cinn_ is None:
            cls.static_instance_with_cinn_ = ApplyToStatic(
                cls.instance(),
                use_cinn=True
            )
        return cls.static_instance_with_cinn_

    @classmethod
    def static_instance_without_cinn(cls):
        if cls.static_instance_without_cinn_ is None:
            cls.static_instance_without_cinn_ = ApplyToStatic(
                cls.instance(),
                use_cinn=False
            )
        return cls.static_instance_without_cinn_


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

    def train(self, use_cinn):
        if GetEnvVarEnableJit():
            net = self.prepare_static_net(use_cinn)
        else:
            net = self.prepare_net()
        out = net(*self.inputs)
        return out
    
    def prepare_data(self):
        self.inputs = self.get_inputs()
        for input in self.inputs:
            input.stop_gradient = True

    def prepare_net(self):
        return self.get_test_class().instance()

    def prepare_static_net(self, use_cinn):
        if use_cinn:
            return self.get_test_class().static_instance_with_cinn()
        else:
            return self.get_test_class().static_instance_without_cinn()

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
    {%- if data == [] and shape == [] -%}
    paddle.to_tensor({{data}}, dtype='{{dtype}}')
    {%- else -%}
    paddle.to_tensor({{data}}, dtype='{{dtype}}').reshape({{shape}})
    {%- endif -%}
{%- elif big_dtype == "bool" -%}
    paddle.cast(paddle.randint(low=0, high=2, shape={{shape}}, dtype='int32'), 'bool')
{%- elif big_dtype == "int64" -%}
    paddle.randint(low={{min}}, high={{max}}, shape={{shape}}, dtype='{{dtype}}')
{%- elif big_dtype == "float64" -%}
    paddle.uniform({{shape}}, dtype='{{dtype}}', min={{min}}, max={{max}})
{%- endif -%}
{%- endmacro %}

{% macro get_primitive_class_methods(op) %}
    def __init__(self):
        super().__init__()

    def forward(self, {{ op.input_tensor_names | join(", ") }}):
        {%- for example_tensor_meta in op.example_inputs_meta %}
        {%- set input_idx = loop.index0 -%}
        {%- set data = example_tensor_meta.data -%}
        {%- if data != None and get_pos_arg_type_name(op, input_idx) == 'IntArray' %}
        {{op.input_tensor_names[input_idx]}} = {{data}}
        {%- endif -%}
        {%- endfor %}
        return {{ op.op_expr }}

    def get_input_spec(self):
        return [
        {%- for shape, dtype in op.input_spec_shape_dtypes %}
        {%- set input_idx = loop.index0 %}
            paddle.static.InputSpec(shape={{shape}}, dtype='{{dtype}}'),
        {%- endfor %}
        ]
        
    instance_ = None
    static_instance_with_cinn_ = None
    static_instance_without_cinn_ = None

{% endmacro %}

{%- macro get_primitive_class_name(op) -%}
PrimitiveOp_{{get_sha_hash_prefix(get_primitive_class_methods(op))}}
{%- endmacro -%}

{% macro get_test_class_methods(op) %}
    def get_test_class(self):
        return {{get_primitive_class_name(op)}}
    def get_inputs(self):
        return [
        {%- for example_tensor_meta in op.example_inputs_meta %}
            {{get_input_tensor_instance(example_tensor_meta)}},
        {%- endfor %}
        ]
{% endmacro %}

{%- macro get_test_class_name(op) -%}
TestPrimitiveOp_{{get_sha_hash_prefix(get_test_class_methods(op))}}
{%- endmacro -%}

{%- for op in ops %}
{%- if not is_cached_before(get_primitive_class_name(op)) -%}
class {{get_primitive_class_name(op)}}(InstanceTrait, paddle.nn.Layer):
    {{get_primitive_class_methods(op)}}
{{cache(get_primitive_class_name(op))}}
{%- endif -%}

class {{get_test_class_name(op)}}(CinnTestBase, unittest.TestCase):
    {{get_test_class_methods(op)}}

{% endfor %}

if __name__ == '__main__':
    unittest.main()
