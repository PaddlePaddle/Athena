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
flags.DEFINE_boolean("is_dynamic", True, "generate dynamic shape unittests if is_dynamic is True")
flags.DEFINE_string("tmp_dir", "", "temp directory.")


def main(argv):
  WithTempDirectory(Main)


def WithTempDirectory(f):
  if FLAGS.tmp_dir == "":
    tmp_dir = tempfile.mkdtemp()
    return f(tmp_dir)
    shutil.rmtree(tmp_dir)
  else:
    assert os.path.isdir(FLAGS.tmp_dir)
    return f(FLAGS.tmp_dir)


def Main(tmp_dir):
  assert os.path.isdir(FLAGS.output_dir), f"directory {FLAGS.output_dir} not existed."
  shutil.copyfile(FLAGS.ir_programs, f"{tmp_dir}/original_programs.py")
  shutil.copyfile(FLAGS.example_inputs, f"{tmp_dir}/programs_example_input_tensor_meta.py")
  file_prefix = "tmp_op_example_input_"
  for file in glob.glob(f"{tmp_dir}/{file_prefix}*.py"):
    os.remove(file)
  System(f"{sys.executable} -m athena.op_example_input_meta_script --output_file_prefix={file_prefix} --input_dir={tmp_dir} --output_dir={tmp_dir}")
  System(f"{sys.executable} -m athena.op_example_input_meta_result --input_file_prefix={file_prefix} --input_dir={tmp_dir} --output_dir={tmp_dir}")
  System(f"{sys.executable} -m athena._primitive_op_unittests --is_dynamic={FLAGS.is_dynamic} --input_dir={tmp_dir} --output_dir={FLAGS.output_dir}")
  sys.exit(exit_code)

exit_code = 0

def System(cmd):
  print(cmd, file=sys.stderr)
  ret = os.system(cmd)
  global exit_code
  if exit_code != 0:
    return
  if ret == 0:
    return
  exit_code = ret

if __name__ == "__main__":
  app.run(main)
