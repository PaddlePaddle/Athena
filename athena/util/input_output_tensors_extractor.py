from collections import defaultdict


class InputOutputTensorsExtractor:
    def __init__(self, block_func):
        self.block_func = block_func
        self.input_tensors = []
        self.output_tensors = []
        self.tensor_name2ancestors = defaultdict(set)
        self.consumed_tensors = set()
        self.invalid_outputs_for_eval = {}

    def Extract(self, free_vars, args, eval_mode=False):
        self.input_tensors += list(free_vars)
        self.input_tensors += list(args)
        self.block_func(self, *free_vars)(*args)

        if eval_mode:
            tensor_names_to_remove = set()
            for op_id, output_names in self.invalid_outputs_for_eval.items():
                tensor_names_to_remove.update(output_names)

            self.output_tensors = [
                t for t in self.output_tensors if t.name not in tensor_names_to_remove
            ]

            ancestors = set(
                ancestor
                for tensor in self.output_tensors
                for ancestor in self.tensor_name2ancestors[tensor.name]
            )
            self.output_tensors = [
                tensor for tensor in self.output_tensors if tensor.name not in ancestors
            ]

        # print(
        #     f"Totally {len(self.input_tensors)} input tensors, {len(self.output_tensors)} output tensors."
        # )
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

    def collect_invalid_outputs(self, op, *input_tensors, **kwargs):
        ret = op.GetResults()
        output_names = [t.name for t in ret]

        # Some operators have multiple outputs, but part of the outputs are training-only (e.g., batch mean and variance) which should not be returned.
        if op.name in [
            "pd_op.batch_norm_",
            "pd_op.layer_norm",
            "pd_op.dropout",
            "pd_op.einsum",
            "pd_op.group_norm",
        ]:
            self.invalid_outputs_for_eval[op.op_id] = output_names[1:]

        if op.name in ["pd_op.full_int_array", "pd_op.assign"]:
            self.invalid_outputs_for_eval[op.op_id] = output_names

        if op.name in ["builtin.split"]:
            # The input tensors are marked invalid.
            all_invalid_output_names = {
                name
                for invalid_output_names in self.invalid_outputs_for_eval.values()
                for name in invalid_output_names
            }
            all_input_tensors_invalid = all(
                input_tensor.name in all_invalid_output_names
                for input_tensor in input_tensors
            )
            if all_input_tensors_invalid:
                self.invalid_outputs_for_eval[op.op_id] = output_names

    def __call__(self, op, *input_tensors, **kwargs):
        method_name = op.GetPyVarName()
        if hasattr(self, method_name):
            getattr(self, method_name)(op, *input_tensors)

        ret = op.GetResults()
        valid_input_tensors = [t for t in input_tensors if t is not None]

        self.collect_invalid_outputs(op, *input_tensors)

        for tensor in valid_input_tensors:
            self.consumed_tensors.add(tensor.name)

        if valid_input_tensors:
            input_ancestors = set(
                ancestor
                for tensor in valid_input_tensors
                for ancestor in self.tensor_name2ancestors[tensor.name]
            )
        else:
            input_ancestors = set()

        for tensor in ret:
            self.tensor_name2ancestors[tensor.name] = input_ancestors | {
                t.name for t in valid_input_tensors
            }

        return ret
