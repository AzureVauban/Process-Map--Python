"""AUTO GENERATED UNIT TEST
"""
import unittest

from main import Node, reversearithmetic

morphite: Node = Node('morphite', None, 0, 1, 1)
a: Node = Node('a', morphite, 0, 5, 1)
b: Node = Node('b', a, 0, 4, 5)
c: Node = Node('c', a, 0, 4, 4)
b: Node = Node('b', morphite, 0, 5, 2)
c: Node = Node('c', morphite, 0, 5, 3)
d: Node = Node('d', morphite, 0, 5, 4)
reversearithmetic(morphite, 4)


class MORPHITE_unittest(unittest.TestCase): # pylint:disable=C0103
	"""tentative test class, add additional comments here:
	"""

	def test_morphite(self): # pylint:disable=C0103
		"""assert that morphite is equal to 4
		"""

		self.assertEqual(morphite.amountonhand,4)

	def test_a(self): # pylint:disable=C0103
		"""assert that a is equal to 0
		"""

		self.assertEqual(a.amountonhand,0)

	def test_b(self): # pylint:disable=C0103
		"""assert that b is equal to 0
		"""

		self.assertEqual(b.amountonhand,0)

	def test_c(self): # pylint:disable=C0103
		"""assert that c is equal to 0
		"""

		self.assertEqual(c.amountonhand,0)

	def test_b(self): # pylint:disable=C0103
		"""assert that b is equal to 1
		"""

		self.assertEqual(b.amountonhand,1)

	def test_c(self): # pylint:disable=C0103
		"""assert that c is equal to 2
		"""

		self.assertEqual(c.amountonhand,2)

	def test_d(self): # pylint:disable=C0103
		"""assert that d is equal to 3
		"""

		self.assertEqual(d.amountonhand,3)

