import sys
from absl import app
from absl import flags
import os
import glob
import tempfile
import shutil

FLAGS = flags.FLAGS
flags.DEFINE_string("ir_programs", "", "ir programs file.")
flags.DEFINE_string("example_inputs", "", "example input tensor meta file.")
flags.DEFINE_string("output_dir", "", "output directory.")

def main(argv):
  assert os.path.isdir(FLAGS.output_dir), f"file {FLAGS.output_dir} not existed."
  tmp_dir = tempfile.mkdtemp()
  shutil.copyfile(FLAGS.ir_programs, f"{tmp_dir}/original_programs.py")
  shutil.copyfile(FLAGS.example_inputs, f"{tmp_dir}/programs_example_input_tensor_meta.py")
  file_prefix = "tmp_op_example_input_"
  os.system(f"{sys.executable} -m athena.op_example_input_meta_script --output_file_prefix={file_prefix} --input_dir={tmp_dir} --output_dir={tmp_dir}")
  os.system(f"{sys.executable} -m athena.op_example_input_meta_result --input_file_prefix={file_prefix} --input_dir={tmp_dir} --output_dir={tmp_dir}")
  os.system(f"{sys.executable} -m athena._primitive_op_unittests --input_dir={tmp_dir} --output_dir={FLAGS.output_dir}")
  shutil.rmtree(tmp_dir)

if __name__ == "__main__":
  app.run(main)