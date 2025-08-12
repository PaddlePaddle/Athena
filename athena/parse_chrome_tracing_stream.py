from absl import app
from absl import flags
import hashlib
from itertools import groupby
import itertools
from collections import defaultdict
import glob
import os
from athena.rp_expr.rp_expr_parser import RpExprParser
from athena.rp_expr.longest_rp_expr_parser import LongestRpExprParser
from athena.rp_expr.rp_expr_util import MakeNestedIndexRangeFromLetsListTokenRpExpr
import sys
import json

FLAGS = flags.FLAGS

flags.DEFINE_string("chrome_tracing_json_file", "", "chrome_tracing_json_file.")
flags.DEFINE_integer("pid", -1, "process id.")
flags.DEFINE_integer("stream", -1, "stream id.")
flags.DEFINE_integer("max_window_size", 1024, "pattern window size.")
flags.DEFINE_integer("min_window_size", 2, "pattern window size.")

def main(argv):
    events = [event for event in get_events()]
    event_names_list = [
        [event['name'] for event in events]
    ]
    # rp_expr_parser = RpExprParser(
    #     FLAGS.max_window_size,
    #     fold_policy="longest",
    #     fold_times=1,
    # )
    rp_expr_parser = LongestRpExprParser(
        max_window_size=FLAGS.max_window_size,
        min_window_size=FLAGS.min_window_size,
    )
    lets_list_rp_expr, token_id2primitive_id = rp_expr_parser(event_names_list)
    lst = lets_list_rp_expr.DebugStrings(token_id2primitive_id, end_of_line=";")
    print("\n\n".join(lst))

def get_events():
    assert FLAGS.pid != -1
    assert FLAGS.stream != -1
    with open(FLAGS.chrome_tracing_json_file) as f:
        tracing_json = json.load(f)
        traceEvents = tracing_json['traceEvents']
        for event in traceEvents:
            if event['pid'] != FLAGS.pid:
                continue
            if 'args' not in event:
                continue
            if 'stream' not in event['args']:
                continue
            if event['args']['stream'] != FLAGS.stream:
                continue
            yield event

if __name__ == "__main__":
    app.run(main)
