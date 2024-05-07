from athena.traits.args_trait import ArgsTrait
from athena.traits.type_trait import TypeTrait
from athena.traits.attr_trait import AttrTrait
from athena.traits.op_trait import OpTrait
from athena.generators.group_op_unittest_generator import GroupOpUnittestGenerator
from athena.apps import load_pir_py_classes
import sys


if __name__ == "__main__":
  for cls in load_pir_py_classes.GetProgramClasses(sys.argv[1]):
    ir_program = cls()
    generator = GroupOpUnittestGenerator()
    op_name2unittest = generator.Generate(ir_program)
    for name, unittest in op_name2unittest.items():
      print("#", "="*80)
      print("# file-splitter-fusion-op-name: ", name)
      print("#", "-"*80)
      print(unittest)