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
from athena.util.primitive_op_extractor import PrimitiveOpExtractor
import athena.ir.ir_type as ir_type
import itertools
from collections import defaultdict

FLAGS = flags.FLAGS

flags.DEFINE_string("ir_programs", "", "ir programs file.")
flags.DEFINE_string("example_inputs", "", "example input tensor meta file.")
flags.DEFINE_string("output_dir", "./output-dir", "output directory.")
flags.DEFINE_boolean("enable_early_return", False, "enable early return.")
flags.DEFINE_boolean("enable_local_tensor", True, "enable local tensor name.")


def main(argv):
  os.environ['ATHENA_ENABLE_LOCAL_TENSOR'] = str(FLAGS.enable_local_tensor)
  os.environ['ATHENA_ENABLE_EARLY_RETURN'] = str(FLAGS.enable_early_return)
  original_programs_file = FLAGS.ir_programs
  example_inputs_file = FLAGS.example_inputs
  for file in glob.glob(f"{FLAGS.output_dir}/test_module_op_*.py"):
    os.remove(file)
  seg_counter = defaultdict(lambda: itertools.count())
  for uid, unittest in GetOutputUnittests(original_programs_file, example_inputs_file):
    unique_name = f"{uid}_{next(seg_counter[uid])}"
    filepath = f"{FLAGS.output_dir}/test_module_op_{unique_name}.py"
    WriteToFile(filepath, unittest)
    PrintToTerminal(unique_name, filepath, unittest)

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
  def MakeUnittestGenerator(ir_program):
    return ModuleOpUnittestGenerator(ir_program, example_inputs_meta_getter)
  yield from (
    (GetSha256sum(",".join(op_names))[0:32], unittest)
    for cls in GetProgramClasses(original_programs_file)
    for ir_program in [cls()]
    if not IsBackwardProgram(ir_program)
    if AllInputOutputTypesSupported(ir_program)
    for generator in [MakeUnittestGenerator(ir_program)]
    for op_names in [GetOpNames(ir_program)]
    for unittest in [generator.Generate()]
  )

def GetOpNames(ir_program):
  primitive_op_extractor = PrimitiveOpExtractor()
  return [
    op.name
    for op in primitive_op_extractor.Extract(ir_program)
  ]

def AllInputOutputTypesSupported(ir_program):
  supported_operand_types = (
    ir_type.DenseTensorType,
    ir_type.NullType,
    ir_type.VectorType
  )
  primitive_op_extractor = PrimitiveOpExtractor()
  return all(
    isinstance(in_out_type, supported_operand_types)
    for op in primitive_op_extractor.Extract(ir_program)
    for in_out_type in op.input_types + op.output_types
  )

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
