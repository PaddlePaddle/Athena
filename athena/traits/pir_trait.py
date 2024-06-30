from athena.traits.args_trait import ArgsTrait
from athena.traits.type_trait import TypeTrait
from athena.traits.attr_trait import AttrTrait
from athena.traits.symbol_trait import SymbolTrait
from athena.traits.op_trait import OpTrait
from athena.traits.constaint_trait import ConstraintTrait
import importlib
import inspect

class PirTrait(ArgsTrait,
               OpTrait,
               TypeTrait,
               AttrTrait,
               SymbolTrait,
               ConstraintTrait):
  pass