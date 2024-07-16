from contextlib import contextmanager
from athena.generators.blocks_generator import BlocksGenerator
from athena.ir_converters.paddle_tensor_converter import ConvertToPaddleTensor
from athena.generators.paddle_block_unittest_stmts_generator import (
  PaddleBlockUnittestStmtsGenerator
)
import athena.ir.ir_type as ir_type
from athena.util.input_tensor_desc import MakeInputTensorDesc
from athena.generators.block_name_generator import BlockNameGenerator
from collections import namedtuple
from jinja2 import Template
import os

BlockDescriptor = namedtuple('BlockDescriptor', [
  'is_entry_block',
  'block_name',
  'input_arg_names',
  'input_tensor_descs',
  'stmts',
  'output_arg_names',
  'input_spec_shape_dtypes',
  'get_unused_vars',
])

ProgramBlocksDescriptor = namedtuple('ProgramDescriptor', [
  'program_id',
  'blocks'
])

InputSpecDesc = namedtuple("InputSpecDesc", [
  "shape",
  "dtype",
])

class ProgramBlocksDescriptorGenerator:
  def __init__(self, ir_program, example_inputs_meta_getter):
    self.example_inputs_meta_getter = example_inputs_meta_getter
    self.name = type(ir_program).__name__
    self.program_id = int(self.name[len('PirProgram_'):])
    self.blocks_generator = BlocksGenerator(ir_program)
    self.block_name_gen = BlockNameGenerator()
    self.unittest_stmts_gen = PaddleBlockUnittestStmtsGenerator(self.block_name_gen)

  def Generate(self):

    def GetShapeInstance(tensor):
      if tensor.arg_name_as_input is not None:
        tensor_meta = self.example_inputs_meta_getter.Get(
          program_id=self.program_id,
          input_tensor=tensor,
        )
        return tensor_meta.shape
      else:
        example_dim = 2
        return [
          (dim if dim >= 0 else example_dim)
          for dim in tensor.shape
        ]

    def GetDataInstance(tensor):
      if tensor.arg_name_as_input is None:
        return None
      tensor_meta = self.example_inputs_meta_getter.Get(
        program_id=self.program_id,
        input_tensor=tensor,
      )
      return tensor_meta.data

    def GetInputTensorDesc(input_tensor):
      return MakeInputTensorDesc(
        shape=GetShapeInstance(input_tensor),
        dtype=input_tensor.dtype,
        data=GetDataInstance(input_tensor),
      )
        
    def MakeBlockDescriptor(block):
      (
        input_local_tensors,
        stmts,
        output_local_tensors,
      ) = self.unittest_stmts_gen.Generate(block)
      input_local_tensors = [ConvertToPaddleTensor(t) for t in input_local_tensors]
      input_spec_shape_dtypes = [
        InputSpecDesc(
          shape=[(dim if dim >= 0 else None) for dim in input_tensor.shape],
          dtype=input_tensor.dtype
        )
        for input_tensor in input_local_tensors
      ]
      return BlockDescriptor(
        is_entry_block=block.is_entry_block,
        block_name=self.block_name_gen.Generate(
          block.owner_op,
          block.region_idx,
          block.block_idx
        ),
        input_arg_names=[tensor.name for tensor in input_local_tensors],
        input_tensor_descs=[GetInputTensorDesc(t) for t in input_local_tensors],
        stmts=stmts,
        output_arg_names=[tensor.name for tensor in output_local_tensors],
        input_spec_shape_dtypes=input_spec_shape_dtypes,
        get_unused_vars=self.MakeGetterUnusedVars(stmts),
      )
    blocks = [
      MakeBlockDescriptor(block)
      for block in self.blocks_generator.Generate()
    ]
    return ProgramBlocksDescriptor(
      program_id=self.program_id,
      blocks=blocks
    )

  def MakeGetterUnusedVars(self, stmts):
    def GetUsedTensor(stmt_idx):
      return stmts[stmt_idx].tensors_used_by_me_and_downstream
    def func(stmt_idx):
      if stmt_idx + 1 >= len(stmts):
        return []  
      return list(set(GetUsedTensor(stmt_idx)) - set(GetUsedTensor(stmt_idx + 1)))
    return func

class OpExampleInputMetaScriptGenerator:

  def __init__(self, ir_programs, example_inputs_meta_getter):
    self.ir_programs = ir_programs
    self.name = "_".join(type(ir_program).__name__ for ir_program in ir_programs)
    self.example_inputs_meta_getter = example_inputs_meta_getter

  def Generate(self):
    def MakeProgramBlocksDescriptor(ir_program):
      generator = ProgramBlocksDescriptorGenerator(
        ir_program,
        self.example_inputs_meta_getter
      )
      return generator.Generate()
    programs = [
      MakeProgramBlocksDescriptor(ir_program)
      for ir_program in self.ir_programs
    ]
    return self.name, self._RenderTemplate(programs=programs)

  def _RenderTemplate(self, programs):
    template = self._GetTemplate("template_op_example_input_meta_script.py")
    return template.render(programs=programs)

  def _GetTemplate(self, template_name):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(f"{dir_path}/{template_name}", "r") as f:
      return Template(f.read())
