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

def NumCurrentUnittestBlocks():
    return 1 # number-of-blocks

def NumOperationsInBlock(block_idx):
    return [188][block_idx] - 1 # number-of-ops-in-block

def GetPaddleDebugNumAllowedBlocks():
    try:
        return int(os.getenv('PADDLE_DEBUG_NUM_ALLOWED_BLOCKS'))
    except:
        return None

paddle_debug_num_allowed_blocks = GetPaddleDebugNumAllowedBlocks()

def ShouldTestBlock(block_idx):
    if paddle_debug_num_allowed_blocks is not int:
        return True
    return block_idx < paddle_debug_num_allowed_blocks

def GetPaddleDebugNumAllowedOps():
    try:
        return int(os.getenv('PADDLE_DEBUG_NUM_ALLOWED_OPS'))
    except:
        return None

paddle_debug_num_allowed_ops = GetPaddleDebugNumAllowedOps()

def FastReturn(block_idx, op_idx):
    if type(paddle_debug_num_allowed_blocks) is not int:
        return False
    if block_idx + 1 != paddle_debug_num_allowed_blocks:
        return False
    if type(paddle_debug_num_allowed_ops) is not int:
        return False
    return op_idx >= paddle_debug_num_allowed_ops



class BlockEntries:

    def builtin_module_0_0_0(self, parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, data_0, data_1, data_2, data_3, data_4):

        # pd_op.full: (1xi32) <- ()
        full_0 = paddle.full(shape=[1], dtype='int32', fill_value=-1)

        # builtin.combine: ([200x1xf32, 200x1xf32]) <- (200x1xf32, 200x1xf32)
        combine_0 = [data_0, data_1]

        # pd_op.concat: (200x2xf32) <- ([200x1xf32, 200x1xf32], 1xi32)
        concat_0 = paddle.concat(combine_0, full_0)

        # pd_op.full: (2x2xf32) <- ()
        full_1 = paddle.full(shape=[2, 2], dtype='float32', fill_value=0)

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_0 = [0]

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_1 = [1]

        # pd_op.slice: (xi64) <- (2xi64, 1xi64, 1xi64)
        slice_0 = paddle.slice(parameter_1, axes=[0], starts=full_int_array_0, ends=full_int_array_1)

        # pd_op.full: (1xf32) <- ()
        full_2 = paddle.full(shape=[1], dtype='float32', fill_value=1)

        # pd_op.scale: (xi64) <- (xi64, 1xf32)
        scale_0 = paddle.scale(slice_0, full_2, bias_after_scale=True, bias=1)

        # pd_op.full: (1xi32) <- ()
        full_3 = paddle.full(shape=[1], dtype='int32', fill_value=0)

        # pd_op.full: (1xi32) <- ()
        full_4 = paddle.full(shape=[1], dtype='int32', fill_value=1)

        # pd_op.full: (xi64) <- ()
        full_5 = paddle.full(shape=[], dtype='int64', fill_value=0)

        # pd_op.full: (xi64) <- ()
        full_6 = paddle.full(shape=[], dtype='int64', fill_value=1)

        # builtin.combine: ([xi64, xi64]) <- (xi64, xi64)
        combine_1 = [slice_0, full_5]

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_2 = [1]

        # pd_op.reshape: (1xi64, 0xi64) <- (xi64, 1xi64)
        reshape_0, reshape_1 = paddle.reshape(slice_0, full_int_array_2), None

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_3 = [1]

        # pd_op.reshape: (1xi64, 0xi64) <- (xi64, 1xi64)
        reshape_2, reshape_3 = paddle.reshape(full_5, full_int_array_3), None

        # builtin.combine: ([1xi64, 1xi64]) <- (1xi64, 1xi64)
        combine_2 = [reshape_0, reshape_2]

        # pd_op.full: (1xi32) <- ()
        full_7 = paddle.full(shape=[1], dtype='int32', fill_value=0)

        # pd_op.concat: (2xi64) <- ([1xi64, 1xi64], 1xi32)
        concat_1 = paddle.concat(combine_2, full_7)

        # builtin.combine: ([xi64, xi64]) <- (xi64, xi64)
        combine_3 = [scale_0, full_6]

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_4 = [1]

        # pd_op.reshape: (1xi64, 0xi64) <- (xi64, 1xi64)
        reshape_4, reshape_5 = paddle.reshape(scale_0, full_int_array_4), None

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_5 = [1]

        # pd_op.reshape: (1xi64, 0xi64) <- (xi64, 1xi64)
        reshape_6, reshape_7 = paddle.reshape(full_6, full_int_array_5), None

        # builtin.combine: ([1xi64, 1xi64]) <- (1xi64, 1xi64)
        combine_4 = [reshape_4, reshape_6]

        # pd_op.full: (1xi32) <- ()
        full_8 = paddle.full(shape=[1], dtype='int32', fill_value=0)

        # pd_op.concat: (2xi64) <- ([1xi64, 1xi64], 1xi32)
        concat_2 = paddle.concat(combine_4, full_8)

        # pd_op.full_int_array: (2xi64) <- ()
        full_int_array_6 = [1, 1]

        # pd_op.set_value_: (2x2xf32) <- (2x2xf32, 2xi64, 2xi64, 2xi64)
        set_value__0 = paddle._C_ops.set_value_(full_1, concat_1, concat_2, full_int_array_6, [0, 1], [0, 1], [], [1], [1])

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_7 = [1]

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_8 = [2]

        # pd_op.slice: (xi64) <- (2xi64, 1xi64, 1xi64)
        slice_1 = paddle.slice(parameter_1, axes=[0], starts=full_int_array_7, ends=full_int_array_8)

        # pd_op.full: (1xf32) <- ()
        full_9 = paddle.full(shape=[1], dtype='float32', fill_value=1)

        # pd_op.scale: (xi64) <- (xi64, 1xf32)
        scale_1 = paddle.scale(slice_1, full_9, bias_after_scale=True, bias=1)

        # pd_op.full: (1xi32) <- ()
        full_10 = paddle.full(shape=[1], dtype='int32', fill_value=1)

        # pd_op.full: (1xi32) <- ()
        full_11 = paddle.full(shape=[1], dtype='int32', fill_value=2)

        # pd_op.full: (xi64) <- ()
        full_12 = paddle.full(shape=[], dtype='int64', fill_value=1)

        # pd_op.full: (xi64) <- ()
        full_13 = paddle.full(shape=[], dtype='int64', fill_value=2)

        # builtin.combine: ([xi64, xi64]) <- (xi64, xi64)
        combine_5 = [slice_1, full_12]

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_9 = [1]

        # pd_op.reshape: (1xi64, 0xi64) <- (xi64, 1xi64)
        reshape_8, reshape_9 = paddle.reshape(slice_1, full_int_array_9), None

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_10 = [1]

        # pd_op.reshape: (1xi64, 0xi64) <- (xi64, 1xi64)
        reshape_10, reshape_11 = paddle.reshape(full_12, full_int_array_10), None

        # builtin.combine: ([1xi64, 1xi64]) <- (1xi64, 1xi64)
        combine_6 = [reshape_8, reshape_10]

        # pd_op.full: (1xi32) <- ()
        full_14 = paddle.full(shape=[1], dtype='int32', fill_value=0)

        # pd_op.concat: (2xi64) <- ([1xi64, 1xi64], 1xi32)
        concat_3 = paddle.concat(combine_6, full_14)

        # builtin.combine: ([xi64, xi64]) <- (xi64, xi64)
        combine_7 = [scale_1, full_13]

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_11 = [1]

        # pd_op.reshape: (1xi64, 0xi64) <- (xi64, 1xi64)
        reshape_12, reshape_13 = paddle.reshape(scale_1, full_int_array_11), None

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_12 = [1]

        # pd_op.reshape: (1xi64, 0xi64) <- (xi64, 1xi64)
        reshape_14, reshape_15 = paddle.reshape(full_13, full_int_array_12), None

        # builtin.combine: ([1xi64, 1xi64]) <- (1xi64, 1xi64)
        combine_8 = [reshape_12, reshape_14]

        # pd_op.full: (1xi32) <- ()
        full_15 = paddle.full(shape=[1], dtype='int32', fill_value=0)

        # pd_op.concat: (2xi64) <- ([1xi64, 1xi64], 1xi32)
        concat_4 = paddle.concat(combine_8, full_15)

        # pd_op.full_int_array: (2xi64) <- ()
        full_int_array_13 = [1, 1]

        # pd_op.set_value_: (2x2xf32) <- (2x2xf32, 2xi64, 2xi64, 2xi64)
        set_value__1 = paddle._C_ops.set_value_(set_value__0, concat_3, concat_4, full_int_array_13, [0, 1], [0, 1], [], [1], [1])

        # pd_op.matmul: (200x2xf32) <- (200x2xf32, 2x2xf32)
        matmul_0 = paddle.matmul(concat_0, set_value__1, transpose_x=False, transpose_y=False)

        # pd_op.matmul: (200x128xf32) <- (200x2xf32, 2x128xf32)
        matmul_1 = paddle.matmul(matmul_0, parameter_0, transpose_x=False, transpose_y=False)

        # pd_op.full: (1xf32) <- ()
        full_16 = paddle.full(shape=[1], dtype='float32', fill_value=6.28319)

        # pd_op.scale: (200x128xf32) <- (200x128xf32, 1xf32)
        scale_2 = paddle.scale(matmul_1, full_16, bias_after_scale=True, bias=0)

        # pd_op.sin: (200x128xf32) <- (200x128xf32)
        sin_0 = paddle.sin(scale_2)

        # pd_op.full: (1xf32) <- ()
        full_17 = paddle.full(shape=[1], dtype='float32', fill_value=6.28319)

        # pd_op.scale: (200x128xf32) <- (200x128xf32, 1xf32)
        scale_3 = paddle.scale(matmul_1, full_17, bias_after_scale=True, bias=0)

        # pd_op.cos: (200x128xf32) <- (200x128xf32)
        cos_0 = paddle.cos(scale_3)

        # pd_op.full: (1xi32) <- ()
        full_18 = paddle.full(shape=[1], dtype='int32', fill_value=-1)

        # builtin.combine: ([200x128xf32, 200x128xf32]) <- (200x128xf32, 200x128xf32)
        combine_9 = [sin_0, cos_0]

        # pd_op.concat: (200x256xf32) <- ([200x128xf32, 200x128xf32], 1xi32)
        concat_5 = paddle.concat(combine_9, full_18)

        # pd_op.full: (1xi32) <- ()
        full_19 = paddle.full(shape=[1], dtype='int32', fill_value=-1)

        # builtin.combine: ([200x2xf32, 200x256xf32]) <- (200x2xf32, 200x256xf32)
        combine_10 = [concat_0, concat_5]

        # pd_op.concat: (200x258xf32) <- ([200x2xf32, 200x256xf32], 1xi32)
        concat_6 = paddle.concat(combine_10, full_19)

        # pd_op.multiply: (256x258xf32) <- (256x258xf32, 256x258xf32)
        multiply_0 = parameter_27 * parameter_27

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_14 = [1]

        # pd_op.sum: (256x1xf32) <- (256x258xf32, 1xi64)
        sum_0 = paddle.sum(multiply_0, keepdim=True, axis=full_int_array_14)

        # pd_op.sqrt: (256x1xf32) <- (256x1xf32)
        sqrt_0 = paddle.sqrt(sum_0)

        # pd_op.multiply: (256x258xf32) <- (256x1xf32, 256x258xf32)
        multiply_1 = parameter_26 * parameter_27

        # pd_op.divide: (256x258xf32) <- (256x258xf32, 256x1xf32)
        divide_0 = multiply_1 / sqrt_0

        # pd_op.transpose: (258x256xf32) <- (256x258xf32)
        transpose_0 = paddle.transpose(divide_0, perm=[1, 0])

        # pd_op.matmul: (200x256xf32) <- (200x258xf32, 258x256xf32)
        matmul_2 = paddle.matmul(concat_6, transpose_0, transpose_x=False, transpose_y=False)

        # pd_op.add: (200x256xf32) <- (200x256xf32, 256xf32)
        add_0 = matmul_2 + parameter_25

        # pd_op.sigmoid: (200x256xf32) <- (200x256xf32)
        sigmoid_0 = paddle.nn.functional.sigmoid(add_0)

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_2 = add_0 * sigmoid_0

        # pd_op.multiply: (256x258xf32) <- (256x258xf32, 256x258xf32)
        multiply_3 = parameter_24 * parameter_24

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_15 = [1]

        # pd_op.sum: (256x1xf32) <- (256x258xf32, 1xi64)
        sum_1 = paddle.sum(multiply_3, keepdim=True, axis=full_int_array_15)

        # pd_op.sqrt: (256x1xf32) <- (256x1xf32)
        sqrt_1 = paddle.sqrt(sum_1)

        # pd_op.multiply: (256x258xf32) <- (256x1xf32, 256x258xf32)
        multiply_4 = parameter_23 * parameter_24

        # pd_op.divide: (256x258xf32) <- (256x258xf32, 256x1xf32)
        divide_1 = multiply_4 / sqrt_1

        # pd_op.transpose: (258x256xf32) <- (256x258xf32)
        transpose_1 = paddle.transpose(divide_1, perm=[1, 0])

        # pd_op.matmul: (200x256xf32) <- (200x258xf32, 258x256xf32)
        matmul_3 = paddle.matmul(concat_6, transpose_1, transpose_x=False, transpose_y=False)

        # pd_op.add: (200x256xf32) <- (200x256xf32, 256xf32)
        add_1 = matmul_3 + parameter_22

        # pd_op.sigmoid: (200x256xf32) <- (200x256xf32)
        sigmoid_1 = paddle.nn.functional.sigmoid(add_1)

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_5 = add_1 * sigmoid_1

        # pd_op.multiply: (256x258xf32) <- (256x258xf32, 256x258xf32)
        multiply_6 = parameter_21 * parameter_21

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_16 = [1]

        # pd_op.sum: (256x1xf32) <- (256x258xf32, 1xi64)
        sum_2 = paddle.sum(multiply_6, keepdim=True, axis=full_int_array_16)

        # pd_op.sqrt: (256x1xf32) <- (256x1xf32)
        sqrt_2 = paddle.sqrt(sum_2)

        # pd_op.multiply: (256x258xf32) <- (256x1xf32, 256x258xf32)
        multiply_7 = parameter_20 * parameter_21

        # pd_op.divide: (256x258xf32) <- (256x258xf32, 256x1xf32)
        divide_2 = multiply_7 / sqrt_2

        # pd_op.transpose: (258x256xf32) <- (256x258xf32)
        transpose_2 = paddle.transpose(divide_2, perm=[1, 0])

        # pd_op.matmul: (200x256xf32) <- (200x258xf32, 258x256xf32)
        matmul_4 = paddle.matmul(concat_6, transpose_2, transpose_x=False, transpose_y=False)

        # pd_op.add: (200x256xf32) <- (200x256xf32, 256xf32)
        add_2 = matmul_4 + parameter_19

        # pd_op.sigmoid: (200x256xf32) <- (200x256xf32)
        sigmoid_2 = paddle.nn.functional.sigmoid(add_2)

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_8 = add_2 * sigmoid_2

        # pd_op.multiply: (256x256xf32) <- (256x256xf32, 256x256xf32)
        multiply_9 = parameter_18 * parameter_18

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_17 = [1]

        # pd_op.sum: (256x1xf32) <- (256x256xf32, 1xi64)
        sum_3 = paddle.sum(multiply_9, keepdim=True, axis=full_int_array_17)

        # pd_op.sqrt: (256x1xf32) <- (256x1xf32)
        sqrt_3 = paddle.sqrt(sum_3)

        # pd_op.multiply: (256x256xf32) <- (256x1xf32, 256x256xf32)
        multiply_10 = parameter_17 * parameter_18

        # pd_op.divide: (256x256xf32) <- (256x256xf32, 256x1xf32)
        divide_3 = multiply_10 / sqrt_3

        # pd_op.transpose: (256x256xf32) <- (256x256xf32)
        transpose_3 = paddle.transpose(divide_3, perm=[1, 0])

        # pd_op.matmul: (200x256xf32) <- (200x256xf32, 256x256xf32)
        matmul_5 = paddle.matmul(multiply_8, transpose_3, transpose_x=False, transpose_y=False)

        # pd_op.add: (200x256xf32) <- (200x256xf32, 256xf32)
        add_3 = matmul_5 + parameter_16

        # pd_op.sigmoid: (200x256xf32) <- (200x256xf32)
        sigmoid_3 = paddle.nn.functional.sigmoid(add_3)

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_11 = add_3 * sigmoid_3

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_12 = multiply_11 * multiply_2

        # pd_op.subtract: (200x256xf32) <- (200x256xf32, 200x256xf32)
        subtract_0 = multiply_2 - multiply_12

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_13 = multiply_11 * multiply_5

        # pd_op.add: (200x256xf32) <- (200x256xf32, 200x256xf32)
        add_4 = subtract_0 + multiply_13

        # pd_op.multiply: (256x256xf32) <- (256x256xf32, 256x256xf32)
        multiply_14 = parameter_15 * parameter_15

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_18 = [1]

        # pd_op.sum: (256x1xf32) <- (256x256xf32, 1xi64)
        sum_4 = paddle.sum(multiply_14, keepdim=True, axis=full_int_array_18)

        # pd_op.sqrt: (256x1xf32) <- (256x1xf32)
        sqrt_4 = paddle.sqrt(sum_4)

        # pd_op.multiply: (256x256xf32) <- (256x1xf32, 256x256xf32)
        multiply_15 = parameter_14 * parameter_15

        # pd_op.divide: (256x256xf32) <- (256x256xf32, 256x1xf32)
        divide_4 = multiply_15 / sqrt_4

        # pd_op.transpose: (256x256xf32) <- (256x256xf32)
        transpose_4 = paddle.transpose(divide_4, perm=[1, 0])

        # pd_op.matmul: (200x256xf32) <- (200x256xf32, 256x256xf32)
        matmul_6 = paddle.matmul(add_4, transpose_4, transpose_x=False, transpose_y=False)

        # pd_op.add: (200x256xf32) <- (200x256xf32, 256xf32)
        add_5 = matmul_6 + parameter_13

        # pd_op.sigmoid: (200x256xf32) <- (200x256xf32)
        sigmoid_4 = paddle.nn.functional.sigmoid(add_5)

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_16 = add_5 * sigmoid_4

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_17 = multiply_16 * multiply_2

        # pd_op.subtract: (200x256xf32) <- (200x256xf32, 200x256xf32)
        subtract_1 = multiply_2 - multiply_17

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_18 = multiply_16 * multiply_5

        # pd_op.add: (200x256xf32) <- (200x256xf32, 200x256xf32)
        add_6 = subtract_1 + multiply_18

        # pd_op.multiply: (256x256xf32) <- (256x256xf32, 256x256xf32)
        multiply_19 = parameter_12 * parameter_12

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_19 = [1]

        # pd_op.sum: (256x1xf32) <- (256x256xf32, 1xi64)
        sum_5 = paddle.sum(multiply_19, keepdim=True, axis=full_int_array_19)

        # pd_op.sqrt: (256x1xf32) <- (256x1xf32)
        sqrt_5 = paddle.sqrt(sum_5)

        # pd_op.multiply: (256x256xf32) <- (256x1xf32, 256x256xf32)
        multiply_20 = parameter_11 * parameter_12

        # pd_op.divide: (256x256xf32) <- (256x256xf32, 256x1xf32)
        divide_5 = multiply_20 / sqrt_5

        # pd_op.transpose: (256x256xf32) <- (256x256xf32)
        transpose_5 = paddle.transpose(divide_5, perm=[1, 0])

        # pd_op.matmul: (200x256xf32) <- (200x256xf32, 256x256xf32)
        matmul_7 = paddle.matmul(add_6, transpose_5, transpose_x=False, transpose_y=False)

        # pd_op.add: (200x256xf32) <- (200x256xf32, 256xf32)
        add_7 = matmul_7 + parameter_10

        # pd_op.sigmoid: (200x256xf32) <- (200x256xf32)
        sigmoid_5 = paddle.nn.functional.sigmoid(add_7)

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_21 = add_7 * sigmoid_5

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_22 = multiply_21 * multiply_2

        # pd_op.subtract: (200x256xf32) <- (200x256xf32, 200x256xf32)
        subtract_2 = multiply_2 - multiply_22

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_23 = multiply_21 * multiply_5

        # pd_op.add: (200x256xf32) <- (200x256xf32, 200x256xf32)
        add_8 = subtract_2 + multiply_23

        # pd_op.multiply: (256x256xf32) <- (256x256xf32, 256x256xf32)
        multiply_24 = parameter_9 * parameter_9

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_20 = [1]

        # pd_op.sum: (256x1xf32) <- (256x256xf32, 1xi64)
        sum_6 = paddle.sum(multiply_24, keepdim=True, axis=full_int_array_20)

        # pd_op.sqrt: (256x1xf32) <- (256x1xf32)
        sqrt_6 = paddle.sqrt(sum_6)

        # pd_op.multiply: (256x256xf32) <- (256x1xf32, 256x256xf32)
        multiply_25 = parameter_8 * parameter_9

        # pd_op.divide: (256x256xf32) <- (256x256xf32, 256x1xf32)
        divide_6 = multiply_25 / sqrt_6

        # pd_op.transpose: (256x256xf32) <- (256x256xf32)
        transpose_6 = paddle.transpose(divide_6, perm=[1, 0])

        # pd_op.matmul: (200x256xf32) <- (200x256xf32, 256x256xf32)
        matmul_8 = paddle.matmul(add_8, transpose_6, transpose_x=False, transpose_y=False)

        # pd_op.add: (200x256xf32) <- (200x256xf32, 256xf32)
        add_9 = matmul_8 + parameter_7

        # pd_op.sigmoid: (200x256xf32) <- (200x256xf32)
        sigmoid_6 = paddle.nn.functional.sigmoid(add_9)

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_26 = add_9 * sigmoid_6

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_27 = multiply_26 * multiply_2

        # pd_op.subtract: (200x256xf32) <- (200x256xf32, 200x256xf32)
        subtract_3 = multiply_2 - multiply_27

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_28 = multiply_26 * multiply_5

        # pd_op.add: (200x256xf32) <- (200x256xf32, 200x256xf32)
        add_10 = subtract_3 + multiply_28

        # pd_op.multiply: (256x256xf32) <- (256x256xf32, 256x256xf32)
        multiply_29 = parameter_6 * parameter_6

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_21 = [1]

        # pd_op.sum: (256x1xf32) <- (256x256xf32, 1xi64)
        sum_7 = paddle.sum(multiply_29, keepdim=True, axis=full_int_array_21)

        # pd_op.sqrt: (256x1xf32) <- (256x1xf32)
        sqrt_7 = paddle.sqrt(sum_7)

        # pd_op.multiply: (256x256xf32) <- (256x1xf32, 256x256xf32)
        multiply_30 = parameter_5 * parameter_6

        # pd_op.divide: (256x256xf32) <- (256x256xf32, 256x1xf32)
        divide_7 = multiply_30 / sqrt_7

        # pd_op.transpose: (256x256xf32) <- (256x256xf32)
        transpose_7 = paddle.transpose(divide_7, perm=[1, 0])

        # pd_op.matmul: (200x256xf32) <- (200x256xf32, 256x256xf32)
        matmul_9 = paddle.matmul(add_10, transpose_7, transpose_x=False, transpose_y=False)

        # pd_op.add: (200x256xf32) <- (200x256xf32, 256xf32)
        add_11 = matmul_9 + parameter_4

        # pd_op.sigmoid: (200x256xf32) <- (200x256xf32)
        sigmoid_7 = paddle.nn.functional.sigmoid(add_11)

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_31 = add_11 * sigmoid_7

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_32 = multiply_31 * multiply_2

        # pd_op.subtract: (200x256xf32) <- (200x256xf32, 200x256xf32)
        subtract_4 = multiply_2 - multiply_32

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_33 = multiply_31 * multiply_5

        # pd_op.add: (200x256xf32) <- (200x256xf32, 200x256xf32)
        add_12 = subtract_4 + multiply_33

        # pd_op.matmul: (200x1xf32) <- (200x256xf32, 256x1xf32)
        matmul_10 = paddle.matmul(add_12, parameter_3, transpose_x=False, transpose_y=False)

        # pd_op.add: (200x1xf32) <- (200x1xf32, 1xf32)
        add_13 = matmul_10 + parameter_2

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_22 = [1]

        # pd_op.full: (1xi32) <- ()
        full_20 = paddle.full(shape=[1], dtype='int32', fill_value=1)

        # pd_op.split: ([200x1xf32]) <- (200x1xf32, 1xi64, 1xi32)
        split_0 = paddle.split(add_13, full_int_array_22, full_20)

        # builtin.split: (200x1xf32) <- ([200x1xf32])
        split_1, = split_0

        # pd_op.full: (1xf32) <- ()
        full_21 = paddle.full(shape=[1], dtype='float32', fill_value=1)

        # pd_op.scale: (200x1xf32) <- (200x1xf32, 1xf32)
        scale_4 = paddle.scale(split_1, full_21, bias_after_scale=True, bias=70)
        return concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4



# [2, 128]
builtin_module_0_0_0_0_0_shape = None
# [2]
builtin_module_0_0_0_0_1_shape = None
# [1]
builtin_module_0_0_0_0_2_shape = None
# [256, 1]
builtin_module_0_0_0_0_3_shape = None
# [256]
builtin_module_0_0_0_0_4_shape = None
# [256, 1]
builtin_module_0_0_0_0_5_shape = None
# [256, 256]
builtin_module_0_0_0_0_6_shape = None
# [256]
builtin_module_0_0_0_0_7_shape = None
# [256, 1]
builtin_module_0_0_0_0_8_shape = None
# [256, 256]
builtin_module_0_0_0_0_9_shape = None
# [256]
builtin_module_0_0_0_0_10_shape = None
# [256, 1]
builtin_module_0_0_0_0_11_shape = None
# [256, 256]
builtin_module_0_0_0_0_12_shape = None
# [256]
builtin_module_0_0_0_0_13_shape = None
# [256, 1]
builtin_module_0_0_0_0_14_shape = None
# [256, 256]
builtin_module_0_0_0_0_15_shape = None
# [256]
builtin_module_0_0_0_0_16_shape = None
# [256, 1]
builtin_module_0_0_0_0_17_shape = None
# [256, 256]
builtin_module_0_0_0_0_18_shape = None
# [256]
builtin_module_0_0_0_0_19_shape = None
# [256, 1]
builtin_module_0_0_0_0_20_shape = None
# [256, 258]
builtin_module_0_0_0_0_21_shape = None
# [256]
builtin_module_0_0_0_0_22_shape = None
# [256, 1]
builtin_module_0_0_0_0_23_shape = None
# [256, 258]
builtin_module_0_0_0_0_24_shape = None
# [256]
builtin_module_0_0_0_0_25_shape = None
# [256, 1]
builtin_module_0_0_0_0_26_shape = None
# [256, 258]
builtin_module_0_0_0_0_27_shape = None
# [200, 1]
builtin_module_0_0_0_0_28_shape = None
# [200, 1]
builtin_module_0_0_0_0_29_shape = None
# [200, 1]
builtin_module_0_0_0_0_30_shape = None
# [200, 1]
builtin_module_0_0_0_0_31_shape = None
# [200, 1]
builtin_module_0_0_0_0_32_shape = None

class BlockShapesExtractor:

    def builtin_module_0_0_0(self, parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, data_0, data_1, data_2, data_3, data_4):
        global builtin_module_0_0_0_0_0_shape
        builtin_module_0_0_0_0_0_shape = parameter_0.shape
        global builtin_module_0_0_0_0_1_shape
        builtin_module_0_0_0_0_1_shape = parameter_1.shape
        global builtin_module_0_0_0_0_2_shape
        builtin_module_0_0_0_0_2_shape = parameter_2.shape
        global builtin_module_0_0_0_0_3_shape
        builtin_module_0_0_0_0_3_shape = parameter_3.shape
        global builtin_module_0_0_0_0_4_shape
        builtin_module_0_0_0_0_4_shape = parameter_4.shape
        global builtin_module_0_0_0_0_5_shape
        builtin_module_0_0_0_0_5_shape = parameter_5.shape
        global builtin_module_0_0_0_0_6_shape
        builtin_module_0_0_0_0_6_shape = parameter_6.shape
        global builtin_module_0_0_0_0_7_shape
        builtin_module_0_0_0_0_7_shape = parameter_7.shape
        global builtin_module_0_0_0_0_8_shape
        builtin_module_0_0_0_0_8_shape = parameter_8.shape
        global builtin_module_0_0_0_0_9_shape
        builtin_module_0_0_0_0_9_shape = parameter_9.shape
        global builtin_module_0_0_0_0_10_shape
        builtin_module_0_0_0_0_10_shape = parameter_10.shape
        global builtin_module_0_0_0_0_11_shape
        builtin_module_0_0_0_0_11_shape = parameter_11.shape
        global builtin_module_0_0_0_0_12_shape
        builtin_module_0_0_0_0_12_shape = parameter_12.shape
        global builtin_module_0_0_0_0_13_shape
        builtin_module_0_0_0_0_13_shape = parameter_13.shape
        global builtin_module_0_0_0_0_14_shape
        builtin_module_0_0_0_0_14_shape = parameter_14.shape
        global builtin_module_0_0_0_0_15_shape
        builtin_module_0_0_0_0_15_shape = parameter_15.shape
        global builtin_module_0_0_0_0_16_shape
        builtin_module_0_0_0_0_16_shape = parameter_16.shape
        global builtin_module_0_0_0_0_17_shape
        builtin_module_0_0_0_0_17_shape = parameter_17.shape
        global builtin_module_0_0_0_0_18_shape
        builtin_module_0_0_0_0_18_shape = parameter_18.shape
        global builtin_module_0_0_0_0_19_shape
        builtin_module_0_0_0_0_19_shape = parameter_19.shape
        global builtin_module_0_0_0_0_20_shape
        builtin_module_0_0_0_0_20_shape = parameter_20.shape
        global builtin_module_0_0_0_0_21_shape
        builtin_module_0_0_0_0_21_shape = parameter_21.shape
        global builtin_module_0_0_0_0_22_shape
        builtin_module_0_0_0_0_22_shape = parameter_22.shape
        global builtin_module_0_0_0_0_23_shape
        builtin_module_0_0_0_0_23_shape = parameter_23.shape
        global builtin_module_0_0_0_0_24_shape
        builtin_module_0_0_0_0_24_shape = parameter_24.shape
        global builtin_module_0_0_0_0_25_shape
        builtin_module_0_0_0_0_25_shape = parameter_25.shape
        global builtin_module_0_0_0_0_26_shape
        builtin_module_0_0_0_0_26_shape = parameter_26.shape
        global builtin_module_0_0_0_0_27_shape
        builtin_module_0_0_0_0_27_shape = parameter_27.shape
        global builtin_module_0_0_0_0_28_shape
        builtin_module_0_0_0_0_28_shape = data_0.shape
        global builtin_module_0_0_0_0_29_shape
        builtin_module_0_0_0_0_29_shape = data_1.shape
        global builtin_module_0_0_0_0_30_shape
        builtin_module_0_0_0_0_30_shape = data_2.shape
        global builtin_module_0_0_0_0_31_shape
        builtin_module_0_0_0_0_31_shape = data_3.shape
        global builtin_module_0_0_0_0_32_shape
        builtin_module_0_0_0_0_32_shape = data_4.shape

        # pd_op.full: (1xi32) <- ()
        full_0 = paddle.full(shape=[1], dtype='int32', fill_value=-1)

        # builtin.combine: ([200x1xf32, 200x1xf32]) <- (200x1xf32, 200x1xf32)
        combine_0 = [data_0, data_1]

        # pd_op.concat: (200x2xf32) <- ([200x1xf32, 200x1xf32], 1xi32)
        concat_0 = paddle.concat(combine_0, full_0)

        # pd_op.full: (2x2xf32) <- ()
        full_1 = paddle.full(shape=[2, 2], dtype='float32', fill_value=0)

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_0 = [0]

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_1 = [1]

        # pd_op.slice: (xi64) <- (2xi64, 1xi64, 1xi64)
        slice_0 = paddle.slice(parameter_1, axes=[0], starts=full_int_array_0, ends=full_int_array_1)

        # pd_op.full: (1xf32) <- ()
        full_2 = paddle.full(shape=[1], dtype='float32', fill_value=1)

        # pd_op.scale: (xi64) <- (xi64, 1xf32)
        scale_0 = paddle.scale(slice_0, full_2, bias_after_scale=True, bias=1)

        # pd_op.full: (1xi32) <- ()
        full_3 = paddle.full(shape=[1], dtype='int32', fill_value=0)

        # pd_op.full: (1xi32) <- ()
        full_4 = paddle.full(shape=[1], dtype='int32', fill_value=1)

        # pd_op.full: (xi64) <- ()
        full_5 = paddle.full(shape=[], dtype='int64', fill_value=0)

        # pd_op.full: (xi64) <- ()
        full_6 = paddle.full(shape=[], dtype='int64', fill_value=1)

        # builtin.combine: ([xi64, xi64]) <- (xi64, xi64)
        combine_1 = [slice_0, full_5]

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_2 = [1]

        # pd_op.reshape: (1xi64, 0xi64) <- (xi64, 1xi64)
        reshape_0, reshape_1 = paddle.reshape(slice_0, full_int_array_2), None

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_3 = [1]

        # pd_op.reshape: (1xi64, 0xi64) <- (xi64, 1xi64)
        reshape_2, reshape_3 = paddle.reshape(full_5, full_int_array_3), None

        # builtin.combine: ([1xi64, 1xi64]) <- (1xi64, 1xi64)
        combine_2 = [reshape_0, reshape_2]

        # pd_op.full: (1xi32) <- ()
        full_7 = paddle.full(shape=[1], dtype='int32', fill_value=0)

        # pd_op.concat: (2xi64) <- ([1xi64, 1xi64], 1xi32)
        concat_1 = paddle.concat(combine_2, full_7)

        # builtin.combine: ([xi64, xi64]) <- (xi64, xi64)
        combine_3 = [scale_0, full_6]

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_4 = [1]

        # pd_op.reshape: (1xi64, 0xi64) <- (xi64, 1xi64)
        reshape_4, reshape_5 = paddle.reshape(scale_0, full_int_array_4), None

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_5 = [1]

        # pd_op.reshape: (1xi64, 0xi64) <- (xi64, 1xi64)
        reshape_6, reshape_7 = paddle.reshape(full_6, full_int_array_5), None

        # builtin.combine: ([1xi64, 1xi64]) <- (1xi64, 1xi64)
        combine_4 = [reshape_4, reshape_6]

        # pd_op.full: (1xi32) <- ()
        full_8 = paddle.full(shape=[1], dtype='int32', fill_value=0)

        # pd_op.concat: (2xi64) <- ([1xi64, 1xi64], 1xi32)
        concat_2 = paddle.concat(combine_4, full_8)

        # pd_op.full_int_array: (2xi64) <- ()
        full_int_array_6 = [1, 1]

        # pd_op.set_value_: (2x2xf32) <- (2x2xf32, 2xi64, 2xi64, 2xi64)
        set_value__0 = paddle._C_ops.set_value_(full_1, concat_1, concat_2, full_int_array_6, [0, 1], [0, 1], [], [1], [1])

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_7 = [1]

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_8 = [2]

        # pd_op.slice: (xi64) <- (2xi64, 1xi64, 1xi64)
        slice_1 = paddle.slice(parameter_1, axes=[0], starts=full_int_array_7, ends=full_int_array_8)

        # pd_op.full: (1xf32) <- ()
        full_9 = paddle.full(shape=[1], dtype='float32', fill_value=1)

        # pd_op.scale: (xi64) <- (xi64, 1xf32)
        scale_1 = paddle.scale(slice_1, full_9, bias_after_scale=True, bias=1)

        # pd_op.full: (1xi32) <- ()
        full_10 = paddle.full(shape=[1], dtype='int32', fill_value=1)

        # pd_op.full: (1xi32) <- ()
        full_11 = paddle.full(shape=[1], dtype='int32', fill_value=2)

        # pd_op.full: (xi64) <- ()
        full_12 = paddle.full(shape=[], dtype='int64', fill_value=1)

        # pd_op.full: (xi64) <- ()
        full_13 = paddle.full(shape=[], dtype='int64', fill_value=2)

        # builtin.combine: ([xi64, xi64]) <- (xi64, xi64)
        combine_5 = [slice_1, full_12]

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_9 = [1]

        # pd_op.reshape: (1xi64, 0xi64) <- (xi64, 1xi64)
        reshape_8, reshape_9 = paddle.reshape(slice_1, full_int_array_9), None

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_10 = [1]

        # pd_op.reshape: (1xi64, 0xi64) <- (xi64, 1xi64)
        reshape_10, reshape_11 = paddle.reshape(full_12, full_int_array_10), None

        # builtin.combine: ([1xi64, 1xi64]) <- (1xi64, 1xi64)
        combine_6 = [reshape_8, reshape_10]

        # pd_op.full: (1xi32) <- ()
        full_14 = paddle.full(shape=[1], dtype='int32', fill_value=0)

        # pd_op.concat: (2xi64) <- ([1xi64, 1xi64], 1xi32)
        concat_3 = paddle.concat(combine_6, full_14)

        # builtin.combine: ([xi64, xi64]) <- (xi64, xi64)
        combine_7 = [scale_1, full_13]

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_11 = [1]

        # pd_op.reshape: (1xi64, 0xi64) <- (xi64, 1xi64)
        reshape_12, reshape_13 = paddle.reshape(scale_1, full_int_array_11), None

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_12 = [1]

        # pd_op.reshape: (1xi64, 0xi64) <- (xi64, 1xi64)
        reshape_14, reshape_15 = paddle.reshape(full_13, full_int_array_12), None

        # builtin.combine: ([1xi64, 1xi64]) <- (1xi64, 1xi64)
        combine_8 = [reshape_12, reshape_14]

        # pd_op.full: (1xi32) <- ()
        full_15 = paddle.full(shape=[1], dtype='int32', fill_value=0)

        # pd_op.concat: (2xi64) <- ([1xi64, 1xi64], 1xi32)
        concat_4 = paddle.concat(combine_8, full_15)

        # pd_op.full_int_array: (2xi64) <- ()
        full_int_array_13 = [1, 1]

        # pd_op.set_value_: (2x2xf32) <- (2x2xf32, 2xi64, 2xi64, 2xi64)
        set_value__1 = paddle._C_ops.set_value_(set_value__0, concat_3, concat_4, full_int_array_13, [0, 1], [0, 1], [], [1], [1])

        # pd_op.matmul: (200x2xf32) <- (200x2xf32, 2x2xf32)
        matmul_0 = paddle.matmul(concat_0, set_value__1, transpose_x=False, transpose_y=False)

        # pd_op.matmul: (200x128xf32) <- (200x2xf32, 2x128xf32)
        matmul_1 = paddle.matmul(matmul_0, parameter_0, transpose_x=False, transpose_y=False)

        # pd_op.full: (1xf32) <- ()
        full_16 = paddle.full(shape=[1], dtype='float32', fill_value=6.28319)

        # pd_op.scale: (200x128xf32) <- (200x128xf32, 1xf32)
        scale_2 = paddle.scale(matmul_1, full_16, bias_after_scale=True, bias=0)

        # pd_op.sin: (200x128xf32) <- (200x128xf32)
        sin_0 = paddle.sin(scale_2)

        # pd_op.full: (1xf32) <- ()
        full_17 = paddle.full(shape=[1], dtype='float32', fill_value=6.28319)

        # pd_op.scale: (200x128xf32) <- (200x128xf32, 1xf32)
        scale_3 = paddle.scale(matmul_1, full_17, bias_after_scale=True, bias=0)

        # pd_op.cos: (200x128xf32) <- (200x128xf32)
        cos_0 = paddle.cos(scale_3)

        # pd_op.full: (1xi32) <- ()
        full_18 = paddle.full(shape=[1], dtype='int32', fill_value=-1)

        # builtin.combine: ([200x128xf32, 200x128xf32]) <- (200x128xf32, 200x128xf32)
        combine_9 = [sin_0, cos_0]

        # pd_op.concat: (200x256xf32) <- ([200x128xf32, 200x128xf32], 1xi32)
        concat_5 = paddle.concat(combine_9, full_18)

        # pd_op.full: (1xi32) <- ()
        full_19 = paddle.full(shape=[1], dtype='int32', fill_value=-1)

        # builtin.combine: ([200x2xf32, 200x256xf32]) <- (200x2xf32, 200x256xf32)
        combine_10 = [concat_0, concat_5]

        # pd_op.concat: (200x258xf32) <- ([200x2xf32, 200x256xf32], 1xi32)
        concat_6 = paddle.concat(combine_10, full_19)

        # pd_op.multiply: (256x258xf32) <- (256x258xf32, 256x258xf32)
        multiply_0 = parameter_27 * parameter_27

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_14 = [1]

        # pd_op.sum: (256x1xf32) <- (256x258xf32, 1xi64)
        sum_0 = paddle.sum(multiply_0, keepdim=True, axis=full_int_array_14)

        # pd_op.sqrt: (256x1xf32) <- (256x1xf32)
        sqrt_0 = paddle.sqrt(sum_0)

        # pd_op.multiply: (256x258xf32) <- (256x1xf32, 256x258xf32)
        multiply_1 = parameter_26 * parameter_27

        # pd_op.divide: (256x258xf32) <- (256x258xf32, 256x1xf32)
        divide_0 = multiply_1 / sqrt_0

        # pd_op.transpose: (258x256xf32) <- (256x258xf32)
        transpose_0 = paddle.transpose(divide_0, perm=[1, 0])

        # pd_op.matmul: (200x256xf32) <- (200x258xf32, 258x256xf32)
        matmul_2 = paddle.matmul(concat_6, transpose_0, transpose_x=False, transpose_y=False)

        # pd_op.add: (200x256xf32) <- (200x256xf32, 256xf32)
        add_0 = matmul_2 + parameter_25

        # pd_op.sigmoid: (200x256xf32) <- (200x256xf32)
        sigmoid_0 = paddle.nn.functional.sigmoid(add_0)

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_2 = add_0 * sigmoid_0

        # pd_op.multiply: (256x258xf32) <- (256x258xf32, 256x258xf32)
        multiply_3 = parameter_24 * parameter_24

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_15 = [1]

        # pd_op.sum: (256x1xf32) <- (256x258xf32, 1xi64)
        sum_1 = paddle.sum(multiply_3, keepdim=True, axis=full_int_array_15)

        # pd_op.sqrt: (256x1xf32) <- (256x1xf32)
        sqrt_1 = paddle.sqrt(sum_1)

        # pd_op.multiply: (256x258xf32) <- (256x1xf32, 256x258xf32)
        multiply_4 = parameter_23 * parameter_24

        # pd_op.divide: (256x258xf32) <- (256x258xf32, 256x1xf32)
        divide_1 = multiply_4 / sqrt_1

        # pd_op.transpose: (258x256xf32) <- (256x258xf32)
        transpose_1 = paddle.transpose(divide_1, perm=[1, 0])

        # pd_op.matmul: (200x256xf32) <- (200x258xf32, 258x256xf32)
        matmul_3 = paddle.matmul(concat_6, transpose_1, transpose_x=False, transpose_y=False)

        # pd_op.add: (200x256xf32) <- (200x256xf32, 256xf32)
        add_1 = matmul_3 + parameter_22

        # pd_op.sigmoid: (200x256xf32) <- (200x256xf32)
        sigmoid_1 = paddle.nn.functional.sigmoid(add_1)

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_5 = add_1 * sigmoid_1

        # pd_op.multiply: (256x258xf32) <- (256x258xf32, 256x258xf32)
        multiply_6 = parameter_21 * parameter_21

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_16 = [1]

        # pd_op.sum: (256x1xf32) <- (256x258xf32, 1xi64)
        sum_2 = paddle.sum(multiply_6, keepdim=True, axis=full_int_array_16)

        # pd_op.sqrt: (256x1xf32) <- (256x1xf32)
        sqrt_2 = paddle.sqrt(sum_2)

        # pd_op.multiply: (256x258xf32) <- (256x1xf32, 256x258xf32)
        multiply_7 = parameter_20 * parameter_21

        # pd_op.divide: (256x258xf32) <- (256x258xf32, 256x1xf32)
        divide_2 = multiply_7 / sqrt_2

        # pd_op.transpose: (258x256xf32) <- (256x258xf32)
        transpose_2 = paddle.transpose(divide_2, perm=[1, 0])

        # pd_op.matmul: (200x256xf32) <- (200x258xf32, 258x256xf32)
        matmul_4 = paddle.matmul(concat_6, transpose_2, transpose_x=False, transpose_y=False)

        # pd_op.add: (200x256xf32) <- (200x256xf32, 256xf32)
        add_2 = matmul_4 + parameter_19

        # pd_op.sigmoid: (200x256xf32) <- (200x256xf32)
        sigmoid_2 = paddle.nn.functional.sigmoid(add_2)

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_8 = add_2 * sigmoid_2

        # pd_op.multiply: (256x256xf32) <- (256x256xf32, 256x256xf32)
        multiply_9 = parameter_18 * parameter_18

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_17 = [1]

        # pd_op.sum: (256x1xf32) <- (256x256xf32, 1xi64)
        sum_3 = paddle.sum(multiply_9, keepdim=True, axis=full_int_array_17)

        # pd_op.sqrt: (256x1xf32) <- (256x1xf32)
        sqrt_3 = paddle.sqrt(sum_3)

        # pd_op.multiply: (256x256xf32) <- (256x1xf32, 256x256xf32)
        multiply_10 = parameter_17 * parameter_18

        # pd_op.divide: (256x256xf32) <- (256x256xf32, 256x1xf32)
        divide_3 = multiply_10 / sqrt_3

        # pd_op.transpose: (256x256xf32) <- (256x256xf32)
        transpose_3 = paddle.transpose(divide_3, perm=[1, 0])

        # pd_op.matmul: (200x256xf32) <- (200x256xf32, 256x256xf32)
        matmul_5 = paddle.matmul(multiply_8, transpose_3, transpose_x=False, transpose_y=False)

        # pd_op.add: (200x256xf32) <- (200x256xf32, 256xf32)
        add_3 = matmul_5 + parameter_16

        # pd_op.sigmoid: (200x256xf32) <- (200x256xf32)
        sigmoid_3 = paddle.nn.functional.sigmoid(add_3)

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_11 = add_3 * sigmoid_3

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_12 = multiply_11 * multiply_2

        # pd_op.subtract: (200x256xf32) <- (200x256xf32, 200x256xf32)
        subtract_0 = multiply_2 - multiply_12

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_13 = multiply_11 * multiply_5

        # pd_op.add: (200x256xf32) <- (200x256xf32, 200x256xf32)
        add_4 = subtract_0 + multiply_13

        # pd_op.multiply: (256x256xf32) <- (256x256xf32, 256x256xf32)
        multiply_14 = parameter_15 * parameter_15

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_18 = [1]

        # pd_op.sum: (256x1xf32) <- (256x256xf32, 1xi64)
        sum_4 = paddle.sum(multiply_14, keepdim=True, axis=full_int_array_18)

        # pd_op.sqrt: (256x1xf32) <- (256x1xf32)
        sqrt_4 = paddle.sqrt(sum_4)

        # pd_op.multiply: (256x256xf32) <- (256x1xf32, 256x256xf32)
        multiply_15 = parameter_14 * parameter_15

        # pd_op.divide: (256x256xf32) <- (256x256xf32, 256x1xf32)
        divide_4 = multiply_15 / sqrt_4

        # pd_op.transpose: (256x256xf32) <- (256x256xf32)
        transpose_4 = paddle.transpose(divide_4, perm=[1, 0])

        # pd_op.matmul: (200x256xf32) <- (200x256xf32, 256x256xf32)
        matmul_6 = paddle.matmul(add_4, transpose_4, transpose_x=False, transpose_y=False)

        # pd_op.add: (200x256xf32) <- (200x256xf32, 256xf32)
        add_5 = matmul_6 + parameter_13

        # pd_op.sigmoid: (200x256xf32) <- (200x256xf32)
        sigmoid_4 = paddle.nn.functional.sigmoid(add_5)

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_16 = add_5 * sigmoid_4

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_17 = multiply_16 * multiply_2

        # pd_op.subtract: (200x256xf32) <- (200x256xf32, 200x256xf32)
        subtract_1 = multiply_2 - multiply_17

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_18 = multiply_16 * multiply_5

        # pd_op.add: (200x256xf32) <- (200x256xf32, 200x256xf32)
        add_6 = subtract_1 + multiply_18

        # pd_op.multiply: (256x256xf32) <- (256x256xf32, 256x256xf32)
        multiply_19 = parameter_12 * parameter_12

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_19 = [1]

        # pd_op.sum: (256x1xf32) <- (256x256xf32, 1xi64)
        sum_5 = paddle.sum(multiply_19, keepdim=True, axis=full_int_array_19)

        # pd_op.sqrt: (256x1xf32) <- (256x1xf32)
        sqrt_5 = paddle.sqrt(sum_5)

        # pd_op.multiply: (256x256xf32) <- (256x1xf32, 256x256xf32)
        multiply_20 = parameter_11 * parameter_12

        # pd_op.divide: (256x256xf32) <- (256x256xf32, 256x1xf32)
        divide_5 = multiply_20 / sqrt_5

        # pd_op.transpose: (256x256xf32) <- (256x256xf32)
        transpose_5 = paddle.transpose(divide_5, perm=[1, 0])

        # pd_op.matmul: (200x256xf32) <- (200x256xf32, 256x256xf32)
        matmul_7 = paddle.matmul(add_6, transpose_5, transpose_x=False, transpose_y=False)

        # pd_op.add: (200x256xf32) <- (200x256xf32, 256xf32)
        add_7 = matmul_7 + parameter_10

        # pd_op.sigmoid: (200x256xf32) <- (200x256xf32)
        sigmoid_5 = paddle.nn.functional.sigmoid(add_7)

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_21 = add_7 * sigmoid_5

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_22 = multiply_21 * multiply_2

        # pd_op.subtract: (200x256xf32) <- (200x256xf32, 200x256xf32)
        subtract_2 = multiply_2 - multiply_22

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_23 = multiply_21 * multiply_5

        # pd_op.add: (200x256xf32) <- (200x256xf32, 200x256xf32)
        add_8 = subtract_2 + multiply_23

        # pd_op.multiply: (256x256xf32) <- (256x256xf32, 256x256xf32)
        multiply_24 = parameter_9 * parameter_9

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_20 = [1]

        # pd_op.sum: (256x1xf32) <- (256x256xf32, 1xi64)
        sum_6 = paddle.sum(multiply_24, keepdim=True, axis=full_int_array_20)

        # pd_op.sqrt: (256x1xf32) <- (256x1xf32)
        sqrt_6 = paddle.sqrt(sum_6)

        # pd_op.multiply: (256x256xf32) <- (256x1xf32, 256x256xf32)
        multiply_25 = parameter_8 * parameter_9

        # pd_op.divide: (256x256xf32) <- (256x256xf32, 256x1xf32)
        divide_6 = multiply_25 / sqrt_6

        # pd_op.transpose: (256x256xf32) <- (256x256xf32)
        transpose_6 = paddle.transpose(divide_6, perm=[1, 0])

        # pd_op.matmul: (200x256xf32) <- (200x256xf32, 256x256xf32)
        matmul_8 = paddle.matmul(add_8, transpose_6, transpose_x=False, transpose_y=False)

        # pd_op.add: (200x256xf32) <- (200x256xf32, 256xf32)
        add_9 = matmul_8 + parameter_7

        # pd_op.sigmoid: (200x256xf32) <- (200x256xf32)
        sigmoid_6 = paddle.nn.functional.sigmoid(add_9)

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_26 = add_9 * sigmoid_6

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_27 = multiply_26 * multiply_2

        # pd_op.subtract: (200x256xf32) <- (200x256xf32, 200x256xf32)
        subtract_3 = multiply_2 - multiply_27

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_28 = multiply_26 * multiply_5

        # pd_op.add: (200x256xf32) <- (200x256xf32, 200x256xf32)
        add_10 = subtract_3 + multiply_28

        # pd_op.multiply: (256x256xf32) <- (256x256xf32, 256x256xf32)
        multiply_29 = parameter_6 * parameter_6

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_21 = [1]

        # pd_op.sum: (256x1xf32) <- (256x256xf32, 1xi64)
        sum_7 = paddle.sum(multiply_29, keepdim=True, axis=full_int_array_21)

        # pd_op.sqrt: (256x1xf32) <- (256x1xf32)
        sqrt_7 = paddle.sqrt(sum_7)

        # pd_op.multiply: (256x256xf32) <- (256x1xf32, 256x256xf32)
        multiply_30 = parameter_5 * parameter_6

        # pd_op.divide: (256x256xf32) <- (256x256xf32, 256x1xf32)
        divide_7 = multiply_30 / sqrt_7

        # pd_op.transpose: (256x256xf32) <- (256x256xf32)
        transpose_7 = paddle.transpose(divide_7, perm=[1, 0])

        # pd_op.matmul: (200x256xf32) <- (200x256xf32, 256x256xf32)
        matmul_9 = paddle.matmul(add_10, transpose_7, transpose_x=False, transpose_y=False)

        # pd_op.add: (200x256xf32) <- (200x256xf32, 256xf32)
        add_11 = matmul_9 + parameter_4

        # pd_op.sigmoid: (200x256xf32) <- (200x256xf32)
        sigmoid_7 = paddle.nn.functional.sigmoid(add_11)

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_31 = add_11 * sigmoid_7

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_32 = multiply_31 * multiply_2

        # pd_op.subtract: (200x256xf32) <- (200x256xf32, 200x256xf32)
        subtract_4 = multiply_2 - multiply_32

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_33 = multiply_31 * multiply_5

        # pd_op.add: (200x256xf32) <- (200x256xf32, 200x256xf32)
        add_12 = subtract_4 + multiply_33

        # pd_op.matmul: (200x1xf32) <- (200x256xf32, 256x1xf32)
        matmul_10 = paddle.matmul(add_12, parameter_3, transpose_x=False, transpose_y=False)

        # pd_op.add: (200x1xf32) <- (200x1xf32, 1xf32)
        add_13 = matmul_10 + parameter_2

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_22 = [1]

        # pd_op.full: (1xi32) <- ()
        full_20 = paddle.full(shape=[1], dtype='int32', fill_value=1)

        # pd_op.split: ([200x1xf32]) <- (200x1xf32, 1xi64, 1xi32)
        split_0 = paddle.split(add_13, full_int_array_22, full_20)

        # builtin.split: (200x1xf32) <- ([200x1xf32])
        split_1, = split_0

        # pd_op.full: (1xf32) <- ()
        full_21 = paddle.full(shape=[1], dtype='float32', fill_value=1)

        # pd_op.scale: (200x1xf32) <- (200x1xf32, 1xf32)
        scale_4 = paddle.scale(split_1, full_21, bias_after_scale=True, bias=70)
        return concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4






def call_once(f):
    once_flag = False
    def ret_func(*args, **kwargs):
        nonlocal once_flag
        if once_flag:
            return
        f(*args, **kwargs)
        once_flag = True
    return ret_func

@call_once
def InferBlockInputShapes():
    extractor = BlockShapesExtractor()
    extractor.builtin_module_0_0_0(
        parameter_0=paddle.uniform([2, 128], dtype='float32', min=-0.5, max=0.5),
        parameter_1=paddle.randint(low=0, high=1, shape=[2], dtype='int64'),
        parameter_2=paddle.uniform([1], dtype='float32', min=-0.5, max=0.5),
        parameter_3=paddle.uniform([256, 1], dtype='float32', min=-0.5, max=0.5),
        parameter_4=paddle.uniform([256], dtype='float32', min=-0.5, max=0.5),
        parameter_5=paddle.uniform([256, 1], dtype='float32', min=-0.5, max=0.5),
        parameter_6=paddle.uniform([256, 256], dtype='float32', min=-0.5, max=0.5),
        parameter_7=paddle.uniform([256], dtype='float32', min=-0.5, max=0.5),
        parameter_8=paddle.uniform([256, 1], dtype='float32', min=-0.5, max=0.5),
        parameter_9=paddle.uniform([256, 256], dtype='float32', min=-0.5, max=0.5),
        parameter_10=paddle.uniform([256], dtype='float32', min=-0.5, max=0.5),
        parameter_11=paddle.uniform([256, 1], dtype='float32', min=-0.5, max=0.5),
        parameter_12=paddle.uniform([256, 256], dtype='float32', min=-0.5, max=0.5),
        parameter_13=paddle.uniform([256], dtype='float32', min=-0.5, max=0.5),
        parameter_14=paddle.uniform([256, 1], dtype='float32', min=-0.5, max=0.5),
        parameter_15=paddle.uniform([256, 256], dtype='float32', min=-0.5, max=0.5),
        parameter_16=paddle.uniform([256], dtype='float32', min=-0.5, max=0.5),
        parameter_17=paddle.uniform([256, 1], dtype='float32', min=-0.5, max=0.5),
        parameter_18=paddle.uniform([256, 256], dtype='float32', min=-0.5, max=0.5),
        parameter_19=paddle.uniform([256], dtype='float32', min=-0.5, max=0.5),
        parameter_20=paddle.uniform([256, 1], dtype='float32', min=-0.5, max=0.5),
        parameter_21=paddle.uniform([256, 258], dtype='float32', min=-0.5, max=0.5),
        parameter_22=paddle.uniform([256], dtype='float32', min=-0.5, max=0.5),
        parameter_23=paddle.uniform([256, 1], dtype='float32', min=-0.5, max=0.5),
        parameter_24=paddle.uniform([256, 258], dtype='float32', min=-0.5, max=0.5),
        parameter_25=paddle.uniform([256], dtype='float32', min=-0.5, max=0.5),
        parameter_26=paddle.uniform([256, 1], dtype='float32', min=-0.5, max=0.5),
        parameter_27=paddle.uniform([256, 258], dtype='float32', min=-0.5, max=0.5),
        data_0=paddle.uniform([200, 1], dtype='float32', min=-0.5, max=0.5),
        data_1=paddle.uniform([200, 1], dtype='float32', min=-0.5, max=0.5),
        data_2=paddle.uniform([200, 1], dtype='float32', min=-0.5, max=0.5),
        data_3=paddle.uniform([200, 1], dtype='float32', min=-0.5, max=0.5),
        data_4=paddle.uniform([200, 1], dtype='float32', min=-0.5, max=0.5),
    )


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


class TestBase:
    def setUp(self):
        paddle.seed(2024)
        InferBlockInputShapes()
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

if ShouldTestBlock(0):

    class Block_builtin_module_0_0_0(paddle.nn.Layer):
        def __init__(self):
            super().__init__()

        def forward(self, parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, data_0, data_1, data_2, data_3, data_4):
            return BlockEntries().builtin_module_0_0_0(parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, data_0, data_1, data_2, data_3, data_4)

    class Test_builtin_module_0_0_0(TestBase, unittest.TestCase):
        def prepare_data(self):
            self.inputs = [
                # parameter_0
                paddle.uniform([2, 128], dtype='float32', min=-0.5, max=0.5),
                # parameter_1
                paddle.randint(low=0, high=1, shape=[2], dtype='int64'),
                # parameter_2
                paddle.uniform([1], dtype='float32', min=-0.5, max=0.5),
                # parameter_3
                paddle.uniform([256, 1], dtype='float32', min=-0.5, max=0.5),
                # parameter_4
                paddle.uniform([256], dtype='float32', min=-0.5, max=0.5),
                # parameter_5
                paddle.uniform([256, 1], dtype='float32', min=-0.5, max=0.5),
                # parameter_6
                paddle.uniform([256, 256], dtype='float32', min=-0.5, max=0.5),
                # parameter_7
                paddle.uniform([256], dtype='float32', min=-0.5, max=0.5),
                # parameter_8
                paddle.uniform([256, 1], dtype='float32', min=-0.5, max=0.5),
                # parameter_9
                paddle.uniform([256, 256], dtype='float32', min=-0.5, max=0.5),
                # parameter_10
                paddle.uniform([256], dtype='float32', min=-0.5, max=0.5),
                # parameter_11
                paddle.uniform([256, 1], dtype='float32', min=-0.5, max=0.5),
                # parameter_12
                paddle.uniform([256, 256], dtype='float32', min=-0.5, max=0.5),
                # parameter_13
                paddle.uniform([256], dtype='float32', min=-0.5, max=0.5),
                # parameter_14
                paddle.uniform([256, 1], dtype='float32', min=-0.5, max=0.5),
                # parameter_15
                paddle.uniform([256, 256], dtype='float32', min=-0.5, max=0.5),
                # parameter_16
                paddle.uniform([256], dtype='float32', min=-0.5, max=0.5),
                # parameter_17
                paddle.uniform([256, 1], dtype='float32', min=-0.5, max=0.5),
                # parameter_18
                paddle.uniform([256, 256], dtype='float32', min=-0.5, max=0.5),
                # parameter_19
                paddle.uniform([256], dtype='float32', min=-0.5, max=0.5),
                # parameter_20
                paddle.uniform([256, 1], dtype='float32', min=-0.5, max=0.5),
                # parameter_21
                paddle.uniform([256, 258], dtype='float32', min=-0.5, max=0.5),
                # parameter_22
                paddle.uniform([256], dtype='float32', min=-0.5, max=0.5),
                # parameter_23
                paddle.uniform([256, 1], dtype='float32', min=-0.5, max=0.5),
                # parameter_24
                paddle.uniform([256, 258], dtype='float32', min=-0.5, max=0.5),
                # parameter_25
                paddle.uniform([256], dtype='float32', min=-0.5, max=0.5),
                # parameter_26
                paddle.uniform([256, 1], dtype='float32', min=-0.5, max=0.5),
                # parameter_27
                paddle.uniform([256, 258], dtype='float32', min=-0.5, max=0.5),
                # data_0
                paddle.uniform([200, 1], dtype='float32', min=-0.5, max=0.5),
                # data_1
                paddle.uniform([200, 1], dtype='float32', min=-0.5, max=0.5),
                # data_2
                paddle.uniform([200, 1], dtype='float32', min=-0.5, max=0.5),
                # data_3
                paddle.uniform([200, 1], dtype='float32', min=-0.5, max=0.5),
                # data_4
                paddle.uniform([200, 1], dtype='float32', min=-0.5, max=0.5),
            ]
            for input in self.inputs:
                input.stop_gradient = True

        def apply_to_static(self, net, use_cinn):
            build_strategy = paddle.static.BuildStrategy()
            input_spec = [
                # parameter_0
                paddle.static.InputSpec(shape=[2, 128], dtype='float32'),
                # parameter_1
                paddle.static.InputSpec(shape=[2], dtype='int64'),
                # parameter_2
                paddle.static.InputSpec(shape=[1], dtype='float32'),
                # parameter_3
                paddle.static.InputSpec(shape=[256, 1], dtype='float32'),
                # parameter_4
                paddle.static.InputSpec(shape=[256], dtype='float32'),
                # parameter_5
                paddle.static.InputSpec(shape=[256, 1], dtype='float32'),
                # parameter_6
                paddle.static.InputSpec(shape=[256, 256], dtype='float32'),
                # parameter_7
                paddle.static.InputSpec(shape=[256], dtype='float32'),
                # parameter_8
                paddle.static.InputSpec(shape=[256, 1], dtype='float32'),
                # parameter_9
                paddle.static.InputSpec(shape=[256, 256], dtype='float32'),
                # parameter_10
                paddle.static.InputSpec(shape=[256], dtype='float32'),
                # parameter_11
                paddle.static.InputSpec(shape=[256, 1], dtype='float32'),
                # parameter_12
                paddle.static.InputSpec(shape=[256, 256], dtype='float32'),
                # parameter_13
                paddle.static.InputSpec(shape=[256], dtype='float32'),
                # parameter_14
                paddle.static.InputSpec(shape=[256, 1], dtype='float32'),
                # parameter_15
                paddle.static.InputSpec(shape=[256, 256], dtype='float32'),
                # parameter_16
                paddle.static.InputSpec(shape=[256], dtype='float32'),
                # parameter_17
                paddle.static.InputSpec(shape=[256, 1], dtype='float32'),
                # parameter_18
                paddle.static.InputSpec(shape=[256, 256], dtype='float32'),
                # parameter_19
                paddle.static.InputSpec(shape=[256], dtype='float32'),
                # parameter_20
                paddle.static.InputSpec(shape=[256, 1], dtype='float32'),
                # parameter_21
                paddle.static.InputSpec(shape=[256, 258], dtype='float32'),
                # parameter_22
                paddle.static.InputSpec(shape=[256], dtype='float32'),
                # parameter_23
                paddle.static.InputSpec(shape=[256, 1], dtype='float32'),
                # parameter_24
                paddle.static.InputSpec(shape=[256, 258], dtype='float32'),
                # parameter_25
                paddle.static.InputSpec(shape=[256], dtype='float32'),
                # parameter_26
                paddle.static.InputSpec(shape=[256, 1], dtype='float32'),
                # parameter_27
                paddle.static.InputSpec(shape=[256, 258], dtype='float32'),
                # data_0
                paddle.static.InputSpec(shape=[200, 1], dtype='float32'),
                # data_1
                paddle.static.InputSpec(shape=[200, 1], dtype='float32'),
                # data_2
                paddle.static.InputSpec(shape=[200, 1], dtype='float32'),
                # data_3
                paddle.static.InputSpec(shape=[200, 1], dtype='float32'),
                # data_4
                paddle.static.InputSpec(shape=[200, 1], dtype='float32'),
            ]
            build_strategy.build_cinn_pass = use_cinn
            return paddle.jit.to_static(
                net,
                input_spec=input_spec,
                build_strategy=build_strategy,
                full_graph=True,
            )

        def train(self, use_cinn):
            net = Block_builtin_module_0_0_0()
            net.eval()
            if GetEnvVarEnableJit():
                net = self.apply_to_static(net, use_cinn)
            out = net(*self.inputs)
            return out

if __name__ == '__main__':
    unittest.main()