from athena.util.load_pir_py_classes import GetProgramClasses
from athena.generators.example_tensor_meta_script_generator import (
  ExampleTensorMetaScriptGenerator
)
import sys
from absl import app
from absl import flags
import hashlib

FLAGS = flags.FLAGS

flags.DEFINE_string("output_dir", "./output-dir", "output directory.")

def main(argv):
  for name, unittest in GetOutputUnittests(argv[1]):
    filepath = f"{FLAGS.output_dir}/example-tensor-meta-scripts/tensor_meta_{name}.py"
    WriteToFile(filepath, unittest)
    PrintToTerminal(name, filepath, unittest)


def PrintToTerminal(name, filepath, unittest):
  print("# file-splitter-begin-fusion-op-name: ", name, filepath)
  print(unittest)
  print("# file-splitter--end--fusion-op-name: ", name, filepath)

def WriteToFile(filepath, unittest):
  with open(filepath, "w") as f:
    f.write(unittest)

def GetOutputUnittests(input_file_path):
  for cls in GetProgramClasses(input_file_path):
    ir_program = cls()
    generator = ExampleTensorMetaScriptGenerator(ir_program)
    name = cls.__name__
    unittest = generator.Generate()
    yield name, unittest

if __name__ == "__main__":
  app.run(main)
