class ArgsTrait:

  def __init__(self):
    self.__args = []
    self.__kwargs = {}

  def SetArgs(self, args):
    self.__args = args
    
  def SetKeywordArgs(self, kwargs):
    self.__kwargs = kwargs

  def GetArgs(self):
    return self.__args

  def GetKeywordArgs(self):
    return self.__kwargs
