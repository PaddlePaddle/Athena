from athena.util.load_pir_py_classes import (
  GetProgramClasses,
  GetClasses
)
from athena.util.example_inputs_meta_getter import ExampleInputsMetaGetter
from athena.generators.op_example_input_meta_script_generator import (
  OpExampleInputMetaScriptGenerator
)
from athena.util.input_output_tensors_extractor import InputOutputTensorsExtractor
import athena.ir.ir_op as ir_op
import sys
from absl import app
from absl import flags
import hashlib
import os
import glob
import itertools

FLAGS = flags.FLAGS

flags.DEFINE_string("output_dir", "./output-dir", "output directory.")
flags.DEFINE_string("input_dir", "./input-dir", "input directory.")
flags.DEFINE_integer("bucket_size", 128, "bucket size.")
flags.DEFINE_string("output_file_prefix", "tmp_op_example_input_", "input file prefix")

def main(argv):
  for f in glob.glob(f"{FLAGS.output_dir}/{FLAGS.output_file_prefix}*.py"):
    os.remove(f)
  original_programs_file = f"{FLAGS.input_dir}/original_programs.py"
  example_inputs_file = f"{FLAGS.input_dir}/programs_example_input_tensor_meta.py"
  for name, unittest in GetOutputUnittests(original_programs_file, example_inputs_file):
    sha256sum = GetSha256sum(unittest)
    filepath = f"{FLAGS.output_dir}/{FLAGS.output_file_prefix}{sha256sum[0:32]}.py"
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

def GetModuleBlockFunc(ir_program):
  module_block_func = None
  def ExtractOpInfo(op, blocks=None):
    assert op.name == "builtin.module"
    assert len(blocks) == 1
    assert len(blocks[0]) == 1
    assert len(blocks[0][0]) == 1
    nonlocal module_block_func
    module_block_func = blocks[0][0][0]
  ir_program(ExtractOpInfo)
  assert module_block_func is not None
  return module_block_func

def IsProgramEmpty(ir_program):
  module_block_func = GetModuleBlockFunc(ir_program)
  op_count = 0
  def IncOpCount(op, *args, **kwargs):
    nonlocal op_count
    op_count += 1
    return op.GetResults()
  module_block_func(IncOpCount)()
  return op_count == 0

def ExtractInputTensors(ir_program):
  module_block_func = GetModuleBlockFunc(ir_program)
  extractor = InputOutputTensorsExtractor(module_block_func)
  input_tensors, _ = extractor.Extract(free_vars=[], args=[])
  return input_tensors

def HasExampleInputs(ir_program, example_inputs_meta_getter):
  input_tensors = ExtractInputTensors(ir_program)
  return example_inputs_meta_getter.HasAllInputExamples(
    program_id=int(type(ir_program).__name__[len('PirProgram_'):]),
    input_tensors=input_tensors
  )

def GetOutputUnittests(original_programs_file, example_inputs_file):
  example_inputs_meta_getter = MakeExampleInputsMetaGetter(example_inputs_file)
  classes = GetProgramClasses(original_programs_file)
  ir_programs = (
    ir_program
    for cls in classes
    for ir_program in [cls()]
    if not IsBackwardProgram(ir_program)
    if not IsProgramEmpty(ir_program)
    if HasExampleInputs(ir_program, example_inputs_meta_getter)
  )
  def GetBucket(elem):
    i, _ = elem
    return i // FLAGS.bucket_size
  ir_program_groups = itertools.groupby(enumerate(ir_programs), GetBucket)
  for _, ir_program_group in ir_program_groups:
    ir_program_group = [x for _, x in ir_program_group]
    generator = OpExampleInputMetaScriptGenerator(
      ir_program_group,
      example_inputs_meta_getter
    )
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
