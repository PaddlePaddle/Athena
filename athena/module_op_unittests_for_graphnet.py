from athena.util.load_pir_py_classes import GetProgramClasses, GetClasses
from athena.util.example_inputs_meta_getter import (
    MakeExampleInputsMetaGetter,
)
from athena.generators.module_op_unittest_for_graphnet_generator import (
    ModuleOpUnittestForGraphnetGenerator,
)
import athena.ir.ir_op as ir_op
from absl import app
from absl import flags
import hashlib
import glob as glob
import os
from athena.util.primitive_op_extractor import PrimitiveOpExtractor
import athena.ir.ir_type as ir_type
import itertools
from collections import defaultdict
import json
from dataclasses import dataclass
from typing import Dict

FLAGS = flags.FLAGS

flags.DEFINE_string("model_name", "", "model name.")
flags.DEFINE_string("ir_programs", "", "ir programs file.")
flags.DEFINE_string("example_inputs", "", "example input tensor meta file.")
flags.DEFINE_string("output_dir", "./output-dir", "output directory.")
flags.DEFINE_boolean(
    "eval_mode",
    False,
    "Generate unittest for eval, which only keep output tensors with maximum depth (longest chain).",
)


@dataclass
class GraphnetSample:
    unique_name: str
    metadata: Dict[str, str]
    input_meta: str
    weight_meta: str
    model: str


def generate_samples(model_name, ir_programs, example_inputs, eval_mode):
    metadata = {
        "framework": "paddle",
        "model_name": model_name,
        "num_devices_required": 1,
        "num_nodes_required": 1,
    }

    graphnet_sample_results = []
    seg_counter = defaultdict(lambda: itertools.count())
    for module_id, (num_unittests, uid, unittest) in enumerate(
        GetOutputUnittests(ir_programs, example_inputs, eval_mode)
    ):
        unique_name = f"{uid}_{next(seg_counter[uid])}"
        input_meta, weight_meta, model = unittest.split("# --- seperate line ----\n")
        sample = GraphnetSample(
            unique_name=unique_name,
            metadata=metadata,
            input_meta=input_meta.strip("\n\n\n") + "\n",
            weight_meta=weight_meta.rstrip("\n\n\n") + "\n",
            model=model,
        )
        graphnet_sample_results.append(sample)
        print(f"Genrating {model_name}/subgraph_{module_id}:")
        # PrintToTerminal(unique_name, unittest)
    return graphnet_sample_results


def main(argv):
    graphnet_sample_results = generate_samples(
        model_name=FLAGS.model_name,
        ir_programs=FLAGS.ir_programs,
        example_inputs=FLAGS.example_inputs,
        eval_mode=FLAGS.eval_mode,
    )
    num_subgraphs = len(graphnet_sample_results)
    for i, sample in enumerate(graphnet_sample_results):
        if num_subgraphs == 1:
            sub_dir_path = f"{FLAGS.output_dir}"
        else:
            sub_dir_path = os.path.join(f"{FLAGS.output_dir}", f"subgraph_{i}")

        for file in glob.glob(f"{sub_dir_path}/*"):
            if os.path.isfile(file):
                os.remove(file)
        if not os.path.exists(sub_dir_path):
            os.makedirs(sub_dir_path)
        WriteToFile(f"{sub_dir_path}/model.py", sample.model)
        WriteToFile(f"{sub_dir_path}/weight_meta.py", sample.weight_meta)
        WriteToFile(f"{sub_dir_path}/input_meta.py", sample.input_meta)
        with open(os.path.join(sub_dir_path, "graph_net.json"), "w") as f:
            json.dump(sample.metadata, f, indent=4)


def GetSha256sum(content):
    m = hashlib.sha256()
    m.update(content.encode())
    return m.hexdigest()


def PrintToTerminal(name, unittest):
    print("# file-splitter-begin-fusion-op-name: ", name)
    print(unittest)
    print("# file-splitter--end--fusion-op-name: ", name)


def WriteToFile(filepath, unittest):
    print(f"Write to {filepath}")
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


def GetOutputUnittests(original_programs_file, example_inputs_file, eval_mode):
    example_inputs_meta_getter = MakeExampleInputsMetaGetter(
        GetClasses(example_inputs_file)
    )

    def MakeUnittestGenerator(ir_program):
        return ModuleOpUnittestForGraphnetGenerator(
            ir_program,
            example_inputs_meta_getter,
            eval_mode=eval_mode,
        )

    def CountNonBuiltinOps(ir_program):
        non_bulitin_ops = 0
        out_ops = 0
        for name, op in vars(ir_program).items():
            if not isinstance(op, ir_op.Op):
                continue
            if not op.name.startswith("builtin."):
                non_bulitin_ops += 1
            elif op.name == "builtin.shadow_output":
                out_ops += 1
        return non_bulitin_ops, out_ops

    ir_programs_dict = dict()
    for cls in list(GetProgramClasses(original_programs_file)):
        ir_program = cls()
        if not IsBackwardProgram(ir_program) and AllInputOutputTypesSupported(
            ir_program
        ):
            ops, outs = CountNonBuiltinOps(ir_program)
            # remove the ir_program which stores intermediate variables
            if ops in ir_programs_dict.keys() and outs < ir_programs_dict[ops][0]:
                ir_programs_dict[ops] = [outs, ir_program]
            elif ops not in ir_programs_dict.keys():
                ir_programs_dict[ops] = [outs, ir_program]
            else:
                pass

    # remove the small ir_program
    ir_programs = []
    for k, v in ir_programs_dict.items():
        if k > 6:
            print(f"Save the ir_program with {k} non-builtin ops")
            ir_programs.append(v[1])
        else:
            print(f"Abandon the ir_program with {k} non-builtin ops")

    num_ir_programs = len(ir_programs)
    yield from (
        (num_ir_programs, GetSha256sum(",".join(op_names))[0:32], unittest)
        for ir_program in ir_programs
        if not IsBackwardProgram(ir_program)
        if AllInputOutputTypesSupported(ir_program)
        for generator in [MakeUnittestGenerator(ir_program)]
        for op_names in [GetOpNames(ir_program)]
        for unittest in [generator.Generate()]
    )


def GetOpNames(ir_program):
    primitive_op_extractor = PrimitiveOpExtractor()
    return [op.name for op in primitive_op_extractor.Extract(ir_program)]


def AllInputOutputTypesSupported(ir_program):
    supported_operand_types = (
        ir_type.DenseTensorType,
        ir_type.NullType,
        ir_type.VectorType,
    )
    primitive_op_extractor = PrimitiveOpExtractor()
    return all(
        isinstance(in_out_type, supported_operand_types)
        for op in primitive_op_extractor.Extract(ir_program)
        for in_out_type in op.input_types + op.output_types
    )


if __name__ == "__main__":
    app.run(main)
