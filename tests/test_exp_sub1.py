@Registry.op_compute("pd_op.exp", "cuda", 0)
def PdOpExp(inputs, outputs, attrs):
  return f"{outputs[0]} = expf({inputs[0]})"

@Registry.op_compute("pd_op.subtract", "cuda", 0)
def PdOpSubstract(inputs, outputs, attrs):
  return f"{outputs[0]} = {inputs[0]} - {inputs[1]}"

@Registry.op_compute("cinn_op.yield_store", "cuda", 0)
def CinnOpYieldStore(inputs, outputs, attrs):
  return f"{outputs[0]} = {inputs[0]}"

@Registry.drr("exp_sub", 0)
def SoftmaxFusionDemo(ctx):

  def SourcePattern(o, t):
    o.trivial_op = o.ap_trivial_fusion_op()
    o.trivial_op(
      [t.input0],
      [t.output0]
    )

  def ResultPattern(o, t):
    o.fustion_op = o.ap_pattern_fusion_op(CodeGen, KernelDispatch.__code__)
    o.fustion_op(
      [t.input0],
      [t.output0]
    )

  def CodeGen(ctx, o, t):
    trivial_code_str = ctx.cuda_code_gen(
      o.trivial_op,
      loop_index_tuple_expr=IndexTupleExpr.Domain([64]),
      loop_var_names=["threadIdx.x"],
      anchor_local_var_name="x",
      local_var_name_bindings=[
        ["x", t.input0],
        ["y", t.output0],
      ]
    )
    return ctx.render_module_template(
      "exp_sub",
      TRIVIAL_CODE_STRING=trivial_code_str
    )

  def KernelDispatch(ctx):
    size = ctx.inputs[0].shape[0]
    ctx.launch_cuda(
      "relu",
      1,
      size,
      [
        DataValue(size).cast(DataType.const_int32),
        ctx.inputs[0].data_ptr,
        ctx.outputs[0].data_ptr
      ]
    )

  return DrrCtx(
    source_pattern=SourcePattern,
    result_pattern=ResultPattern
  )

@Registry.module_template("exp_sub", "cuda")
def ExpSubModuleTemplte(ctx):
  code = """
#include <cstdint>
#define CINN_WITH_CUDA

extern "C" __global__
void relu(const int num, const float* input, float* output) {
int idx = blockIdx.x * blockDim.x + threadIdx.x;
if (idx < num) {
  float x = input[idx];
  float y;
  TRIVIAL_CODE_STRING
  output[idx] = y;
}
}
"""
  code = code.replace("TRIVIAL_CODE_STRING", ctx.TRIVIAL_CODE_STRING)
  print(code)
  return CodeModule(
    FuncDeclare("relu", [
      DataType.const_int32,
      PointerType.const_float_ptr,
      PointerType.float_ptr,
    ]),
    CudaKernelSourceCode(code)
  )