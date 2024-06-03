# Athena

## How to generate pir python files?

Set environment variable `FLAGS_logging_pir_py_code_dir` to an existed logging directory before running a paddle program. Once the paddle program finished, there are some pir python files generated under the logging directory.

The orignal pir programs passed into ApplyCinnPass are collected in log file `original_programs.py` in the logging directory

The file named `group_op_programs.py` in the logging directory collects all pir programs after pass `ApplyBuildGroupOpPass`

The file named `fusion_op_programs.py` in the logging directory collects all pir programs after pass `ApplyDivideGroupOpToFusionOpPass`

## How to generate unittest files?

### module op unittests

```bash
python3 -m athena.module_op_unittests --input_dir=/path/to/input/directory --output_dir=/path/to/output/directory
```
Please put `original_programs.py` and `programs_example_input_tensor_meta.py` into `input_dir`

examples see `tests/test-generate-module-op-unittests.sh`

### group op unittests

```bash
python3 -m athena.group_op_unittests /path/to/group_op_programs.py --output_dir=/path/to/output/dir
```
examples see `tests/test-generate-group-op-unittests.sh`

### fusion op unittests

```bash
python3 -m athena.fusion_op_unittests /path/to/fusion_op_programs.py --output_dir=/path/to/output/dir
```
examples see `tests/test-generate-fusion-op-unittests.sh`


### primitive op unittests 

```bash
# Generate op example input tensor meta script
# required file 0: $input_dir/original_programs.py
# required file 1: $input_dir/programs_example_input_tensor_meta.py
# returned file 0: $output_dir/op_example_input_meta_script.py
python3 -m athena.op_example_input_meta_script --input_dir=/path/to/input/dir --output_dir=/path/to/output/dir
# Dump op example input meta results
# required file 0: $input_dir/op_example_input_meta_script.py
# returned file 0: $output_dir/op_example_input_meta_result.py
python3 -m athena.op_example_input_meta_result --input_dir=/path/to/input/dir --output_dir=/path/to/output/dir
# Generate primitive op unittests.
# required file 0: $input_dir/original_programs.py
# required file 1: $input_dir/op_example_input_meta_result.py
# returned file $op: $output_dir/test_$op_*.py for each $op in original_programs.py
python3 -m athena.primitive_op_unittests --input_dir=/path/to/input/dir --output_dir=/path/to/output/dir
```
examples see `tests/test-generate-primitive-op-unittests.sh`

## How to bisearch bug op for a unittest?

You can bisearch on `PADDLE_DEBUG_NUM_ALLOWED_OPS` to find the bug op.

The environment variable `PADDLE_DEBUG_NUM_ALLOWED_OPS` allows you to reduce compute graph
```bash
# e.g.1: reduce compute graph to 0 ops
PADDLE_DEBUG_NUM_ALLOWED_OPS=0 python3.9 ./tmp/test_90a61f91bf628c33b3e398b98f44cf26.py
```
```bash
# e.g.2: reduce compute graph to 1 op
PADDLE_DEBUG_NUM_ALLOWED_OPS=1 python3.9 ./tmp/test_90a61f91bf628c33b3e398b98f44cf26.py
```
```bash
# e.g.3: reduce compute graph to 10000 ops
PADDLE_DEBUG_NUM_ALLOWED_OPS=10000 python3.9 ./tmp/test_90a61f91bf628c33b3e398b98f44cf26.py
```
