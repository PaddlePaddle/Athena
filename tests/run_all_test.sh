#!/bin/bash

failed_scripts=()
whitelist=(
    # "tests/test-generate-fusion-op-unittests.sh"
)

for script in tests/test-generate*.sh; do
    if [[ " ${whitelist[@]} " =~ " ${script} " ]]; then
        output=$(bash "$script" 2>&1)
        status=$?
        if [ $status -ne 0 ]; then
            failed_scripts+=("$script: $output")
        fi
    else
        echo "Skip $script"
    fi
done

if [ ${#failed_scripts[@]} -gt 0 ]; then
    echo "The following tests failed: "
    for script in "${failed_scripts[@]}"; do
        echo "$script"
    done
    echo "Failed!"
    exit 1
else
    echo "All tests run successfully!"
fi
