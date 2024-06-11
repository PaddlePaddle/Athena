import sys
from absl import app
from absl import flags
import os
import glob

FLAGS = flags.FLAGS

flags.DEFINE_string("input_file_prefix", "tmp_op_example_input_", "input file prefix")
flags.DEFINE_string("output_dir", "./output-dir", "output directory.")
flags.DEFINE_string("input_dir", "./input-dir", "input directory.")
flags.DEFINE_integer("max_infer_try_cnt", 10, "max infer try cnt")

def main(argv):
  for f in glob.glob(f"{FLAGS.output_dir}/result_{FLAGS.input_file_prefix}*.py"):
    os.remove(f)
  for pyfile in sorted(glob.glob(f"{FLAGS.input_dir}/{FLAGS.input_file_prefix}*.py")):
    output_file = f"{FLAGS.output_dir}/result_{os.path.basename(pyfile)}"
    System(f"{sys.executable} {pyfile} --max_try_cnt={FLAGS.max_infer_try_cnt} --output_file={output_file}")
  concated_out = f"{FLAGS.output_dir}/op_example_input_meta_result.py"
  System(f"cat {FLAGS.output_dir}/result_{FLAGS.input_file_prefix}*.py 2>/dev/null | tee {concated_out}")

def System(cmd):
  print(cmd, file=sys.stderr)
  os.system(cmd)

if __name__ == "__main__":
  app.run(main)
