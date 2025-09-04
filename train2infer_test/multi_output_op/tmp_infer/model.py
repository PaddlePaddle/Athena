
import paddle


class GraphModule(paddle.nn.Layer):
    def __init__(self):
        super().__init__()
        
    def forward(self, data_0):

        # pd_op.full: (1xi32) <- ()
        full_0 = paddle._C_ops.full([1], float('1'), paddle.int32, paddle.core.CPUPlace())

        # pd_op.split_with_num: ([4x3xf32, 4x3xf32]) <- (4x6xf32, 1xi32)
        split_with_num_0 = paddle._C_ops.split_with_num(data_0, 2, full_0)
        del data_0, full_0

        # builtin.split: (4x3xf32, 4x3xf32) <- ([4x3xf32, 4x3xf32])
        split_0, split_1, = split_with_num_0
        del split_with_num_0

        return split_0, split_1