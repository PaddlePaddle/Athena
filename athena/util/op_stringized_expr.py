from dataclasses import dataclass
from athena.util.hash_combine import hash_combine

@dataclass
class OpStringizedExpr:
  op_name: str
  op_expr: str
  input_name_prefix: str
  num_results: int

  def __hash__(self):
    hash_value = hash(self.op_name)
    hash_value = hash_combine(hash_value, hash(self.op_expr))
    hash_value = hash_combine(hash_value, hash(self.input_name_prefix))
    hash_value = hash_combine(hash_value, hash(self.num_results))
    return hash_value