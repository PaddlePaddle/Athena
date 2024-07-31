from dataclasses import dataclass
import typing as t
import numpy as np
import paddle
from collections import defaultdict

PrimitiveId = t.TypeVar("PrimitiveId")

TokenId = int


# Repeat Pattern Expression
@dataclass
class RpExpr:
    pass


@dataclass
class ListRpExpr(RpExpr):
    pass


@dataclass
class NaiveTokenListRpExpr(ListRpExpr):
    tensors: t.List[np.ndarray["N", np.int64]]


@dataclass
class TokenizedRpExpr(RpExpr):
    token_id2primitive_id: t.List[PrimitiveId]
    token_tensors: ListRpExpr


@dataclass
class TokenRpExpr(RpExpr):
    pass


@dataclass
class FlattenedTokenListRpExpr(ListRpExpr):
    tensor_list_size: int
    flattened_tensor: TokenRpExpr


@dataclass
class NaiveTokenRpExpr(TokenRpExpr):
    tensor: np.ndarray["N", np.int64]


@dataclass
class LetsTokenRpExpr(TokenRpExpr):
    symbol_token_ids: t.List[TokenId]
    symbol_token_tensors: t.List[np.ndarray["N", np.int64]]
    body_rp_expr: NaiveTokenRpExpr


@dataclass
class LetsListTokenRpExpr(TokenRpExpr):
    symbol_token_ids: t.List[TokenId]
    symbol_token_tensors: t.List[np.ndarray["N", np.int64]]
    body_rp_expr: t.List[np.ndarray["N", np.int64]]


class TokenIdAllocator:
    def __init__(self, next_token_id: int = 0):
        self.next_token_id = next_token_id

    def NewTokenId(self):
        value = self.next_token_id
        self.next_token_id += 1
        return value

    def NextTokenId(self):
        return self.next_token_id

    def Skip(self, size):
        self.next_token_id += size


def Tokenize(
    primitive_id_lists: t.List[t.List[PrimitiveId]],
) -> t.Tuple[TokenizedRpExpr, TokenIdAllocator]:
    token_id_allocator = TokenIdAllocator()
    primitive_id2token_id = defaultdict(token_id_allocator.NewTokenId)
    token_tensors = [
        paddle.to_tensor(
            [primitive_id2token_id[primitive_id] for primitive_id in primitive_id_list],
            paddle.int64,
        )
        for primitive_id_list in primitive_id_lists
    ]
    token_id2primitive_id = [None] * len(primitive_id2token_id)
    for primitive_id, token_id in primitive_id2token_id.items():
        token_id2primitive_id[token_id] = primitive_id
    return (
        NaiveTokenListRpExpr(token_tensors),
        token_id_allocator,
        token_id2primitive_id,
    )
