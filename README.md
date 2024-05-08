# Athena

# How to generate pir python files?

Set environment variable `FLAGS_logging_pir_py_code_dir` to an existed logging directory before running a paddle program. Once the paddle program finished, there are some pir python files generated under the logging directory.

The file named `fusion_op_programs.py` in the logging directory collects all pir programs after pass `ApplyDivideGroupOpToFusionOpPass`, which is more important than other files usually.

## How to generate unittest files?

cd to tests directory
```bash
cd tests
```

run demo case
```bash
sh test-generate-fusion-op-unittests.sh
```

You will get unittest files in ./tmp directory
```
λ ~/workspace/Athena ls tests/tmp/
test_18dff13414273d546da42f50b425db63.py  test_d273ad8cf9c5c9c0ba433db9058c4193.py
test_90a61f91bf628c33b3e398b98f44cf26.py  test_d824ead229f44cc871666a9eda1d1881.py
test_91ef0107e1a5c12d9aff298098ccec28.py
```

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
