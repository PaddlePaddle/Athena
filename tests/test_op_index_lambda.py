def KernelDefine(ctx):
    return ctx.module(
        ctx.declare_func("relu", [
            ctx.const_float_ptr(),
            ctx.int32(),
            ctx.float_ptr(),
            *ctx.drr_arg_declare("fusion_op0")
        ]),
        ctx.source_code("""
  #include <cstdint>
  #define CINN_WITH_CUDA

  extern "C" __global__
  void relu(const float* input, const int num, float* output FUSION_OP0_ARG_DEFINE) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
   if (idx < num) {
      FUSION_OP0_ARG_COMPUTE(output, input, idx)
      // output[idx] = input[idx] > 0 ? input[idx] : 0;
    }
  }
""".replace("FUSION_OP0_ARG_DEFINE", ctx.drr_arg_def("fusion_op0")))
   .replace("FUSION_OP0_ARG_COMPUTE", ctx.drr_trivial_fusion_compute("fusion_op0", ["blockIdx.x", "threadIdx.x"])))
    )

def KernelDispatch(ctx):
    a = ctx.inputs[0]
    b = ctx.outputs[0]
    a = ctx.drr_input_var("tensor0")
    b = ctx.drr_output_var("tensor1")
    ctx.call('relu',[
        a.data_ptr,
        a.shape[0] * a.shape[1],
        b.data_ptr,
        *ctx.drr_trivial_op_args("fusion_op0")
    ])

def InferFullIntArrayIndexExpr(
    ctx, in_meta, out_meta, in_vars, loop_index_tuple_expr
):
    return OpIndexTupleExprSignature(
        InIndexTupleExprSignature(), OutIndexTupleExprSignature(kIntArrayLikeIndexes)
    )


RegisterOpIndexTupleLambda(
    0,
    InferFullIntArrayIndexExpr,
    "pd_op.full_int_array",
)


def InferReduceIndexExpr(
    ctx, in_meta, out_meta, in_vars, loop_index_tuple_expr
):
    return OpIndexTupleExprSignature(
        InIndexTupleExprSignature(kUndefined, kIntArrayLikeIndexes),
        OutIndexTupleExprSignature(kUndefined),
    )


RegisterOpIndexTupleLambda(
    0,
    InferReduceIndexExpr,
    "pd_op.reduce",
)


def InferReshapeIndexExpr(
    ctx, in_meta, out_meta, in_vars, loop_index_tuple_expr
):
    x_meta, s_meta = in_meta
    y_meta, xs_meta = out_meta
    return OpIndexTupleExprSignature(
        InIndexTupleExprSignature(
            IndexTupleReshape(loop_index_tuple_expr, x_meta.shape),
            kIntArrayLikeIndexes,
        ),
        OutIndexTupleExprSignature(
            IndexTupleReshape(loop_index_tuple_expr, y_meta.shape), kNothing
        ),
    )


RegisterOpIndexTupleLambda(
    0,
    InferReshapeIndexExpr,
    "pd_op.reshape",
)
