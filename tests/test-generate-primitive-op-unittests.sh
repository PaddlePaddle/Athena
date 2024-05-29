original_programs=example-original-programs.py
output_dir=./primitive-op-tmp
python3 -m athena.example_tensor_meta_scripts $original_programs --output_dir=$output_dir
python3 -m athena.example_tensor_meta_results $original_programs --output_dir=$output_dir
python3 -m athena.primitive_op_unittests $original_programs --output_dir=$output_dir
