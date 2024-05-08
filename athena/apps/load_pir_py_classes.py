from athena.traits.pir_trait import PirTrait
import importlib
import inspect

def GetProgramClasses(filepath):
  spec = importlib.util.spec_from_file_location("pir_py_code_module", filepath)
  pir_py_code_module = importlib.util.module_from_spec(spec)
  spec.loader.exec_module(pir_py_code_module)
  clsmembers = inspect.getmembers(pir_py_code_module, inspect.isclass)
  for name, cls in clsmembers:
    yield type(name, (cls, PirTrait), {})
