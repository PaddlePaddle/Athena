from dataclasses import dataclass
import typing as t
import numpy as np
import re
import itertools

PrimitiveId = int

@dataclass
class PatternTree:
  pass

@dataclass
class PrimitivePattern(PatternTree):
  value: PrimitiveId

@dataclass
class TrivialPattern(PatternTree):
  children: t.List[PrimitivePattern]

@dataclass
class RepeatedPattern:
  repeated_count: int
  value: PatternTree

@dataclass
class TuplePattern(PatternTree):
  children: t.List[RepeatedPattern]

class RepeatPatternsParser:
  def __init__(
    self,
    window_size: int = 4096,
  ):
    self.window_size = window_size

  def Parse(
    self,
    primitive_ids: t.List[PrimitiveId],
  ) -> t.Optional[PatternTree]:
    if len(primitive_ids) == 0:
      return None
    kThreshold = 4096
    loop_count = itertools.count()
    pattern_tree = self.ConvertPrimitiveIdsToPatternTree(primitive_ids)
    while True:
      if next(loop_count) >= kThreshold:
        raise RuntimeError("Dead loop detected.")
      (
        pattern_tree_from_trivial,
        replace_ctx
      ) = self.ConvertPrimitivePatternsToPatternTree(pattern_tree)
      if isinstance(pattern_tree_from_trivial, TrivialPattern):
        break
      pattern_tree = self.ReplaceTrivialPatterns(
        pattern_tree,
        pattern_tree_from_trivial,
        replace_ctx
      )

  def ConvertPrimitiveIdsToPatternTree(
    self,
    primitive_ids: t.List[PrimitiveId],
  ) -> t.Optional[PatternTree]:
    if len(primitive_ids) == 0:
      return None
    ctx = ParserCtx.InitFromPrimitiveIds(primitive_ids)
    while len(ctx.pattern_ids) > 1:
      ctx = ctx.ReduceFrequentest(
        window_size=self.window_size,
      )
    return ctx.id2pattern_tree[int(ctx.pattern_ids[0])]

@dataclass
class ParserCtx:
  pattern_ids: np.ndarray[("N",), np.int32]
  id2pattern_tree: t.Dict[int, PatternTree]
  make_new_pattern_id: Callable[[], int]

  @classmethod
  def InitFromPrimitiveIds(cls, primitive_ids: t.List[PrimitiveId]):
    primitive2pattern_id = {}
    id2pattern_tree = {}
    max_pattern_id = 0
    def GetOrCreatePatternId(primitive_id: PrimitiveId):
      nonlocal max_pattern_id
      if primitive_id not in primitive2pattern_id:
        new_pattern_id = max_pattern_id
        primitive2pattern_id[primitive_id] = new_pattern_id
        id2pattern_tree[new_pattern_id] = PrimitivePattern(primitive_id)
        max_pattern_id += 1
      return primitive2pattern_id[primitive_id]
    pattern_ids = [GetOrCreatePatternId(i) for i in primitive_ids]
    return ParserCtx(
      pattern_ids=np.array(pattern_ids, dtype=np.int32),
      id2pattern_tree=id2pattern_tree,
      make_new_pattern_id=lambda pattern_ids: np.max(pattern_ids) + 1,
    )

  def ReduceFrequentest(
    self,
    window_size,
  ) -> ParserCtx:
    repeated_pattern_ids = self.FindRepeatedPatternIds(
      window_size
    )
    if repeated_pattern_ids is None:
      # take all pattern_ids as repeated.
      repeated_pattern_ids = self.pattern_ids
    assert len(repeated_pattern_ids.shape) == 1
    if repeated_pattern_ids.shape[0] == 1:
      # take all pattern_ids as repeated.
      repeated_pattern_ids = self.pattern_ids
    new_pattern_id = self.make_new_pattern_id(self.pattern_ids)
    id2pattern_tree = self.UpdateId2PatternTree(
      new_pattern_id=new_pattern_id,
      repeated_pattern_ids=repeated_pattern_ids,
    )
    new_pattern_ids = self.ReplacePatternId(
      new_pattern_id,
      repeated_pattern_ids,
    )
    return ParserCtx(
      pattern_ids=new_pattern_ids,
      id2pattern_tree=id2pattern_tree,
      make_new_pattern_id=lambda pattern_ids: np.max(pattern_ids) + 1,
    )

  def FindRepeatedPatternIds(self, window_size):
    assert len(self.pattern_ids.shape) == 1
    window = self.pattern_ids[0:window_size,]
    window_size = window.shape[0]
    diff = window.reshape((1, window_size)) - window.reshape((window_size, 1))
    is_equal = (diff == 0)
    not_equal_myself = np.logical_not(np.eye(window_size, dtype=np.bool))
    xs, ys = np.where(is_equal and not_equal_myself)
    if xs.shape[0] == 0:
      return None
    intervals = xs - ys
    interval_values, interval_counts = np.unique(np.abs(intervals), return_counts=True)
    frequentest_interval_idx = np.argmax(interval_counts)
    frequentest_interval_value = interval_values[frequentest_interval_idx]
    pointer_indexes, = np.where(intervals == frequentest_interval_value)
    pointer_xs = np.take(xs, pointer_indexes)
    consecutive_index_groups = GetConsecutiveGroups(pointer_xs)
    group_lens = np.array([x.shape[0] for x in consecutive_index_groups])
    longest_group_idx = np.argmax(group_lens)
    longest_group = consecutive_index_groups[longest_group_idx]
    repeated_pattern_ids = np.take(window, longest_group)
    if frequentest_interval_value > 1:
      repeated_pattern_ids = repeated_pattern_ids[0:frequentest_interval_value]
    return repeated_pattern_ids

  # reference: https://stackoverflow.com/questions/7352684/how-to-find-the-groups-of-consecutive-elements-in-a-numpy-array
  def GetConsecutiveGroups(self, data, stepsize=1):
    return np.split(data, np.where(np.diff(data) != stepsize)[0] + 1)

  def UpdateId2PatternTree(self, new_pattern_id, repeated_pattern_ids):
    children = [
      self.id2pattern_tree[pattern_id]
      for pattern_id in repeated_pattern_ids.tolist()
    ]
    if all(isinstance(x, PrimitivePattern) for x in children):
      new_pattern = TrivialPattern(children=children)
    else:
      new_pattern = TuplePattern(children=children)
    self.id2pattern_tree[new_pattern_id] = new_pattern
    return self.id2pattern_tree

  def ReplacePatternId(
    self,
    new_pattern_id,
    repeated_pattern_ids,
  ):
    ids = self.pattern_ids.tolist()
    ids_str = "".join(f"{num:08d}" for num in ids)
    repeated_pattern_ids = repeated_pattern_ids.tolist()
    repeated_pattern_ids_str = "".join(f"{num:08d}" for num in repeated_pattern_ids)
    new_pattern_id_str = f"{new_pattern_id:08d}"
    replaced_ids_str = re.sub(repeated_pattern_ids_str, new_pattern_id_str, ids_str)
    assert len(replaced_ids_str) % 8 == 0
    replaced_ids = [
      int(replaced_ids_str[i:(i + 8)])
      for i in range(start=0, stop=len(replaced_ids_str), step=8)
    ]
    return np.array(replaced_ids, dtype=np.int32)