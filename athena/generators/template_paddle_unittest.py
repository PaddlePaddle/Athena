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

def NumCurrentUnittestOperations():
    return {{stmts[:-1] | length}}

def GetPaddleDebugNumAllowedOps():
    try:
        return int(os.getenv('PADDLE_DEBUG_NUM_ALLOWED_OPS'))
    except:
        return None

paddle_debug_num_allowed_ops = GetPaddleDebugNumAllowedOps()

def FastReturn(i):
    return (
        type(paddle_debug_num_allowed_ops) is int
        and i >= paddle_debug_num_allowed_ops
    )

class {{unittest_class_name}}(paddle.nn.Layer):
    def __init__(self):
        super().__init__()

    def forward(self, {{ input_arg_names | join(", ") }}):
    {%- for i, stmt in stmts %}
    {%- if (i + 1) < (stmts | length) %}

        if FastReturn({{i}}):
            return {{ stmt.tensors_used_by_downstream | join(", ") }}
    {%- endif %}

        {{stmt.comment}}
        {{stmt.pycode}}
    {%- endfor %}


class Test{{unittest_class_name}}(unittest.TestCase):
    def setUp(self):
        paddle.seed(2024)
        self.prepare_data()

    def prepare_data(self):
        self.inputs = [
        {%- for shape, dtype, big_dtype, min, max in input_tensor_descs %}
        {%- if big_dtype == "bool" %}
            paddle.zeros({{shape}}, dtype='{{dtype}}'),
        {%- elif big_dtype == "int64" %}
            paddle.randint(low={{min}}, high={{max}}, shape={{shape}}, dtype='{{dtype}}'),
        {%- elif big_dtype == "float64" %}
            paddle.uniform({{shape}}, dtype='{{dtype}}', min={{min}}, max={{max}}),
        {%- endif %}
        {%- endfor %}
        ]
        for input in self.inputs:
          input.stop_gradient = True

    def apply_to_static(self, net, use_cinn):
        build_strategy = paddle.static.BuildStrategy()
        input_spec = [
        {%- for shape, dtype in input_spec_shape_dtypes %}
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
        net = {{unittest_class_name}}()
        net.eval()
        net = self.apply_to_static(net, use_cinn)
        out = net(*self.inputs)
        return out

    def test_train(self):
        dy_outs = self.train(use_cinn=False)
        cinn_outs = self.train(use_cinn=True)

        for cinn_out, dy_out in zip(cinn_outs, dy_outs):
          if type(cinn_out) is list and type(dy_out) is list:
            for x, y in zip(cinn_out, dy_out):
              self.assert_all_close(x, y)
          else:
            self.assert_all_close(cinn_out, dy_out)

    def assert_all_close(self, x, y):
        if (hasattr(x, "numpy") and hasattr(y, "numpy")):
            np.testing.assert_allclose(x.numpy(), y.numpy(), atol=1e-6)
        else:
            assert x == y


if __name__ == '__main__':
    unittest.main()
