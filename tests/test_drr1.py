def SoftmaxFusionDemo(ctx):
  ctx.pass_name = "softmax_prologue"

  @ctx.demo_graph
  def DemoGraph(o, t):
    o.foo_op = o.ap_trivial_fusion_op()
    o.foo_op(
      [*t.foo_input],
      [t.foo_output, *t.foo_other_output]
    )
    o.softmax_op = o.ap_native_op("pd_op.softmax")
    o.softmax_op(
      [t.foo_output],
      [t.tensor1]
    )

  @ctx.source_pattern
  def SourcePattern(o, t):
    o.foo_op = o.ap_trivial_fusion_op()
    o.foo_op(
      [*t.foo_input],
      [t.foo_output, *t.foo_other_output]
    )
    o.softmax_op = o.ap_native_op("pd_op.softmax")
    o.softmax_op(
      [t.foo_output],
      [t.tensor1]
    )
  return ctx.test_source_pattern_by_demo_graph()
