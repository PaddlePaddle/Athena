import ap_drr_fuser
import trivial_template_module


@ap_drr_fuser.register_drr_pass("trivial_fusion", nice=0)
class TrivialFusionDemo(ap_drr_fuser.DrrPass):

  def source_pattern(self, o, t):
    o.trivial_op = o.ap_trivial_fusion_op()
    o.trivial_op(
      [t.input0],
      [t.output0]
    )

  def get_constraint_func(self):
    return Constraint.__function__

  def result_pattern(self, o, t):
    o.fustion_op = o.ap_pattern_fusion_op(CodeGen.__function__)
    o.fustion_op(
      [t.input0],
      [t.output0]
    )

def Constraint(o, t):
  return True

def CodeGen(ctx, o, t):
  trivial_op_code_gen_class = ctx.make_fusion_op_code_gen_class(
    o.trivial_op,
    input_index_loop_anchor_flags=[False],
    output_index_loop_anchor_flags=[True],
  )
  template_module = trivial_template_module.TrivialTemplateModule(
    trivial_op_code_gen_class=trivial_op_code_gen_class
  )
  return template_module.compile(
    dim0_karg=ctx.dim_expr_kernel_arg_id(t.input0.shape[0]),
    input0_karg=ctx.in_tensor_data_ptr_kernel_arg_id(t.input0),
    output0_karg=ctx.out_tensor_data_ptr_kernel_arg_id(t.output0),
  )
