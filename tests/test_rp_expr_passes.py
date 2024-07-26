import unittest
from athena.rp_expr.rp_expr import Tokenize
from athena.rp_expr.rp_expr_passes import (
    FlattenTokenListPass,
    FoldTokensPass,
    RecursiveFoldTokensPass,
)


class TestTokenize(unittest.TestCase):

    def test_simple(self):
        primitive_id_lists = [list(range(10 + i)) for i in range(5)]
        token_list, id_allocator = Tokenize(primitive_id_lists)
        self.assertEqual(len(token_list.tensors), len(primitive_id_lists))


class TestFlattenTokenListPass(unittest.TestCase):

    def test_simple(self):
        base = 10
        size = 5
        primitive_id_lists = [list(range(base + i)) for i in range(size)]
        token_list, id_allocator = Tokenize(primitive_id_lists)
        rp_expr_pass = FlattenTokenListPass(id_allocator)
        success, flattened_rp_expr_pass = rp_expr_pass(token_list)
        self.assertTrue(success)
        self.assertEqual(id_allocator.NextTokenId(), base + 2 * size - 1)


class TestFoldTokensPass(unittest.TestCase):

    def test_simple(self):
        base = 3
        size = 3
        primitive_id_lists = [list(range(base + i)) for i in range(size)]
        token_list, id_allocator = Tokenize(primitive_id_lists)
        flatten_pass = FlattenTokenListPass(id_allocator)
        _, flattened_rp_expr = flatten_pass(token_list)
        fold_pass = FoldTokensPass(id_allocator)
        success, fold_rp_expr = fold_pass(flattened_rp_expr.flattened_tensor)
        self.assertTrue(success)
        input = flattened_rp_expr.flattened_tensor.tensor.numpy().tolist()
        pattern = fold_rp_expr.symbol_token_tensors[0].numpy().tolist()
        replacement = fold_rp_expr.symbol_token_ids[0]
        output = fold_rp_expr.body_rp_expr.tensor.numpy().tolist()
        self.assertEqual(input, [3, 4, 5, 1, 3, 4, 5, 6, 2, 3, 4, 5, 6, 7])
        self.assertEqual(pattern, [3, 4, 5])
        self.assertEqual(replacement, 8)
        self.assertEqual(output, [8, 1, 8, 6, 2, 8, 6, 7])


class TestRecursiveFoldTokensPass(unittest.TestCase):

    def test_simple(self):
        base = 3
        size = 3
        primitive_id_lists = [list(range(base + i)) for i in range(size)]
        token_list, id_allocator = Tokenize(primitive_id_lists)
        flatten_pass = FlattenTokenListPass(id_allocator)
        _, flattened_rp_expr = flatten_pass(token_list)
        fold_pass = RecursiveFoldTokensPass(id_allocator)
        success, fold_rp_expr = fold_pass(flattened_rp_expr.flattened_tensor)
        self.assertTrue(success)
        input = flattened_rp_expr.flattened_tensor.tensor.numpy().tolist()
        pattern = [x.numpy().tolist() for x in fold_rp_expr.symbol_token_tensors]
        replacement = fold_rp_expr.symbol_token_ids
        output = fold_rp_expr.body_rp_expr.tensor.numpy().tolist()
        self.assertEqual(input, [3, 4, 5, 1, 3, 4, 5, 6, 2, 3, 4, 5, 6, 7])
        self.assertEqual(pattern, [[3, 4, 5], [8, 6]])
        self.assertEqual(replacement, [8, 9])
        self.assertEqual(output, [8, 1, 9, 2, 9, 7])


if __name__ == "__main__":
    unittest.main()
