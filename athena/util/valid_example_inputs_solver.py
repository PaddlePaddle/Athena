import typing as t
from typing import Callable
from athena.ir.ir_constraint import (
  Constraint,
  SymmetricDimVar
)
import athena.ir.ir_constraint as ir_constraint
from athena.ir.ir_symbol import DimExpr
import athena.ir.ir_symbol as ir_symbol
import numpy as np
import itertools
from functools import reduce
import operator
import math
import networkx as nx
from collections import OrderedDict
import random
from dataclasses import dataclass

SmallList = t.List
SymbolName = str
Dim = int

@dataclass
class SymbolConstraints:
  input_names: SmallList[SymbolName]
  constraints: t.List[Constraint]

@dataclass
class DecomposedSymbolConstraints:
  input_names: SmallList[SymbolName]
  core_symbol_cstrs: SymbolConstraints
  symmetric_dim_vars: t.List[SymmetricDimVar]

ExampleInputDims = np.ndarray[('NumberCases', 'len(symbol_cstrs.input_names)'), Dim]

@dataclass
class ValidExampleInputs:
  symbol_cstrs: SymbolConstraints
  example_input_dims: ExampleInputDims

class ValidExampleInputsSolver:
  
  def __init__(
    self,
    constrained_dim_size_limit: int,
    independent_dim_size_limit: int,
  ):
    self.constrained_dim_size_limit = constrained_dim_size_limit
    self.independent_dim_size_limit = independent_dim_size_limit
    self.constrained_dims_ndarray = np.array(
      range(1, constrained_dim_size_limit + 1),
      dtype=np.int64,
    ).reshape((-1, 1))
    self.independent_dims_ndarray = np.array(
      range(1, independent_dim_size_limit + 1),
      dtype=np.int64,
    ).reshape((-1, 1))
    self.core_symbol_name_prefix_ = "T"
    self.core_symbol_name_seq_ = 0
  
  def Solve(
  	self,
    input_names: SmallList[SymbolName],
    constraints: t.List[Constraint],
  ) -> ValidExampleInputs:
    symbol_cstrs = SymbolConstraints(input_names, constraints)
    disjoint_constraints_group = self.GetDisjointConstraintsGroup(symbol_cstrs)
    constrained_valid_inputs_group = [
      self.SolveConstrainedValidInputs(disjoint_constraints)
      for disjoint_constraints in disjoint_constraints_group
    ]
    valid_example_inputs = self.GetPartialCartesionProduct(
      constrained_valid_inputs_group
    )
    return self.ReorderValidExampleInputs(
      valid_example_inputs,
      ordered_input_names=input_names
    )

  def ReorderValidExampleInputs(
    self,
    valid_example_inputs: ValidExampleInputs,
    ordered_input_names: SmallList[SymbolName],
  ) -> ValidExampleInputs:
    old_input_names = valid_example_inputs.symbol_cstrs.input_names
    assert len(old_input_names) == len(set(old_input_names))
    assert len(ordered_input_names) == len(set(ordered_input_names))
    assert set(old_input_names) == set(ordered_input_names)
    input_name2old_idx = {
      input_name:idx for idx, input_name in enumerate(old_input_names)
    }
    old_indexes = [input_name2old_idx[input_name] for input_name in ordered_input_names]
    dims = valid_example_inputs.example_input_dims
    ordered_dims = np.concatenate(
      tuple(dims[:, idx:idx+1] for idx in old_indexes),
      axis=1
    )
    return ValidExampleInputs(
      symbol_cstrs=SymbolConstraints(
        input_names=ordered_input_names,
        constraints=valid_example_inputs.symbol_cstrs.constraints,
      ),
      example_input_dims=ordered_dims,
    )

  def GetPartialCartesionProduct(
    self,
    constrained_valid_inputs_group: t.List[ValidExampleInputs],
  ) -> ValidExampleInputs:
    def PickMainAndZipRemainder(main_idx):
      return self.PickMainAndZipRemainder(constrained_valid_inputs_group, main_idx)
    valid_example_inputs_list = [
      self.GetCartesionProduct(main, remainder)
      for main_idx in range(len(constrained_valid_inputs_group))
      for main, remainder in [PickMainAndZipRemainder(main_idx)]
    ]
    return self.ConcatenateValidExampleInputs(valid_example_inputs_list)

  def ConcatenateValidExampleInputs(
    self,
    constrained_valid_inputs_list: t.List[ValidExampleInputs],
  ):
    assert len(constrained_valid_inputs_list) > 0
    first = constrained_valid_inputs_list[0]
    ordered_input_names = first.symbol_cstrs.input_names
    reordered_dims_ndarray_list = tuple(
      self.ReorderValidExampleInputs(
        valid_example_inputs=valid_example_inputs,
        ordered_input_names=ordered_input_names
      ).example_input_dims
      for valid_example_inputs in constrained_valid_inputs_list
    )
    concated_dims = np.concatenate(reordered_dims_ndarray_list, axis=0)
    return ValidExampleInputs(
      symbol_cstrs=SymbolConstraints(
        input_names=ordered_input_names,
        constraints=first.symbol_cstrs.constraints,
      ),
      example_input_dims=concated_dims,
    )

  def GetCartesionProduct(
    self,
    lhs: ValidExampleInputs,
    rhs: ValidExampleInputs,
  ) -> ValidExampleInputs:
    if rhs is None:
      return lhs
    assert lhs.symbol_cstrs.constraints == rhs.symbol_cstrs.constraints
    lhs_dims = lhs.example_input_dims.tolist()
    rhs_dims = rhs.example_input_dims.tolist()
    cartesion_dims = [
      (*lhs_tuple, *rhs_tuple)
      for lhs_tuple, rhs_tuple in itertools.product(lhs_dims, rhs_dims)
    ]
    return ValidExampleInputs(
      symbol_cstrs=SymbolConstraints(
        input_names=lhs.symbol_cstrs.input_names + rhs.symbol_cstrs.input_names,
        constraints=lhs.symbol_cstrs.constraints,
      ),
      example_input_dims=np.array(cartesion_dims, dtype=np.int64),
    )

  def PickMainAndZipRemainder(
    self,
    constrained_valid_inputs_group: t.List[ValidExampleInputs],
    main_idx: int,
  ) -> tuple[ValidExampleInputs, ValidExampleInputs]:
    main = constrained_valid_inputs_group[main_idx]
    remainder = [
      *constrained_valid_inputs_group[0:main_idx],
      *constrained_valid_inputs_group[main_idx+1:]
    ]
    constraints = main.symbol_cstrs.constraints
    return main, self.RoundZipValidExampleInputs(remainder, constraints)

  def RoundZipValidExampleInputs(
    self,
    constrained_valid_inputs_group: t.List[ValidExampleInputs],
    constraints: t.List[Constraint],
  ) -> ValidExampleInputs:
    input_names = [
      input_name
      for group in constrained_valid_inputs_group
      for input_name in group.symbol_cstrs.input_names
    ]
    example_input_dims = self.RoundZip(
      [group.example_input_dims for group in constrained_valid_inputs_group],
      num_input_names=len(input_names)
    )
    return ValidExampleInputs(
      symbol_cstrs=SymbolConstraints(
        input_names=input_names,
        constraints=constraints,
      ),
      example_input_dims=example_input_dims,
    )

  def RoundZip(self, ndarrays: t.List[np.ndarray], num_input_names: int) -> np.ndarray:
    if len(ndarrays) == 0:
      assert num_input_names == 0
      return np.array([()], dtype=np.int64)
    for ndarray in ndarrays:
      assert len(ndarray.shape) == 2, f"{len(ndarray.shape)} v.s. 2"
      assert ndarray.shape[0] > 0
    sum_num_col = reduce(lambda x, y: x + y, (
      ndarray.shape[1]
      for ndarray in ndarrays
    )) 
    assert sum_num_col == num_input_names, f"{sum_num_col} v.s. {num_input_names}"
    max_dim0_size = reduce(max, (ndarray.shape[0] for ndarray in ndarrays))
    def Extend(idx, ndarray):
      repeated = np.repeat(
        ndarray[None, :, :],
        math.ceil(ndarray.shape[0] / max_dim0_size),
        axis=0
      )
      reshaped = repeated.reshape((-1, ndarray.shape[1]))
      rolled = np.roll(reshaped, int(idx * (max_dim0_size / len(ndarrays))), axis=0)
      return rolled[0:max_dim0_size, :]
    return np.concatenate(
      [Extend(idx, ndarray) for idx, ndarray in enumerate(ndarrays)],
      axis=1
    )

  def SolveConstrainedValidInputs(
    self,
    symbol_cstrs: SymbolConstraints,
  ) -> ValidExampleInputs:
    if len(symbol_cstrs.constraints) == 0:
      assert len(symbol_cstrs.input_names) == 1
      return ValidExampleInputs(
        symbol_cstrs=symbol_cstrs,
        example_input_dims=self.independent_dims_ndarray,
      )
    decomposed_symbol_cstrs = self.DecomposeSymbolConstraints(symbol_cstrs)
    return ValidExampleInputs(
      symbol_cstrs=symbol_cstrs,
      example_input_dims=self.SolveDecomposedSymbolConstraints(
        decomposed_symbol_cstrs
      )
    )
  
  def GetDisjointConstraintsGroup(
    self,
    symbol_cstrs: SymbolConstraints,
 	) -> SmallList[SymbolConstraints]:
    symbol2cstrs = {}
    def GetConstraintSet(symbol_name):
      if symbol_name not in symbol2cstrs:
        symbol2cstrs[symbol_name] = set()
      return symbol2cstrs[symbol_name]
    for symbol_name in self.GetConstraintsSymbolNames(symbol_cstrs.constraints):
      for constraint in symbol_cstrs.constraints:
        GetConstraintSet(symbol_name).add(constraint)
    G = nx.Graph()
    G.add_nodes_from(symbol_cstrs.constraints)
    G.add_edges_from(
      (cstrs[i], cstrs[i+1])
      for _, _cstrs in symbol2cstrs.items()
      for cstrs in [list(_cstrs)]
      for i in range(len(cstrs) - 1)
    )
    constraints_from_graph = [
      SymbolConstraints(
        input_names=self.GetConstraintsSymbolNames(constraints),
        constraints=constraints,
      )
      for constraint_set in nx.connected_components(G)
      for constraints in [list(constraint_set)]
    ]
    no_constrained_input_names = set(symbol_cstrs.input_names) - set(
      input_name for cstr in constraints_from_graph for input_name in cstr.input_names
    )
    return constraints_from_graph + [
      SymbolConstraints(
        input_names=[input_name],
        constraints=[],
      )
      for input_name in no_constrained_input_names
    ]

  def Unique(self, l):
    ordered_dict: t.Dict[t.Any, bool] = OrderedDict()
    for element in l:
      ordered_dict[element] = True
    return list(ordered_dict)

  def GetConstraintsSymbolNames(self, constraints: t.List[Constraint]):
    symbol_names_ctx : t.List[SymbolName] = []
    for constraint in constraints:
      self.CollectCstrSymbolName(constraint, symbol_names_ctx)
    return self.Unique(symbol_names_ctx)

  def CollectCstrSymbolName(
    self,
    constraint: Constraint,
    symbol_names_ctx: t.List[SymbolName],
  ):
    return getattr(self, f"CollectCstrSymbolName_{type(constraint).__name__}")(
      constraint=constraint,
      symbol_names_ctx=symbol_names_ctx,
    )

  def CollectCstrSymbolName_NoConstraint(
    self,
    constraint: ir_constraint.EqualConstraint,
    symbol_names_ctx: t.List[SymbolName],
  ):
    for dim_expr in constraint.no_dim_exprs:
      self.CollectDimExprSymbolName(dim_expr, symbol_names_ctx)

  def CollectCstrSymbolName_EqualConstraint(
    self,
    constraint: ir_constraint.EqualConstraint,
    symbol_names_ctx: t.List[SymbolName],
  ):
    for dim_expr in constraint.equal_dim_exprs:
      self.CollectDimExprSymbolName(dim_expr, symbol_names_ctx)

  def CollectCstrSymbolName_BroadcastableConstraint(
    self,
    constraint: ir_constraint.BroadcastableConstraint,
    symbol_names_ctx: t.List[SymbolName],
  ):
    for dim_expr in constraint.braodcastable_dim_exprs:
      self.CollectDimExprSymbolName(dim_expr, symbol_names_ctx)

  def CollectCstrSymbolName_GtOneConstraint(
    self,
    constraint: ir_constraint.GtOneConstraint,
    symbol_names_ctx: t.List[SymbolName],
  ):
    self.CollectDimExprSymbolName(constraint.gt_one_dim_expr, symbol_names_ctx)

  def CollectDimExprSymbolName(
    self,
    dim_expr: ir_symbol.DimExpr,
    symbol_names_ctx: t.List[SymbolName],
  ):
    getattr(self, f"CollectDimExprSymbolName_{type(dim_expr).__name__}")(
      dim_expr=dim_expr,
      symbol_names_ctx=symbol_names_ctx,
    )

  def CollectDimExprSymbolName_Int64(
    self,
    dim_expr: ir_symbol.Int64,
    symbol_names_ctx: t.List[SymbolName],
  ):
    pass

  def CollectDimExprSymbolName_String(
    self,
    dim_expr: ir_symbol.String,
    symbol_names_ctx: t.List[SymbolName],
  ):
    symbol_names_ctx.append(dim_expr.value)

  def CollectDimExprSymbolName_Negative(
    self,
    dim_expr: ir_symbol.Negative,
    symbol_names_ctx: t.List[SymbolName],
  ):
    self.CollectDimExprSymbolName(dim_expr.operand, symbol_names_ctx)

  def CollectDimExprSymbolName_Reciprocal(
    self,
    dim_expr: ir_symbol.Reciprocal,
    symbol_names_ctx: t.List[SymbolName],
  ):
    for operand in dim_expr.operands:
      self.CollectDimExprSymbolName(operand, symbol_names_ctx)

  def CollectDimExprSymbolName_Add(
    self,
    dim_expr: ir_symbol.Add,
    symbol_names_ctx: t.List[SymbolName],
  ):
    for operand in dim_expr.operands:
      self.CollectDimExprSymbolName(operand, symbol_names_ctx)

  def CollectDimExprSymbolName_Mul(
    self,
    dim_expr: ir_symbol.Mul,
    symbol_names_ctx: t.List[SymbolName],
  ):
    for operand in dim_expr.operands:
      self.CollectDimExprSymbolName(operand, symbol_names_ctx)

  def CollectDimExprSymbolName_Max(
    self,
    dim_expr: ir_symbol.Max,
    symbol_names_ctx: t.List[SymbolName],
  ):
    for operand in dim_expr.operands:
      self.CollectDimExprSymbolName(operand, symbol_names_ctx)

  def CollectDimExprSymbolName_Min(
    self,
    dim_expr: ir_symbol.Min,
    symbol_names_ctx: t.List[SymbolName],
  ):
    for operand in dim_expr.operands:
      self.CollectDimExprSymbolName(operand, symbol_names_ctx)

  def CollectDimExprSymbolName_Broadcast(
    self,
    dim_expr: ir_symbol.Broadcast,
    symbol_names_ctx: t.List[SymbolName],
  ):
    for operand in dim_expr.operands:
      self.CollectDimExprSymbolName(operand, symbol_names_ctx)

  def DecomposeSymbolConstraints(
    self,
    symbol_cstrs: SymbolConstraints,   
  ) -> DecomposedSymbolConstraints:
    dim_expr2symmetric_dim_var_ctx = {}
    constraints = self.DecomposeConstraints(
      constraints=symbol_cstrs.constraints,
      dim_expr2symmetric_dim_var_ctx=dim_expr2symmetric_dim_var_ctx,
    )
    core_input_names = self.GetConstraintsSymbolNames(constraints)
    symmetric_dim_vars = [
      dim_expr2symmetric_dim_var_ctx[ir_symbol.String(core_input_name)]
      for core_input_name in core_input_names
    ]
    return DecomposedSymbolConstraints(
      input_names=symbol_cstrs.input_names,
      core_symbol_cstrs=SymbolConstraints(
        input_names=core_input_names,
        constraints=constraints,
      ),
      symmetric_dim_vars=symmetric_dim_vars,
    )

  
  def DecomposeConstraints(
    self,
    constraints: t.List[Constraint],
    dim_expr2symmetric_dim_var_ctx: t.Dict[DimExpr, SymmetricDimVar]
  ) -> t.List[Constraint]:
    return [
      decomposed
      for constraint in constraints
      for decomposed in [
        self.DecomposeConstraint(constraint, dim_expr2symmetric_dim_var_ctx)
      ]
      if decomposed is not None
    ]
  
  def DecomposeConstraint(
    self,
    constraint: Constraint,
    dim_expr2symmetric_dim_var_ctx: t.Dict[DimExpr, SymmetricDimVar]
  ) -> Constraint:
    return getattr(self, f"DecomposeConstraint_{type(constraint).__name__}")(
      constraint,
      dim_expr2symmetric_dim_var_ctx
    )

  def DecomposeConstraint_EqualConstraint(
    self,
    constraint: ir_constraint.EqualConstraint,
    dim_expr2symmetric_dim_var_ctx: t.Dict[DimExpr, SymmetricDimVar]
  ) -> Constraint:
    return self.DecomposeVariadicConstraint(
      constraint=constraint,
      dim_expr2symmetric_dim_var_ctx=dim_expr2symmetric_dim_var_ctx,
      GetDimExprs=lambda constraint: constraint.equal_dim_exprs,
      MakeConstraint=ir_constraint.EqualConstraint,
      MakeComposedSymmetricDimVar=ir_constraint.AnySymmetricDimVar,
    )
    
  def DecomposeConstraint_BroadcastableConstraint(
    self,
    constraint: ir_constraint.BroadcastableConstraint,
    dim_expr2symmetric_dim_var_ctx: t.Dict[DimExpr, SymmetricDimVar]
  ) -> Constraint:
    return self.DecomposeVariadicConstraint(
      constraint=constraint,
      dim_expr2symmetric_dim_var_ctx=dim_expr2symmetric_dim_var_ctx,
      GetDimExprs=lambda constraint: constraint.braodcastable_dim_exprs,
      MakeConstraint=ir_constraint.BroadcastableConstraint,
      MakeComposedSymmetricDimVar=ir_constraint.BroadcastSymmetricDimVar,
    )

  def DecomposeVariadicConstraint(
    self,
    constraint: Constraint,
    dim_expr2symmetric_dim_var_ctx: t.Dict[DimExpr, SymmetricDimVar],
    GetDimExprs: Callable[Constraint, t.List[DimExpr]],
    MakeConstraint: Callable[t.List[DimExpr], Constraint],
    MakeComposedSymmetricDimVar: Callable[t.List[SymmetricDimVar], SymmetricDimVar]
  ) -> Constraint:
    core_dim_exprs = [
      self.DecomposeDimExpr(dim_expr, dim_expr2symmetric_dim_var_ctx)
      for dim_expr in GetDimExprs(constraint)
    ]
    symmetric_dim_exprs = [
      dim_expr
      for dim_expr in core_dim_exprs
      if dim_expr in dim_expr2symmetric_dim_var_ctx
    ]
    if len(symmetric_dim_exprs) <= 1:
      return MakeConstraint(core_dim_exprs)
    symbol_dim_expr = ir_symbol.String(self.NewSymbolName())
    symmetric_dim_var = MakeComposedSymmetricDimVar([
      dim_expr2symmetric_dim_var_ctx[symmetric_dim_expr]
      for symmetric_dim_expr in symmetric_dim_exprs
    ])
    dim_expr2symmetric_dim_var_ctx[symbol_dim_expr] = symmetric_dim_var
    non_symmetric_dim_exprs = [
      dim_expr
      for dim_expr in core_dim_exprs
      if dim_expr not in dim_expr2symmetric_dim_var_ctx
    ]
    args = [symbol_dim_expr] + non_symmetric_dim_exprs
    return MakeConstraint(args) if len(args) > 1 else ir_constraint.NoConstraint(args)

  def NewSymbolName(self):
    symbol_name = f"{self.core_symbol_name_prefix_}{self.core_symbol_name_seq_}"
    self.core_symbol_name_seq_ += 1
    return symbol_name
        
  def DecomposeConstraint_GtOneConstraint(
    constraint: ir_constraint.GtOneConstraint,
    dim_expr2symmetric_dim_var_ctx: t.Dict[DimExpr, SymmetricDimVar]
  ) -> Constraint:
    return ir_constraint.GtOneConstraint([
      self.DecomposeDimExpr(dim_expr, dim_expr2symmetric_dim_var_ctx)
      for dim_expr in GetDimExprs(constraint)
    ])

  def DecomposeDimExpr(
    self,
    dim_expr: DimExpr,
    dim_expr2symmetric_dim_var_ctx: t.Dict[DimExpr, SymmetricDimVar]
  ) -> DimExpr:
    return getattr(self, f"DecomposeDimExpr_{type(dim_expr).__name__}")(
      dim_expr=dim_expr,
      dim_expr2symmetric_dim_var_ctx=dim_expr2symmetric_dim_var_ctx,
    )

  def DecomposeDimExpr_Int64(
    self,
    dim_expr: ir_symbol.Int64,
    dim_expr2symmetric_dim_var_ctx: t.Dict[DimExpr, SymmetricDimVar]
  ) -> DimExpr:
    return dim_expr
    
  def DecomposeDimExpr_String(
    self,
    dim_expr: ir_symbol.String,
    dim_expr2symmetric_dim_var_ctx: t.Dict[DimExpr, SymmetricDimVar]
  ) -> DimExpr:
    ret_dim_expr = ir_symbol.String(f"_athena_tmp_{dim_expr.value}_")
    dim_expr2symmetric_dim_var_ctx[ret_dim_expr] = ir_constraint.SymbolSymmetricDimVar(
      dim_expr.value
    )
    return ret_dim_expr
    
  def DecomposeDimExpr_Negative(
    self,
    dim_expr: ir_symbol.Negative,
    dim_expr2symmetric_dim_var_ctx: t.Dict[DimExpr, SymmetricDimVar]
  ) -> DimExpr:
    return self.DecomposeUnaryDimExpr(
      dim_expr=dim_expr,
      dim_expr2symmetric_dim_var_ctx=dim_expr2symmetric_dim_var_ctx,
      MakeDimExpr=ir_symbol.Negative
    )
    
  def DecomposeDimExpr_Reciprocal(
    self,
    dim_expr: ir_symbol.Reciprocal,
    dim_expr2symmetric_dim_var_ctx: t.Dict[DimExpr, SymmetricDimVar]
  ) -> DimExpr:
    return self.DecomposeUnaryDimExpr(
      dim_expr=dim_expr,
      dim_expr2symmetric_dim_var_ctx=dim_expr2symmetric_dim_var_ctx,
      MakeDimExpr=ir_symbol.Reciprocal
    )
    
  def DecomposeUnaryDimExpr(
    self,
    dim_expr: ir_symbol.Reciprocal,
    dim_expr2symmetric_dim_var_ctx: t.Dict[DimExpr, SymmetricDimVar],
    MakeDimExpr: Callable[DimExpr, DimExpr]
  ) -> DimExpr:
    operand = self.DecomposeDimExpr(dim_expr, dim_expr2symmetric_dim_var_ctx)
    return MakeDimExpr(operand)
    
  def DecomposeDimExpr_Add(
    self,
    dim_expr: ir_symbol.Add,
    dim_expr2symmetric_dim_var_ctx: t.Dict[DimExpr, SymmetricDimVar]
  ) -> DimExpr:
    return self.DecomposeVariadicDimExpr(
      dim_expr=dim_expr,
      dim_expr2symmetric_dim_var_ctx=dim_expr2symmetric_dim_var_ctx,
      MakeDimExpr=ir_symbol.Add,
      MakeComposedSymmetricDimVar=ir_constraint.AddSymmetricDimVar,
    )
    
  def DecomposeDimExpr_Mul(
    self,
    dim_expr: ir_symbol.Mul,
    dim_expr2symmetric_dim_var_ctx: t.Dict[DimExpr, SymmetricDimVar]
  ) -> DimExpr:
    return self.DecomposeVariadicDimExpr(
      dim_expr=dim_expr,
      dim_expr2symmetric_dim_var_ctx=dim_expr2symmetric_dim_var_ctx,
      MakeDimExpr=ir_symbol.Mul,
      MakeComposedSymmetricDimVar=ir_constraint.MulSymmetricDimVar,
    )
    
  def DecomposeDimExpr_Max(
    self,
    dim_expr: ir_symbol.Max,
    dim_expr2symmetric_dim_var_ctx: t.Dict[DimExpr, SymmetricDimVar]
  ) -> DimExpr:
    return self.DecomposeVariadicDimExpr(
      dim_expr=dim_expr,
      dim_expr2symmetric_dim_var_ctx=dim_expr2symmetric_dim_var_ctx,
      MakeDimExpr=ir_symbol.Max,
      MakeComposedSymmetricDimVar=ir_constraint.MaxSymmetricDimVar,
    )
    
  def DecomposeDimExpr_Min(
    self,
    dim_expr: ir_symbol.Min,
    dim_expr2symmetric_dim_var_ctx: t.Dict[DimExpr, SymmetricDimVar]
  ) -> DimExpr:
    return self.DecomposeVariadicDimExpr(
      dim_expr=dim_expr,
      dim_expr2symmetric_dim_var_ctx=dim_expr2symmetric_dim_var_ctx,
      MakeDimExpr=ir_symbol.Min,
      MakeComposedSymmetricDimVar=ir_constraint.MinSymmetricDimVar,
    )
    
  def DecomposeDimExpr_Broadcast(
    self,
    dim_expr: ir_symbol.Broadcast,
    dim_expr2symmetric_dim_var_ctx: t.Dict[DimExpr, SymmetricDimVar]
  ) -> DimExpr:
    return self.DecomposeVariadicDimExpr(
      dim_expr=dim_expr,
      dim_expr2symmetric_dim_var_ctx=dim_expr2symmetric_dim_var_ctx,
      MakeDimExpr=ir_symbol.Broadcast,
      MakeComposedSymmetricDimVar=ir_constraint.BroadcastSymmetricDimVar,
    )
    
  def DecomposeVariadicDimExpr(
    self,
    dim_expr: DimExpr,
    dim_expr2symmetric_dim_var_ctx: t.Dict[DimExpr, SymmetricDimVar],
    MakeDimExpr: Callable[t.List[DimExpr], DimExpr],
    MakeComposedSymmetricDimVar: Callable[t.List[SymmetricDimVar], SymmetricDimVar]
  ) -> Constraint:
    operand_dim_exprs = [
      self.DecomposeDimExpr(dim_expr, dim_expr2symmetric_dim_var_ctx)
      for dim_expr in dim_expr.operands
    ]
    symmetric_dim_exprs = [
      dim_expr
      for dim_expr in operand_dim_exprs
      if dim_expr in dim_expr2symmetric_dim_var_ctx
    ]
    if len(symmetric_dim_exprs) <= 1:
      return MakeDimExpr(operand_dim_exprs)
    symbol_dim_expr = ir_symbol.String(self.NewSymbolName())
    symmetric_dim_var = MakeComposedSymmetricDimVar([
      dim_expr2symmetric_dim_var_ctx[symmetric_dim_expr]
      for symmetric_dim_expr in symmetric_dim_exprs
    ])
    dim_expr2symmetric_dim_var_ctx[symbol_dim_expr] = symmetric_dim_var
    non_symmetric_dim_exprs = [
      dim_expr
      for dim_expr in operand_dim_exprs
      if dim_expr not in dim_expr2symmetric_dim_var_ctx
    ]
    return MakeDimExpr([symbol_dim_expr] + non_symmetric_dim_exprs)
        
  def SolveDecomposedSymbolConstraints(
    self,
    decomposed_symbol_constraints: DecomposedSymbolConstraints,
  ) -> ExampleInputDims:
    core_example_input_dims = self.SolveSymbolConstraints(
      symbol_cstrs=decomposed_symbol_constraints.core_symbol_cstrs,
    )
    return self.ExpandInputShapesBySymmetricDimVars(
      input_names=decomposed_symbol_constraints.input_names,
      core_example_input_dims=core_example_input_dims,
      symmetric_dim_vars=decomposed_symbol_constraints.symmetric_dim_vars
    )

  def SolveSymbolConstraints(
    self,
    symbol_cstrs: SymbolConstraints,
  ) -> ExampleInputDims:
    input_names = symbol_cstrs.input_names
    assert self.GetConstraintsSymbolNames(symbol_cstrs.constraints) == input_names
    symbol2example_dims_ndarray = self.MakeSymbol2ExampleDimsNdarray(
      input_names
    )
    constraints_test_ndarray = self.MakeSymbolConstraintsTestNdarray(
      symbol_cstrs=symbol_cstrs,
      symbol2example_dims_ndarray=symbol2example_dims_ndarray
    )
    return self.MakeExampleInputDimsFromConstraintsTestNdarray(constraints_test_ndarray)

  def MakeSymbolConstraintsTestNdarray(
    self,
    symbol_cstrs: SymbolConstraints,
    symbol2example_dims_ndarray: t.Dict[SymbolName, ExampleInputDims],
  ) -> np.ndarray:
    return reduce(
      np.logical_and,
      [
        self.EvalConstraintTestNdarray(constraint, symbol2example_dims_ndarray)
        for constraint in symbol_cstrs.constraints
      ]
    )

  def EvalConstraintTestNdarray(
    self,
    constraint: Constraint,
    symbol2example_dims_ndarray: t.Dict[SymbolName, ExampleInputDims],
  ) -> np.ndarray:
    return getattr(self, f"EvalConstraintTestNdarray_{type(constraint).__name__}")(
      constraint=constraint,
      symbol2example_dims_ndarray=symbol2example_dims_ndarray,
    )

  def EvalConstraintTestNdarray_NoConstraint(
    self,
    constraint: ir_constraint.EqualConstraint,
    symbol2example_dims_ndarray: t.Dict[SymbolName, ExampleInputDims],
  ) -> np.ndarray:
    ret = True
    for _, example_dims_ndarray in symbol2example_dims_ndarray.items():
      ret = np.logical_or(ret, example_dims_ndarray)
    return ret

  def EvalConstraintTestNdarray_EqualConstraint(
    self,
    constraint: ir_constraint.EqualConstraint,
    symbol2example_dims_ndarray: t.Dict[SymbolName, ExampleInputDims],
  ) -> np.ndarray:
    return self.MakeVariadicConstraintTestNdarray(
      constraint=constraint,
      symbol2example_dims_ndarray=symbol2example_dims_ndarray,
      BinaryLogicalPredicator=lambda x, y: x==y,
    )

  def EvalConstraintTestNdarray_BroadcastableConstraint(
    self,
    constraint: ir_constraint.BroadcastableConstraint,
    symbol2example_dims_ndarray: t.Dict[SymbolName, ExampleInputDims],
  ) -> np.ndarray:
    def IsBroadcastable(x, y):
      return (x == y) or (x == 1) or (y == 1)
    return self.MakeVariadicConstraintTestNdarray(
      constraint=constraint,
      symbol2example_dims_ndarray=symbol2example_dims_ndarray,
      BinaryLogicalPredicator=IsBroadcastable,
    )

  def MakeVariadicConstraintTestNdarray(
    self,
    constraint: ir_constraint.EqualConstraint,
    symbol2example_dims_ndarray: t.Dict[SymbolName, ExampleInputDims],
    BinaryLogicalPredicator: Callable[[np.ndarray, np.ndarray], np.ndarray],
  ) -> np.ndarray:
    dim_exprs = constraint.equal_dim_exprs
    assert len(constraint.equal_dim_exprs) > 1
    eq_operand_pairs = [
      (dim_exprs[i], dim_exprs[i+1])
      for i in range(len(dim_exprs) - 1)
    ]
    def EvalOperand(dim_expr):
      return self.EvalDimExprTestNdarray(dim_expr, symbol2example_dims_ndarray)
    return reduce(
      np.logical_and,
      [
        BinaryLogicalPredicator(EvalOperand(lhs), EvalOperand(rhs))
        for lhs, rhs in eq_operand_pairs
      ]
    )

  def EvalConstraintTestNdarray_GtOneConstraint(
    self,
    constraint: ir_constraint.GtOneConstraint,
    symbol2example_dims_ndarray: t.Dict[SymbolName, ExampleInputDims],
  ) -> np.ndarray:
    dim_expr = constraint.gt_one_dim_expr
    return self.EvalDimExprTestNdarray(dim_expr, symbol2example_dims_ndarray) > 1

  def EvalDimExprTestNdarray(
    self,
    dim_expr: ir_symbol.DimExpr,
    symbol2example_dims_ndarray: t.Dict[SymbolName, ExampleInputDims],
  ) -> np.ndarray:
    return getattr(self, f"EvalDimExprTestNdarray_{type(dim_expr).__name__}")(
      dim_expr=dim_expr,
      symbol2example_dims_ndarray=symbol2example_dims_ndarray,
    )

  def EvalDimExprTestNdarray_Int64(
    self,
    dim_expr: ir_symbol.Int64,
    symbol2example_dims_ndarray: t.Dict[SymbolName, ExampleInputDims],
  ) -> np.ndarray:
    return dim_expr.value

  def EvalDimExprTestNdarray_String(
    self,
    dim_expr: ir_symbol.String,
    symbol2example_dims_ndarray: t.Dict[SymbolName, ExampleInputDims],
  ) -> np.ndarray:
    return symbol2example_dims_ndarray[dim_expr.value]

  def EvalDimExprTestNdarray_Negative(
    self,
    dim_expr: ir_symbol.Negative,
    symbol2example_dims_ndarray: t.Dict[SymbolName, ExampleInputDims],
  ) -> np.ndarray:
    return -self.EvalDimExprTestNdarray(dim_expr.operand, symbol2example_dims_ndarray)

  def EvalDimExprTestNdarray_Reciprocal(
    self,
    dim_expr: ir_symbol.Reciprocal,
    symbol2example_dims_ndarray: t.Dict[SymbolName, ExampleInputDims],
  ) -> np.ndarray:
    raise NotImplementedError("Reciprocal")

  def EvalDimExprTestNdarray_Add(
    self,
    dim_expr: ir_symbol.Add,
    symbol2example_dims_ndarray: t.Dict[SymbolName, ExampleInputDims],
  ) -> np.ndarray:
    def Accumulator(x, y):
      if isinstance(y, ir_symbol.Negative):
        return x - self.EvalDimExprTestNdarray(y.operand, symbol2example_dims_ndarray)
      return x + self.EvalDimExprTestNdarray(y, symbol2example_dims_ndarray)
    return self.EvalVariadicDimExprTestNdarray(
      dim_expr=dim_expr,
      symbol2example_dims_ndarray=symbol2example_dims_ndarray,
      Accumulator=Accumulator,
    )

  def EvalDimExprTestNdarray_Mul(
    self,
    dim_expr: ir_symbol.Mul,
    symbol2example_dims_ndarray: t.Dict[SymbolName, ExampleInputDims],
  ) -> np.ndarray:
    def Accumulator(x, y):
      if isinstance(y, ir_symbol.Reciprocal):
        return x // self.EvalDimExprTestNdarray(y.operand, symbol2example_dims_ndarray)
      return x * self.EvalDimExprTestNdarray(y, symbol2example_dims_ndarray)
    return self.EvalVariadicDimExprTestNdarray(
      dim_expr=dim_expr,
      symbol2example_dims_ndarray=symbol2example_dims_ndarray,
      Accumulator=Accumulator,
    )

  def EvalDimExprTestNdarray_Max(
    self,
    dim_expr: ir_symbol.Max,
    symbol2example_dims_ndarray: t.Dict[SymbolName, ExampleInputDims],
  ) -> np.ndarray:
    def Accumulator(x, y):
      y = self.EvalDimExprTestNdarray(y, symbol2example_dims_ndarray)
      return np.maximum(x, y)
    return self.EvalVariadicDimExprTestNdarray(
      dim_expr=dim_expr,
      symbol2example_dims_ndarray=symbol2example_dims_ndarray,
      Accumulator=Accumulator,
    )

  def EvalDimExprTestNdarray_Min(
    self,
    dim_expr: ir_symbol.Min,
    symbol2example_dims_ndarray: t.Dict[SymbolName, ExampleInputDims],
  ) -> np.ndarray:
    def Accumulator(x, y):
      y = self.EvalDimExprTestNdarray(y, symbol2example_dims_ndarray)
      return np.minimum(x, y)
    return self.EvalVariadicDimExprTestNdarray(
      dim_expr=dim_expr,
      symbol2example_dims_ndarray=symbol2example_dims_ndarray,
      Accumulator=Accumulator,
    )

  def EvalDimExprTestNdarray_Broadcast(
    self,
    dim_expr: ir_symbol.Broadcast,
    symbol2example_dims_ndarray: t.Dict[SymbolName, ExampleInputDims],
  ) -> np.ndarray:
    def Accumulator(x, y):
      y = self.EvalDimExprTestNdarray(y, symbol2example_dims_ndarray)
      return np.maximum(x, y)
    return self.EvalVariadicDimExprTestNdarray(
      dim_expr=dim_expr,
      symbol2example_dims_ndarray=symbol2example_dims_ndarray,
      Accumulator=Accumulator,
    )

  def EvalVariadicDimExprTestNdarray(
    self,
    dim_expr: ir_symbol.DimExpr,
    symbol2example_dims_ndarray: t.Dict[SymbolName, ExampleInputDims],
    Accumulator: t.Callable[[np.ndarray, ir_symbol.DimExpr], np.ndarray],
  ) -> np.ndarray:
    operands = dim_expr.operands
    assert len(operands) > 0
    ret = self.EvalDimExprTestNdarray(operands[0], symbol2example_dims_ndarray)
    for operand in operands[1:]:
      ret = Accumulator(ret, operand)
    return ret


  def MakeExampleInputDimsFromConstraintsTestNdarray(
    self,
    constraints_test_ndarray: np.ndarray
  ):
    dim_indexes_tuple = np.where(constraints_test_ndarray)
    assert len(dim_indexes_tuple) > 0
    example_dims_tuple = tuple(
      np.take(self.constrained_dims_ndarray, dim_indexes)[:, None]
      for dim_indexes in dim_indexes_tuple
    )
    return np.concatenate(example_dims_tuple, axis=1)

  def MakeSymbol2ExampleDimsNdarray(
    self,
    input_names: t.List[SymbolName]
  ) -> ExampleInputDims:
    return {
      input_name:self.MakePrimitiveExampleDimsNdarray(idx, len(input_names))
      for idx, input_name in enumerate(input_names)
    }

  def MakePrimitiveExampleDimsNdarray(
    self,
    idx: int,
    num_input_names: int
  ) -> ExampleInputDims:
    shape = tuple(
      self.constrained_dim_size_limit if i == idx else 1
      for i in range(num_input_names)
    )
    return self.constrained_dims_ndarray.reshape(shape)

  def ExpandInputShapesBySymmetricDimVars(
    self,
    input_names: t.List[SymbolName],
    core_example_input_dims: ExampleInputDims,
    symmetric_dim_vars: t.List[SymmetricDimVar],
  ) -> ExampleInputDims:
    expander = SymmetricDimsExpander(input_names, symmetric_dim_vars)
    shape_list = [
      expanded_shape
      for core_example_input_shape in core_example_input_dims.tolist()
      for expanded_shape in expander.Expand(core_example_input_shape)
    ]
    return np.array(shape_list, dtype=np.int64)

class SymmetricDimsExpander:
  def __init__(
    self,
    input_names: t.List[SymbolName],
    symmetric_dim_vars: t.List[SymmetricDimVar],
  ):
    self.input_names = input_names
    self.symmetric_dim_vars = symmetric_dim_vars

  def Expand(
    self,
    core_example_input_shape: t.List[Dim],
  ) -> t.Iterator[SmallList[Dim]]:
    assert len(self.symmetric_dim_vars) == len(core_example_input_shape)
    kMaxTryCnt = 16
    for i in range(kMaxTryCnt):
      input_name2dim = reduce(
        lambda x, y: {**x, **y},
        (
          self.ExpandSymmetricDimVar(dim, symmetric_dim_var)
          for dim, symmetric_dim_var in zip(
            core_example_input_shape,
            self.symmetric_dim_vars
          )
        )
      )
      if len(input_name2dim) == len(self.input_names):
        yield [input_name2dim[input_name] for input_name in self.input_names]
        return
    yield from []

  def ExpandSymmetricDimVar(
    self,
    dim: Dim,
    symmetric_dim_var: SymmetricDimVar
  ) -> t.Dict[SymbolName, Dim]:
    input_name2dim_ctx: t.Dict[SymbolName, Dim] = {}
    self.CollectExpandedInputName2Dim(dim, symmetric_dim_var, input_name2dim_ctx)
    return input_name2dim_ctx

  def CollectExpandedInputName2Dim(
    self,
    dim: Dim,
    symmetric_dim_var: SymmetricDimVar,
    input_name2dim_ctx: t.Dict[SymbolName, Dim],
  ):
    class_name = type(symmetric_dim_var).__name__
    getattr(self, f"CollectExpandedInputName2Dim_{class_name}")(
      dim=dim,
      symmetric_dim_var=symmetric_dim_var,
      input_name2dim_ctx=input_name2dim_ctx,
    )

  def CollectExpandedInputName2Dim_SymbolSymmetricDimVar(
    self,
    dim: Dim,
    symmetric_dim_var: SymmetricDimVar,
    input_name2dim_ctx: t.Dict[SymbolName, Dim],
  ):
    input_name2dim_ctx[symmetric_dim_var.symbol] = dim

  def CollectExpandedInputName2Dim_AnySymmetricDimVar(
    self,
    dim: Dim,
    symmetric_dim_var: SymmetricDimVar,
    input_name2dim_ctx: t.Dict[SymbolName, Dim],
  ):
    for dim_var in symmetric_dim_var.symmetric_dim_vars:
      self.CollectExpandedInputName2Dim(
        dim=dim,
        symmetric_dim_var=dim_var,
        input_name2dim_ctx=input_name2dim_ctx,
      )

  def CollectExpandedInputName2Dim_AddSymmetricDimVar(
    self,
    dim: Dim,
    symmetric_dim_var: SymmetricDimVar,
    input_name2dim_ctx: t.Dict[SymbolName, Dim],
  ):
    operands = symmetric_dim_var.symmetric_dim_vars
    add_operands = self.RandomInferAddOperands(
      dim=dim,
      num_operands=len(symmetric_dim_var.symmetric_dim_vars),
    )
    for operand_dim, sub_symmetric_dim_var in zip(add_operands, operands):
      self.CollectExpandedInputName2Dim(
        dim=operand_dim,
        symmetric_dim_var=sub_symmetric_dim_var,
        input_name2dim_ctx=input_name2dim_ctx,
      )

  def CollectExpandedInputName2Dim_MulSymmetricDimVar(
    self,
    dim: Dim,
    symmetric_dim_var: SymmetricDimVar,
    input_name2dim_ctx: t.Dict[SymbolName, Dim],
  ):
    operands = symmetric_dim_var.symmetric_dim_vars
    mul_operands = self.RandomInferMulOperands(
      dim=dim,
      num_operands=len(symmetric_dim_var.symmetric_dim_vars),
    )
    for operand_dim, sub_symmetric_dim_var in zip(mul_operands, operands):
      self.CollectExpandedInputName2Dim(
        dim=operand_dim,
        symmetric_dim_var=sub_symmetric_dim_var,
        input_name2dim_ctx=input_name2dim_ctx,
      )

  def CollectExpandedInputName2Dim_MaxSymmetricDimVar(
    self,
    dim: Dim,
    symmetric_dim_var: SymmetricDimVar,
    input_name2dim_ctx: t.Dict[SymbolName, Dim],
  ):
    operands = symmetric_dim_var.symmetric_dim_vars
    max_operands = self.RandomInferMaxOperands(
      dim=dim,
      num_operands=len(symmetric_dim_var.symmetric_dim_vars),
    )
    for operand_dim, sub_symmetric_dim_var in zip(max_operands, operands):
      self.CollectExpandedInputName2Dim(
        dim=operand_dim,
        symmetric_dim_var=sub_symmetric_dim_var,
        input_name2dim_ctx=input_name2dim_ctx,
      )

  def CollectExpandedInputName2Dim_MinSymmetricDimVar(
    self,
    dim: Dim,
    symmetric_dim_var: SymmetricDimVar,
    input_name2dim_ctx: t.Dict[SymbolName, Dim],
  ):
    operands = symmetric_dim_var.symmetric_dim_vars
    min_operands = self.RandomInferMinOperands(
      dim=dim,
      num_operands=len(symmetric_dim_var.symmetric_dim_vars),
    )
    for operand_dim, sub_symmetric_dim_var in zip(min_operands, operands):
      self.CollectExpandedInputName2Dim(
        dim=operand_dim,
        symmetric_dim_var=sub_symmetric_dim_var,
        input_name2dim_ctx=input_name2dim_ctx,
      )

  def CollectExpandedInputName2Dim_BroadcastSymmetricDimVar(
    self,
    dim: Dim,
    symmetric_dim_var: SymmetricDimVar,
    input_name2dim_ctx: t.Dict[SymbolName, Dim],
  ):
    operands = symmetric_dim_var.symmetric_dim_vars
    broadcast_operands = self.RandomInferBroadcastOperands(
      dim=dim,
      num_operands=len(symmetric_dim_var.symmetric_dim_vars),
    )
    for operand_dim, sub_symmetric_dim_var in zip(broadcast_operands, operands):
      self.CollectExpandedInputName2Dim(
        dim=operand_dim,
        symmetric_dim_var=sub_symmetric_dim_var,
        input_name2dim_ctx=input_name2dim_ctx,
      )

  def RandomInferAddOperands(
    self,
    dim: int,
    num_operands: int,
  ) -> t.List[int]:
    ret = [0] * num_operands
    for _ in range(dim):
      ret[random.randrange(0, num_operands)] += 1
    return ret

  def RandomInferMulOperands(
    self,
    dim: int,
    num_operands: int,
  ) -> t.List[int]:
    ret = [1] * num_operands
    for factor in self.GetFactors(dim):
      ret[random.randrange(0, num_operands)] *= factor
    return ret

  def RandomInferMaxOperands(
    self,
    dim: int,
    num_operands: int,
  ) -> t.List[int]:
    ret = [0] * num_operands
    ret[random.randrange(0, num_operands)] = dim
    for i in range(num_operands):
      ret[i] = random.randint(0, num_operands)
    return ret

  def RandomInferMinOperands(
    self,
    dim: int,
    num_operands: int,
  ) -> t.List[int]:
    ret = [0] * num_operands
    ret[random.randrange(0, num_operands)] = dim
    for i in range(num_operands):
      ret[i] = random.randint(num_operands, num_operands*2)
    return ret

  def RandomInferBroadcastOperands(
    self,
    dim: int,
    num_operands: int,
  ) -> t.List[int]:
    ret = [0] * num_operands
    for i in range(num_operands):
      ret[i] = 1 + random.randint(0, 1) * (dim - 1)
    return ret

  def GetFactors(self, n: int) -> t.List[int]:
    prime_numbers = self.GetPrimeNumbers()
    for prime in prime_numbers:
      if prime * prime > n:
        break
      while n % prime == 0:
        yield prime
        n = n // prime
    if n != 1:
      yield n


  def GetPrimeNumbers(self) -> t.List[int]:
    return type(self).prime_numbers

  prime_numbers = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
    101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
    211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,
    307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,
    401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
    503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599,
    601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691,
    701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797,
    809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887,
    907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997,
  ]