BEGIN {
  cls_no = 0
  bucket_id = 0
  output_file="/dev/null"
}

/class PirProgram_/ {
  cls_no += 1
  bucket_id = int(cls_no / bucket_size)
  output_file = dir "/pir_program_" sprintf("%08d", bucket_id) ".py"
}

{
  print $0 > output_file
}
