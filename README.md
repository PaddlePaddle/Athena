# Athena

## How to generate ir programs files and program example input tensor meta files?

Set environment variable `FLAGS_logging_pir_py_code_dir` to an existed logging directory before running a paddle program. Once the paddle program finished, under the logging directory, there are two generated pir python files: `exec_programs.py` and `programs_example_input_tensor_meta.py`.

Dumped example python files see `tests/example_exec_programs.py` and `tests/example_programs_example_input_tensor_meta.py`.

## How to prepare op example input tensor meta files?
Op example input tensor meta file are generated from pir programs file and program example input tensor meta file.
```bash
python3.9 -m athena.op_example_input_tensor_meta --ir_programs=./example_exec_programs.py --example_inputs=./example_programs_example_input_tensor_meta.py  --tmp_dir=/tmp --output=/tmp/op_example_input_tensor_meta.py
```
Details see `tests/test_op_example_input_tensor_meta.sh`.

## How to generate unittest files?

### Module op unittests
Module op unittests are generated from pir programs file and program example input tensor meta file.
```bash
python3 -m athena.module_op_unittests --ir_programs=./example_exec_programs.py --example_inputs=./example_programs_example_input_tensor_meta.py  --output_dir=/tmp
```
Details see `tests/test_module_op_unittests.sh

examples see `tests/test-generate-module-op-unittests.sh`.

### Sequence unittests

Sequence statement unittests are generated from pir programs file and op example input tensor meta file.
```bash
python3.9 -m athena.sequence_unittests --ir_programs=./example_exec_programs.py --op_example_input_tensor_meta=./example_op_example_input_tensor_meta.py --output_dir=/tmp
```
Details see `tests/test_sequence_unittests.sh`.

### Typical sequence unittests

Typical sequence statement unittests are generated from pir programs file and op example input tensor meta file.
```bash
python3.9 -m athena.typical_sequence_unittests --length_slice="16:33" --ir_programs=./example_exec_programs.py --op_example_input_tensor_meta=./example_op_example_input_tensor_meta.py --output_dir=/tmp
```
Details see `tests/test_typical_sequence_unittests.sh`.

### Primitive op unittests 
Primitive op unittests are generated from pir programs file and op example input tensor meta file.
```bash
python3.9 -m athena.primitive_op_unittests --ir_programs=./example_exec_programs.py --op_example_input_tensor_meta=./example_op_example_input_tensor_meta.py --output_dir=/tmp
```
Details see `tests/test_primitive_op_unittests.sh`.
