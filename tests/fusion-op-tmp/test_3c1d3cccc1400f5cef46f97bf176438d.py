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
    return 7 # number-of-ops

def GetPaddleDebugNumAllowedOps():
    try:
        return int(os.getenv('PADDLE_DEBUG_NUM_ALLOWED_OPS'))
    except:
        return None

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


paddle_debug_num_allowed_ops = GetPaddleDebugNumAllowedOps()

def FastReturn(i):
    return (
        type(paddle_debug_num_allowed_ops) is int
        and i >= paddle_debug_num_allowed_ops
    )

class FusionOp(paddle.nn.Layer):
    def __init__(self):
        super().__init__()

    def forward(self, data_0, full_2):

        if FastReturn(0):
            return data_0, full_2

        #  type: (xf32) <- (1x-1x768xf32)
        # shape: ([]) <- ([1, S0, 768])
        #  data: (None) <- (None)
        reduce_sum_0 = paddle.sum(data_0, keepdim=False, axis=[])

        if FastReturn(1):
            return full_2, reduce_sum_0

        #  type: (1xf32) <- ()
        # shape: ([1]) <- ()
        #  data: ([0]) <- ()
        full_0 = paddle.full(shape=[1], dtype='float32', fill_value=0)

        if FastReturn(2):
            return full_2, reduce_sum_0, full_0

        #  type: (1xf32) <- (xf32)
        # shape: ([1]) <- ([])
        #  data: (None) <- (None)
        broadcast_0 = paddle.broadcast_to(reduce_sum_0, [1])

        if FastReturn(3):
            return full_2, full_0, broadcast_0

        #  type: (1xb) <- (1xf32, 1xf32)
        # shape: ([1]) <- ([1], [1])
        #  data: (None) <- (None, [0])
        greater_than_0 = broadcast_0 > full_0

        if FastReturn(4):
            return full_2, greater_than_0

        #  type: (1xf32) <- ()
        # shape: ([1]) <- ()
        #  data: ([1]) <- ()
        full_1 = paddle.full(shape=[1], dtype='float32', fill_value=1)

        if FastReturn(5):
            return full_2, greater_than_0, full_1

        #  type: (1xb) <- (1xf32, 1xf32)
        # shape: ([1]) <- ([1], [1])
        #  data: (None) <- ([0], [1])
        less_than_0 = full_2 < full_1

        if FastReturn(6):
            return greater_than_0, less_than_0

        #  type: (1xb) <- (1xb, 1xb)
        # shape: ([1]) <- ([1], [1])
        #  data: (None) <- (None, None)
        logical_and_0 = paddle.logical_and(greater_than_0, less_than_0)

        #  type: () <- (1xb)
        # shape: () <- ([1])
        #  data: () <- (None)
        None
        return logical_and_0


class TestFusionOp(unittest.TestCase):
    def setUp(self):
        paddle.seed(2024)
        self.prepare_data()

    def prepare_data(self):
        self.inputs = [
            paddle.uniform([1, 2, 768], dtype='float32', min=-0.5, max=0.5),
            paddle.to_tensor([-1], dtype='float32').reshape([1]),
        ]
        for input in self.inputs:
          input.stop_gradient = True

    def apply_to_static(self, net, use_cinn):
        build_strategy = paddle.static.BuildStrategy()
        input_spec = [
            paddle.static.InputSpec(shape=[1, None, 768], dtype='float32'),
            paddle.static.InputSpec(shape=[1], dtype='float32'),
        ]
        build_strategy.build_cinn_pass = use_cinn
        return paddle.jit.to_static(
            net,
            input_spec=input_spec,
            build_strategy=build_strategy,
            full_graph=True,
        )

    def train(self, use_cinn):
        net = FusionOp()
        net.eval()
        if GetEnvVarEnableJit():
            net = self.apply_to_static(net, use_cinn)
        out = net(*self.inputs)
        return out

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

if __name__ == '__main__':
    unittest.main()