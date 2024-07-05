from athena.util.load_pir_py_classes import (
  GetProgramClasses,
  GetClasses
)
from athena.util.op_example_inputs_meta_getter import (
  MakeOpExampleInputsMetaGetter,
)
from athena.util.primitive_op_extractor import PrimitiveOpExtractor
from athena.generators.constraint_unittests_generator import (
  ConstraintUnittestsGenerator
)
from athena.util.ir_program_util import (
  IsBackwardProgram,
  GetProgramId
)
import athena.ir.ir_op as ir_op
import athena.ir.ir_type as ir_type
import sys
from absl import app
from absl import flags
import hashlib
from itertools import groupby

FLAGS = flags.FLAGS

flags.DEFINE_string("output_dir", "./output-dir", "output directory.")
flags.DEFINE_string("input_dir", "./input-dir", "input directory.")

def main(argv):
  original_programs_file = f"{FLAGS.input_dir}/original_programs.py"
  op_example_inputs_file = f"{FLAGS.input_dir}/op_example_input_meta_result.py"
  unittests = GetOutputUnittests(original_programs_file, op_example_inputs_file)
  for name, unittest in unittests:
    filepath = f"{FLAGS.output_dir}/test_constraint_{name}.py"
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

def GetOutputUnittests(original_programs_file, op_example_inputs_file):
  op_example_inputs_meta_getter = MakeOpExampleInputsMetaGetter(
    GetClasses(op_example_inputs_file)
  )
  ir_programs = [
    ir_program
    for cls in GetProgramClasses(original_programs_file)
    for ir_program in [cls()]
    if not IsBackwardProgram(ir_program)
  ]
  primitive_op_extractor = PrimitiveOpExtractor()
  ops = [
    (program_id, op)
    for ir_program in ir_programs
    for program_id in [GetProgramId(ir_program)]
    for op in primitive_op_extractor.Extract(ir_program)
  ]
  def GetPyVarName(uid_and_op):
    return uid_and_op[1].GetPyVarName()
  grouped_ops = [
    (name, list(ops))
    for name, ops in groupby(sorted(ops, key=GetPyVarName), key=GetPyVarName)
  ]
  valid_operand_types = (ir_type.DenseTensorType, ir_type.NullType, ir_type.VectorType)
  for name, uid_and_ops in grouped_ops:
    generator = ConstraintUnittestsGenerator(
      op_example_inputs_meta_getter=op_example_inputs_meta_getter,
    )
    uid_and_ops = [
      (program_id, op)
      for program_id, op in uid_and_ops
      if op_example_inputs_meta_getter.HasAllInputs(
        program_id, op.op_id, num_inputs=len(op.input_types)
      )
      if all(
        isinstance(input_type, valid_operand_types)
        for input_type in op.input_types
      )
      if all(
        isinstance(output_type, valid_operand_types)
        for output_type in op.output_types
      )
    ]
    if len(uid_and_ops) == 0:
      continue
    unittest = generator.Generate(uid_and_ops)
    yield name, unittest

if __name__ == "__main__":
  app.run(main)
