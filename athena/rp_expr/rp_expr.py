from dataclasses import dataclass
import typing as t

PrimitiveId = t.TypeVar('PrimitiveId')
PatternId = int

# Repeat Pattern Expression
@dataclass
class RpExpr:
  pass

@dataclass
class PrimitiveRpExpr(RpExpr):
  # len(pattern_ids) == len(primitive_ids)
  pattern_ids: t.List[PatternId]
  primitive_ids: t.List[PrimitiveId]

@dataclass
class SymbolRpExpr(RpExpr):
  symbol_pattern_id: PatternId

@dataclass
class ConcatenatedSymbolRpExpr(RpExpr):
  children: t.List[SymbolRpExpr]

@dataclass
class LetsListRpExpr(RpExpr):
  symbol_pattern_ids: t.List[PatternId]
  symbol_rp_exprs: t.Union[t.List[PrimitiveRpExpr], 'LetsListRpExpr']
  body_rp_expr: t.List[ConcatenatedSymbolRpExpr]

@dataclass
class LetsRpExpr(RpExpr):
  symbol_pattern_ids: t.List[PatternId]
  symbol_rp_exprs: t.Union[t.List[PrimitiveRpExpr], LetsListRpExpr]
  body_rp_expr: t.Union[ConcatenatedSymbolRpExpr, 'LetsRpExpr']


class PatternIdAllocator:
  def __init__(self):
    self.next_pattern_id: int = 0
    self.primitive_id2pattern_id: t.Dict[PrimitiveId, PatternId] = {}

  def NewPatternId(self):
    value = self.next_pattern_id
    self.next_pattern_id += 1
    return value

  def GetOrAllocatePatternId(primitive_id: PrimitiveId):
    if primitive_id not in self.primitive_id2pattern_id:
      self.primitive_id2pattern_id[primitive_id] = self.NewPatternId()
    return self.primitive_id2pattern_id[primitive_id]

def TrivialParse(
  primitive_ids: t.List[PrimitiveId]
) -> t.Tuple[PrimitiveRpExpr, PatternIdAllocator]:
  pattern_id_allocator = PatternIdAllocator()
  pattern_ids = [
    pattern_id_allocator.GetOrAllocatePatternId(primitive_id)
    for primitive_id in primitive_ids
  ]
  primitive_rp_expr = PrimitiveRpExpr(
    pattern_ids=pattern_ids,
    primitive_ids=primitive_ids,
  )
  return primitive_rp_expr, pattern_id_allocator