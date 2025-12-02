import os
import sys
import json
from absl import app
from absl import flags
import hashlib
import tempfile
import itertools
from itertools import groupby
from collections import defaultdict
from dataclasses import dataclass
from typing import Dict

from athena.generators.blocks_generator import BlocksGenerator
from athena.generators.block_name_generator import BlockNameGenerator
from athena.generators.graphnet_module_op_sample_generator import (
    GraphnetModuleOpSampleGenerator,
)
from athena.generators.paddle_block_unittest_stmts_generator import (
    PaddleBlockUnittestStmtsGenerator,
)
from athena.generators.graphnet_sequence_sample_generator import (
    GraphnetSequenceSampleGenerator,
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
from athena.op_example_input_meta_script import (
    GetOutputUnittests as GetOpExampleInputMetaUnittests,
)


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
flags.DEFINE_boolean(
    "group_head_and_tail",
    True,
    "Whether extend split_positions to include the head and tail of the statement sequence.",
)
flags.DEFINE_boolean(
    "eval_mode",
    False,
    "Generate graphnet sample for eval, which only keep output tensors with maximum depth (longest chain).",
)
flags.DEFINE_string("tmp_dir", tempfile.gettempdir(), "tmp directory.")


@dataclass
class GraphnetSample:
    unique_name: str
    subgraph_idx: int
    metadata: Dict[str, str]
    input_meta: str
    weight_meta: str
    model: str


def RunGeneration(
    model_name,
    ir_programs,
    example_inputs,
    op_example_inputs,
    split_positions,
    group_head_and_tail,
    eval_mode,
    tmp_dir=None,
):
    metadata = {
        "framework": "paddle",
        "model_name": model_name,
        "num_devices_required": 1,
        "num_nodes_required": 1,
    }

    graphnet_sample_results = []
    seg_counter = defaultdict(lambda: itertools.count())
    for module_id, (subgraph_idx, uid, sample_str) in enumerate(
        GetOutputSampleStrings(
            ir_programs,
            example_inputs,
            op_example_inputs,
            split_positions,
            group_head_and_tail,
            eval_mode,
            tmp_dir,
        )
    ):
        unique_name = f"{uid}_{next(seg_counter[uid])}"
        input_meta, weight_meta, model = sample_str.split("# --- seperate line ----\n")
        sample = GraphnetSample(
            unique_name=unique_name,
            subgraph_idx=subgraph_idx,
            metadata=metadata,
            input_meta=input_meta.strip("\n\n\n") + "\n",
            weight_meta=weight_meta.rstrip("\n\n\n") + "\n",
            model=model,
        )
        graphnet_sample_results.append(sample)
        # PrintToTerminal(unique_name, sample_str)
    print(f"Generate {len(graphnet_sample_results)} graphnet samples.")
    return graphnet_sample_results


def main(argv):
    split_positions = [int(x) for x in FLAGS.split_positions.split(",") if x.strip()]

    graphnet_sample_results = RunGeneration(
        model_name=FLAGS.model_name,
        ir_programs=FLAGS.ir_programs,
        example_inputs=FLAGS.example_inputs,
        op_example_inputs=FLAGS.op_example_inputs,
        split_positions=split_positions,
        group_head_and_tail=FLAGS.group_head_and_tail,
        eval_mode=FLAGS.eval_mode,
        tmp_dir=FLAGS.tmp_dir,
    )

    subgraph_idx2samples = {}
    for sample in graphnet_sample_results:
        if sample.subgraph_idx not in subgraph_idx2samples.keys():
            subgraph_idx2samples[sample.subgraph_idx] = []
        subgraph_idx2samples[sample.subgraph_idx].append(sample)

    num_samples = len(graphnet_sample_results)
    for subgraph_idx, samples in subgraph_idx2samples.items():
        for sample_idx in range(len(samples)):
            if num_samples == 1 and len(samples) == 1:
                subgraph_path = FLAGS.output_dir
            elif len(samples) == 1:
                subgraph_path = os.path.join(
                    FLAGS.output_dir, f"subgraph_{subgraph_idx}"
                )
            else:
                subgraph_path = os.path.join(
                    FLAGS.output_dir, f"subgraph_{subgraph_idx}_{sample_idx}"
                )
            if not os.path.exists(subgraph_path):
                os.makedirs(subgraph_path)
            WriteToFile(f"{subgraph_path}/model.py", samples[sample_idx].model)
            WriteToFile(
                f"{subgraph_path}/weight_meta.py", samples[sample_idx].weight_meta
            )
            WriteToFile(
                f"{subgraph_path}/input_meta.py", samples[sample_idx].input_meta
            )
            with open(os.path.join(subgraph_path, "graph_net.json"), "w") as f:
                json.dump(samples[sample_idx].metadata, f, indent=4)


def GetSha256sum(content):
    m = hashlib.sha256()
    m.update(content.encode())
    return m.hexdigest()


def GetOpNamesHash(op_names):
    return GetSha256sum(",".join(op_names))[0:32]


def GetSeqStmtsHash(seq_stmts):
    op_names = ",".join(s.op_name for s in seq_stmts)
    return GetSha256sum(op_names)[0:32]


def PrintToTerminal(name, sample_str):
    print("# file-splitter-begin-fusion-op-name: ", name)
    print(sample_str)
    print("# file-splitter--end--fusion-op-name: ", name)


def WriteToFile(filepath, content):
    print(f"Write to {filepath}")
    with open(filepath, "w") as f:
        f.write(content)


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
    print(f"Totally {len(ir_programs)} valid ir_programs.")
    return ir_programs


def GenerateOpExampleInputFile(
    programs_file, example_inputs_file, op_example_inputs_file, tmp_dir
):
    if os.path.isfile(op_example_inputs_file):
        print(f"Remove the existing {op_example_inputs_file}")
        os.remove(op_example_inputs_file)

    if tmp_dir is None:
        tmp_dir = tempfile.gettempdir()

    print(f"Generate {op_example_inputs_file} ...")
    tmp_output_file_prefix = "tmp_op_example_input_"
    for name, unittest in GetOpExampleInputMetaUnittests(
        programs_file, example_inputs_file, bucket_size=128
    ):
        sha256sum = GetSha256sum(unittest)
        tmp_output_filepath = os.path.join(
            tmp_dir, f"{tmp_output_file_prefix}{sha256sum[0:32]}.py"
        )
        WriteToFile(tmp_output_filepath, unittest)

        # Execute the generated tmp file
        generate_op_example_inputs_cmd = f"ATHENA_WHILE_LOOP_LIMIT=8 {sys.executable} {tmp_output_filepath} --max_try_cnt=10 --output_file={op_example_inputs_file}"
        System(generate_op_example_inputs_cmd)


def GetOutputSampleStrings(
    programs_file,
    example_inputs_file,
    op_example_inputs_file,
    split_positions,
    group_head_and_tail=True,
    eval_mode=True,
    tmp_dir=None,
):
    def MakeModuleOpSampleGenerator(ir_program, example_inputs_meta_getter):
        return GraphnetModuleOpSampleGenerator(
            ir_program,
            example_inputs_meta_getter,
            eval_mode=eval_mode,
        )

    def MakeSequenceSampleGenerator(
        program_id, seq_stmts, op_example_inputs_meta_getter
    ):
        generator = GraphnetSequenceSampleGenerator(
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
            generator = MakeModuleOpSampleGenerator(
                ir_program, example_inputs_meta_getter
            )
            sample_str = generator.Generate()
            yield (subgraph_idx, program_hash, sample_str)
            subgraph_idx += 1
    else:
        print(f"origin split_positions: {split_positions}")
        GenerateOpExampleInputFile(
            programs_file, example_inputs_file, op_example_inputs_file, tmp_dir
        )
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

        generated_sample_strs = set()
        subgraph_idx = 0
        for program_id, seq_stmts in program_seq_stmts_list:
            split_positions_for_seq_stmts = ExtendHeadAndTail(
                seq_stmts, split_positions, group_head_and_tail
            )
            for i in range(len(split_positions_for_seq_stmts) - 1):
                seq_stmts_slice = seq_stmts[
                    split_positions_for_seq_stmts[i] : split_positions_for_seq_stmts[
                        i + 1
                    ]
                ]
                sample_str = MakeSequenceSampleGenerator(
                    program_id, seq_stmts_slice, op_example_inputs_meta_getter
                )
                if sample_str not in generated_sample_strs:
                    generated_sample_strs.add(sample_str)
                    stmt_hash = GetSeqStmtsHash(seq_stmts_slice)
                    yield (subgraph_idx, stmt_hash, sample_str)
            subgraph_idx += 1


def ExtendHeadAndTail(seq_stmts, split_positions, group_head_and_tail):
    split_positions_for_seq_stmts = (
        [0, *split_positions, len(seq_stmts)]
        if group_head_and_tail
        else split_positions
    )
    split_positions_for_seq_stmts = [
        min(x, len(seq_stmts)) for x in split_positions_for_seq_stmts
    ]
    split_positions_for_seq_stmts = list(dict.fromkeys(split_positions_for_seq_stmts))
    print(f"split_positions_for_seq_stmts: {split_positions_for_seq_stmts}")
    return split_positions_for_seq_stmts


def IsPrimitive(stmt):
    op = stmt.op
    return all(
        arg_names_or_types is None or len(arg_names_or_types) == 0
        for arg_names_or_types in (
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


def System(cmd):
    print(f"Run system command: {cmd}", flush=True)
    ret = os.system(cmd)
    assert ret == 0, f"Run system command failed!\n  Detail command: {cmd}"


if __name__ == "__main__":
    app.run(main)
