from athena.util.load_pir_py_classes import (
  GetProgramClasses,
  GetClasses
)
from athena.util.example_inputs_meta_getter import ExampleInputsMetaGetter
from athena.generators.op_example_input_meta_script_generator import (
  OpExampleInputMetaScriptGenerator
)
import athena.ir.ir_op as ir_op
import sys
from absl import app
from absl import flags
import hashlib
import os
import glob

FLAGS = flags.FLAGS

flags.DEFINE_string("python", "python3", "python cli")
flags.DEFINE_string("input_file_prefix", "tmp_op_example_input_", "input file prefix")
flags.DEFINE_string("output_dir", "./output-dir", "output directory.")
flags.DEFINE_string("input_dir", "./input-dir", "input directory.")

def main(argv):
  map(os.remove, glob.glob(f"{FLAGS.output_dir}/result_{FLAGS.input_file_prefix}*.py"))
  for pyfile in glob.glob(f"{FLAGS.input_dir}/{FLAGS.input_file_prefix}*.py"):
    output_file = f"{FLAGS.output_dir}/result_{os.path.basename(pyfile)}"
    os.system(f"{FLAGS.python} {pyfile} {output_file} > /dev/null 2>&1")
  concated_out = f"{FLAGS.output_dir}/op_example_input_meta_result.py"
  os.system(f"cat {FLAGS.output_dir}/result_{FLAGS.input_file_prefix}*.py | tee {concated_out}")
  os.system(f"echo")
  os.system(f"echo '# {concated_out}'")

if __name__ == "__main__":
  app.run(main)
