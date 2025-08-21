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

FLAGS = flags.FLAGS

flags.DEFINE_string("ir_programs", "", "ir programs file.")
flags.DEFINE_string("example_inputs", "", "example input tensor meta file.")
flags.DEFINE_string("output_dir", "./output-dir", "output directory.")
flags.DEFINE_boolean("enable_early_return", False, "enable early return.")
flags.DEFINE_boolean("enable_local_tensor", True, "enable local tensor name.")


def main(argv):
    os.environ["ATHENA_ENABLE_LOCAL_TENSOR"] = str(FLAGS.enable_local_tensor)
    os.environ["ATHENA_ENABLE_EARLY_RETURN"] = str(FLAGS.enable_early_return)
    original_programs_file = FLAGS.ir_programs
    example_inputs_file = FLAGS.example_inputs
    seg_counter = defaultdict(lambda: itertools.count())
    for module_id, (uid, unittest) in enumerate(
        GetOutputUnittests(original_programs_file, example_inputs_file)
    ):
        if module_id == 0:
            sub_dir_path = f"{FLAGS.output_dir}"
        else:
            sub_dir_path = f"{FLAGS.output_dir}_{module_id}"
        inputs_meta, weighs_meta, model_arch = unittest.split(
            "# --- seperate line ----\n"
        )
        for file in glob.glob(f"{sub_dir_path}/*"):
            if os.path.isfile(file):
                os.remove(file)
        if not os.path.exists(sub_dir_path):
            os.mkdir(sub_dir_path)
        WriteToFile(f"{sub_dir_path}/model.py", model_arch)
        WriteToFile(
            f"{sub_dir_path}/weight_meta.py", weighs_meta.rstrip("\n\n\n") + "\n"
        )
        WriteToFile(f"{sub_dir_path}/input_meta.py", inputs_meta.strip("\n\n\n") + "\n")
        metadata = {
            "framework": "paddle",
            "num_devices_required": 1,
            "num_nodes_required": 1,
        }
        with open(os.path.join(sub_dir_path, "graph_net.json"), "w") as f:
            json.dump(metadata, f, indent=4)
        print("flag", f"{sub_dir_path}/model.py")
        unique_name = f"{uid}_{next(seg_counter[uid])}"
        PrintToTerminal(unique_name, f"{sub_dir_path}/model.py", unittest)


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
    example_inputs_meta_getter = MakeExampleInputsMetaGetter(
        GetClasses(example_inputs_file)
    )

    def MakeUnittestGenerator(ir_program):
        return ModuleOpUnittestForGraphnetGenerator(
            ir_program, example_inputs_meta_getter
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
    ir_programs = [v[1] for k, v in ir_programs_dict.items() if k > 6]
    # raise ValueError("The longest ir program is not forward program.")
    yield from (
        (GetSha256sum(",".join(op_names))[0:32], unittest)
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
