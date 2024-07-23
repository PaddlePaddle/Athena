import unittest
from athena.util.valid_example_inputs_solver import ValidExampleInputsSolver
from athena.traits.symbol_trait import SymbolTrait
from athena.traits.constaint_trait import ConstraintTrait


class TestValidExampleInputsSolver(unittest.TestCase, SymbolTrait, ConstraintTrait):

    def SetUp(self):
        self.clear_all_cstrs()

    def test_eq_constraint(self):
        kLimit = 8
        solver = ValidExampleInputsSolver(
            constrained_dim_size_limit=kLimit,
            independent_dim_size_limit=kLimit,
        )
        self.add_eq_cstr(self.s_str("S0"), self.s_str("S1"))
        result = solver.Solve(
            input_names=["S0", "S1"],
            constraints=self.CollectConstraints(),
        )
        self.assertEqual(result.example_input_dims.shape[0], kLimit)

    def test_two_symbol_independence(self):
        kLimit = 4
        solver = ValidExampleInputsSolver(
            constrained_dim_size_limit=kLimit,
            independent_dim_size_limit=kLimit,
        )
        result = solver.Solve(
            input_names=["S0", "S1"],
            constraints=[],
        )
        self.assertEqual(result.example_input_dims.shape[0], kLimit * kLimit * 2)

    def test_three_symbol_independence(self):
        kLimit = 4
        solver = ValidExampleInputsSolver(
            constrained_dim_size_limit=kLimit,
            independent_dim_size_limit=kLimit,
        )
        result = solver.Solve(
            input_names=["S0", "S1", "S2"],
            constraints=[],
        )
        self.assertEqual(result.example_input_dims.shape[0], kLimit * kLimit * 3)

    def test_four_symbol_independence(self):
        kLimit = 4
        solver = ValidExampleInputsSolver(
            constrained_dim_size_limit=kLimit,
            independent_dim_size_limit=kLimit,
        )
        result = solver.Solve(
            input_names=["S0", "S1", "S2", "S3"],
            constraints=[],
        )
        self.assertEqual(result.example_input_dims.shape[0], kLimit * kLimit * 4)

    def test_add_constraint(self):
        kLimit = 8
        solver = ValidExampleInputsSolver(
            constrained_dim_size_limit=kLimit,
            independent_dim_size_limit=kLimit,
        )
        self.add_eq_cstr(
            self.s_str("S0"), self.s_add(self.s_str("S1"), self.s_str("S2"))
        )
        result = solver.Solve(
            input_names=["S0", "S1", "S2"],
            constraints=self.CollectConstraints(),
        )
        self.assertEqual(result.example_input_dims.shape[0], kLimit)

    def test_mul_constraint(self):
        kLimit = 8
        solver = ValidExampleInputsSolver(
            constrained_dim_size_limit=kLimit,
            independent_dim_size_limit=kLimit,
        )
        self.add_eq_cstr(
            self.s_mul(self.s_str("S0"), self.s_str("S1")),
            self.s_mul(self.s_str("S2"), self.s_str("S3")),
        )
        result = solver.Solve(
            input_names=["S0", "S1", "S2", "S3"],
            constraints=self.CollectConstraints(),
        )
        self.assertEqual(result.example_input_dims.shape[0], kLimit)

    def test_broadcast_constraint(self):
        kLimit = 32
        solver = ValidExampleInputsSolver(
            constrained_dim_size_limit=kLimit,
            independent_dim_size_limit=kLimit,
        )
        self.add_broadcastable_cstr(
            self.s_str("S0"),
            self.s_str("S1"),
        )
        self.add_broadcastable_cstr(
            self.s_str("S1"),
            self.s_str("S2"),
        )
        result = solver.Solve(
            input_names=["S0", "S1", "S2"],
            constraints=self.CollectConstraints(),
        )
        self.assertEqual(result.example_input_dims.shape[0], kLimit)


if __name__ == "__main__":
    unittest.main()
