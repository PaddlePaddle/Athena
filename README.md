# Athena

## How to generate pir python files?

Set environment variable `FLAGS_logging_pir_py_code_dir` to an existed logging directory before running a paddle program. Once the paddle program finished, under the logging directory, there are two generated pir python files: `exec_programs.py` and `programs_example_input_tensor_meta.py`.

## How to prepare op example input tensor meta files?

Generates op example input tensor meta file from pir programs file and programs example input tensor meta file
```bash
python3.9 -m athena.op_example_input_tensor_meta --ir_programs=./example_exec_programs.py --example_inputs=./example_programs_example_input_tensor_meta.py  --tmp_dir=/tmp --output=/tmp/op_example_input_tensor_meta.py
```
Details see `tests/test_op_example_input_tensor_meta.sh`.

## How to generate unittest files?

### module op unittests

```bash
Generates module op unittests from pir programs file and programs example input tensor meta file.
python3 -m athena.module_op_unittests --ir_programs=./example_exec_programs.py --example_inputs=./example_programs_example_input_tensor_meta.py  --output_dir=/tmp
```
Details see `tests/test_module_op_unittests.sh

examples see `tests/test-generate-module-op-unittests.sh`

### sequence unittests

Generates sequence statement unittests from pir programs file and op example input tensor meta file.
```bash
python3.9 -m athena.sequence_unittests --ir_programs=./example_exec_programs.py --op_example_input_tensor_meta=./example_op_example_input_tensor_meta.py --output_dir=/tmp
```
Details see `tests/test_sequence_unittests.sh`.

### primitive op unittests 

```bash
python3.9 -m athena.primitive_op_unittests --ir_programs=./example_exec_programs.py --op_example_input_tensor_meta=./example_op_example_input_tensor_meta.py --output_dir=/tmp
```
Details see `tests/test_primitive_op_unittests.sh`
