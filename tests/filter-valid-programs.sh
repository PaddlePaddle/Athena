tmp_dir=./tmp-dir-filter-valid-programs
awk -v dir=$tmp_dir -f ./filter.awk $1
find $tmp_dir -name "*.py" | sort | while read script; do
python3.9 $script && cat $script
done
#rm $tmp_dir/* -rf
