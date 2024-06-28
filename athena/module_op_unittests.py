from athena.util.load_pir_py_classes import (
  GetProgramClasses,
  GetClasses
)
from athena.util.example_inputs_meta_getter import ExampleInputsMetaGetter
from athena.generators.module_op_unittest_generator import (
  ModuleOpUnittestGenerator
)
import athena.ir.ir_op as ir_op
import sys
from absl import app
from absl import flags
import hashlib
import glob as glob
import os

FLAGS = flags.FLAGS

flags.DEFINE_string("ir_programs", "", "ir programs file.")
flags.DEFINE_string("example_inputs", "", "example input tensor meta file.")
flags.DEFINE_string("output_dir", "./output-dir", "output directory.")

def main(argv):
  original_programs_file = FLAGS.ir_programs
  example_inputs_file = FLAGS.example_inputs
  for file in glob.glob(f"{FLAGS.output_dir}/test_module_op_*.py"):
    os.remove(file)
  for name, unittest in GetOutputUnittests(original_programs_file, example_inputs_file):
    sha256sum = GetSha256sum(unittest)
    filepath = f"{FLAGS.output_dir}/test_module_op_{sha256sum[0:32]}.py"
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

def IsBackwardProgram(ir_program):
  for name, op in vars(ir_program).items():
    if not isinstance(op, ir_op.Op):
      continue
    if op.name != "builtin.module":
      continue
    keyword_arg_names = op.block_keyword_arg_names[0][0]
    if len(keyword_arg_names) > 0:
      return True
  return False

def GetOutputUnittests(original_programs_file, example_inputs_file):
  example_inputs_meta_getter = MakeExampleInputsMetaGetter(example_inputs_file)
  for cls in GetProgramClasses(original_programs_file):
    ir_program = cls()
    if IsBackwardProgram(ir_program):
      # Ignore backward programs
      continue
    generator = ModuleOpUnittestGenerator(ir_program, example_inputs_meta_getter)
    name, unittest = generator.Generate()
    yield name, unittest

def MakeExampleInputsMetaGetter(example_inputs_file):
  classes = [
    cls
    for name, cls in GetClasses(example_inputs_file)
    if name.startswith('PirProgram_example_input_tensor_meta_')
  ]
  return ExampleInputsMetaGetter(
    records=classes
  )

if __name__ == "__main__":
  app.run(main)
