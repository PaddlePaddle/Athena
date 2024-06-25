import numpy as np
import paddle
import sys
import random
from absl import app
from absl import flags
import traceback

flags.DEFINE_integer("max_try_cnt", 10, "max try cnt")
flags.DEFINE_string("output_file", "", "output file")

FLAGS = flags.FLAGS

def InitTensorShape(tensor):
    if tensor is None:
        return None
    if isinstance(tensor, list) and len(tensor) > 0 and isinstance(tensor[0], int):
        return [len(tensor)]
    if isinstance(tensor, list):
        return [InitTensorShape(t) for t in tensor]
    if not hasattr(tensor, 'shape'):
        raise NotImplementedError(f"type(tensor): {type(tensor)}")
    return tensor.shape

def InitTensorData(tensor):
    if tensor is None:
        return None
    if isinstance(tensor, list) and len(tensor) > 0 and isinstance(tensor[0], int):
        return tensor
    if isinstance(tensor, list):
        return [InitTensorData(t) for t in tensor]
    if not hasattr(tensor, 'numel'):
        raise NotImplementedError(f"type(tensor): {type(tensor)}")
    kLimit = 32
    if tensor.numel().item() >= kLimit:
        return None
    if not hasattr(tensor, 'numpy'):
        raise NotImplementedError(f"type(tensor): {type(tensor)}")
    ndarray = tensor.numpy()
    if np.isnan(ndarray).any():
        return None
    if np.isinf(ndarray).any():
        return None
    return ndarray.tolist()

def IsInteger(dtype):
    return np.dtype(dtype).char in np.typecodes['AllInteger']

def GetRecordClass(program_id, op_id, op_name, input_idx, shape, data):
    return f"""
class PirProgram_op_input_tensor_meta_{random.randint(0, sys.maxsize)}:
    program_id = {program_id}
    op_id = {op_id}
    op_name = "{op_name}"
    input_idx = {input_idx}
    shape = {str(shape)}
    data = {str(data)}

"""

def AppendRecordClassToOutputFile(content):
    with open(FLAGS.output_file, 'a') as f:
            f.write(content)

{% macro get_input_shape_instance(block, block_idx, input_idx) -%}
    {{block.input_tensor_descs[input_idx].shape}}
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
    paddle.cast(paddle.randint(low=0, high=2, shape={{shape}}, dtype='int32'), 'bool')
{%- elif big_dtype == "int64" -%}
    paddle.randint(low={{min}}, high={{max}}, shape={{shape}}, dtype='{{dtype}}')
{%- elif big_dtype == "float64" -%}
    paddle.uniform({{shape}}, dtype='{{dtype}}', min={{min}}, max={{max}})
{%- endif -%}
{%- endmacro -%}


{% for program_id, blocks in programs %}
def InferAndSaveOpInputDims_Program{{program_id}}():
    op_input2shape = {}
    op_input2data = {}

    def GetInputMetaRecorder(op_name, op_id, *inputs):
        def AllInitialized():
            return all(
                (op_id, input_idx) in op_input2shape
                for input_idx in range(len(inputs))
            )
        if AllInitialized():
            return lambda: None
        for input_idx in range(len(inputs)):
            op_input2shape[(op_id, input_idx)] = InitTensorShape(inputs[input_idx])
            op_input2data[(op_id, input_idx)] = InitTensorData(inputs[input_idx])
        def Record():
            for input_idx in range(len(inputs)):
                AppendRecordClassToOutputFile(GetRecordClass(
                    program_id={{program_id}},
                    op_id=op_id,
                    op_name=op_name,
                    input_idx=input_idx,
                    shape=op_input2shape.get((op_id, input_idx), None),
                    data=op_input2data.get((op_id, input_idx), None),
                ))
        return Record

    def AllShapesInfered():
        {% for block in blocks %}
        {% for stmt in block.stmts %}
        {%- for input_tensor_name in stmt.input_tensor_names %}
        {%- set input_idx = loop.index0 %}
        if ({{stmt.op_id}}, {{input_idx}}) not in op_input2shape:
            return False
        {%- endfor %}
        {%- endfor %}
        {%- endfor %}
        return True

    class OpInputShapesExtractor:
    {%- for block in blocks %}
    {%- set block_idx = loop.index0 %}

        def {{block.block_name}}(self, {{block.input_arg_names | join(", ")}}):
            
        {%- for stmt in block.stmts %}
            # ({{stmt.outputs_type_strs|join(", ")}}) <- ({{stmt.inputs_type_strs|join(", ")}})
            recorder = GetInputMetaRecorder("{{stmt.op_name}}", {{stmt.op_id}}, {{stmt.input_tensor_names | join(", ")}})
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
            recorder()
            
        {%- endfor %}
            return {{block.output_arg_names | join(", ")}}
    {%- endfor %}
    extractor = OpInputShapesExtractor()
    for _ in range(FLAGS.max_try_cnt):
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
        if AllShapesInfered():
            break
{% endfor %}

def InferAndSaveOpInputDims(argv):
{%- for program_id, blocks in programs %}
    try:
        InferAndSaveOpInputDims_Program{{program_id}}()
    except Exception as e:
        traceback.print_exc()
{%- endfor %}

if __name__ == '__main__':
    app.run(InferAndSaveOpInputDims)