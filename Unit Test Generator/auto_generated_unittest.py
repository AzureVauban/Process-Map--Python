"""AUTO GENERATED UNIT TEST
"""
import unittest

from main import Node, reversearithmetic

morphite2: Node = Node('morphite2', None, 0, 1, 1)
pixels2: Node = Node('pixels2', morphite2, 0, 5, 20)
pixels2: Node = Node('pixels2', morphite2, 0, 5, 30)
pixels2: Node = Node('pixels2', morphite2, 0, 5, 40)
pixels2: Node = Node('pixels2', morphite2, 0, 5, 50)
reversearithmetic(morphite2, 8)


class MORPHITE2_unittest(unittest.TestCase): # pylint:disable=C0103
	"""tentative test class, add additional comments here:
	"""

	def test_morphite2(self): # pylint:disable=C0103
		"""assert that morphite2 is equal to 8
		"""

		self.assertEqual(morphite2.amountonhand,8)

	def test_pixels2(self): # pylint:disable=C0103
		"""assert that pixels2 is equal to 32
		"""

		self.assertEqual(pixels2.amountonhand,32)

	def test_pixels2(self): # pylint:disable=C0103
		"""assert that pixels2 is equal to 48
		"""

		self.assertEqual(pixels2.amountonhand,48)

	def test_pixels2(self): # pylint:disable=C0103
		"""assert that pixels2 is equal to 64
		"""

		self.assertEqual(pixels2.amountonhand,64)

	def test_pixels2(self): # pylint:disable=C0103
		"""assert that pixels2 is equal to 80
		"""

		self.assertEqual(pixels2.amountonhand,80)

