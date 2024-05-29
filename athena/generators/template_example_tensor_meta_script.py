import os
os.environ['FLAGS_cinn_new_group_scheduler'] = '1'
os.environ['FLAGS_group_schedule_tiling_first'] = '1'
os.environ['FLAGS_prim_all'] = 'true'
os.environ['FLAGS_prim_enable_dynamic'] = '1'
os.environ['FLAGS_enable_pir_api'] = '1'
os.environ['FLAGS_cinn_bucket_compile'] = '1'

import numpy as np
import paddle

{% macro block_input_shape_global_var_name(block, input_idx) -%}
{{block.block_name}}_in{{input_idx}}_shape
{%- endmacro %}

class BlockShapesExtractor:
{%- for block in blocks %}
{%- set block_idx = loop.index0 %}

    def {{block.block_name}}(self, {{block.input_arg_names | join(", ")}}):
    {%- for arg_name in block.input_arg_names %}
    {%- set input_idx = loop.index0 %}
        global {{block_input_shape_global_var_name(block, input_idx)}}
        {{block_input_shape_global_var_name(block, input_idx)}} = {{arg_name}}.shape
    {%- endfor %}
        
    {%- for stmt in block.stmts %}
    {%- set op_idx = loop.index0 %}

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
        {{block_input_shape_global_var_name(block, input_idx)}}
    {%- endif -%}
{%- endmacro %}


{% macro get_input_tensor_instance(block, block_idx, input_idx) -%}
{%- set shape = get_input_shape_instance(block, block_idx, input_idx) -%}
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

def InferOpInputOutputShapeAndData():
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


if __name__ == '__main__':
    InferOpInputOutputShapeAndData()
