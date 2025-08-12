# set -x
cat /tmp/pir_py_code_dir.txt | while read i;
do
  echo '# typical_sequence program: ' $i
  sh make-typical-sequence-inputs.sh $i /tmp/output/
done
