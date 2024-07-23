import yaml
import sys
import re

with open(sys.argv[1]) as stream:

    def ConvertOp(op):
        args = op["args"]
        args = re.sub(r"{[^}][^}]*}", "{}", args)
        # args = re.sub(r"[[^]][^]]*]", "[]", args)
        args = re.sub(r"[ ]*=[^,]*,", ",", args)
        args = re.sub(r"[ ]*=[^,]*\)", ")", args)
        args = re.sub(r",[ ]*", ", ", args)
        args = re.sub(r"[ ][ ]*", " ", args)
        args = args[1:-1]
        op_name = op["op"]
        return (f"{op_name}",) + tuple(
            (f"{type_name}", f"{arg_name}")
            for arg in args.split(", ")
            for type_name, arg_name in [arg.split(" ")]
        )

    import pprint

    pprint.pprint([ConvertOp(op) for op in yaml.safe_load(stream)])
