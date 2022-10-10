"""AUTO GENERATED UNIT TEST
"""
import unittest

from main import Node

Head: Node = Node('Head', None, 0, 1, 1)
Body_A: Node = Node('Body A', Head, 0, 1, 1)
Body_B: Node = Node('Body B', Body_A, 0, 1, 1)
Body_C: Node = Node('Body C', Body_B, 0, 1, 1)
Body_D: Node = Node('Body D', Body_C, 0, 1, 1)


class Head_unittest(unittest.TestCase): #pylint:disable
	"""tentative test class, add additional comments here: 
	"""
	def test_Head(self):
		"""assert that Head is equal to 0
		"""
		self.assertEqual(Head.amountonhand,0

