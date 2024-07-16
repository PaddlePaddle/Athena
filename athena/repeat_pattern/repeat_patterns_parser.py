from dataclasses import dataclass
import typing as t
import numpy as np

PrimitivePattern = int

@dataclass
class PatternTree:
  pass

@dataclass
class LeafPattern(PatternTree):
  value: t.List[PrimitivePattern]

@dataclass
class RepeatedPattern:
  repeated_count: int
  value: PatternTree

@dataclass
class TuplePattern(PatternTree):
  value: t.List[RepeatedPattern]

class RepeatPatternsParser:
  def __init__(
    self,
    window_size: int = 4096,
    conv_kernel_size: int = 9,
  ):
    self.window_size = window_size
    self.conv_kernel_size = conv_kernel_size

  def Parse(
    self,
    primitive_patterns: t.List[PrimitivePattern],
  ) -> t.Optional[PatternTree]:
    ctx = ParserCtx.InitFromPrimitivePatterns(primitive_patterns)
    if len(ctx.pattern_ids) == 0:
      return None
    while len(ctx.pattern_ids) > 1:
      ctx = ctx.ReduceFrequentest(
        window_size=self.window_size,
        conv_kernel_size=self.conv_kernel_size,
      )
    return ctx.id2pattern_tree[int(ctx.pattern_ids[0])]

@dataclass
class ParserCtx:
  pattern_ids: np.ndarray[("N",), np.int32]
  embedding: np.ndarray[("num_words",), np.float32]
  id2pattern_tree: t.List[PatternTree]

  @classmethod
  def InitFromPrimitivePatterns(cls, primitive_patterns: t.List[PrimitivePattern]):
    if len(primitive_patterns) == 0:
      return None
    TODO

  def ReduceFrequentest(
    self,
    window_size,
    conv_kernel_size,
  ) -> ParserCtx:
    frequentest_ids, locations = self.FindFrequentestIds(
      window_size=window_size,
      conv_kernel_size=conv_kernel_size,
    )
    new_embedding, new_word_id = self.IncreaseEmbedding()
    new_map_id2pattern_tree = self.MakeNewMapId2PatternTree(frequentest_ids, new_word_id)
    new_pattern_ids = self.ReplacePatternId(new_word_id, frequentest_ids, locations)
    return ParserCtx(
      pattern_ids=new_pattern_ids,
      embedding=new_embedding,
      id2pattern_tree=new_map_id2pattern_tree,
    )

  def FindFrequentestIds(self, window_size, conv_kernel_size):
    window = self.pattern_ids[0:window_size,]
    window_size = window.shape[0]
    x = np.take(self.embedding, window, axis=0)
    w = np.random.normal(0.0, scale=100.0, size=(conv_kernel_size,))
    convolved = np.convolve(x, w, mode='same')
    diff = convolved.reshape((1, window_size)) - convolved.reshape((window_size, 1))
    is_equal = (diff * diff < 1e-9) 
    not_equal_myself = np.logical_not(np.eye(window_size, dtype=np.bool))
    xs, ys = np.where(is_equal and not_equal_myself)
    intervals = xs - ys


  def IncreaseEmbedding(self):
    TODO
  
  def MakeNewMapId2PatternTree(self, frequentest_ids, new_word_id):
    TODO

  def ReplacePatternId(self, new_word_id, frequentest_ids, locations):
    TODO