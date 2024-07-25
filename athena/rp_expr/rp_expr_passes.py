from dataclasses import dataclass
import typing as t
import numpy as np
import re
import itertools
import paddle
import paddle.nn.functional as F
import math
from athena.rp_expr.rp_expr import (
    TokenIdAllocator,
    NaiveTokenListRpExpr,
    FlattenedTokenListRpExpr,
    NaiveTokenRpExpr,
    LetsTokenRpExpr,
)
import itertools

class Pass:
    pass

class FlattenTokenListPass(Pass):
    def __init__(self, id_allocator: TokenIdAllocator):
        self.id_allocator = id_allocator

    def __call__(self, token_tensors_rp_expr: NaiveTokenListRpExpr):
        tensor_list_size = len(token_tensors_rp_expr.tensors)
        self.id_allocator.Skip(tensor_list_size)
        def GetSepTensor(i):
            if i == 0:
                return []
            return [paddle.to_tensor([i], paddle.int64)]
        token_tensors = [
            tensor
            for i, token_tensor in enumerate(token_tensors_rp_expr.tensors)
            for tensor in GetSepTensor(i) + [token_tensor + tensor_list_size]
        ]
        return True, FlattenedTokenListRpExpr(
            tensor_list_size=tensor_list_size,
            flattened_tensor=NaiveTokenRpExpr(
                tensor=paddle.concat(token_tensors, axis=0),
            ),
        )


class FoldTokensPass(Pass):
    def __init__(self, id_allocator: TokenIdAllocator):
        self.max_windows_size = 64
        self.id_allocator = id_allocator
        size = id_allocator.NextTokenId()
        self.embedding = paddle.uniform([size], dtype='float64', min=-1, max=1)
        self.embedding.stop_gradient = False

    def __call__(self, token_tensor: NaiveTokenRpExpr):
        input_tensor = token_tensor.tensor
        most_frequent_length, indexes = self.GetMostFrequentPatternLengthAndIndexes(
            input_tensor
        )
        new_token_id = self.id_allocator.NewTokenId()
        success, replacement = self.Replace(
            pattern_length=most_frequent_length,
            indexes=indexes,
            new_token_id=new_token_id,
            input_tensor=input_tensor,
        )
        if not success:
            return False, token_tensor
        start = indexes[0]
        return True, LetsTokenRpExpr(
            symbol_token_ids=[new_token_id],
            symbol_token_tensors=[input_tensor[start:(start + most_frequent_length)]],
            body_rp_expr=NaiveTokenRpExpr(tensor=replacement),
        )

    def Replace(
        self,
        pattern_length,
        indexes,
        new_token_id,
        input_tensor: np.ndarray["N", np.int64],
    ) -> t.Tuple[bool,  np.ndarray["N", np.int64]]:
        new_token_tensor = paddle.to_tensor([new_token_id], paddle.int64)
        num_tokens = input_tensor.shape[0]
        if pattern_length == 1:
            return False, input_tensor
        assert indexes.shape[0] > 0
        disjoint_range_starts = [
            start
            for start in self.GetDisjoint(pattern_length, indexes.numpy().tolist())
        ]
        if len(disjoint_range_starts) <= 1:
            return False, input_tensor
        assert disjoint_range_starts[-1] + pattern_length <= num_tokens
        first_start = disjoint_range_starts[0]
        pattern_tensor = input_tensor[first_start:(first_start + pattern_length)]
        segment_starts = [0] + [
            index
            for start in disjoint_range_starts
            for index in [start, start + pattern_length]
        ] + [num_tokens]
        uniqued_segment_starts = paddle.unique(paddle.to_tensor(segment_starts))
        segment_lengths = paddle.diff(uniqued_segment_starts).numpy().tolist()
        def ReplaceTensor(tensor):
            if tensor.shape != pattern_tensor.shape:
                return tensor
            if bool(paddle.all(tensor == pattern_tensor)):
                return new_token_tensor
            return tensor
        replaced_segment_tensors = [
            ReplaceTensor(tensor)
            for tensor in paddle.split(input_tensor, segment_lengths)
        ]
        output_tensor = paddle.concat(replaced_segment_tensors)
        return True, output_tensor

    def GetConv(self, num_tokens):
        windows_size = min(num_tokens, self.max_windows_size)
        weight = paddle.uniform(
            [windows_size, windows_size],
            dtype='float64',
            min=-1,
            max=1
        )
        weight.stop_gradient = False
        weight_shape = (windows_size, 1, windows_size)
        conv_weight = paddle.triu(weight).transpose([1, 0]).reshape(weight_shape)
        conv = lambda input: F.conv1d(input, conv_weight, padding='VALID')
        return conv, windows_size

    def GetDisjoint(self, gap, indexes):
        if len(indexes) == 0:
            return
        last = indexes[0]
        yield last
        for current in indexes:
            if current >= (last + gap):
                yield current
                last = current

    def GetMostFrequentPatternLengthAndIndexes(
        self,
        token_tensor: np.ndarray["N", np.int64],
    ):
        conv, windows_size = self.GetConv(num_tokens=token_tensor.shape[0])
        input = paddle.gather(self.embedding, token_tensor)
        input.stop_gradient = False
        zeros = paddle.zeros([windows_size - 1], paddle.float64)
        input = paddle.concat([input, zeros])
        input = input.reshape((1, 1, -1))
        y = conv(input)
        y = y.reshape((windows_size, -1))
        y_hash = y.view(paddle.int64)
        hash_weight = paddle.arange(windows_size).reshape((-1, 1)).expand(y_hash.shape)
        weighted_y_hash = paddle.concat(
            [hash_weight.reshape((-1, 1)), y_hash.reshape((-1, 1))],
            axis=1
        )
        unique_weighted_hash, counts = paddle.unique(
            weighted_y_hash,
            axis=0,
            return_counts=True
        )
        most_frequent_hash_idx = paddle.argmax(unique_weighted_hash[:, 0] * (counts - 1))
        most_frequent_hash = int(unique_weighted_hash[most_frequent_hash_idx, 1])
        most_frequent_hash_weight = int(unique_weighted_hash[most_frequent_hash_idx, 0])
        indexes, = paddle.where(most_frequent_hash == y_hash[most_frequent_hash_weight, :])
        indexes = indexes.reshape((-1,))
        return most_frequent_hash_weight + 1, indexes

class RecursiveFoldTokensPass(Pass):
    def __init__(self, id_allocator: TokenIdAllocator):
        self.id_allocator = id_allocator

    def __call__(self, token_tensor: NaiveTokenRpExpr):
        success, ret = FoldTokensPass(self.id_allocator)(token_tensor)
        if not success:
            return False, token_tensor
        symbol_token_ids = ret.symbol_token_ids
        symbol_token_tensors = ret.symbol_token_tensors
        token_tensor = ret.body_rp_expr
        counter = itertools.count()
        kLimit = 9999999
        while True:
            success, ret = FoldTokensPass(self.id_allocator)(token_tensor)
            if not success:
                token_tensor = ret
                break
            assert ret.body_rp_expr.tensor.shape[0] < token_tensor.tensor.shape[0]
            if next(counter) > kLimit:
                raise RuntimeError("dead loop detected.")
            symbol_token_ids += ret.symbol_token_ids
            symbol_token_tensors += ret.symbol_token_tensors
            token_tensor = ret.body_rp_expr
        return True, LetsTokenRpExpr(
            symbol_token_ids=symbol_token_ids,
            symbol_token_tensors=symbol_token_tensors,
            body_rp_expr=token_tensor,
        )
