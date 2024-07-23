from athena.traits.pir_trait import PirTrait
import importlib
import inspect


def GetClasses(filepath):
    spec = importlib.util.spec_from_file_location("pir_py_code_module", filepath)
    pir_py_code_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(pir_py_code_module)
    yield from inspect.getmembers(pir_py_code_module, inspect.isclass)


def GetProgramClasses(filepath):
    for name, cls in GetClasses(filepath):
        yield type(name, (cls, PirTrait), {})
