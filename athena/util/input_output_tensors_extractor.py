class InputOutputTensorsExtractor:

    def __init__(self, block_func):
        self.block_func = block_func
        self.input_tensors = []
        self.output_tensors = []

    def Extract(self, free_vars, args):
        self.input_tensors += list(free_vars)
        self.input_tensors += list(args)
        self.block_func(self, *free_vars)(*args)
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
        self.output_tensors += list(inputs)

    def pd_op_fetch(self, op, *inputs):
        self.output_tensors += list(inputs)

    def cf_yield(self, op, *inputs):
        self.output_tensors += list(inputs)

    def __call__(self, op, *input_tensors, **kwargs):
        method_name = op.GetPyVarName()
        if hasattr(self, method_name):
            getattr(self, method_name)(op, *input_tensors)
        return op.GetResults()
