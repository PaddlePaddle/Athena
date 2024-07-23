import unittest
import athena.ir.ir_symbol as ir_symbol
from athena.util.global_dim_expr_converter import (
    SingleDimExprSimplifier,
    MultiDimExprSimplifier,
    GlobalDimExprConverter,
)


class TestSingleDimExprSimplifier(unittest.TestCase):

    def test_naive(self):
        simplifier = SingleDimExprSimplifier()
        key2dim_expr = dict(
            a=ir_symbol.Add([ir_symbol.String("S0"), ir_symbol.Int64(1)]),
            b=ir_symbol.Add([ir_symbol.String("S0"), ir_symbol.Int64(1)]),
        )
        key2dim_expr = simplifier.Simplify(key2dim_expr)
        self.assertEqual(key2dim_expr["a"], ir_symbol.String("(S0+1)"))
        self.assertEqual(key2dim_expr["b"], ir_symbol.String("(S0+1)"))

    def test_nested(self):
        simplifier = SingleDimExprSimplifier()
        pattern_dim_expr = ir_symbol.Add([ir_symbol.String("S0"), ir_symbol.Int64(1)])
        key2dim_expr = dict(
            a=pattern_dim_expr,
            b=ir_symbol.Negative(pattern_dim_expr),
        )
        key2dim_expr = simplifier.Simplify(key2dim_expr)
        result = ir_symbol.String("(S0+1)")
        self.assertEqual(key2dim_expr["a"], result)
        self.assertEqual(key2dim_expr["b"], ir_symbol.Negative(result))

    def test_no_simplify(self):
        simplifier = SingleDimExprSimplifier()
        key2origin_dim_expr = dict(
            a=ir_symbol.Add([ir_symbol.String("S0"), ir_symbol.Int64(1)]),
            b=ir_symbol.Mul([ir_symbol.String("S0"), ir_symbol.Int64(1)]),
        )
        key2dim_expr = simplifier.Simplify(key2origin_dim_expr)
        self.assertEqual(key2dim_expr["a"], key2origin_dim_expr["a"])
        self.assertEqual(key2dim_expr["b"], key2origin_dim_expr["b"])


class TestMultiDimExprSimplifier(unittest.TestCase):

    def test_naive(self):
        simplifier = MultiDimExprSimplifier()
        key2dim_expr = dict(
            a=ir_symbol.Add([ir_symbol.String("S0"), ir_symbol.String("S1")]),
            b=ir_symbol.Add([ir_symbol.String("S0"), ir_symbol.String("S1")]),
        )
        key2dim_expr = simplifier.Simplify(key2dim_expr)
        self.assertEqual(key2dim_expr["a"], ir_symbol.String("(S0+S1)"))
        self.assertEqual(key2dim_expr["b"], ir_symbol.String("(S0+S1)"))

    def test_S0S1S2_S0S1(self):
        simplifier = MultiDimExprSimplifier()
        operands = [ir_symbol.String("S0"), ir_symbol.String("S1")]
        key2dim_expr = dict(
            a=ir_symbol.Mul([*operands, ir_symbol.String("S2")]),
            b=ir_symbol.Mul(operands),
        )
        key2dim_expr = simplifier.Simplify(key2dim_expr)
        self.assertEqual(
            key2dim_expr["a"],
            ir_symbol.Mul([ir_symbol.String("(S0*S1)"), ir_symbol.String("S2")]),
        )
        self.assertEqual(key2dim_expr["b"], ir_symbol.String("(S0*S1)"))


class TestGlobalDimExprConverter(unittest.TestCase):

    def test_naive(self):
        dim_expr0 = ir_symbol.Add(
            [
                ir_symbol.Mul(
                    [
                        ir_symbol.Add(
                            [
                                ir_symbol.String("S0"),
                                ir_symbol.Negative(ir_symbol.Int64(1)),
                            ]
                        ),
                        ir_symbol.Reciprocal(ir_symbol.Int64(2)),
                    ]
                ),
                ir_symbol.Int64(1),
            ]
        )
        dim_expr1 = ir_symbol.String("S1")
        a = ir_symbol.Mul(
            [
                dim_expr0,
                dim_expr1,
            ]
        )
        b = ir_symbol.Mul(
            [
                dim_expr0,
                dim_expr1,
                ir_symbol.Int64(64),
            ]
        )
        converter = GlobalDimExprConverter([a, b])
        self.assertEqual(
            converter.GetLocalDimExpr(a),
            ir_symbol.String("(((S0-1)/2+1)*S1)"),
        )

        self.assertEqual(
            converter.GetLocalDimExpr(b),
            ir_symbol.Mul(
                [
                    ir_symbol.String("(((S0-1)/2+1)*S1)"),
                    ir_symbol.Int64(64),
                ]
            ),
        )


if __name__ == "__main__":
    unittest.main()
