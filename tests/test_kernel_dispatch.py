def KernelDispatch(ctx):
  size = ctx.inputs[0].shape[0]
  ctx.launch_cuda(
    "relu",
    1,
    size,
    [
      ctx.DataValue(size).cast(ctx.const_int32),
      ctx.inputs[0].data_ptr,
      ctx.outputs[0].data_ptr
    ]
  )