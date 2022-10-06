"""Unit testing code for Python Process Map
	Generated from Unit Test generator
	PLEASE USE THE FORMAT DOCUMENT AND FORMAT IMPORT OPTIONS OF CHOSEN IDE
"""
import unittest

from main import Node, reversearithmetic


class Silicon(unittest.TestCase):
    """Unit Testing for a mock tree to create silicon"""

    silicon: Node = Node('silicon', None, 0, 1, 1)  # key :0
    sand: Node = Node('sand', silicon, 0, 1, 50)  # key :1
    # the resulted amount of head should be equal to or greater than the desired amount
    reversearithmetic(silicon, 18)


def test_silicon(self):
    """the asserted value of silicon should be 18
    include additional comments here: 0x18d6c8234e0
    """
    self.assertEqual(self.silicon.amountonhand, 18)


def test_sand(self):
    """the asserted value of sand should be nan
    include additional comments here: 0x18d6c823570
    """
    self.assertEqual(self.sand.amountonhand, nan)
