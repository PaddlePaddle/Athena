import os
import json
from absl import app
from absl import flags
import hashlib
import glob as glob
import itertools
from itertools import groupby
from collections import defaultdict
from dataclasses import dataclass
from typing import Dict

from athena.generators.blocks_generator import BlocksGenerator
from athena.generators.block_name_generator import BlockNameGenerator
from athena.generators.module_op_unittest_for_graphnet_generator import (
    ModuleOpUnittestForGraphnetGenerator,
)
from athena.generators.paddle_block_unittest_stmts_generator import (
    PaddleBlockUnittestStmtsGenerator,
)
from athena.generators.sequence_unittests_generator_for_graphnet import (
    SequenceUnittestsGenerator,
)
import athena.ir.ir_op as ir_op
import athena.ir.ir_type as ir_type
import athena.ir.ir_block as ir_block
from athena.util.load_pir_py_classes import GetProgramClasses, GetClasses
from athena.util.example_inputs_meta_getter import (
    MakeExampleInputsMetaGetter,
)
from athena.util.op_example_inputs_meta_getter import (
    MakeOpExampleInputsMetaGetter,
)
from athena.util.ir_program_util import IsBackwardProgram, GetProgramId
from athena.util.block_op_calls_extractor import BlockOpCallsExtractor
from athena.util.primitive_op_extractor import PrimitiveOpExtractor


FLAGS = flags.FLAGS

flags.DEFINE_string("model_name", "", "model name.")
flags.DEFINE_string("ir_programs", "", "ir programs file.")
flags.DEFINE_string("example_inputs", "", "example input tensor meta file.")
flags.DEFINE_string("op_example_inputs", "", "op example input tensor meta file.")
flags.DEFINE_string(
    "split_positions",
    "",
    "a comma-separated string of integer list to specify the split positions.",
)
flags.DEFINE_string("output_dir", "./output-dir", "output directory.")
flags.DEFINE_boolean(
    "eval_mode",
    False,
    "Generate unittest for eval, which only keep output tensors with maximum depth (longest chain).",
)


@dataclass
class GraphnetSample:
    unique_name: str
    subgraph_idx: int
    metadata: Dict[str, str]
    input_meta: str
    weight_meta: str
    model: str


def generate_samples(
    model_name,
    ir_programs,
    example_inputs,
    op_example_inputs,
    split_positions,
    eval_mode,
):
    metadata = {
        "framework": "paddle",
        "model_name": model_name,
        "num_devices_required": 1,
        "num_nodes_required": 1,
    }

    graphnet_sample_results = []
    seg_counter = defaultdict(lambda: itertools.count())
    for module_id, (subgraph_idx, uid, unittest) in enumerate(
        GetOutputUnittests(
            ir_programs, example_inputs, op_example_inputs, split_positions, eval_mode
        )
    ):
        unique_name = f"{uid}_{next(seg_counter[uid])}"
        input_meta, weight_meta, model = unittest.split("# --- seperate line ----\n")
        sample = GraphnetSample(
            unique_name=unique_name,
            subgraph_idx=subgraph_idx,
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
    split_positions = [int(x) for x in FLAGS.split_positions.split(",") if x.strip()]

    graphnet_sample_results = generate_samples(
        model_name=FLAGS.model_name,
        ir_programs=FLAGS.ir_programs,
        example_inputs=FLAGS.example_inputs,
        op_example_inputs=FLAGS.op_example_inputs,
        split_positions=split_positions,
        eval_mode=FLAGS.eval_mode,
    )

    subgraph_idx2samples = {}
    for sample in graphnet_sample_results:
        if sample.subgraph_idx not in subgraph_idx2samples.keys():
            subgraph_idx2samples[sample.subgraph_idx] = [sample]
        else:
            subgraph_idx2samples[sample.subgraph_idx].append(sample)

    num_samples = len(graphnet_sample_results)
    for subgraph_idx, samples in subgraph_idx2samples.items():
        for sample_idx in range(len(samples)):
            if num_samples == 1 and len(samples) == 1:
                subgraph_path = f"{FLAGS.output_dir}"
            elif len(samples) == 1:
                subgraph_path = os.path.join(
                    f"{FLAGS.output_dir}", f"subgraph_{subgraph_idx}"
                )
            else:
                subgraph_path = os.path.join(
                    f"{FLAGS.output_dir}", f"subgraph_{subgraph_idx}_{sample_idx}"
                )
            if not os.path.exists(subgraph_path):
                os.makedirs(subgraph_path)
            WriteToFile(f"{subgraph_path}/model.py", sample.model)
            WriteToFile(f"{subgraph_path}/weight_meta.py", sample.weight_meta)
            WriteToFile(f"{subgraph_path}/input_meta.py", sample.input_meta)
            with open(os.path.join(subgraph_path, "graph_net.json"), "w") as f:
                json.dump(sample.metadata, f, indent=4)


def GetSha256sum(content):
    m = hashlib.sha256()
    m.update(content.encode())
    return m.hexdigest()


def GetOpNamesHash(op_names):
    return GetSha256sum(",".join(op_names))[0:32]


def GetSeqStmtsHash(seq_stmts):
    op_names = ",".join(s.op_name for s in seq_stmts)
    return GetSha256sum(op_names)[0:32]


def PrintToTerminal(name, unittest):
    print("# file-splitter-begin-fusion-op-name: ", name)
    print(unittest)
    print("# file-splitter--end--fusion-op-name: ", name)


def WriteToFile(filepath, unittest):
    print(f"Write to {filepath}")
    with open(filepath, "w") as f:
        f.write(unittest)


def CountNonBuiltinOps(ir_program):
    non_bulitin_ops = 0
    num_outs = 0
    for name, op in vars(ir_program).items():
        if not isinstance(op, ir_op.Op):
            continue
        if not op.name.startswith("builtin."):
            non_bulitin_ops += 1
        elif op.name == "builtin.shadow_output":
            num_outs += 1
    return non_bulitin_ops, num_outs


def GetValidIrPrograms(programs_file):
    ir_programs_dict = dict()
    for cls in list(GetProgramClasses(programs_file)):
        ir_program = cls()
        num_ops, num_outs = CountNonBuiltinOps(ir_program)
        op_names = GetOpNames(ir_program)
        print(f"num_ops={num_ops}, len(op_names)={len(op_names)}")
        print(f"op_names:{op_names}")
        # skip the small ir_program
        if (
            not IsBackwardProgram(ir_program)
            and AllInputOutputTypesSupported(ir_program)
            and num_ops > 6
        ):
            program_hash = GetOpNamesHash(GetOpNames(ir_program))
            # remove the ir_program with the same op lists and more outputs
            if program_hash not in ir_programs_dict.keys():
                ir_programs_dict[program_hash] = [num_outs, ir_program]
            elif num_outs < ir_programs_dict[program_hash][0]:
                ir_programs_dict[program_hash] = [num_outs, ir_program]
            else:
                pass

    ir_programs = [v[1] for k, v in ir_programs_dict.items()]
    return ir_programs


def GetOutputUnittests(
    programs_file,
    example_inputs_file,
    op_example_inputs_file,
    split_positions,
    eval_mode,
):
    def MakeModuleUnittestGenerator(ir_program, example_inputs_meta_getter):
        return ModuleOpUnittestForGraphnetGenerator(
            ir_program,
            example_inputs_meta_getter,
            eval_mode=eval_mode,
        )

    def MakeSequenceUnittestGenerator(
        program_id, seq_stmts, op_example_inputs_meta_getter
    ):
        generator = SequenceUnittestsGenerator(
            program_id, op_example_inputs_meta_getter
        )
        return generator.Generate(seq_stmts)

    ir_programs = GetValidIrPrograms(programs_file)
    if not split_positions:
        example_inputs_meta_getter = MakeExampleInputsMetaGetter(
            GetClasses(example_inputs_file)
        )
        subgraph_idx = 0
        for ir_program in ir_programs:
            op_names = GetOpNames(ir_program)
            program_hash = GetOpNamesHash(op_names)
            generator = MakeModuleUnittestGenerator(
                ir_program, example_inputs_meta_getter
            )
            unittest = generator.Generate()
            yield (subgraph_idx, program_hash, unittest)
            subgraph_idx += 1
    else:
        print(f"split_positions: {split_positions}")
        op_example_inputs_meta_getter = MakeOpExampleInputsMetaGetter(
            GetClasses(op_example_inputs_file)
        )
        unittest_stmts_gen = PaddleBlockUnittestStmtsGenerator(BlockNameGenerator())
        program_seq_stmts_list = [
            (program_id, seq_stmts)
            for ir_program in ir_programs
            for program_id in [GetProgramId(ir_program)]
            for block in BlocksGenerator(ir_program).Generate()
            if AllInputOutputTypesSupported(block)
            for _, stmts, _ in [unittest_stmts_gen.Generate(block)]
            for seq_stmts in ExtractSeqStmts(
                stmts, program_id, op_example_inputs_meta_getter
            )
            if len(seq_stmts) > 1
            if op_example_inputs_meta_getter.HasAllInputs(program_id, seq_stmts[0].op)
        ]

        generated_unittests = set()
        subgraph_idx = 0
        for program_id, seq_stmts in program_seq_stmts_list:
            split_positions_for_seq_stmts = ExtendStartAndEnd(
                seq_stmts, split_positions
            )
            for i in range(len(split_positions_for_seq_stmts) - 1):
                seq_stmts_slice = seq_stmts[
                    split_positions_for_seq_stmts[i] : split_positions_for_seq_stmts[
                        i + 1
                    ]
                ]
                unittest = MakeSequenceUnittestGenerator(
                    program_id, seq_stmts_slice, op_example_inputs_meta_getter
                )
                if unittest not in generated_unittests:
                    generated_unittests.add(unittest)
                    stmt_hash = GetSeqStmtsHash(seq_stmts_slice)
                    yield (subgraph_idx, stmt_hash, unittest)
            subgraph_idx += 1


def ExtendStartAndEnd(seq_stmts, split_positions):
    split_positions_for_seq_stmts = [0] + [
        v for v in split_positions if v < len(seq_stmts)
    ]
    if split_positions_for_seq_stmts[-1] < len(seq_stmts):
        split_positions_for_seq_stmts.append(len(seq_stmts))
    print(f"split_positions_for_seq_stmts:{split_positions_for_seq_stmts}")
    return split_positions_for_seq_stmts


def IsPrimitive(stmt):
    op = stmt.op
    return all(
        l is None or len(l) == 0
        for l in (
            op.block_positional_arg_names,
            op.block_keyword_arg_names,
            op.block_positional_arg_types,
            op.block_keyword_arg_types,
        )
    )


def ExtractSeqStmts(stmts, program_id, op_example_inputs_meta_getter):
    def IsValidPrimitive(stmt):
        return op_example_inputs_meta_getter.HasAllInputs(
            program_id, stmt.op
        ) and IsPrimitive(stmt)

    yield from (
        seq_stmts
        for is_primitive, stmt_group in groupby(stmts, key=IsValidPrimitive)
        if is_primitive
        for seq_stmts in [list(stmt_group)]
    )


def GetOpNames(ir_program):
    primitive_op_extractor = PrimitiveOpExtractor()
    return [op.name for op in primitive_op_extractor.Extract(ir_program)]


def AllInputOutputTypesSupported(ir_program_or_block):
    supported_operand_types = (
        ir_type.DenseTensorType,
        ir_type.NullType,
        ir_type.VectorType,
    )
    if isinstance(ir_program_or_block, ir_block.Block):
        block = ir_program_or_block
        extractor = BlockOpCallsExtractor()
        block_op_calls = extractor.Extract(
            block.block_func, block.free_vars, block.args
        )
        return all(
            isinstance(in_out_type, supported_operand_types)
            for op_call in block_op_calls.body_op_calls
            for in_out_type in (op_call.op.input_types + op_call.op.output_types)
        )
    else:
        ir_program = ir_program_or_block
        primitive_op_extractor = PrimitiveOpExtractor()
        return all(
            isinstance(in_out_type, supported_operand_types)
            for op in primitive_op_extractor.Extract(ir_program)
            for in_out_type in op.input_types + op.output_types
        )


if __name__ == "__main__":
    app.run(main)
