import os
from jinja2 import Template
from collections import namedtuple
from athena.generators.paddle_func_body_generator import PaddleFuncBodyGenerator
import athena.ir.ir_symbol as ir_symbol
from athena.util.dim_exprs_extractor import DimExprsExtractor
from athena.util.dim_instance_generator import DimInstanceGenerator
from athena.util.input_tensor_desc import MakeInputTensorDesc


class PaddleUnittestGenerator:

    def __init__(self, unittest_class_name, func, body_generator=None):
        self.unittest_class_name = unittest_class_name
        self.func = func
        self.body_generator = body_generator
        if self.body_generator is None:
            self.body_generator = PaddleFuncBodyGenerator(func)

    def Generate(self, free_vars, args):
        all_dim_exprs = DimExprsExtractor().Extract(self.func, free_vars, args)
        dim_instance_generator = DimInstanceGenerator(all_dim_exprs)
        (
            input_tensors,
            body_code_stmts,
            output_tensors,
        ) = self.body_generator.Generate(free_vars, args)
        return RenderTemplate(
            unittest_class_name=self.unittest_class_name,
            input_tensors=input_tensors,
            body_code_stmts=body_code_stmts,
            output_tensors=output_tensors,
            dim_instance_generator=dim_instance_generator,
        )


InputSpecDesc = namedtuple(
    "InputSpecDesc",
    [
        "shape",
        "dtype",
    ],
)


def RenderTemplate(
    unittest_class_name,
    input_tensors: list,
    body_code_stmts: list,
    output_tensors: list,
    dim_instance_generator: DimInstanceGenerator,
):
    template = _GetTemplate("template_paddle_unittest.jinja")
    input_arg_names = [input_tensor.name for input_tensor in input_tensors]

    def GetShapeInstanceFromDimExprs(tensor):
        if type(tensor.dim_exprs) is not ir_symbol.TensorShapeOrDataDimExprs:
            return []
        return [
            dim_instance_generator.GetDimInstance(dim_expr)
            for dim_expr in tensor.dim_exprs.shape
        ]

    def GetDataInstanceFromDimExprs(tensor):
        if type(tensor.dim_exprs) is not ir_symbol.TensorShapeOrDataDimExprs:
            return None
        if tensor.dim_exprs.data is None:
            return None
        return [
            dim_instance_generator.GetDimInstance(dim_expr)
            for dim_expr in tensor.dim_exprs.data
        ]

    input_tensor_descs = [
        MakeInputTensorDesc(
            shape=GetShapeInstanceFromDimExprs(input_tensor),
            dtype=input_tensor.dtype,
            data=GetDataInstanceFromDimExprs(input_tensor),
        )
        for input_tensor in input_tensors
    ]
    input_spec_shape_dtypes = [
        InputSpecDesc(
            shape=[(dim if dim >= 0 else None) for dim in input_tensor.shape],
            dtype=input_tensor.dtype,
        )
        for input_tensor in input_tensors
    ]
    return template.render(
        stmts=body_code_stmts,
        unittest_class_name=unittest_class_name,
        input_arg_names=input_arg_names,
        output_arg_names=[tensor.name for tensor in output_tensors],
        input_tensor_descs=input_tensor_descs,
        input_spec_shape_dtypes=input_spec_shape_dtypes,
    )


def _GetTemplate(template_name):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(f"{dir_path}/{template_name}", "r") as f:
        return Template(f.read())
