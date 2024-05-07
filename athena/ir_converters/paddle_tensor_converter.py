import athena.ir.ir_type as ir_type
import athena.ir.ir_tensor as ir_tensor
import athena.ir_converters.paddle_type_converter as paddle_type_converter

def ConvertToPaddleTensor(tensor):
  return getattr(PaddleTensorConverter, type(tensor.type).__name__)(tensor)

class PaddleTensorConverter:

  @classmethod
  def DenseTensorType(cls, tensor):
    return ir_tensor.Tensor(
      local_name_prefix=tensor.local_name_prefix,
      name=tensor.name,
      type=ir_type.DenseTensorType(
        tensor.shape,
        paddle_type_converter.ConvertTypeToString(tensor.dtype)
      )
    )

  @classmethod
  def VectorType(cls, tensor):
    return ir_tensor.Tensor(
      local_name_prefix=tensor.local_name_prefix,
      name=tensor.name,
      type=ir_type.VectorType(
        value=[
          ir_type.DenseTensorType(
            t.shape,
            paddle_type_converter.ConvertTypeToString(t.dtype)
          )
          for t in tensor.type.value
        ]
      )
    )
