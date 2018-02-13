import utility.path as upath
import sys
import unittest

class TestPath(unittest.TestCase):
    def test_1(self):
        try:
            print(upath.GetCurrentAbsPath())
        except Exception:
            print("Exception" + sys.exc_info()[2])
            pass
