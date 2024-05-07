from athena.generators.paddle_func_body_generator import (
  PaddleFuncBodyGenerator
)

class PaddleUnittestGenerator:

  def __init__(self, unittest_class_name, func, body_generator = None):
    self.unittest_class_name = unittest_class_name
    self.body_generator = body_generator
    if self.body_generator is None:
      self.body_generator = PaddleFuncBodyGenerator(func)

  def Generate(self, input_tensors):
    input_tensors, body_code_stmts = self.body_generator.Generate(input_tensors)
    return RunStaticUnittest(
      unittest_class_name=self.unittest_class_name,
      input_tensors=input_tensors,
      body_code_stmts=body_code_stmts
    )



class InitMinGetter:
  def bool():
    return "False" 

  def bfloat16():
    return "-0.5" 

  def float16():
    return "-0.5" 

  def float32():
    return "-0.5" 

  def float64():
    return "-0.5"

  def int32():
    return "0"

  def int64():
    return "0"


class InitMaxGetter:
  def bool():
    return "False" 

  def bfloat16():
    return "0.5" 

  def float16():
    return "0.5" 

  def float32():
    return "0.5" 

  def float64():
    return "0.5" 
    
  def int32():
    return "1"

  def int64():
    return "1"


type2bigger_type = dict(
  bool="bool",
  bfloat16="float64",
  float16="float64",
  float32="float64",
  int16="int64",
  int32="int64",
  int64="int64",
)


def RunStaticUnittest(unittest_class_name, input_tensors: list, body_code_stmts: list):
  example_dim = 2
  input_arg_names = ", ".join([
    input_tensor.name for input_tensor in input_tensors
  ])
  bigger_type2render_name = dict(
    bool="render_bool_init",
    int64="render_int_init",
    float64="render_float_init",
  )
  def render_input_tensors(num_tab_spaces, **kwargs):
    sep=",\n" + (" " * num_tab_spaces)
    l = []
    for input_tensor in input_tensors:
      render = kwargs[bigger_type2render_name[type2bigger_type[input_tensor.dtype]]]
      l.append(render(
        [(dim if dim >= 0 else example_dim) for dim in input_tensor.shape],
        input_tensor.dtype,
        getattr(InitMinGetter, input_tensor.dtype)(),
        getattr(InitMaxGetter, input_tensor.dtype)()))
    return sep.join(l)

  def render_input_spec(num_tab_spaces, render):
    sep=",\n" + (" " * num_tab_spaces)
    l = []
    for input_tensor in input_tensors:
      l.append(render(
        [(dim if dim >= 0 else None) for dim in input_tensor.shape],
        input_tensor.dtype))
    return sep.join(l)
      
  def render_unittest_body(num_tab_spaces):
    sep="\n" + (" " * num_tab_spaces)
    return sep.join(body_code_stmts)
  
  return f"""
import os
os.environ['FLAGS_cinn_new_group_scheduler'] = '1'
os.environ['FLAGS_group_schedule_tiling_first'] = '1'
os.environ['FLAGS_prim_all'] = 'true'
os.environ['FLAGS_prim_enable_dynamic'] = '1'
os.environ['FLAGS_enable_pir_api'] = '1'
os.environ['FLAGS_cinn_bucket_compile'] = '1'

import unittest
import numpy as np
import paddle


class {unittest_class_name}(paddle.nn.Layer):
    def __init__(self):
        super().__init__()

    def forward(self, {input_arg_names}):
        {render_unittest_body(num_tab_spaces=2*4)}


class Test{unittest_class_name}(unittest.TestCase):
    def setUp(self):
        paddle.seed(2024)
        self.prepare_data()

    def prepare_data(self):
        self.inputs = [
          {render_input_tensors(
            num_tab_spaces=2*5,
            render_bool_init=lambda shape, dtype, min, max:
              f"paddle.zeros({shape}, dtype='{dtype}')",
            render_int_init=lambda shape, dtype, min, max:
              f"paddle.randint(low={min}, high={max}, shape={shape}, dtype='{dtype}')",
            render_float_init=lambda shape, dtype, min, max:
              f"paddle.uniform({shape}, dtype='{dtype}', min={min}, max={max})",
          )}
        ]
        for input in self.inputs:
          input.stop_gradient = True

    def apply_to_static(self, net, use_cinn):
        build_strategy = paddle.static.BuildStrategy()
        input_spec = [
          {render_input_spec(
            num_tab_spaces=2*5,
            render=lambda shape, dtype:
              f"paddle.static.InputSpec(shape={shape}, dtype='{dtype}')"
          )}
        ]
        build_strategy.build_cinn_pass = use_cinn
        return paddle.jit.to_static(
            net,
            input_spec=input_spec,
            build_strategy=build_strategy,
            full_graph=True,
        )

    def train(self, use_cinn):
        net = {unittest_class_name}()
        net.eval()
        net = self.apply_to_static(net, use_cinn)
        out = net(*self.inputs)
        return out

    def test_train(self):
        dy_outs = self.train(use_cinn=False)
        cinn_outs = self.train(use_cinn=True)

        for cinn_out, dy_out in zip(cinn_outs, dy_outs):
          np.testing.assert_allclose(cinn_out.numpy(), dy_out.numpy(), atol=1e-6)


if __name__ == '__main__':
    unittest.main()
"""
