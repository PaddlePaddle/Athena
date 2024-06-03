BEGIN {
  cls_no = 0
  output_file="/dev/null"
}

/class PirProgram_/ {
  cls_no += 1
  output_file = dir "/pir_program_" sprintf("%08d", cls_no) ".py"
}

{
  print $0 > output_file
}
