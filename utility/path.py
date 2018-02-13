import os
import inspect

def GetCurrentAbsPath():
    """ Get absolute path of this file
   
    Returns:
        [str] -- [absolute path of path.py]
    """

    return os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

class TestPath(object):
    def test_GetCurrentAbsPath(self):
        print(GetCurrentAbsPath())