
import paddle


class GraphModule(paddle.nn.Layer):
    def __init__(self):
        super().__init__()
        
    def forward(self, parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, data_0):

        # pd_op.matmul: (-1x5xf32) <- (-1x10xf32, 10x5xf32)
        matmul_0 = paddle._C_ops.matmul(data_0, parameter_5, False, False)
        del data_0, parameter_5

        # pd_op.add: (-1x5xf32) <- (-1x5xf32, 5xf32)
        add_2 = paddle._C_ops.add(matmul_0, parameter_4)
        del matmul_0, parameter_4

        # pd_op.tanh: (-1x5xf32) <- (-1x5xf32)
        tanh_0 = paddle._C_ops.tanh(add_2)
        del add_2

        # pd_op.matmul: (-1x3xf32) <- (-1x5xf32, 5x3xf32)
        matmul_1 = paddle._C_ops.matmul(tanh_0, parameter_3, False, False)
        del parameter_3

        # pd_op.add: (-1x3xf32) <- (-1x3xf32, 3xf32)
        add_0 = paddle._C_ops.add(matmul_1, parameter_2)
        del matmul_1, parameter_2

        # pd_op.matmul: (-1x1xf32) <- (-1x5xf32, 5x1xf32)
        matmul_2 = paddle._C_ops.matmul(tanh_0, parameter_1, False, False)
        del parameter_1, tanh_0

        # pd_op.add: (-1x1xf32) <- (-1x1xf32, 1xf32)
        add_1 = paddle._C_ops.add(matmul_2, parameter_0)
        del matmul_2, parameter_0

        return add_0, add_1