from collections import defaultdict


class InputOutputTensorsExtractor:
    def __init__(self, block_func):
        self.block_func = block_func
        self.input_tensors = []
        self.output_tensors = []
        self.op_id2depth = defaultdict(int)
        self.tensor_name2depth = defaultdict(int)

    def Extract(self, free_vars, args, max_depth_output_only=False):
        self.input_tensors += list(free_vars)
        self.input_tensors += list(args)
        self.block_func(self, *free_vars)(*args)

        if max_depth_output_only:
            max_output_tensor_depth = max(
                self.tensor_name2depth[tensor.name] for tensor in self.output_tensors
            )
            self.output_tensors = [
                tensor
                for tensor in self.output_tensors
                if self.tensor_name2depth[tensor.name] == max_output_tensor_depth
            ]

        return self.input_tensors, self.output_tensors

    def pd_op_data(self, op):
        self.input_tensors += list(op.GetResults())

    def pd_op_feed(self, op):
        self.input_tensors += list(op.GetResults())

    def builtin_parameter(self, op):
        self.input_tensors += list(op.GetResults())

    def builtin_constant(self, op):
        self.input_tensors += list(op.GetResults())

    def builtin_shadow_output(self, op, *inputs):
        self.output_tensors += [t for t in inputs if t is not None]

    def pd_op_fetch(self, op, *inputs):
        self.output_tensors += [t for t in inputs if t is not None]

    def cf_yield(self, op, *inputs):
        self.output_tensors += [t for t in inputs if t is not None]

    def __call__(self, op, *input_tensors, **kwargs):
        method_name = op.GetPyVarName()
        if hasattr(self, method_name):
            getattr(self, method_name)(op, *input_tensors)

        ret = op.GetResults()

        valid_input_tensors = [t for t in input_tensors if t is not None]

        if valid_input_tensors:
            input_depth = max(
                (self.tensor_name2depth[tensor.name] for tensor in valid_input_tensors),
                default=0,
            )
        else:
            input_depth = 0

        op_depth = input_depth + 1
        self.op_id2depth[op.op_id] = op_depth
        for tensor in ret:
            self.tensor_name2depth[tensor.name] = op_depth

        return ret
