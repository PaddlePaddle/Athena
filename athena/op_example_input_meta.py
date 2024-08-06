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
flags.DEFINE_string("output", "./op_example_input_tensor_meta.py", "output file.")
flags.DEFINE_string("tmp_dir", "./tmp", "temp directory.")
flags.DEFINE_integer("bucket_size", 128, "bucket size.")
flags.DEFINE_integer("while_loop_limit", 8, "while loop limit")


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
    assert os.path.isdir(FLAGS.tmp_dir), f"directory {FLAGS.tmp_dir} not existed."
    shutil.copyfile(FLAGS.ir_programs, f"{tmp_dir}/original_programs.py")
    shutil.copyfile(
        FLAGS.example_inputs, f"{tmp_dir}/programs_example_input_tensor_meta.py"
    )
    file_prefix = "tmp_op_example_input_"
    for file in glob.glob(f"{tmp_dir}/{file_prefix}*.py"):
        os.remove(file)
    enable_local_tensor = os.getenv("ATHENA_ENABLE_LOCAL_TENSOR")
    enable_local_tensor = False if enable_local_tensor is None else enable_local_tensor
    System(
        f"ATHENA_ENABLE_LOCAL_TENSOR={enable_local_tensor} {sys.executable} -m athena.op_example_input_meta_script --output_file_prefix={file_prefix} --input_dir={tmp_dir} --output_dir={tmp_dir} --bucket_size={FLAGS.bucket_size}"
    )
    System(
        f"{sys.executable} -m athena.op_example_input_meta_result --input_file_prefix={file_prefix} --input_dir={tmp_dir} --output={FLAGS.output} --output_dir={tmp_dir} --tmp_dir={tmp_dir} --while_loop_limit={FLAGS.while_loop_limit}"
    )
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
