from athena.generators.operands_symbols_signature_generator import (
  OperandsSymbolsSignatureGenerator
)
import os

dirname = os.path.dirname(__file__)
generator = OperandsSymbolsSignatureGenerator(f"{dirname}/pir-group-op-programs.py")

for signature in generator.Generate():
  print(' '*80)
  print("op_expr=", signature.op_expr)
  print("operands_symbols_signature=", signature.operands_symbols_signature)
  print("constraints=", signature.constraints)
