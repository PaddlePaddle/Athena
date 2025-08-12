class DrrPass:

  def make_drr_ctx(self):
    drr_ctx = DrrCtx()
    drr_ctx.init_source_pattern(self.source_pattern)
    drr_ctx.init_constraint_func(self.get_constraint_func())
    drr_ctx.init_result_pattern(self.result_pattern)
    return drr_ctx


class register_drr_pass:
  def __init__(self, pass_name, nice):
    self.pass_name = pass_name
    self.nice = nice

  def __call__(self, drr_pass_cls):
    Registry.classic_drr_pass(self.pass_name, self.nice, drr_pass_cls)
    return drr_pass_cls