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
    return [273][block_idx] - 1 # number-of-ops-in-block

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

        # builtin.parameter: (2x128xf32) <- ()
        None

        if FastReturn(block_idx=0, op_idx=0):
            return parameter_0

        # builtin.parameter: (2xi64) <- ()
        None

        if FastReturn(block_idx=0, op_idx=1):
            return parameter_0, parameter_1

        # builtin.parameter: (1xf32) <- ()
        None

        if FastReturn(block_idx=0, op_idx=2):
            return parameter_0, parameter_1, parameter_2

        # builtin.parameter: (256x1xf32) <- ()
        None

        if FastReturn(block_idx=0, op_idx=3):
            return parameter_0, parameter_1, parameter_2, parameter_3

        # builtin.parameter: (256xf32) <- ()
        None

        if FastReturn(block_idx=0, op_idx=4):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4

        # builtin.parameter: (256x1xf32) <- ()
        None

        if FastReturn(block_idx=0, op_idx=5):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5

        # builtin.parameter: (256x256xf32) <- ()
        None

        if FastReturn(block_idx=0, op_idx=6):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6

        # builtin.parameter: (256xf32) <- ()
        None

        if FastReturn(block_idx=0, op_idx=7):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7

        # builtin.parameter: (256x1xf32) <- ()
        None

        if FastReturn(block_idx=0, op_idx=8):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8

        # builtin.parameter: (256x256xf32) <- ()
        None

        if FastReturn(block_idx=0, op_idx=9):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9

        # builtin.parameter: (256xf32) <- ()
        None

        if FastReturn(block_idx=0, op_idx=10):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10

        # builtin.parameter: (256x1xf32) <- ()
        None

        if FastReturn(block_idx=0, op_idx=11):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11

        # builtin.parameter: (256x256xf32) <- ()
        None

        if FastReturn(block_idx=0, op_idx=12):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12

        # builtin.parameter: (256xf32) <- ()
        None

        if FastReturn(block_idx=0, op_idx=13):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13

        # builtin.parameter: (256x1xf32) <- ()
        None

        if FastReturn(block_idx=0, op_idx=14):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14

        # builtin.parameter: (256x256xf32) <- ()
        None

        if FastReturn(block_idx=0, op_idx=15):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15

        # builtin.parameter: (256xf32) <- ()
        None

        if FastReturn(block_idx=0, op_idx=16):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16

        # builtin.parameter: (256x1xf32) <- ()
        None

        if FastReturn(block_idx=0, op_idx=17):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17

        # builtin.parameter: (256x256xf32) <- ()
        None

        if FastReturn(block_idx=0, op_idx=18):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18

        # builtin.parameter: (256xf32) <- ()
        None

        if FastReturn(block_idx=0, op_idx=19):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19

        # builtin.parameter: (256x1xf32) <- ()
        None

        if FastReturn(block_idx=0, op_idx=20):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20

        # builtin.parameter: (256x258xf32) <- ()
        None

        if FastReturn(block_idx=0, op_idx=21):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21

        # builtin.parameter: (256xf32) <- ()
        None

        if FastReturn(block_idx=0, op_idx=22):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22

        # builtin.parameter: (256x1xf32) <- ()
        None

        if FastReturn(block_idx=0, op_idx=23):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23

        # builtin.parameter: (256x258xf32) <- ()
        None

        if FastReturn(block_idx=0, op_idx=24):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24

        # builtin.parameter: (256xf32) <- ()
        None

        if FastReturn(block_idx=0, op_idx=25):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25

        # builtin.parameter: (256x1xf32) <- ()
        None

        if FastReturn(block_idx=0, op_idx=26):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26

        # builtin.parameter: (256x258xf32) <- ()
        None

        if FastReturn(block_idx=0, op_idx=27):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27

        # pd_op.data: (200x1xf32) <- ()
        None

        if FastReturn(block_idx=0, op_idx=28):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, data_0

        # pd_op.data: (200x1xf32) <- ()
        None

        if FastReturn(block_idx=0, op_idx=29):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, data_0, data_1

        # pd_op.data: (200x1xf32) <- ()
        None

        if FastReturn(block_idx=0, op_idx=30):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, data_0, data_1

        # pd_op.data: (200x1xf32) <- ()
        None

        if FastReturn(block_idx=0, op_idx=31):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, data_0, data_1

        # pd_op.data: (200x1xf32) <- ()
        None

        if FastReturn(block_idx=0, op_idx=32):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, data_0, data_1

        # pd_op.full: (1xi32) <- ()
        full_0 = paddle.full(shape=[1], dtype='int32', fill_value=-1)

        if FastReturn(block_idx=0, op_idx=33):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, data_0, data_1, full_0

        # builtin.combine: ([200x1xf32, 200x1xf32]) <- (200x1xf32, 200x1xf32)
        combine_0 = [data_0, data_1]

        if FastReturn(block_idx=0, op_idx=34):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, full_0, combine_0

        # pd_op.concat: (200x2xf32) <- ([200x1xf32, 200x1xf32], 1xi32)
        concat_0 = paddle.concat(combine_0, full_0)

        if FastReturn(block_idx=0, op_idx=35):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0

        # pd_op.full: (2x2xf32) <- ()
        full_1 = paddle.full(shape=[2, 2], dtype='float32', fill_value=0)

        if FastReturn(block_idx=0, op_idx=36):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, full_1

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_0 = [0]

        if FastReturn(block_idx=0, op_idx=37):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, full_1, full_int_array_0

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_1 = [1]

        if FastReturn(block_idx=0, op_idx=38):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, full_1, full_int_array_0, full_int_array_1

        # pd_op.slice: (xi64) <- (2xi64, 1xi64, 1xi64)
        slice_0 = paddle.slice(parameter_1, axes=[0], starts=full_int_array_0, ends=full_int_array_1)

        if FastReturn(block_idx=0, op_idx=39):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, full_1, slice_0

        # pd_op.full: (1xf32) <- ()
        full_2 = paddle.full(shape=[1], dtype='float32', fill_value=1)

        if FastReturn(block_idx=0, op_idx=40):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, full_1, slice_0, full_2

        # pd_op.scale: (xi64) <- (xi64, 1xf32)
        scale_0 = paddle.scale(slice_0, full_2, bias_after_scale=True, bias=1)

        if FastReturn(block_idx=0, op_idx=41):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, full_1, slice_0, scale_0

        # pd_op.full: (1xi32) <- ()
        full_3 = paddle.full(shape=[1], dtype='int32', fill_value=0)

        if FastReturn(block_idx=0, op_idx=42):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, full_1, slice_0, scale_0

        # pd_op.full: (1xi32) <- ()
        full_4 = paddle.full(shape=[1], dtype='int32', fill_value=1)

        if FastReturn(block_idx=0, op_idx=43):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, full_1, slice_0, scale_0

        # pd_op.full: (xi64) <- ()
        full_5 = paddle.full(shape=[], dtype='int64', fill_value=0)

        if FastReturn(block_idx=0, op_idx=44):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, full_1, slice_0, scale_0, full_5

        # pd_op.full: (xi64) <- ()
        full_6 = paddle.full(shape=[], dtype='int64', fill_value=1)

        if FastReturn(block_idx=0, op_idx=45):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, full_1, slice_0, scale_0, full_5, full_6

        # builtin.combine: ([xi64, xi64]) <- (xi64, xi64)
        combine_1 = [slice_0, full_5]

        if FastReturn(block_idx=0, op_idx=46):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, full_1, slice_0, scale_0, full_5, full_6

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_2 = [1]

        if FastReturn(block_idx=0, op_idx=47):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, full_1, slice_0, scale_0, full_5, full_6, full_int_array_2

        # pd_op.reshape: (1xi64, 0xi64) <- (xi64, 1xi64)
        reshape_0, reshape_1 = paddle.reshape(slice_0, full_int_array_2), None

        if FastReturn(block_idx=0, op_idx=48):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, full_1, scale_0, full_5, full_6, reshape_0

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_3 = [1]

        if FastReturn(block_idx=0, op_idx=49):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, full_1, scale_0, full_5, full_6, reshape_0, full_int_array_3

        # pd_op.reshape: (1xi64, 0xi64) <- (xi64, 1xi64)
        reshape_2, reshape_3 = paddle.reshape(full_5, full_int_array_3), None

        if FastReturn(block_idx=0, op_idx=50):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, full_1, scale_0, full_6, reshape_0, reshape_2

        # builtin.combine: ([1xi64, 1xi64]) <- (1xi64, 1xi64)
        combine_2 = [reshape_0, reshape_2]

        if FastReturn(block_idx=0, op_idx=51):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, full_1, scale_0, full_6, combine_2

        # pd_op.full: (1xi32) <- ()
        full_7 = paddle.full(shape=[1], dtype='int32', fill_value=0)

        if FastReturn(block_idx=0, op_idx=52):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, full_1, scale_0, full_6, combine_2, full_7

        # pd_op.concat: (2xi64) <- ([1xi64, 1xi64], 1xi32)
        concat_1 = paddle.concat(combine_2, full_7)

        if FastReturn(block_idx=0, op_idx=53):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, full_1, scale_0, full_6, concat_1

        # builtin.combine: ([xi64, xi64]) <- (xi64, xi64)
        combine_3 = [scale_0, full_6]

        if FastReturn(block_idx=0, op_idx=54):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, full_1, scale_0, full_6, concat_1

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_4 = [1]

        if FastReturn(block_idx=0, op_idx=55):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, full_1, scale_0, full_6, concat_1, full_int_array_4

        # pd_op.reshape: (1xi64, 0xi64) <- (xi64, 1xi64)
        reshape_4, reshape_5 = paddle.reshape(scale_0, full_int_array_4), None

        if FastReturn(block_idx=0, op_idx=56):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, full_1, full_6, concat_1, reshape_4

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_5 = [1]

        if FastReturn(block_idx=0, op_idx=57):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, full_1, full_6, concat_1, reshape_4, full_int_array_5

        # pd_op.reshape: (1xi64, 0xi64) <- (xi64, 1xi64)
        reshape_6, reshape_7 = paddle.reshape(full_6, full_int_array_5), None

        if FastReturn(block_idx=0, op_idx=58):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, full_1, concat_1, reshape_4, reshape_6

        # builtin.combine: ([1xi64, 1xi64]) <- (1xi64, 1xi64)
        combine_4 = [reshape_4, reshape_6]

        if FastReturn(block_idx=0, op_idx=59):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, full_1, concat_1, combine_4

        # pd_op.full: (1xi32) <- ()
        full_8 = paddle.full(shape=[1], dtype='int32', fill_value=0)

        if FastReturn(block_idx=0, op_idx=60):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, full_1, concat_1, combine_4, full_8

        # pd_op.concat: (2xi64) <- ([1xi64, 1xi64], 1xi32)
        concat_2 = paddle.concat(combine_4, full_8)

        if FastReturn(block_idx=0, op_idx=61):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, full_1, concat_1, concat_2

        # pd_op.full_int_array: (2xi64) <- ()
        full_int_array_6 = [1, 1]

        if FastReturn(block_idx=0, op_idx=62):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, full_1, concat_1, concat_2, full_int_array_6

        # pd_op.set_value_: (2x2xf32) <- (2x2xf32, 2xi64, 2xi64, 2xi64)
        set_value__0 = paddle._C_ops.set_value_(full_1, concat_1, concat_2, full_int_array_6, [0, 1], [0, 1], [], [1], [1])

        if FastReturn(block_idx=0, op_idx=63):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, set_value__0

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_7 = [1]

        if FastReturn(block_idx=0, op_idx=64):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, set_value__0, full_int_array_7

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_8 = [2]

        if FastReturn(block_idx=0, op_idx=65):
            return parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, set_value__0, full_int_array_7, full_int_array_8

        # pd_op.slice: (xi64) <- (2xi64, 1xi64, 1xi64)
        slice_1 = paddle.slice(parameter_1, axes=[0], starts=full_int_array_7, ends=full_int_array_8)

        if FastReturn(block_idx=0, op_idx=66):
            return parameter_0, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, set_value__0, slice_1

        # pd_op.full: (1xf32) <- ()
        full_9 = paddle.full(shape=[1], dtype='float32', fill_value=1)

        if FastReturn(block_idx=0, op_idx=67):
            return parameter_0, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, set_value__0, slice_1, full_9

        # pd_op.scale: (xi64) <- (xi64, 1xf32)
        scale_1 = paddle.scale(slice_1, full_9, bias_after_scale=True, bias=1)

        if FastReturn(block_idx=0, op_idx=68):
            return parameter_0, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, set_value__0, slice_1, scale_1

        # pd_op.full: (1xi32) <- ()
        full_10 = paddle.full(shape=[1], dtype='int32', fill_value=1)

        if FastReturn(block_idx=0, op_idx=69):
            return parameter_0, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, set_value__0, slice_1, scale_1

        # pd_op.full: (1xi32) <- ()
        full_11 = paddle.full(shape=[1], dtype='int32', fill_value=2)

        if FastReturn(block_idx=0, op_idx=70):
            return parameter_0, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, set_value__0, slice_1, scale_1

        # pd_op.full: (xi64) <- ()
        full_12 = paddle.full(shape=[], dtype='int64', fill_value=1)

        if FastReturn(block_idx=0, op_idx=71):
            return parameter_0, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, set_value__0, slice_1, scale_1, full_12

        # pd_op.full: (xi64) <- ()
        full_13 = paddle.full(shape=[], dtype='int64', fill_value=2)

        if FastReturn(block_idx=0, op_idx=72):
            return parameter_0, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, set_value__0, slice_1, scale_1, full_12, full_13

        # builtin.combine: ([xi64, xi64]) <- (xi64, xi64)
        combine_5 = [slice_1, full_12]

        if FastReturn(block_idx=0, op_idx=73):
            return parameter_0, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, set_value__0, slice_1, scale_1, full_12, full_13

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_9 = [1]

        if FastReturn(block_idx=0, op_idx=74):
            return parameter_0, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, set_value__0, slice_1, scale_1, full_12, full_13, full_int_array_9

        # pd_op.reshape: (1xi64, 0xi64) <- (xi64, 1xi64)
        reshape_8, reshape_9 = paddle.reshape(slice_1, full_int_array_9), None

        if FastReturn(block_idx=0, op_idx=75):
            return parameter_0, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, set_value__0, scale_1, full_12, full_13, reshape_8

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_10 = [1]

        if FastReturn(block_idx=0, op_idx=76):
            return parameter_0, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, set_value__0, scale_1, full_12, full_13, reshape_8, full_int_array_10

        # pd_op.reshape: (1xi64, 0xi64) <- (xi64, 1xi64)
        reshape_10, reshape_11 = paddle.reshape(full_12, full_int_array_10), None

        if FastReturn(block_idx=0, op_idx=77):
            return parameter_0, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, set_value__0, scale_1, full_13, reshape_8, reshape_10

        # builtin.combine: ([1xi64, 1xi64]) <- (1xi64, 1xi64)
        combine_6 = [reshape_8, reshape_10]

        if FastReturn(block_idx=0, op_idx=78):
            return parameter_0, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, set_value__0, scale_1, full_13, combine_6

        # pd_op.full: (1xi32) <- ()
        full_14 = paddle.full(shape=[1], dtype='int32', fill_value=0)

        if FastReturn(block_idx=0, op_idx=79):
            return parameter_0, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, set_value__0, scale_1, full_13, combine_6, full_14

        # pd_op.concat: (2xi64) <- ([1xi64, 1xi64], 1xi32)
        concat_3 = paddle.concat(combine_6, full_14)

        if FastReturn(block_idx=0, op_idx=80):
            return parameter_0, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, set_value__0, scale_1, full_13, concat_3

        # builtin.combine: ([xi64, xi64]) <- (xi64, xi64)
        combine_7 = [scale_1, full_13]

        if FastReturn(block_idx=0, op_idx=81):
            return parameter_0, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, set_value__0, scale_1, full_13, concat_3

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_11 = [1]

        if FastReturn(block_idx=0, op_idx=82):
            return parameter_0, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, set_value__0, scale_1, full_13, concat_3, full_int_array_11

        # pd_op.reshape: (1xi64, 0xi64) <- (xi64, 1xi64)
        reshape_12, reshape_13 = paddle.reshape(scale_1, full_int_array_11), None

        if FastReturn(block_idx=0, op_idx=83):
            return parameter_0, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, set_value__0, full_13, concat_3, reshape_12

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_12 = [1]

        if FastReturn(block_idx=0, op_idx=84):
            return parameter_0, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, set_value__0, full_13, concat_3, reshape_12, full_int_array_12

        # pd_op.reshape: (1xi64, 0xi64) <- (xi64, 1xi64)
        reshape_14, reshape_15 = paddle.reshape(full_13, full_int_array_12), None

        if FastReturn(block_idx=0, op_idx=85):
            return parameter_0, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, set_value__0, concat_3, reshape_12, reshape_14

        # builtin.combine: ([1xi64, 1xi64]) <- (1xi64, 1xi64)
        combine_8 = [reshape_12, reshape_14]

        if FastReturn(block_idx=0, op_idx=86):
            return parameter_0, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, set_value__0, concat_3, combine_8

        # pd_op.full: (1xi32) <- ()
        full_15 = paddle.full(shape=[1], dtype='int32', fill_value=0)

        if FastReturn(block_idx=0, op_idx=87):
            return parameter_0, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, set_value__0, concat_3, combine_8, full_15

        # pd_op.concat: (2xi64) <- ([1xi64, 1xi64], 1xi32)
        concat_4 = paddle.concat(combine_8, full_15)

        if FastReturn(block_idx=0, op_idx=88):
            return parameter_0, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, set_value__0, concat_3, concat_4

        # pd_op.full_int_array: (2xi64) <- ()
        full_int_array_13 = [1, 1]

        if FastReturn(block_idx=0, op_idx=89):
            return parameter_0, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, set_value__0, concat_3, concat_4, full_int_array_13

        # pd_op.set_value_: (2x2xf32) <- (2x2xf32, 2xi64, 2xi64, 2xi64)
        set_value__1 = paddle._C_ops.set_value_(set_value__0, concat_3, concat_4, full_int_array_13, [0, 1], [0, 1], [], [1], [1])

        if FastReturn(block_idx=0, op_idx=90):
            return parameter_0, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, set_value__1

        # pd_op.matmul: (200x2xf32) <- (200x2xf32, 2x2xf32)
        matmul_0 = paddle.matmul(concat_0, set_value__1, transpose_x=False, transpose_y=False)

        if FastReturn(block_idx=0, op_idx=91):
            return parameter_0, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, set_value__1, matmul_0

        # pd_op.matmul: (200x128xf32) <- (200x2xf32, 2x128xf32)
        matmul_1 = paddle.matmul(matmul_0, parameter_0, transpose_x=False, transpose_y=False)

        if FastReturn(block_idx=0, op_idx=92):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, set_value__1, matmul_0, matmul_1

        # pd_op.full: (1xf32) <- ()
        full_16 = paddle.full(shape=[1], dtype='float32', fill_value=6.28319)

        if FastReturn(block_idx=0, op_idx=93):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, set_value__1, matmul_0, matmul_1, full_16

        # pd_op.scale: (200x128xf32) <- (200x128xf32, 1xf32)
        scale_2 = paddle.scale(matmul_1, full_16, bias_after_scale=True, bias=0)

        if FastReturn(block_idx=0, op_idx=94):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, set_value__1, matmul_0, matmul_1, scale_2

        # pd_op.sin: (200x128xf32) <- (200x128xf32)
        sin_0 = paddle.sin(scale_2)

        if FastReturn(block_idx=0, op_idx=95):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, set_value__1, matmul_0, matmul_1, scale_2, sin_0

        # pd_op.full: (1xf32) <- ()
        full_17 = paddle.full(shape=[1], dtype='float32', fill_value=6.28319)

        if FastReturn(block_idx=0, op_idx=96):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, set_value__1, matmul_0, matmul_1, scale_2, sin_0, full_17

        # pd_op.scale: (200x128xf32) <- (200x128xf32, 1xf32)
        scale_3 = paddle.scale(matmul_1, full_17, bias_after_scale=True, bias=0)

        if FastReturn(block_idx=0, op_idx=97):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, set_value__1, matmul_0, scale_2, sin_0, scale_3

        # pd_op.cos: (200x128xf32) <- (200x128xf32)
        cos_0 = paddle.cos(scale_3)

        if FastReturn(block_idx=0, op_idx=98):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, set_value__1, matmul_0, scale_2, sin_0, scale_3, cos_0

        # pd_op.full: (1xi32) <- ()
        full_18 = paddle.full(shape=[1], dtype='int32', fill_value=-1)

        if FastReturn(block_idx=0, op_idx=99):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, set_value__1, matmul_0, scale_2, sin_0, scale_3, cos_0, full_18

        # builtin.combine: ([200x128xf32, 200x128xf32]) <- (200x128xf32, 200x128xf32)
        combine_9 = [sin_0, cos_0]

        if FastReturn(block_idx=0, op_idx=100):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, set_value__1, matmul_0, scale_2, scale_3, full_18, combine_9

        # pd_op.concat: (200x256xf32) <- ([200x128xf32, 200x128xf32], 1xi32)
        concat_5 = paddle.concat(combine_9, full_18)

        if FastReturn(block_idx=0, op_idx=101):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_5

        # pd_op.full: (1xi32) <- ()
        full_19 = paddle.full(shape=[1], dtype='int32', fill_value=-1)

        if FastReturn(block_idx=0, op_idx=102):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_5, full_19

        # builtin.combine: ([200x2xf32, 200x256xf32]) <- (200x2xf32, 200x256xf32)
        combine_10 = [concat_0, concat_5]

        if FastReturn(block_idx=0, op_idx=103):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, set_value__1, matmul_0, scale_2, scale_3, full_19, combine_10

        # pd_op.concat: (200x258xf32) <- ([200x2xf32, 200x256xf32], 1xi32)
        concat_6 = paddle.concat(combine_10, full_19)

        if FastReturn(block_idx=0, op_idx=104):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6

        # pd_op.multiply: (256x258xf32) <- (256x258xf32, 256x258xf32)
        multiply_0 = parameter_27 * parameter_27

        if FastReturn(block_idx=0, op_idx=105):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, multiply_0

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_14 = [1]

        if FastReturn(block_idx=0, op_idx=106):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, multiply_0, full_int_array_14

        # pd_op.sum: (256x1xf32) <- (256x258xf32, 1xi64)
        sum_0 = paddle.sum(multiply_0, keepdim=True, axis=full_int_array_14)

        if FastReturn(block_idx=0, op_idx=107):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sum_0

        # pd_op.sqrt: (256x1xf32) <- (256x1xf32)
        sqrt_0 = paddle.sqrt(sum_0)

        if FastReturn(block_idx=0, op_idx=108):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, parameter_26, parameter_27, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0

        # pd_op.multiply: (256x258xf32) <- (256x1xf32, 256x258xf32)
        multiply_1 = parameter_26 * parameter_27

        if FastReturn(block_idx=0, op_idx=109):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1

        # pd_op.divide: (256x258xf32) <- (256x258xf32, 256x1xf32)
        divide_0 = multiply_1 / sqrt_0

        if FastReturn(block_idx=0, op_idx=110):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, divide_0

        # pd_op.transpose: (258x256xf32) <- (256x258xf32)
        transpose_0 = paddle.transpose(divide_0, perm=[1, 0])

        if FastReturn(block_idx=0, op_idx=111):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0

        # pd_op.matmul: (200x256xf32) <- (200x258xf32, 258x256xf32)
        matmul_2 = paddle.matmul(concat_6, transpose_0, transpose_x=False, transpose_y=False)

        if FastReturn(block_idx=0, op_idx=112):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, parameter_25, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, matmul_2

        # pd_op.add: (200x256xf32) <- (200x256xf32, 256xf32)
        add_0 = matmul_2 + parameter_25

        if FastReturn(block_idx=0, op_idx=113):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0

        # pd_op.sigmoid: (200x256xf32) <- (200x256xf32)
        sigmoid_0 = paddle.nn.functional.sigmoid(add_0)

        if FastReturn(block_idx=0, op_idx=114):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, sigmoid_0

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_2 = add_0 * sigmoid_0

        if FastReturn(block_idx=0, op_idx=115):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2

        # pd_op.multiply: (256x258xf32) <- (256x258xf32, 256x258xf32)
        multiply_3 = parameter_24 * parameter_24

        if FastReturn(block_idx=0, op_idx=116):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, multiply_3

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_15 = [1]

        if FastReturn(block_idx=0, op_idx=117):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, multiply_3, full_int_array_15

        # pd_op.sum: (256x1xf32) <- (256x258xf32, 1xi64)
        sum_1 = paddle.sum(multiply_3, keepdim=True, axis=full_int_array_15)

        if FastReturn(block_idx=0, op_idx=118):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sum_1

        # pd_op.sqrt: (256x1xf32) <- (256x1xf32)
        sqrt_1 = paddle.sqrt(sum_1)

        if FastReturn(block_idx=0, op_idx=119):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, parameter_23, parameter_24, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1

        # pd_op.multiply: (256x258xf32) <- (256x1xf32, 256x258xf32)
        multiply_4 = parameter_23 * parameter_24

        if FastReturn(block_idx=0, op_idx=120):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4

        # pd_op.divide: (256x258xf32) <- (256x258xf32, 256x1xf32)
        divide_1 = multiply_4 / sqrt_1

        if FastReturn(block_idx=0, op_idx=121):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, divide_1

        # pd_op.transpose: (258x256xf32) <- (256x258xf32)
        transpose_1 = paddle.transpose(divide_1, perm=[1, 0])

        if FastReturn(block_idx=0, op_idx=122):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1

        # pd_op.matmul: (200x256xf32) <- (200x258xf32, 258x256xf32)
        matmul_3 = paddle.matmul(concat_6, transpose_1, transpose_x=False, transpose_y=False)

        if FastReturn(block_idx=0, op_idx=123):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, parameter_22, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, matmul_3

        # pd_op.add: (200x256xf32) <- (200x256xf32, 256xf32)
        add_1 = matmul_3 + parameter_22

        if FastReturn(block_idx=0, op_idx=124):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1

        # pd_op.sigmoid: (200x256xf32) <- (200x256xf32)
        sigmoid_1 = paddle.nn.functional.sigmoid(add_1)

        if FastReturn(block_idx=0, op_idx=125):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, sigmoid_1

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_5 = add_1 * sigmoid_1

        if FastReturn(block_idx=0, op_idx=126):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5

        # pd_op.multiply: (256x258xf32) <- (256x258xf32, 256x258xf32)
        multiply_6 = parameter_21 * parameter_21

        if FastReturn(block_idx=0, op_idx=127):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, multiply_6

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_16 = [1]

        if FastReturn(block_idx=0, op_idx=128):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, multiply_6, full_int_array_16

        # pd_op.sum: (256x1xf32) <- (256x258xf32, 1xi64)
        sum_2 = paddle.sum(multiply_6, keepdim=True, axis=full_int_array_16)

        if FastReturn(block_idx=0, op_idx=129):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sum_2

        # pd_op.sqrt: (256x1xf32) <- (256x1xf32)
        sqrt_2 = paddle.sqrt(sum_2)

        if FastReturn(block_idx=0, op_idx=130):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, parameter_20, parameter_21, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2

        # pd_op.multiply: (256x258xf32) <- (256x1xf32, 256x258xf32)
        multiply_7 = parameter_20 * parameter_21

        if FastReturn(block_idx=0, op_idx=131):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7

        # pd_op.divide: (256x258xf32) <- (256x258xf32, 256x1xf32)
        divide_2 = multiply_7 / sqrt_2

        if FastReturn(block_idx=0, op_idx=132):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, divide_2

        # pd_op.transpose: (258x256xf32) <- (256x258xf32)
        transpose_2 = paddle.transpose(divide_2, perm=[1, 0])

        if FastReturn(block_idx=0, op_idx=133):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2

        # pd_op.matmul: (200x256xf32) <- (200x258xf32, 258x256xf32)
        matmul_4 = paddle.matmul(concat_6, transpose_2, transpose_x=False, transpose_y=False)

        if FastReturn(block_idx=0, op_idx=134):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, parameter_19, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, matmul_4

        # pd_op.add: (200x256xf32) <- (200x256xf32, 256xf32)
        add_2 = matmul_4 + parameter_19

        if FastReturn(block_idx=0, op_idx=135):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2

        # pd_op.sigmoid: (200x256xf32) <- (200x256xf32)
        sigmoid_2 = paddle.nn.functional.sigmoid(add_2)

        if FastReturn(block_idx=0, op_idx=136):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, sigmoid_2

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_8 = add_2 * sigmoid_2

        if FastReturn(block_idx=0, op_idx=137):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8

        # pd_op.multiply: (256x256xf32) <- (256x256xf32, 256x256xf32)
        multiply_9 = parameter_18 * parameter_18

        if FastReturn(block_idx=0, op_idx=138):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, multiply_9

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_17 = [1]

        if FastReturn(block_idx=0, op_idx=139):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, multiply_9, full_int_array_17

        # pd_op.sum: (256x1xf32) <- (256x256xf32, 1xi64)
        sum_3 = paddle.sum(multiply_9, keepdim=True, axis=full_int_array_17)

        if FastReturn(block_idx=0, op_idx=140):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sum_3

        # pd_op.sqrt: (256x1xf32) <- (256x1xf32)
        sqrt_3 = paddle.sqrt(sum_3)

        if FastReturn(block_idx=0, op_idx=141):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, parameter_17, parameter_18, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3

        # pd_op.multiply: (256x256xf32) <- (256x1xf32, 256x256xf32)
        multiply_10 = parameter_17 * parameter_18

        if FastReturn(block_idx=0, op_idx=142):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10

        # pd_op.divide: (256x256xf32) <- (256x256xf32, 256x1xf32)
        divide_3 = multiply_10 / sqrt_3

        if FastReturn(block_idx=0, op_idx=143):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, divide_3

        # pd_op.transpose: (256x256xf32) <- (256x256xf32)
        transpose_3 = paddle.transpose(divide_3, perm=[1, 0])

        if FastReturn(block_idx=0, op_idx=144):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3

        # pd_op.matmul: (200x256xf32) <- (200x256xf32, 256x256xf32)
        matmul_5 = paddle.matmul(multiply_8, transpose_3, transpose_x=False, transpose_y=False)

        if FastReturn(block_idx=0, op_idx=145):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, parameter_16, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, matmul_5

        # pd_op.add: (200x256xf32) <- (200x256xf32, 256xf32)
        add_3 = matmul_5 + parameter_16

        if FastReturn(block_idx=0, op_idx=146):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3

        # pd_op.sigmoid: (200x256xf32) <- (200x256xf32)
        sigmoid_3 = paddle.nn.functional.sigmoid(add_3)

        if FastReturn(block_idx=0, op_idx=147):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, sigmoid_3

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_11 = add_3 * sigmoid_3

        if FastReturn(block_idx=0, op_idx=148):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_12 = multiply_11 * multiply_2

        if FastReturn(block_idx=0, op_idx=149):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, multiply_12

        # pd_op.subtract: (200x256xf32) <- (200x256xf32, 200x256xf32)
        subtract_0 = multiply_2 - multiply_12

        if FastReturn(block_idx=0, op_idx=150):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, subtract_0

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_13 = multiply_11 * multiply_5

        if FastReturn(block_idx=0, op_idx=151):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, subtract_0, multiply_13

        # pd_op.add: (200x256xf32) <- (200x256xf32, 200x256xf32)
        add_4 = subtract_0 + multiply_13

        if FastReturn(block_idx=0, op_idx=152):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4

        # pd_op.multiply: (256x256xf32) <- (256x256xf32, 256x256xf32)
        multiply_14 = parameter_15 * parameter_15

        if FastReturn(block_idx=0, op_idx=153):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, multiply_14

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_18 = [1]

        if FastReturn(block_idx=0, op_idx=154):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, multiply_14, full_int_array_18

        # pd_op.sum: (256x1xf32) <- (256x256xf32, 1xi64)
        sum_4 = paddle.sum(multiply_14, keepdim=True, axis=full_int_array_18)

        if FastReturn(block_idx=0, op_idx=155):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sum_4

        # pd_op.sqrt: (256x1xf32) <- (256x1xf32)
        sqrt_4 = paddle.sqrt(sum_4)

        if FastReturn(block_idx=0, op_idx=156):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, parameter_14, parameter_15, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4

        # pd_op.multiply: (256x256xf32) <- (256x1xf32, 256x256xf32)
        multiply_15 = parameter_14 * parameter_15

        if FastReturn(block_idx=0, op_idx=157):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15

        # pd_op.divide: (256x256xf32) <- (256x256xf32, 256x1xf32)
        divide_4 = multiply_15 / sqrt_4

        if FastReturn(block_idx=0, op_idx=158):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, divide_4

        # pd_op.transpose: (256x256xf32) <- (256x256xf32)
        transpose_4 = paddle.transpose(divide_4, perm=[1, 0])

        if FastReturn(block_idx=0, op_idx=159):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4

        # pd_op.matmul: (200x256xf32) <- (200x256xf32, 256x256xf32)
        matmul_6 = paddle.matmul(add_4, transpose_4, transpose_x=False, transpose_y=False)

        if FastReturn(block_idx=0, op_idx=160):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, parameter_13, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, matmul_6

        # pd_op.add: (200x256xf32) <- (200x256xf32, 256xf32)
        add_5 = matmul_6 + parameter_13

        if FastReturn(block_idx=0, op_idx=161):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5

        # pd_op.sigmoid: (200x256xf32) <- (200x256xf32)
        sigmoid_4 = paddle.nn.functional.sigmoid(add_5)

        if FastReturn(block_idx=0, op_idx=162):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, sigmoid_4

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_16 = add_5 * sigmoid_4

        if FastReturn(block_idx=0, op_idx=163):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_17 = multiply_16 * multiply_2

        if FastReturn(block_idx=0, op_idx=164):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, multiply_17

        # pd_op.subtract: (200x256xf32) <- (200x256xf32, 200x256xf32)
        subtract_1 = multiply_2 - multiply_17

        if FastReturn(block_idx=0, op_idx=165):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, subtract_1

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_18 = multiply_16 * multiply_5

        if FastReturn(block_idx=0, op_idx=166):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, subtract_1, multiply_18

        # pd_op.add: (200x256xf32) <- (200x256xf32, 200x256xf32)
        add_6 = subtract_1 + multiply_18

        if FastReturn(block_idx=0, op_idx=167):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6

        # pd_op.multiply: (256x256xf32) <- (256x256xf32, 256x256xf32)
        multiply_19 = parameter_12 * parameter_12

        if FastReturn(block_idx=0, op_idx=168):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, multiply_19

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_19 = [1]

        if FastReturn(block_idx=0, op_idx=169):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, multiply_19, full_int_array_19

        # pd_op.sum: (256x1xf32) <- (256x256xf32, 1xi64)
        sum_5 = paddle.sum(multiply_19, keepdim=True, axis=full_int_array_19)

        if FastReturn(block_idx=0, op_idx=170):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sum_5

        # pd_op.sqrt: (256x1xf32) <- (256x1xf32)
        sqrt_5 = paddle.sqrt(sum_5)

        if FastReturn(block_idx=0, op_idx=171):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, parameter_11, parameter_12, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5

        # pd_op.multiply: (256x256xf32) <- (256x1xf32, 256x256xf32)
        multiply_20 = parameter_11 * parameter_12

        if FastReturn(block_idx=0, op_idx=172):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20

        # pd_op.divide: (256x256xf32) <- (256x256xf32, 256x1xf32)
        divide_5 = multiply_20 / sqrt_5

        if FastReturn(block_idx=0, op_idx=173):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, divide_5

        # pd_op.transpose: (256x256xf32) <- (256x256xf32)
        transpose_5 = paddle.transpose(divide_5, perm=[1, 0])

        if FastReturn(block_idx=0, op_idx=174):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5

        # pd_op.matmul: (200x256xf32) <- (200x256xf32, 256x256xf32)
        matmul_7 = paddle.matmul(add_6, transpose_5, transpose_x=False, transpose_y=False)

        if FastReturn(block_idx=0, op_idx=175):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_10, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, matmul_7

        # pd_op.add: (200x256xf32) <- (200x256xf32, 256xf32)
        add_7 = matmul_7 + parameter_10

        if FastReturn(block_idx=0, op_idx=176):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7

        # pd_op.sigmoid: (200x256xf32) <- (200x256xf32)
        sigmoid_5 = paddle.nn.functional.sigmoid(add_7)

        if FastReturn(block_idx=0, op_idx=177):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, sigmoid_5

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_21 = add_7 * sigmoid_5

        if FastReturn(block_idx=0, op_idx=178):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_22 = multiply_21 * multiply_2

        if FastReturn(block_idx=0, op_idx=179):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, multiply_22

        # pd_op.subtract: (200x256xf32) <- (200x256xf32, 200x256xf32)
        subtract_2 = multiply_2 - multiply_22

        if FastReturn(block_idx=0, op_idx=180):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, subtract_2

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_23 = multiply_21 * multiply_5

        if FastReturn(block_idx=0, op_idx=181):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, subtract_2, multiply_23

        # pd_op.add: (200x256xf32) <- (200x256xf32, 200x256xf32)
        add_8 = subtract_2 + multiply_23

        if FastReturn(block_idx=0, op_idx=182):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8

        # pd_op.multiply: (256x256xf32) <- (256x256xf32, 256x256xf32)
        multiply_24 = parameter_9 * parameter_9

        if FastReturn(block_idx=0, op_idx=183):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, multiply_24

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_20 = [1]

        if FastReturn(block_idx=0, op_idx=184):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, multiply_24, full_int_array_20

        # pd_op.sum: (256x1xf32) <- (256x256xf32, 1xi64)
        sum_6 = paddle.sum(multiply_24, keepdim=True, axis=full_int_array_20)

        if FastReturn(block_idx=0, op_idx=185):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sum_6

        # pd_op.sqrt: (256x1xf32) <- (256x1xf32)
        sqrt_6 = paddle.sqrt(sum_6)

        if FastReturn(block_idx=0, op_idx=186):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6

        # pd_op.multiply: (256x256xf32) <- (256x1xf32, 256x256xf32)
        multiply_25 = parameter_8 * parameter_9

        if FastReturn(block_idx=0, op_idx=187):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25

        # pd_op.divide: (256x256xf32) <- (256x256xf32, 256x1xf32)
        divide_6 = multiply_25 / sqrt_6

        if FastReturn(block_idx=0, op_idx=188):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, divide_6

        # pd_op.transpose: (256x256xf32) <- (256x256xf32)
        transpose_6 = paddle.transpose(divide_6, perm=[1, 0])

        if FastReturn(block_idx=0, op_idx=189):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6

        # pd_op.matmul: (200x256xf32) <- (200x256xf32, 256x256xf32)
        matmul_8 = paddle.matmul(add_8, transpose_6, transpose_x=False, transpose_y=False)

        if FastReturn(block_idx=0, op_idx=190):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, matmul_8

        # pd_op.add: (200x256xf32) <- (200x256xf32, 256xf32)
        add_9 = matmul_8 + parameter_7

        if FastReturn(block_idx=0, op_idx=191):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9

        # pd_op.sigmoid: (200x256xf32) <- (200x256xf32)
        sigmoid_6 = paddle.nn.functional.sigmoid(add_9)

        if FastReturn(block_idx=0, op_idx=192):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, sigmoid_6

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_26 = add_9 * sigmoid_6

        if FastReturn(block_idx=0, op_idx=193):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_27 = multiply_26 * multiply_2

        if FastReturn(block_idx=0, op_idx=194):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, multiply_27

        # pd_op.subtract: (200x256xf32) <- (200x256xf32, 200x256xf32)
        subtract_3 = multiply_2 - multiply_27

        if FastReturn(block_idx=0, op_idx=195):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, subtract_3

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_28 = multiply_26 * multiply_5

        if FastReturn(block_idx=0, op_idx=196):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, subtract_3, multiply_28

        # pd_op.add: (200x256xf32) <- (200x256xf32, 200x256xf32)
        add_10 = subtract_3 + multiply_28

        if FastReturn(block_idx=0, op_idx=197):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10

        # pd_op.multiply: (256x256xf32) <- (256x256xf32, 256x256xf32)
        multiply_29 = parameter_6 * parameter_6

        if FastReturn(block_idx=0, op_idx=198):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, multiply_29

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_21 = [1]

        if FastReturn(block_idx=0, op_idx=199):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, multiply_29, full_int_array_21

        # pd_op.sum: (256x1xf32) <- (256x256xf32, 1xi64)
        sum_7 = paddle.sum(multiply_29, keepdim=True, axis=full_int_array_21)

        if FastReturn(block_idx=0, op_idx=200):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sum_7

        # pd_op.sqrt: (256x1xf32) <- (256x1xf32)
        sqrt_7 = paddle.sqrt(sum_7)

        if FastReturn(block_idx=0, op_idx=201):
            return parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7

        # pd_op.multiply: (256x256xf32) <- (256x1xf32, 256x256xf32)
        multiply_30 = parameter_5 * parameter_6

        if FastReturn(block_idx=0, op_idx=202):
            return parameter_2, parameter_3, parameter_4, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30

        # pd_op.divide: (256x256xf32) <- (256x256xf32, 256x1xf32)
        divide_7 = multiply_30 / sqrt_7

        if FastReturn(block_idx=0, op_idx=203):
            return parameter_2, parameter_3, parameter_4, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, divide_7

        # pd_op.transpose: (256x256xf32) <- (256x256xf32)
        transpose_7 = paddle.transpose(divide_7, perm=[1, 0])

        if FastReturn(block_idx=0, op_idx=204):
            return parameter_2, parameter_3, parameter_4, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7

        # pd_op.matmul: (200x256xf32) <- (200x256xf32, 256x256xf32)
        matmul_9 = paddle.matmul(add_10, transpose_7, transpose_x=False, transpose_y=False)

        if FastReturn(block_idx=0, op_idx=205):
            return parameter_2, parameter_3, parameter_4, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, matmul_9

        # pd_op.add: (200x256xf32) <- (200x256xf32, 256xf32)
        add_11 = matmul_9 + parameter_4

        if FastReturn(block_idx=0, op_idx=206):
            return parameter_2, parameter_3, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11

        # pd_op.sigmoid: (200x256xf32) <- (200x256xf32)
        sigmoid_7 = paddle.nn.functional.sigmoid(add_11)

        if FastReturn(block_idx=0, op_idx=207):
            return parameter_2, parameter_3, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, sigmoid_7

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_31 = add_11 * sigmoid_7

        if FastReturn(block_idx=0, op_idx=208):
            return parameter_2, parameter_3, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_32 = multiply_31 * multiply_2

        if FastReturn(block_idx=0, op_idx=209):
            return parameter_2, parameter_3, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, multiply_32

        # pd_op.subtract: (200x256xf32) <- (200x256xf32, 200x256xf32)
        subtract_4 = multiply_2 - multiply_32

        if FastReturn(block_idx=0, op_idx=210):
            return parameter_2, parameter_3, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, subtract_4

        # pd_op.multiply: (200x256xf32) <- (200x256xf32, 200x256xf32)
        multiply_33 = multiply_31 * multiply_5

        if FastReturn(block_idx=0, op_idx=211):
            return parameter_2, parameter_3, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, subtract_4, multiply_33

        # pd_op.add: (200x256xf32) <- (200x256xf32, 200x256xf32)
        add_12 = subtract_4 + multiply_33

        if FastReturn(block_idx=0, op_idx=212):
            return parameter_2, parameter_3, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12

        # pd_op.matmul: (200x1xf32) <- (200x256xf32, 256x1xf32)
        matmul_10 = paddle.matmul(add_12, parameter_3, transpose_x=False, transpose_y=False)

        if FastReturn(block_idx=0, op_idx=213):
            return parameter_2, concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, matmul_10

        # pd_op.add: (200x1xf32) <- (200x1xf32, 1xf32)
        add_13 = matmul_10 + parameter_2

        if FastReturn(block_idx=0, op_idx=214):
            return concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, add_13

        # pd_op.full_int_array: (1xi64) <- ()
        full_int_array_22 = [1]

        if FastReturn(block_idx=0, op_idx=215):
            return concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, add_13, full_int_array_22

        # pd_op.full: (1xi32) <- ()
        full_20 = paddle.full(shape=[1], dtype='int32', fill_value=1)

        if FastReturn(block_idx=0, op_idx=216):
            return concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, add_13, full_int_array_22, full_20

        # pd_op.split: ([200x1xf32]) <- (200x1xf32, 1xi64, 1xi32)
        split_0 = paddle.split(add_13, full_int_array_22, full_20)

        if FastReturn(block_idx=0, op_idx=217):
            return concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, split_0

        # builtin.split: (200x1xf32) <- ([200x1xf32])
        split_1, = split_0

        if FastReturn(block_idx=0, op_idx=218):
            return concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, split_1

        # pd_op.full: (1xf32) <- ()
        full_21 = paddle.full(shape=[1], dtype='float32', fill_value=1)

        if FastReturn(block_idx=0, op_idx=219):
            return concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, split_1, full_21

        # pd_op.scale: (200x1xf32) <- (200x1xf32, 1xf32)
        scale_4 = paddle.scale(split_1, full_21, bias_after_scale=True, bias=70)

        if FastReturn(block_idx=0, op_idx=220):
            return concat_0, set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (200x2xf32)
        None

        if FastReturn(block_idx=0, op_idx=221):
            return set_value__1, matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (2x2xf32)
        None

        if FastReturn(block_idx=0, op_idx=222):
            return matmul_0, scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (200x2xf32)
        None

        if FastReturn(block_idx=0, op_idx=223):
            return scale_2, scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (200x128xf32)
        None

        if FastReturn(block_idx=0, op_idx=224):
            return scale_3, concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (200x128xf32)
        None

        if FastReturn(block_idx=0, op_idx=225):
            return concat_6, sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (200x258xf32)
        None

        if FastReturn(block_idx=0, op_idx=226):
            return sqrt_0, multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (256x1xf32)
        None

        if FastReturn(block_idx=0, op_idx=227):
            return multiply_1, transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (256x258xf32)
        None

        if FastReturn(block_idx=0, op_idx=228):
            return transpose_0, add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (258x256xf32)
        None

        if FastReturn(block_idx=0, op_idx=229):
            return add_0, multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (200x256xf32)
        None

        if FastReturn(block_idx=0, op_idx=230):
            return multiply_2, sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (200x256xf32)
        None

        if FastReturn(block_idx=0, op_idx=231):
            return sqrt_1, multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (256x1xf32)
        None

        if FastReturn(block_idx=0, op_idx=232):
            return multiply_4, transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (256x258xf32)
        None

        if FastReturn(block_idx=0, op_idx=233):
            return transpose_1, add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (258x256xf32)
        None

        if FastReturn(block_idx=0, op_idx=234):
            return add_1, multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (200x256xf32)
        None

        if FastReturn(block_idx=0, op_idx=235):
            return multiply_5, sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (200x256xf32)
        None

        if FastReturn(block_idx=0, op_idx=236):
            return sqrt_2, multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (256x1xf32)
        None

        if FastReturn(block_idx=0, op_idx=237):
            return multiply_7, transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (256x258xf32)
        None

        if FastReturn(block_idx=0, op_idx=238):
            return transpose_2, add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (258x256xf32)
        None

        if FastReturn(block_idx=0, op_idx=239):
            return add_2, multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (200x256xf32)
        None

        if FastReturn(block_idx=0, op_idx=240):
            return multiply_8, sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (200x256xf32)
        None

        if FastReturn(block_idx=0, op_idx=241):
            return sqrt_3, multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (256x1xf32)
        None

        if FastReturn(block_idx=0, op_idx=242):
            return multiply_10, transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (256x256xf32)
        None

        if FastReturn(block_idx=0, op_idx=243):
            return transpose_3, add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (256x256xf32)
        None

        if FastReturn(block_idx=0, op_idx=244):
            return add_3, multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (200x256xf32)
        None

        if FastReturn(block_idx=0, op_idx=245):
            return multiply_11, add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (200x256xf32)
        None

        if FastReturn(block_idx=0, op_idx=246):
            return add_4, sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (200x256xf32)
        None

        if FastReturn(block_idx=0, op_idx=247):
            return sqrt_4, multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (256x1xf32)
        None

        if FastReturn(block_idx=0, op_idx=248):
            return multiply_15, transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (256x256xf32)
        None

        if FastReturn(block_idx=0, op_idx=249):
            return transpose_4, add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (256x256xf32)
        None

        if FastReturn(block_idx=0, op_idx=250):
            return add_5, multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (200x256xf32)
        None

        if FastReturn(block_idx=0, op_idx=251):
            return multiply_16, add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (200x256xf32)
        None

        if FastReturn(block_idx=0, op_idx=252):
            return add_6, sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (200x256xf32)
        None

        if FastReturn(block_idx=0, op_idx=253):
            return sqrt_5, multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (256x1xf32)
        None

        if FastReturn(block_idx=0, op_idx=254):
            return multiply_20, transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (256x256xf32)
        None

        if FastReturn(block_idx=0, op_idx=255):
            return transpose_5, add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (256x256xf32)
        None

        if FastReturn(block_idx=0, op_idx=256):
            return add_7, multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (200x256xf32)
        None

        if FastReturn(block_idx=0, op_idx=257):
            return multiply_21, add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (200x256xf32)
        None

        if FastReturn(block_idx=0, op_idx=258):
            return add_8, sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (200x256xf32)
        None

        if FastReturn(block_idx=0, op_idx=259):
            return sqrt_6, multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (256x1xf32)
        None

        if FastReturn(block_idx=0, op_idx=260):
            return multiply_25, transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (256x256xf32)
        None

        if FastReturn(block_idx=0, op_idx=261):
            return transpose_6, add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (256x256xf32)
        None

        if FastReturn(block_idx=0, op_idx=262):
            return add_9, multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (200x256xf32)
        None

        if FastReturn(block_idx=0, op_idx=263):
            return multiply_26, add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (200x256xf32)
        None

        if FastReturn(block_idx=0, op_idx=264):
            return add_10, sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (200x256xf32)
        None

        if FastReturn(block_idx=0, op_idx=265):
            return sqrt_7, multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (256x1xf32)
        None

        if FastReturn(block_idx=0, op_idx=266):
            return multiply_30, transpose_7, add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (256x256xf32)
        None

        if FastReturn(block_idx=0, op_idx=267):
            return transpose_7, add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (256x256xf32)
        None

        if FastReturn(block_idx=0, op_idx=268):
            return add_11, multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (200x256xf32)
        None

        if FastReturn(block_idx=0, op_idx=269):
            return multiply_31, add_12, scale_4

        # builtin.shadow_output: () <- (200x256xf32)
        None

        if FastReturn(block_idx=0, op_idx=270):
            return add_12, scale_4

        # builtin.shadow_output: () <- (200x256xf32)
        None

        if FastReturn(block_idx=0, op_idx=271):
            return scale_4

        # builtin.shadow_output: () <- (200x1xf32)
        None
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

        # builtin.parameter: (2x128xf32) <- ()
        None

        # builtin.parameter: (2xi64) <- ()
        None

        # builtin.parameter: (1xf32) <- ()
        None

        # builtin.parameter: (256x1xf32) <- ()
        None

        # builtin.parameter: (256xf32) <- ()
        None

        # builtin.parameter: (256x1xf32) <- ()
        None

        # builtin.parameter: (256x256xf32) <- ()
        None

        # builtin.parameter: (256xf32) <- ()
        None

        # builtin.parameter: (256x1xf32) <- ()
        None

        # builtin.parameter: (256x256xf32) <- ()
        None

        # builtin.parameter: (256xf32) <- ()
        None

        # builtin.parameter: (256x1xf32) <- ()
        None

        # builtin.parameter: (256x256xf32) <- ()
        None

        # builtin.parameter: (256xf32) <- ()
        None

        # builtin.parameter: (256x1xf32) <- ()
        None

        # builtin.parameter: (256x256xf32) <- ()
        None

        # builtin.parameter: (256xf32) <- ()
        None

        # builtin.parameter: (256x1xf32) <- ()
        None

        # builtin.parameter: (256x256xf32) <- ()
        None

        # builtin.parameter: (256xf32) <- ()
        None

        # builtin.parameter: (256x1xf32) <- ()
        None

        # builtin.parameter: (256x258xf32) <- ()
        None

        # builtin.parameter: (256xf32) <- ()
        None

        # builtin.parameter: (256x1xf32) <- ()
        None

        # builtin.parameter: (256x258xf32) <- ()
        None

        # builtin.parameter: (256xf32) <- ()
        None

        # builtin.parameter: (256x1xf32) <- ()
        None

        # builtin.parameter: (256x258xf32) <- ()
        None

        # pd_op.data: (200x1xf32) <- ()
        None

        # pd_op.data: (200x1xf32) <- ()
        None

        # pd_op.data: (200x1xf32) <- ()
        None

        # pd_op.data: (200x1xf32) <- ()
        None

        # pd_op.data: (200x1xf32) <- ()
        None

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

        # builtin.shadow_output: () <- (200x2xf32)
        None

        # builtin.shadow_output: () <- (2x2xf32)
        None

        # builtin.shadow_output: () <- (200x2xf32)
        None

        # builtin.shadow_output: () <- (200x128xf32)
        None

        # builtin.shadow_output: () <- (200x128xf32)
        None

        # builtin.shadow_output: () <- (200x258xf32)
        None

        # builtin.shadow_output: () <- (256x1xf32)
        None

        # builtin.shadow_output: () <- (256x258xf32)
        None

        # builtin.shadow_output: () <- (258x256xf32)
        None

        # builtin.shadow_output: () <- (200x256xf32)
        None

        # builtin.shadow_output: () <- (200x256xf32)
        None

        # builtin.shadow_output: () <- (256x1xf32)
        None

        # builtin.shadow_output: () <- (256x258xf32)
        None

        # builtin.shadow_output: () <- (258x256xf32)
        None

        # builtin.shadow_output: () <- (200x256xf32)
        None

        # builtin.shadow_output: () <- (200x256xf32)
        None

        # builtin.shadow_output: () <- (256x1xf32)
        None

        # builtin.shadow_output: () <- (256x258xf32)
        None

        # builtin.shadow_output: () <- (258x256xf32)
        None

        # builtin.shadow_output: () <- (200x256xf32)
        None

        # builtin.shadow_output: () <- (200x256xf32)
        None

        # builtin.shadow_output: () <- (256x1xf32)
        None

        # builtin.shadow_output: () <- (256x256xf32)
        None

        # builtin.shadow_output: () <- (256x256xf32)
        None

        # builtin.shadow_output: () <- (200x256xf32)
        None

        # builtin.shadow_output: () <- (200x256xf32)
        None

        # builtin.shadow_output: () <- (200x256xf32)
        None

        # builtin.shadow_output: () <- (256x1xf32)
        None

        # builtin.shadow_output: () <- (256x256xf32)
        None

        # builtin.shadow_output: () <- (256x256xf32)
        None

        # builtin.shadow_output: () <- (200x256xf32)
        None

        # builtin.shadow_output: () <- (200x256xf32)
        None

        # builtin.shadow_output: () <- (200x256xf32)
        None

        # builtin.shadow_output: () <- (256x1xf32)
        None

        # builtin.shadow_output: () <- (256x256xf32)
        None

        # builtin.shadow_output: () <- (256x256xf32)
        None

        # builtin.shadow_output: () <- (200x256xf32)
        None

        # builtin.shadow_output: () <- (200x256xf32)
        None

        # builtin.shadow_output: () <- (200x256xf32)
        None

        # builtin.shadow_output: () <- (256x1xf32)
        None

        # builtin.shadow_output: () <- (256x256xf32)
        None

        # builtin.shadow_output: () <- (256x256xf32)
        None

        # builtin.shadow_output: () <- (200x256xf32)
        None

        # builtin.shadow_output: () <- (200x256xf32)
        None

        # builtin.shadow_output: () <- (200x256xf32)
        None

        # builtin.shadow_output: () <- (256x1xf32)
        None

        # builtin.shadow_output: () <- (256x256xf32)
        None

        # builtin.shadow_output: () <- (256x256xf32)
        None

        # builtin.shadow_output: () <- (200x256xf32)
        None

        # builtin.shadow_output: () <- (200x256xf32)
        None

        # builtin.shadow_output: () <- (200x256xf32)
        None

        # builtin.shadow_output: () <- (200x1xf32)
        None
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