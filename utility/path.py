import os
import inspect

def GetCurrentAbsPath():
    return os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))