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
    return {{blocks | length}} # number-of-blocks

def NumOperationsInBlock(block_idx):
    return [{{blocks | map(attribute='stmts') | map('length') | join(", ") }}][block_idx] - 1 # number-of-ops-in-block

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

{% macro block_input_shape_global_var_name(block, block_idx, input_idx) -%}
{{block.block_name}}_{{block_idx}}_{{input_idx}}_shape
{%- endmacro %}

class BlockEntries:
{%- for block in blocks %}
{%- set block_idx = loop.index0 %}

    def {{block.block_name}}(self, {{block.input_arg_names | join(", ")}}):
    {%- for stmt in block.stmts %}
    {%- set op_idx = loop.index0 %}
    {%- if op_idx > 0 %}

        if FastReturn(block_idx={{block_idx}}, op_idx={{op_idx - 1}}):
            return {{ stmt.tensors_used_by_downstream | join(", ") }}
    {%- endif %}

        # {{stmt.op_name}}: ({{stmt.outputs_type_strs|join(", ")}}) <- ({{stmt.inputs_type_strs|join(", ")}})
        {%- for pycode in stmt.pycode %}
        {%- if pycode.num_tabs == 0 %}
        {{pycode.pycode}}
        {%- elif pycode.num_tabs == 1 %}
            {{pycode.pycode}}
        {%- elif pycode.num_tabs == 2 %}
                {{pycode.pycode}}
        {%- else %}
        raise NotImplementedError("unsupported indent size {{pycode.num_tabs}}")
        {%- endif %}
        {%- endfor %}
    {%- endfor %}
        return {{block.output_arg_names | join(", ")}}
{%- endfor %}


{% for block in blocks %}
{%- set block_idx = loop.index0 %}
{%- for shape, _ in block.input_spec_shape_dtypes %}
{%- set input_idx = loop.index0 %}
# {{shape}}
{{block_input_shape_global_var_name(block, block_idx, input_idx)}} = None
{%- endfor %}
{%- endfor %}

class BlockShapesExtractor:
{%- for block in blocks %}
{%- set block_idx = loop.index0 %}

    def {{block.block_name}}(self, {{block.input_arg_names | join(", ")}}):
    {%- for arg_name in block.input_arg_names %}
    {%- set input_idx = loop.index0 %}
        global {{block_input_shape_global_var_name(block, block_idx, input_idx)}}
        {{block_input_shape_global_var_name(block, block_idx, input_idx)}} = {{arg_name}}.shape
    {%- endfor %}
        
    {%- for stmt in block.stmts %}
    {%- set op_idx = loop.index0 %}

        # {{stmt.op_name}}: ({{stmt.outputs_type_strs|join(", ")}}) <- ({{stmt.inputs_type_strs|join(", ")}})
        {%- for pycode in stmt.pycode %}
        {%- if pycode.num_tabs == 0 %}
        {{pycode.pycode}}
        {%- elif pycode.num_tabs == 1 %}
            {{pycode.pycode}}
        {%- elif pycode.num_tabs == 2 %}
                {{pycode.pycode}}
        {%- else %}
        raise NotImplementedError("unsupported indent size {{pycode.num_tabs}}")
        {%- endif %}
        {%- endfor %}
    {%- endfor %}
        return {{block.output_arg_names | join(", ")}}
{%- endfor %}

{% macro get_input_shape_instance(block, block_idx, input_idx) -%}
    {%- if block.is_entry_block -%}
        {{block.input_tensor_descs[input_idx].shape}}
    {%- else -%}
        {{block_input_shape_global_var_name(block, block_idx, input_idx)}}
    {%- endif -%}
{%- endmacro %}


{% macro get_input_tensor_instance(block, block_idx, input_idx) -%}
{%- set shape = block.input_tensor_descs[input_idx].shape -%}
{%- set dtype = block.input_tensor_descs[input_idx].dtype -%}
{%- set big_dtype = block.input_tensor_descs[input_idx].big_dtype -%}
{%- set data = block.input_tensor_descs[input_idx].data -%}
{%- set min = block.input_tensor_descs[input_idx].min -%}
{%- set max = block.input_tensor_descs[input_idx].max -%}
{%- if data != None -%}
    paddle.to_tensor({{data}}, dtype='{{dtype}}').reshape({{shape}})
{%- elif big_dtype == "bool" -%}
    paddle.zeros({{shape}}, dtype='{{dtype}}')
{%- elif big_dtype == "int64" -%}
    paddle.randint(low={{min}}, high={{max}}, shape={{shape}}, dtype='{{dtype}}')
{%- elif big_dtype == "float64" -%}
    paddle.uniform({{shape}}, dtype='{{dtype}}', min={{min}}, max={{max}})
{%- endif %}
{%- endmacro %}

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
{%- for block in blocks %}
{%- if block.is_entry_block %}
{%- set block_idx = loop.index0 %}
    extractor.{{block.block_name}}(
    {%- for arg_name in block.input_arg_names %}
    {%- set input_idx = loop.index0 %}
        {{arg_name}}={{get_input_tensor_instance(block, block_idx, input_idx)}},
    {%- endfor %}
    )
{%- endif %}
{%- endfor %}


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

{%- for block in blocks %}
{%- set block_idx = loop.index0 %}

if ShouldTestBlock({{block_idx}}):

    class Block_{{block.block_name}}(paddle.nn.Layer):
        def __init__(self):
            super().__init__()

        def forward(self, {{ block.input_arg_names | join(", ") }}):
            return BlockEntries().{{block.block_name}}({{ block.input_arg_names | join(", ") }})

    class Test_{{block.block_name}}(TestBase, unittest.TestCase):
        def prepare_data(self):
            self.inputs = [
            {%- for arg_name in block.input_arg_names %}
            {%- set input_idx = loop.index0 %}
                # {{arg_name}}
                {{get_input_tensor_instance(block, block_idx, input_idx)}},
            {%- endfor %}
            ]
            for input in self.inputs:
                input.stop_gradient = True

        def apply_to_static(self, net, use_cinn):
            build_strategy = paddle.static.BuildStrategy()
            input_spec = [
            {%- for shape, dtype in block.input_spec_shape_dtypes %}
            {%- set input_idx = loop.index0 %}
                # {{block.input_arg_names[input_idx]}}
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
            net = Block_{{block.block_name}}()
            net.eval()
            if GetEnvVarEnableJit():
                net = self.apply_to_static(net, use_cinn)
            out = net(*self.inputs)
            return out

{%- endfor %}

if __name__ == '__main__':
    unittest.main()
