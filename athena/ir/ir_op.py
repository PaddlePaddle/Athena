from dataclasses import dataclass, field
import athena.ir.ir_tensor as ir_tensor

@dataclass
class Op:
  name: str
  op_id: int
  input_types: list
  output_types: list
  attrs: dict
  block_positional_arg_names: list = field(
    default_factory=lambda:[[]]
  )
  block_keyword_arg_names: list = field(
    default_factory=lambda:[[]]
  )

  def GetResults(self):
    return [self.GetResult(i) for i in range(len(self.output_types))]

  def GetResult(self, i):
    return ir_tensor.Tensor(
      local_name_prefix=self.GetNameSuffix(),
      name=self.GetResultTensorName(i),
      type=self.output_types[i],
    )
  
  def GetResultTensorName(self, i):
    return f"{self.GetUniqueName()}{i}"

  def GetUniqueName(self):
    return f"{self.GetNameSuffix()}_{self.op_id}"

  def GetPyVarName(self):
    return "_".join(self._GetValidPyVarNameComponents())

  def GetNameSuffix(self):
    return self._GetValidPyVarNameComponents()[-1]

  def _GetValidPyVarNameComponents(self):
    def IsValidVarChar(ch):
      return (
        (ch >= 'a' and ch <= 'z')
        or (ch >= 'A' and ch <= 'Z')
        or (ch >= '0' and ch <= '9')
        or ch == "_"
      )
    ret = ""
    for i in range(len(self.name)):
      ret += self.name[i] if IsValidVarChar(self.name[i]) else ":" 
    return ret.split(":")
