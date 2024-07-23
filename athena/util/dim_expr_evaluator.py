import athena.ir.ir_symbol as ir_symbol


class DimExprEvaluator:

    def __init__(self, get_symbol_binding):
        self.get_symbol_binding = get_symbol_binding

    def Eval(self, dim_expr):
        return getattr(self, f"{type(dim_expr).__name__}")(dim_expr)

    def Int64(self, dim_expr):
        return int(dim_expr.value)

    def String(self, dim_expr):
        return int(self.get_symbol_binding(dim_expr.value))

    def Negative(self, dim_expr):
        return int(-self.Eval(dim_expr.operand))

    def Reciprocal(self, dim_expr):
        raise NotImplementedError("Invalid DimExpr")

    def Add(self, dim_expr):
        dim_instance = 1
        for operand in dim_expr.operands:
            if isinstance(operand, ir_symbol.Negative):
                dim_instance -= self.Eval(operand.operand)
            else:
                dim_instance += self.Eval(operand)
        return int(dim_instance)

    def Mul(self, dim_expr):
        dim_instance = 1
        for operand in dim_expr.operands:
            if isinstance(operand, ir_symbol.Reciprocal):
                dim_instance //= self.Eval(operand.operand)
            else:
                dim_instance *= self.Eval(operand)
        return int(dim_instance)

    def Max(self, dim_expr):
        return max(*[self.Eval(operand) for operand in dim_expr.operands])

    def Min(self, dim_expr):
        return min(*[self.Eval(operand) for operand in dim_expr.operands])

    def Broadcast(self, dim_expr):
        return max(*[self.Eval(operand) for operand in dim_expr.operands])
