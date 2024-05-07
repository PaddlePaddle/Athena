from dataclasses import dataclass
import athena.ir.ir_op as ir_op
from athena.ir_converters.paddle_tensor_converter import ConvertToPaddleTensor

@dataclass
class Op(ir_op.Op):
  base_op: ir_op.Op = None
  
  def GetResult(self, i):
    return ConvertToPaddleTensor(ir_op.Op.GetResult(self, i))