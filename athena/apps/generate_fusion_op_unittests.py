from athena.generators.fusion_op_unittest_generator import (
  FusionOpUnittestGenerator
)
from athena.apps import load_pir_py_classes
import sys
from absl import app
from absl import flags
import hashlib

FLAGS = flags.FLAGS

flags.DEFINE_string("output_dir", "./output-dir", "output directory.")

def main(argv):
  for name, unittest in GetOutputUnittests(argv[1]):
    sha256sum = GetSha256sum(unittest)
    filepath = f"{FLAGS.output_dir}/test_{sha256sum[0:32]}.py"
    WriteToFile(filepath, unittest)
    PrintToTerminal(name, filepath, unittest)

def GetSha256sum(content):
  m = hashlib.sha256()
  m.update(content.encode())
  return m.hexdigest()

def PrintToTerminal(name, filepath, unittest):
  print("# file-splitter-begin-fusion-op-name: ", name, filepath)
  print(unittest)
  print("# file-splitter--end--fusion-op-name: ", name, filepath)

def WriteToFile(filepath, unittest):
  with open(filepath, "w") as f:
    f.write(unittest)

def GetOutputUnittests(input_file_path):
  for cls in load_pir_py_classes.GetProgramClasses(input_file_path):
    ir_program = cls()
    generator = FusionOpUnittestGenerator()
    op_name2unittest = generator.Generate(ir_program)
    yield from op_name2unittest.items()

if __name__ == "__main__":
  app.run(main)