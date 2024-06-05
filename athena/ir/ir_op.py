from dataclasses import dataclass, field
import athena.ir.ir_tensor as ir_tensor
import typing as t

@dataclass
class Op:
  name: str
  op_id: int
  input_types: list
  output_types: list
  attrs: dict
  block_positional_arg_names: t.Optional[t.List[t.List[t.List[str]]]]
  block_keyword_arg_names: t.Optional[t.List[t.List[t.List[str]]]]
  block_positional_arg_types: t.Optional[t.List[t.List[t.List["Type"]]]]
  block_keyword_arg_types: t.Optional[t.List[t.List[t.List["Type"]]]]
  __operands_symbols_signature__: "ArrayAttribute" = None
  __results_symbols_signature__: "ArrayAttribute" = None

  def GetResults(self):
    return [self.GetResult(i) for i in range(len(self.output_types))]

  def GetResult(self, i):
    return ir_tensor.Tensor(
      local_name_prefix=self.GetNameSuffix(),
      name=self.GetResultTensorName(i),
      arg_name_as_input=self.GetArgNameAsInput(),
      type=self.output_types[i],
      dim_exprs=self.__results_symbols_signature__.value[i].value
    )

  def GetArgNameAsInput(self):
    if self.name == 'pd_op.data':
      return self.attrs['name'].value
    if self.name == 'builtin.parameter':
      return self.attrs['name'].value
    return None
  
  def GetResultTensorName(self, i):
    return f"{self.GetUniqueName()}{i}"

  def GetUniqueName(self):
    return f"{self.GetNameSuffix()}_{self.op_id}"

  def GetPyVarName(self):
    return "_".join(self.GetValidPyVarNameComponents())

  def GetNameSuffix(self):
    return self.GetValidPyVarNameComponents()[-1]

  def GetValidPyVarNameComponents(self):
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
