pir_py_code_dir=$1
output_dir=$2
python3.9 -m athena.op_example_input_tensor_meta --ir_programs=$pir_py_code_dir/exec_programs.py --example_inputs=$pir_py_code_dir/programs_example_input_tensor_meta.py  --tmp_dir=./tmp --output=./op_example_input_tensor_meta.py
python3.9 -m athena.typical_sequence_unittests --length_slice="2:33" --ir_programs=$pir_py_code_dir/exec_programs.py --op_example_input_tensor_meta=./op_example_input_tensor_meta.py --output_dir=$output_dir
