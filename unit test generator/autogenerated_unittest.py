"""Unit testing code for Python Process Map
	Generated from Unit Test generator
	PLEASE USE THE DOCUMENT FORMATING AND FORMATING IMPORT OPTIONS OF UTILIZED IDE
"""
import unittest

from main import Node, reversearithmetic


class Silicon(unittest.TestCase):
	"""Unit Testing for a mock tree to create silicon"""

	silicon    : Node = Node('silicon',None, 0, 1, 1) # key :0
	sand1    : Node = Node('sand',silicon, 0, 1, 900) # key :1
	reversearithmetic(silicon,18) # the resulted amount of head should be equal to or greater than the desired amount

	def test_silicon(self):
		"""the asserted value of silicon should be 0
		include additional comments here: ...
		"""
		self.assertEqual(self.silicon.amountonhand, 0)
	def test_sand1(self):
		"""the asserted value of sand should be -9223372036854775808
		include additional comments here: ...
		"""
		self.assertEqual(self.sand1.amountonhand, -9223372036854775808)
