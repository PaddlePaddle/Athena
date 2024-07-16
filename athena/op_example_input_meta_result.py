import sys
from absl import app
from absl import flags
import os
import glob

FLAGS = flags.FLAGS

flags.DEFINE_string("input_file_prefix", "tmp_op_example_input_", "input file prefix")
flags.DEFINE_string("output_dir", "./output-dir", "output directory.")
flags.DEFINE_string("input_dir", "./input-dir", "input directory.")
flags.DEFINE_string("tmp_dir", "./tmp-dir", "tmp directory.")
flags.DEFINE_integer("max_infer_try_cnt", 10, "max infer try cnt")
flags.DEFINE_integer("while_loop_limit", 128, "while loop limit")

def GetFailedCmdFilePath():
  return f"{FLAGS.tmp_dir}/failed_commands.sh"

def main(argv):
  os.remove(GetFailedCmdFilePath()) if os.path.exists(GetFailedCmdFilePath()) else None
  for f in glob.glob(f"{FLAGS.output_dir}/result_{FLAGS.input_file_prefix}*.py"):
    os.remove(f)
  for pyfile in sorted(glob.glob(f"{FLAGS.input_dir}/{FLAGS.input_file_prefix}*.py")):
    output_file = f"{FLAGS.output_dir}/result_{os.path.basename(pyfile)}"
    System(f"ATHENA_WHILE_LOOP_LIMIT={FLAGS.while_loop_limit} {sys.executable} {pyfile} --max_try_cnt={FLAGS.max_infer_try_cnt} --output_file={output_file}")
  concated_out = f"{FLAGS.output_dir}/op_example_input_meta_result.py"
  System(f"cat {FLAGS.output_dir}/result_{FLAGS.input_file_prefix}*.py 2>/dev/null | tee {concated_out}")

def System(cmd):
  print(cmd, file=sys.stderr)
  if os.system(cmd) != 0:
    with open(GetFailedCmdFilePath(), 'a') as f:
      f.write(f"{cmd}\n")

if __name__ == "__main__":
  app.run(main)
