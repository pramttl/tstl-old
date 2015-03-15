"""
Unit tests to test TSTL code
"""

from src.harnessmaker import *
import unittest


class TestParseImportLine(unittest.TestCase):

    """
    To test the parse_import_line function.
    """

    def test_simple_import(self):
        line = "import math"
        output = parse_import_line(line)
        self.assertSequenceEqual(output, ['math'])

    def test_from_X_import_Y(self):
        line = "from math import sqrt"
        output = parse_import_line(line)
        self.assertSequenceEqual(output, ['sqrt'])

    def test_from_X_import_YZ(self):
        line = "from math import sqrt, ceil"
        output = parse_import_line(line)
        self.assertSequenceEqual(output, ['sqrt', 'ceil'])

    def test_from_X_import_Y_as_Z(self):
        line = "from math import sqrt as sq"
        output = parse_import_line(line)
        self.assertSequenceEqual(output, ['sq'])

    def test_multi_imports(self):
        line = "import math as m, collections as c"
        output = parse_import_line(line)
        self.assertSequenceEqual(output, ['m', 'c'])

if __name__ == '__main__':
    unittest.main()