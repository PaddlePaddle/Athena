from dataclasses import dataclass
import typing as t
import numpy as np

PatternId = int


# Repeat Pattern Expression
@dataclass
class RpExpr:
    pass


@dataclass
class PrimitiveRpExpr(RpExpr):
    primitive_tensor: np.ndarray["N", np.int32]


@dataclass
class FoldRpExpr(RpExpr):
    fold_tensor: np.ndarray["N", np.int32]


@dataclass
class LetsListRpExpr(RpExpr):
    symbol_pattern_ids: t.List[PatternId]
    symbol_rp_exprs: t.Union[t.List[PrimitiveRpExpr], "LetsListRpExpr"]
    body_rp_expr: t.List[FoldRpExpr]


@dataclass
class LetsRpExpr(RpExpr):
    symbol_pattern_ids: t.List[PatternId]
    symbol_rp_exprs: t.Union[t.List[PrimitiveRpExpr], LetsListRpExpr]
    body_rp_expr: t.Union[FoldRpExpr, "LetsRpExpr"]


class PatternIdAllocator:
    def __init__(self, next_pattern_id: int):
        self.next_pattern_id = next_pattern_id

    def NewPatternId(self):
        value = self.next_pattern_id
        self.next_pattern_id += 1
        return value


def TrivialParse(
    primitive_ids: t.List[int],
) -> t.Tuple[PrimitiveRpExpr, PatternIdAllocator]:
    primitive_tensor = np.array(primitive_ids, dtype=np.int32)
    min_pattern_id = int(np.min(primitive_tensor))
    assert min_pattern_id >= 0
    return PrimitiveRpExpr(primitive_tensor), PatternIdAllocator(min_pattern_id + 1)
