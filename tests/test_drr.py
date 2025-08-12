def SoftmaxFusionDemo(ctx):
  @ctx.source_pattern
  def SourcePattern(o, t):
    o.trivial_op = o.ap_trivial_fusion_op()
    o.trivial_op(
      [*t.inputs],
      [t.tensor0, *t.tensor0_siblings]
    )
    o.softmax_op = o.ap_native_op("pd_op.softmax")
    o.softmax_op(
      [t.tensor0],
      [t.tensor1]
    )

  def KernelDefine(ctx):
    return None

  def KernelDispatch(ctx):
    return None

  @ctx.result_pattern
  def ResultPattern(o, t):
    o.fustion_op = o.ap_pattern_fusion_op(KernelDefine, KernelDispatch)
    o.fustion_op(
      [*t.inputs],
      [t.tensor1, *t.tensor0_siblings]
    )
