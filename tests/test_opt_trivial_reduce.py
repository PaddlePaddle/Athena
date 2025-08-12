
@Registry.drr("trivial_fusion", 0)
def TrivialFusionDemo():

  def SourcePattern(o, t):
    o.trivial_op = o.optional_ap_trivial_fusion_op()
    o.full_int_array = o.ap_native_op("pd_op.full_int_array")
    o.reduce_op = o.ap_native_op("pd_op.sum")

    o.trivial_op(
      [t.input0, *t.input_xs],
      [t.output0]
    )
    o.full_int_array(
      [],
      [t.axis]
    )
    o.reduce_op(
      [t.output0, t.axis],
      [t.output1]
    )


  def ResultPattern(o, t):
    o.fustion_op = o.ap_pattern_fusion_op(CodeGen.__code__, KernelDispatch.__code__)
    o.fustion_op(
      [t.input0],
      [t.output1]
    )
  
  def Constraints(o, t):
    return True

  def CodeGen(ctx, o, t):
    trivial_code_str = ctx.op_code_gen(
      o.trivial_op,
      loop_index_tuple_expr=IndexTupleExpr.Domain([64]),
      loop_var_names=["threadIdx.x"],
      anchor_local_var_name="x",
      ir_value_to_local_var_name=OrderedDict([
        [t.input0, "x"],
        [t.output0, "y"],
      ]),
      kernel_arg_id_to_arg_name=OrderedDict(),
    )
    print("trivial_code_str:")
    print(trivial_code_str)
    module = ctx.render_module_template(
      "trivial_reduce",
      TRIVIAL_CODE_STRING=trivial_code_str
    )
    return CodeGenResult(
      module=module
    )

  def KernelDispatch(ctx):
    size = ctx.inputs[0].shape[0]
    ctx.launch_cuda(
      "trivial_reduce",
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

@Registry.module_template("trivial_reduce", "cuda", 0)
def ExpSubModuleTemplte(ctx):
  code = """
#include <cstdint>
#define CINN_WITH_CUDA

extern "C" __global__
void trivial_reduce(const int num, const float* input, float* output) {
int idx = blockIdx.x * blockDim.x + threadIdx.x;
__shared__ float buf[1024];
float y;
if (idx < num) {
  float x = input[idx];
  TRIVIAL_CODE_STRING;
  buf[idx] = y;
}
__syncthreads();
if (idx==0) {
  for (int i = 1; i < num; ++i) {
    buf[0] += buf[i];
  }
  output[0] = buf[0];
}
}
"""
  code = code.replace("TRIVIAL_CODE_STRING", ctx.TRIVIAL_CODE_STRING)
  print(code)
  return CodeModule(
    FuncDeclare("trivial_reduce", [
      DataType.const_int32,
      PointerType.const_float_ptr,
      PointerType.float_ptr,
    ]),
    CudaKernelSourceCode(code)
  )

@Registry.op_compute("pd_op.exp", "cuda", 0)
def PdOpExp(inputs, outputs, attrs):
  return f"{outputs[0]} = expf({inputs[0]})"

@Registry.op_compute("pd_op.subtract", "cuda", 0)
def PdOpSubstract(inputs, outputs, attrs):
  return f"{outputs[0]} = {inputs[0]} - {inputs[1]}"

@Registry.op_compute("pd_op.add", "cuda", 0)
def PdOpAdd(inputs, outputs, attrs):
  return f"{outputs[0]} = {inputs[0]} + {inputs[1]}"

@Registry.op_compute("pd_op.multiply", "cuda", 0)
def PdOpAdd(inputs, outputs, attrs):
  return f"{outputs[0]} = {inputs[0]} * {inputs[1]}"

@Registry.op_compute("cinn_op.yield_store", "cuda", 0)
def CinnOpYieldStore(inputs, outputs, attrs):
  return f"{outputs[0]} = {inputs[0]}"

@Registry.op_compute("cinn_op.broadcast", "cuda", 0)
def CinnOpYieldStore(inputs, outputs, attrs):
  return f"{outputs[0]} = {inputs[0]}"
