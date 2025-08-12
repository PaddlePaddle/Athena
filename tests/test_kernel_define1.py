
def GetterN(ctx):
      return ctx.tensor.tensor0.shape[0]

def GetInput0DataPtr(ctx):
    return ctx.tensor.input0.data_ptr

def GetInput0Dim0(ctx):
    return ctx.tensor.input0.shape[0]

def GetOutput0DataPtr(ctx):
    return ctx.tensor.output0.data_ptr

def KernelDefine(ctx):
    ctx.register_kernel_arg("N", KernelArg(DataType.int64, GetterN.__code__))
    code0 = ctx.cuda_code_gen(
        ctx.op.trivial_op1,
        loop_index_tuple_expr=IndexTupleExpr([ctx.kernel_arg.N]),
        loop_var_names=["i", "j", "k"],
        local_var_name_bindings=[
            ["x0", ctx.tensor.input0],
            ["y0", ctx.tensor.output0]
        ],
        anchor_local_var_name="x0"
    )
    return CodeModule(
        FuncDeclare("relu", [
            KernelArg(PointerType.const_float_ptr, GetInput0DataPtr.__code__)
            KernelArg(DataType.const_int32, GetInput0Dim0.__code__)
            KernelArg(PointerType.float_ptr, GetOutput0DataPtr.__code__)
        ]),
        CudaKernelSourceCode(
"""
#include <cstdint>
#define CINN_WITH_CUDA

extern "C" __global__
void relu(const float* input, const int num, float* output, KERNEL_ARGS) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    if (idx < num) {
        output[idx] = input[idx] > 0 ? input[idx] : 0;
    }
}
""".replace(KERNEL_ARGS, ctx.get_registered_kernel_arg_declares())
        )
    )