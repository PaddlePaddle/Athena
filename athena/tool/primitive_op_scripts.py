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
flags.DEFINE_integer("bucket_size", 10, "bucket size")
flags.DEFINE_string("workspace_dir", "", "output directory.")


def main(argv):
    assert os.path.isdir(
        FLAGS.workspace_dir
    ), f"directory {FLAGS.workspace_dir} not existed."
    for f in glob.glob(f"{FLAGS.workspace_dir}/pir_program_*.py"):
        os.remove(f)
    System(f"mkdir -p {FLAGS.workspace_dir}/tmp-dir")
    System(f"mkdir -p {FLAGS.workspace_dir}/output-dir")
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    awk_script = f"{cur_dir}/split-ir-programs.awk"
    System(
        f"awk -v bucket_size={FLAGS.bucket_size} -v dir={FLAGS.workspace_dir} -f {awk_script} {FLAGS.ir_programs}"
    )
    program_filepaths = sorted(
        list(glob.glob(f"{FLAGS.workspace_dir}/pir_program_*.py"))
    )
    for program_filepath in program_filepaths:
        print(
            f"{sys.executable} -m athena.primitive_op_unittests --ir_programs={program_filepath} --example_inputs={FLAGS.example_inputs} --output_dir={FLAGS.workspace_dir}/output-dir --tmp_dir={FLAGS.workspace_dir}/tmp-dir"
        )


def System(cmd):
    os.system(cmd)


if __name__ == "__main__":
    app.run(main)
