"""AUTO GENERATED UNIT TEST
"""
import unittest

from main import Node

Head: Node = Node('Head', None, 0, 1, 1)
Body_A: Node = Node('Body A', Head, 0, 1, 1)
Body_B: Node = Node('Body B', Body_A, 0, 1, 1)
Body_C: Node = Node('Body C', Body_B, 0, 1, 1)
Body_D: Node = Node('Body D', Body_C, 0, 1, 1)


class Head_unittest(unittest.TestCase): #pylint:disable=C0103
	"""tentative test class, add additional comments here: 
	"""

	def test_Head(self):
		"""assert that Head is equal to 0
		"""
		self.assertEqual(Head.amountonhand,0)
	def test_Body_A(self):
		"""assert that Body A is equal to 0
		"""
		self.assertEqual(Body_A.amountonhand,0)
	def test_Body_B(self):
		"""assert that Body B is equal to 0
		"""
		self.assertEqual(Body_B.amountonhand,0)
	def test_Body_C(self):
		"""assert that Body C is equal to 0
		"""
		self.assertEqual(Body_C.amountonhand,0)
	def test_Body_D(self):
		"""assert that Body D is equal to 0
		"""
		self.assertEqual(Body_D.amountonhand,0)

