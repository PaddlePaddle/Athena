from athena.util.load_pir_py_classes import GetProgramClasses, GetClasses
from athena.util.op_example_inputs_meta_getter import (
    MakeOpExampleInputsMetaGetter,
)
from athena.generators.sequence_unittests_generator import SequenceUnittestsGenerator
from athena.util.primitive_op_extractor import PrimitiveOpExtractor
from athena.generators.blocks_generator import BlocksGenerator
from athena.generators.paddle_block_unittest_stmts_generator import (
    PaddleBlockUnittestStmtsGenerator,
)
from athena.generators.block_name_generator import BlockNameGenerator
from athena.util.ir_program_util import IsBackwardProgram, GetProgramId
import athena.ir.ir_op as ir_op
import athena.ir.ir_type as ir_type
from absl import app
from absl import flags
import hashlib
from itertools import groupby
import itertools
from collections import defaultdict
from athena.util.block_op_calls_extractor import BlockOpCallsExtractor
import glob
import os
from athena.rp_expr.rp_expr_parser import RpExprParser
from athena.rp_expr.rp_expr_util import MakeNestedIndexRangeFromLetsListTokenRpExpr
import sys

FLAGS = flags.FLAGS

flags.DEFINE_string("ir_programs", "", "ir programs file.")
flags.DEFINE_string(
    "op_example_input_tensor_meta", "", "op example input tensor meta file."
)
flags.DEFINE_string(
    "length_slice", "2:33", "syntax is like python list slice: 0:1, 30:40."
)
flags.DEFINE_string("output_dir", "./output-dir", "output directory.")


def main(argv):
    for file in glob.glob(f"{FLAGS.output_dir}/test_sequence_*.py"):
        os.remove(file)
    assert FLAGS.ir_programs != ""
    assert FLAGS.op_example_input_tensor_meta != ""
    original_programs_file = FLAGS.ir_programs
    op_example_inputs_file = FLAGS.op_example_input_tensor_meta
    unittests = GetOutputUnittests(original_programs_file, op_example_inputs_file)
    seg_counter = defaultdict(lambda: itertools.count())
    for name, unittest in unittests:
        unique_name = f"{name}_{next(seg_counter[name])}"
        filepath = f"{FLAGS.output_dir}/test_sequence_{unique_name}.py"
        WriteToFile(filepath, unittest)
        PrintToTerminal(unique_name, filepath, unittest)


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

    unittest_stmts_gen = PaddleBlockUnittestStmtsGenerator(BlockNameGenerator())
    program_seq_stmts_list = [
        (program_id, seq_stmts)
        for ir_program in ir_programs
        for program_id in [GetProgramId(ir_program)]
        for block in BlocksGenerator(ir_program).Generate()
        if AllInputOutputTypeValid(block)
        for _, stmts, _ in [unittest_stmts_gen.Generate(block)]
        for seq_stmts in ExtractSeqStmts(
            stmts, program_id, op_example_inputs_meta_getter
        )
        if len(seq_stmts) > 1
        if op_example_inputs_meta_getter.HasAllInputs(program_id, seq_stmts[0].op)
    ]

    stmts_primitive_ids_list = [
        [MakeStmtPrimitiveId(stmt) for stmt in seq_stmts]
        for _, seq_stmts in program_seq_stmts_list
    ]
    rp_expr_parser = RpExprParser()
    lets_list_rp_expr, token_id2primitive_id = rp_expr_parser(stmts_primitive_ids_list)
    print("\n".join(lets_list_rp_expr.DebugStrings(token_id2primitive_id)))
    trees = MakeNestedIndexRangeFromLetsListTokenRpExpr(lets_list_rp_expr)
    assert len(trees) == len(program_seq_stmts_list)
    min_length, max_length = map(int, FLAGS.length_slice.split(":"))
    ranges_list = [
        tree.FilterSubTreeRangeBySize(min_length, max_length) for tree in trees
    ]
    program_seq_stmts_list = (
        (program_id, seq_stmts)
        for ranges, pair in zip(ranges_list, program_seq_stmts_list)
        for start, end in ranges
        for program_id, origin_seq_stmts in [pair]
        for seq_stmts in [origin_seq_stmts[start:end]]
    )

    def GetUnittests(program_id, seq_stmts):
        return GetSequenceUnittests(
            program_id, seq_stmts, op_example_inputs_meta_getter
        )

    generated_unittests = set()
    yield from (
        (name, unittest)
        for program_id, seq_stmts in program_seq_stmts_list
        for unittest in [GetUnittests(program_id, seq_stmts)]
        if unittest not in generated_unittests
        for name in [GetSeqStmtsHash(seq_stmts)]
        for _ in [generated_unittests.add(unittest)]
    )


def MakeStmtPrimitiveId(stmt):
    counter = itertools.count()
    name2counter = defaultdict(lambda: next(counter))
    return "\n".join(
        pycode.pycode(lambda x: f"t{name2counter[x]}") for pycode in stmt.pycode
    )


def AllInputOutputTypeValid(block):
    extractor = BlockOpCallsExtractor()
    block_op_calls = extractor.Extract(block.block_func, block.free_vars, block.args)
    return all(
        isinstance(in_out_type, valid_operand_types)
        for op_call in block_op_calls.body_op_calls
        for in_out_type in (op_call.op.input_types + op_call.op.output_types)
    )


def GetSeqStmtsHash(seq_stmts):
    op_names = ",".join(s.op_name for s in seq_stmts)
    return GetSha256sum(op_names)[0:32]


def GetSha256sum(content):
    m = hashlib.sha256()
    m.update(content.encode())
    return m.hexdigest()


def GetSequenceUnittests(program_id, seq_stmts, op_example_inputs_meta_getter):
    generator = SequenceUnittestsGenerator(program_id, op_example_inputs_meta_getter)
    return generator.Generate(seq_stmts)


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


valid_operand_types = (
    ir_type.DenseTensorType,
    ir_type.NullType,
    ir_type.VectorType,
)


if __name__ == "__main__":
    app.run(main)
