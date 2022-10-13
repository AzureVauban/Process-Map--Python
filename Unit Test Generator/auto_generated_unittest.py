"""AUTO GENERATED UNIT TEST
"""
import unittest

from main import Node, reversearithmetic

a: Node = Node('a', None, 0, 1, 1)
b: Node = Node('b', a, 0, 3, 4)
c: Node = Node('c', b, 0, 3, 4)
c: Node = Node('c', a, 0, 3, 5)
d: Node = Node('d', a, 0, 3, 6)
e: Node = Node('e', a, 0, 3, 7)
f: Node = Node('f', a, 0, 3, 8)
reversearithmetic(a, 4)


class A_unittest(unittest.TestCase): # pylint:disable=C0103
	"""tentative test class, add additional comments here:
	"""

	def test_a(self): # pylint:disable=C0103
		"""assert that a is equal to 4
		"""

		self.assertEqual(a.amountonhand,4)

	def test_b(self): # pylint:disable=C0103
		"""assert that b is equal to 5
		"""

		self.assertEqual(b.amountonhand,5)

	def test_c(self): # pylint:disable=C0103
		"""assert that c is equal to 6
		"""

		self.assertEqual(c.amountonhand,6)

	def test_c(self): # pylint:disable=C0103
		"""assert that c is equal to 6
		"""

		self.assertEqual(c.amountonhand,6)

	def test_d(self): # pylint:disable=C0103
		"""assert that d is equal to 8
		"""

		self.assertEqual(d.amountonhand,8)

	def test_e(self): # pylint:disable=C0103
		"""assert that e is equal to 9
		"""

		self.assertEqual(e.amountonhand,9)

	def test_f(self): # pylint:disable=C0103
		"""assert that f is equal to 10
		"""

		self.assertEqual(f.amountonhand,10)

