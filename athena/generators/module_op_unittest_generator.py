from contextlib import contextmanager
from athena.generators.blocks_generator import BlocksGenerator
from athena.ir_converters.paddle_tensor_converter import ConvertToPaddleTensor
from athena.generators.paddle_block_unittest_stmts_generator import (
    PaddleBlockUnittestStmtsGenerator,
)
import athena.ir.ir_type as ir_type
from athena.util.input_tensor_desc import MakeInputTensorDesc
from athena.generators.block_name_generator import BlockNameGenerator
from collections import namedtuple
from jinja2 import Template
import os

BlockDescriptor = namedtuple(
    "BlockDescriptor",
    [
        "is_entry_block",
        "block_name",
        "input_arg_names",
        "input_tensor_descs",
        "stmts",
        "output_arg_names",
        "input_spec_shape_dtypes",
    ],
)

InputSpecDesc = namedtuple(
    "InputSpecDesc",
    [
        "shape",
        "dtype",
    ],
)


class ModuleOpUnittestGenerator:

    def __init__(self, ir_program, example_inputs_meta_getter):
        self.example_inputs_meta_getter = example_inputs_meta_getter
        self.name = type(ir_program).__name__
        self.program_id = int(self.name[len("PirProgram_") :])
        self.blocks_generator = BlocksGenerator(ir_program)
        self.block_name_gen = BlockNameGenerator()
        self.unittest_stmts_gen = PaddleBlockUnittestStmtsGenerator(self.block_name_gen)

    def Generate(self):

        def GetInstanceShape(tensor):
            if tensor.arg_name_as_input is not None:
                tensor_meta = self.example_inputs_meta_getter.Get(
                    program_id=self.program_id,
                    input_tensor=tensor,
                )
                return tensor_meta.shape
            else:
                example_dim = 2
                return [(dim if dim >= 0 else example_dim) for dim in tensor.shape]

        def GetInstanceData(tensor):
            if tensor.arg_name_as_input is None:
                return None
            tensor_meta = self.example_inputs_meta_getter.Get(
                program_id=self.program_id,
                input_tensor=tensor,
            )
            return tensor_meta.data

        def GetInputTensorDesc(input_tensor):
            return MakeInputTensorDesc(
                shape=GetInstanceShape(input_tensor),
                dtype=input_tensor.dtype,
                data=GetInstanceData(input_tensor),
            )

        def MakeBlockDescriptor(block):
            (
                input_local_tensors,
                stmts,
                output_local_tensors,
            ) = self.unittest_stmts_gen.Generate(block)
            input_local_tensors = [
                ConvertToPaddleTensor(t) for t in input_local_tensors
            ]
            input_spec_shape_dtypes = [
                InputSpecDesc(
                    shape=[(dim if dim >= 0 else None) for dim in input_tensor.shape],
                    dtype=input_tensor.dtype,
                )
                for input_tensor in input_local_tensors
            ]
            return BlockDescriptor(
                is_entry_block=block.is_entry_block,
                block_name=self.block_name_gen.Generate(
                    block.owner_op, block.region_idx, block.block_idx
                ),
                input_arg_names=[tensor.name for tensor in input_local_tensors],
                input_tensor_descs=[GetInputTensorDesc(t) for t in input_local_tensors],
                stmts=stmts,
                output_arg_names=[tensor.name for tensor in output_local_tensors],
                input_spec_shape_dtypes=input_spec_shape_dtypes,
            )

        blocks = [
            MakeBlockDescriptor(block) for block in self.blocks_generator.Generate()
        ]
        return self._RenderTemplate(blocks=blocks)

    def _RenderTemplate(self, blocks):
        template = self._GetTemplate("template_module_op_unittests.jinja")
        return template.render(
            blocks=blocks,
            enable_early_return=self.EnableEarlyReturn(),
            tensor_name_converter=lambda x: x,
        )

    def EnableEarlyReturn(self):
        return os.getenv("ATHENA_ENABLE_EARLY_RETURN") not in {
            "0",
            "false",
            "False",
            "off",
            "OFF",
        }

    def _GetTemplate(self, template_name):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(f"{dir_path}/{template_name}", "r") as f:
            return Template(f.read())
