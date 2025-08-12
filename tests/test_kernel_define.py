def KernelDefine(ctx):
    return ctx.module(
        ctx.declare_func("relu", [
            ctx.const_float_ptr,
            ctx.const_int32,
            ctx.float_ptr,
        ]),
        ctx.source_code(
"""
#include <cstdint>
#define CINN_WITH_CUDA

extern "C" __global__
void relu(const float* input, const int num, float* output, ) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    if (idx < num) {
        output[idx] = input[idx] > 0 ? input[idx] : 0;
    }
}
"""
        )
    )