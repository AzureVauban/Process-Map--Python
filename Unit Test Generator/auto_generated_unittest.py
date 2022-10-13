"""AUTO GENERATED UNIT TEST
"""
import unittest

from main import Node, reversearithmetic

Morphite2: Node = Node('Morphite2', None, 0, 1, 1)
pixels2: Node = Node('pixels2', Morphite2, 0, 3, 4)
pixels2: Node = Node('pixels2', Morphite2, 0, 3, 3)
pixels2: Node = Node('pixels2', Morphite2, 0, 3, 3)
reversearithmetic(Morphite2, 3)


class MORPHITE2_unittest(unittest.TestCase): # pylint:disable=C0103
	"""tentative test class, add additional comments here:
	"""

	def test_Morphite2(self): # pylint:disable=C0103
		"""assert that Morphite2 is equal to 3
		"""

		self.assertEqual(Morphite2.amountonhand,3)

	def test_pixels2(self): # pylint:disable=C0103
		"""assert that pixels2 is equal to 4
		"""

		self.assertEqual(pixels2.amountonhand,4)

	def test_pixels2(self): # pylint:disable=C0103
		"""assert that pixels2 is equal to 3
		"""

		self.assertEqual(pixels2.amountonhand,3)

	def test_pixels2(self): # pylint:disable=C0103
		"""assert that pixels2 is equal to 3
		"""

		self.assertEqual(pixels2.amountonhand,3)

