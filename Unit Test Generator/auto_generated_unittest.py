"""AUTO GENERATED UNIT TEST
"""
import unittest

from main import Node, reversearithmetic

morphite2: Node = Node('morphite2', None, 0, 1, 1)
pixels2: Node = Node('pixels2', morphite2, 0, 4, 5)
52: Node = Node('52', pixels2, 0, 1, 1)
pixels2: Node = Node('pixels2', morphite2, 0, 4, 4)
pixels2: Node = Node('pixels2', morphite2, 0, 4, 5)
pixels2: Node = Node('pixels2', morphite2, 0, 4, 4)
reversearithmetic(morphite2, 50)


class MORPHITE2_unittest(unittest.TestCase): # pylint:disable=C0103
	"""tentative test class, add additional comments here:
	"""

	def test_morphite2(self): # pylint:disable=C0103
		"""assert that morphite2 is equal to 50
		"""

		self.assertEqual(morphite2.amountonhand,50)

	def test_pixels2(self): # pylint:disable=C0103
		"""assert that pixels2 is equal to 62
		"""

		self.assertEqual(pixels2.amountonhand,62)

	def test_52(self): # pylint:disable=C0103
		"""assert that 52 is equal to 62
		"""

		self.assertEqual(52.amountonhand,62)

	def test_pixels2(self): # pylint:disable=C0103
		"""assert that pixels2 is equal to 50
		"""

		self.assertEqual(pixels2.amountonhand,50)

	def test_pixels2(self): # pylint:disable=C0103
		"""assert that pixels2 is equal to 62
		"""

		self.assertEqual(pixels2.amountonhand,62)

	def test_pixels2(self): # pylint:disable=C0103
		"""assert that pixels2 is equal to 50
		"""

		self.assertEqual(pixels2.amountonhand,50)

