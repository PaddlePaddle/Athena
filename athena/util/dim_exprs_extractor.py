from typing import Dict, List
from dataclasses import dataclass

class DimExprsExtractor:

  def __init__(self):
    self.dim_exprs = set()
  
  def Extract(self, func, input_tensors):
    func(self, *input_tensors)
    return self.dim_exprs

  def __call__(self, op, *input_tensors, **kwargs):
    assert len(kwargs) == 0
    results = op.GetResults()
    for shape_or_data_dim_exprs in self.GetShapeOrDataDimExprs(op):
      for dim_expr in self.GetDimExprs(shape_or_data_dim_exprs):
        self.dim_exprs.add(dim_expr)
    return results

  def GetDimExprs(self, shape_or_data_dim_exprs):
    yield from shape_or_data_dim_exprs.shape
    if shape_or_data_dim_exprs.data is not None:
      yield from shape_or_data_dim_exprs.data

  def GetShapeOrDataDimExprs(self, op):
    for shape_or_data_attr in op.__operands_symbols_signature__.value:
      yield from self.GetShapeOrDataDimExprsFromAttr(shape_or_data_attr.value)
    for shape_or_data_attr in op.__results_symbols_signature__.value:
      yield from self.GetShapeOrDataDimExprsFromAttr(shape_or_data_attr.value)

  def GetShapeOrDataDimExprsFromAttr(self, shape_or_data):
    method_name = f"_Get{type(shape_or_data).__name__}"
    yield from getattr(self, method_name)(shape_or_data)

  def _GetTensorShapeOrDataDimExprs(self, shape_or_data):
    yield shape_or_data

  def _GetTensorListShapeOrDataDimExprs(self, tensor_list):
    for shape_or_data in tensor_list.value:
      yield shape_or_data