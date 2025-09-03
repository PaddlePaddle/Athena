from athena.generators.blocks_generator import BlocksGenerator
from athena.ir_converters.paddle_tensor_converter import ConvertToPaddleTensor
from athena.generators.paddle_block_unittest_stmts_generator import (
    PaddleBlockUnittestStmtsGenerator,
)
from athena.util.input_tensor_desc import MakeInputTensorDesc
from athena.generators.block_name_generator import BlockNameGenerator
from collections import namedtuple
import os
import jinja2
import numpy as np

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
        "get_unused_tensor_name",
    ],
)

InputSpecDesc = namedtuple(
    "InputSpecDesc",
    [
        "shape",
        "dtype",
    ],
)


class ModuleOpUnittestForGraphnetGenerator:
    def __init__(
        self, ir_program, example_inputs_meta_getter, max_depth_output_only=False
    ):
        self.example_inputs_meta_getter = example_inputs_meta_getter
        self.max_depth_output_only = max_depth_output_only
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
                return None, None, None, None, None
            tensor_meta = self.example_inputs_meta_getter.Get(
                program_id=self.program_id,
                input_tensor=tensor,
            )
            data, max_value, min_value = tensor_meta.data, None, None
            mean = getattr(tensor_meta, "mean", None)
            std = getattr(tensor_meta, "std", None)

            if data is not None and isinstance(data, list) and len(data) > 0:
                array = np.array(data)
                max_value = np.max(array)
                min_value = np.min(array)
                if len(data) > 64:
                    # Don't save all the values for large array.
                    data = None
            else:
                max_value = getattr(tensor_meta, "max", None)
                min_value = getattr(tensor_meta, "min", None)

            return data, max_value, min_value, mean, std

        def GetInputTensorDesc(input_tensor):
            data, max_value, min_value, mean, std = GetInstanceData(input_tensor)
            return MakeInputTensorDesc(
                shape=GetInstanceShape(input_tensor),
                dtype=input_tensor.dtype,
                data=data,
                max_value=max_value,
                min_value=min_value,
                mean=mean,
                std=std,
            )

        def MakeBlockDescriptor(block):
            (
                input_local_tensors,
                stmts,
                output_local_tensors,
            ) = self.unittest_stmts_gen.Generate(block, self.max_depth_output_only)
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

            def GetUnusedTensorName(stmt):
                return sorted(
                    list(
                        set(stmt.tensors_used_by_me_and_downstream)
                        - set(stmt.tensors_used_by_downstream)
                    )
                )

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
                get_unused_tensor_name=GetUnusedTensorName,
            )

        blocks = [
            MakeBlockDescriptor(block) for block in self.blocks_generator.Generate()
        ]
        return self._RenderTemplate(blocks=blocks)

    def _RenderTemplate(self, blocks):
        template = jinja_env.get_template(
            "template_module_op_unittest_for_graphnet.jinja"
        )
        return template.render(
            blocks=blocks,
            tensor_name_converter=lambda x: x,
        )


jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(
        searchpath=os.path.dirname(os.path.realpath(__file__))
    )
)
jinja_env.filters["py_map"] = lambda values, f: map(f, values)
