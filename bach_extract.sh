extract_fields() {
    local str="$1"
    local start_n="$2"
    local end_from_last="$3"

    IFS='_' read -ra fields <<< "$str"
    local len=${#fields[@]}

    local start_idx=$((start_n - 1))
    local end_idx=$((len - end_from_last))

    if [ $start_idx -gt $end_idx ]; then
        echo ""
        return
    fi

    local result=""
    for ((i=start_idx; i<end_idx; i++)); do
        result+="${fields[i]}_"
    done
    result+="${fields[end_idx]}"

    echo "$result"
}

# cd Athena
i=0
DIR=./jelly/
for dir in $DIR/*
do
    if test -f $dir
    then
        echo $dir is file
    else
        i=$((i+1))
        echo $dir 
        out_dir=$(extract_fields "$dir" 2 3)
        echo $out_dir

        # python3.10 -m athena.op_example_input_tensor_meta --ir_programs=$dir/exec_programs.py --example_inputs=$dir/programs_example_input_tensor_meta.py  --tmp_dir=./test_tmp --output=./test_tmp/op_example_input_tensor_meta.py
        mkdir -p ../GraphNet/paddle_samples/$out_dir
        # python3.10 -m athena.full_graph_unittests  --ir_programs=$dir/exec_programs.py --op_example_input_tensor_meta=./test_tmp/op_example_input_tensor_meta.py --output_dir=../GraphNet/paddle_samples/$out_dir
        # mkdir -p ./test_tmp/$out_dir
        python3.10 -m athena.full_graph_unittests_v2  --ir_programs=$dir/exec_programs.py --example_inputs=$dir/programs_example_input_tensor_meta.py  --output_dir=../GraphNet/paddle_samples/$out_dir
    
    fi
    if [ $i -eq 1 ]; then
        exit
    fi
    sleep 1
done
