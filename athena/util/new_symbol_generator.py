import athena.ir.ir_symbol as ir_symbol 

class NewSymbolGenerator:
  
  def Mangle(self, dim_expr):
    short_str = dim_expr.GetShortStr()
    return ir_symbol.String(f"({short_str})")