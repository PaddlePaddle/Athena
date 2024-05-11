import athena.ir.ir_symbol as ir_symbol
from athena.util.dim_expr_evaluator import DimExprEvaluator

class DimInstanceGenerator:

  def __init__(self, dim_exprs):
    self.dim_exprs = dim_exprs
    symbol_binding_value = self.SearchValidSymbolBindingValue(dim_exprs)
    self.dim_expr_evaluator = DimExprEvaluator(
      lambda name: symbol_binding_value
    )
    self.example_dim = -1

  def GetDimInstance(self, dim_expr):
    dim_instance = self.dim_expr_evaluator.Eval(dim_expr)
    return dim_instance if dim_instance > 0 else self.example_dim

  def SearchValidSymbolBindingValue(self, dim_exprs):
    threshold = 0
    try_cnt = 64
    for i in range(2, try_cnt):
      dim_expr_evaluator = DimExprEvaluator(lambda name: i)
      if self.AllDimExprGreaterThan(threshold, dim_exprs, dim_expr_evaluator):
        return i
    return 0

  def AllDimExprGreaterThan(self, threshold, dim_exprs, dim_expr_evaluator):
    def Ignored(dim_expr):
      if isinstance(dim_expr, ir_symbol.Int64):
        return True
      if isinstance(dim_expr, ir_symbol.Negative):
        return isinstance(dim_expr.operand, ir_symbol.Int64)
      if isinstance(dim_expr, ir_symbol.Reciprocal):
        return isinstance(dim_expr.operand, ir_symbol.Int64)
    for dim_expr in dim_exprs:
      if Ignored(dim_expr):
        continue
      if dim_expr_evaluator.Eval(dim_expr) < threshold:
        return False
    return True