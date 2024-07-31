import typing as t
import numpy as np
from athena.rp_expr.rp_expr import Tokenize, PrimitiveId, LetsListTokenRpExpr
from athena.rp_expr.rp_expr_passes import (
    FlattenTokenListPass,
    FoldTokensPass,
    RecursiveFoldTokensPass,
    FoldIfTokenIdGreatEqualPass,
)


class RpExprParser:
    def __init__(self):
        pass

    def __call__(self, primitive_id_lists: t.List[t.List[PrimitiveId]]):
        token_list, id_allocator, token_id2primitive_id = Tokenize(primitive_id_lists)
        flatten_pass = FlattenTokenListPass(id_allocator)
        success, flattened_rp_expr = flatten_pass(token_list)
        assert success
        fold_pass = RecursiveFoldTokensPass(id_allocator)
        success, fold_rp_expr = fold_pass(flattened_rp_expr.flattened_tensor)
        assert success
        threshold = len(primitive_id_lists)
        threshold_fold_pass = FoldIfTokenIdGreatEqualPass(
            id_allocator=id_allocator,
            threshold_start_token_id=threshold,
        )
        success, threshold_fold_rp_expr = threshold_fold_pass(fold_rp_expr.body_rp_expr)
        assert success
        threshold_fold_rp_expr = self.MergeAndUnflatten(
            fold_rp_expr, threshold_fold_rp_expr, threshold
        )
        return threshold_fold_rp_expr, token_id2primitive_id

    def MergeAndUnflatten(self, fold_rp_expr, threshold_fold_rp_expr, threshold):
        assert len(threshold_fold_rp_expr.body_rp_expr) == threshold
        return LetsListTokenRpExpr(
            symbol_token_ids=[
                x - threshold
                for x in (
                    fold_rp_expr.symbol_token_ids
                    + threshold_fold_rp_expr.symbol_token_ids
                )
            ],
            symbol_token_tensors=[
                x - threshold
                for x in (
                    fold_rp_expr.symbol_token_tensors
                    + threshold_fold_rp_expr.symbol_token_tensors
                )
            ],
            body_rp_expr=[x - threshold for x in threshold_fold_rp_expr.body_rp_expr],
        )
