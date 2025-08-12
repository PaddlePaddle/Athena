import ap_tpl_codegen

class TrivialTemplateModule:
  def __init__(self, trivial_op_code_gen_class):
    self.class_factory = ap_tpl_codegen.GeneratorClassFactory()
    self.lir_code_gen_ctx_class = ap_tpl_codegen.CudaLikeIrCodeGenCtx
    self.trivial_op_code_gen_class = trivial_op_code_gen_class

  def compile(self, dim0_karg, input0_karg, output0_karg):
    fusion_code_gen = self.trivial_op_code_gen_class(
      class_factory=self.class_factory,
      loop_index_tuple_expr=IndexTupleExpr.Domain([dim0_karg.value]),
      loop_var_names=["threadIdx.x"]
    )
    lir_code_gen_ctx = self.lir_code_gen_ctx_class()
    values = fusion_code_gen.load_from_register(lir_code_gen_ctx, "x", 0)
    values = fusion_code_gen.compute(lir_code_gen_ctx, values)
    values = fusion_code_gen.store_to_register(lir_code_gen_ctx, values, "y", 0)
    print("===================================")
    print("fusion_code_gen.compute(): ", values)
    print("low level ir of fusion_op:\n", lir_code_gen_ctx.get_stmts_joined_str())
    print("===================================")
    trivial_code_str = lir_code_gen_ctx.get_stmts_joined_str()
    module = self.render_template(trivial_code_str)
    print("dim0_karg.runtime_getter\n", dim0_karg.runtime_getter)
    return CodeGenResult(
      module=module,
      kernel_dispatch_func=KernelDispatch,
      kernel_dispatch_const_data=BuiltinSerializableAttrMap(
        kernel_args_getters=[
          dim0_karg.runtime_getter,
          input0_karg.runtime_getter,
          output0_karg.runtime_getter
        ]
      )
    )

  def render_template(self, trivial_code_str):
    code = """
#include <cstdint>
#define CINN_WITH_CUDA

extern "C" __global__
void trivial(const int64_t num, const float* input, float* output) {
  int idx = blockIdx.x * blockDim.x + threadIdx.x;
  if (idx < num) {
    float x = input[idx];
    float y;
    TRIVIAL_CODE_STRING
    output[idx] = y;
  }
}
  """
    code = code.replace("TRIVIAL_CODE_STRING", trivial_code_str)
    print(code)
    return CodeModule(
      FuncDeclare("trivial", [
        DataType.const_int64,
        PointerType.const_float_ptr,
        PointerType.float_ptr,
      ]),
      CudaKernelSourceCode(code)
    )

def KernelDispatch(ctx):
  size = ctx.inputs[0].shape[0]
  def GetArg(getter):
    return getter(ctx)
  ctx.launch_cuda(
    "trivial",
    1,
    size,
    map(GetArg, ctx.kernel_dispatch_const_data.kernel_args_getters)
  )
