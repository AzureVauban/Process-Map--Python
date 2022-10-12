"""AUTO GENERATED UNIT TEST
"""
import unittest

from main import Node, reversearithmetic

Morphite: Node = Node('Morphite', None, 0, 1, 1)
Mini_Morphit: Node = Node('Mini Morphit', Morphite, 0, 1, 9)
booitem: Node = Node('booitem', Mini_Morphit, 0, 9, 1)
reversearithmetic(Morphite, 64)


class MORPHITE_unittest(unittest.TestCase): # pylint:disable=C0103
	"""tentative test class, add additional comments here:
	"""

	def test_Morphite(self): # pylint:disable=C0103
		"""assert that Morphite is equal to 64
		"""

		self.assertEqual(Morphite.amountonhand,64)

	def test_Mini_Morphit(self): # pylint:disable=C0103
		"""assert that Mini Morphit is equal to 576
		"""

		self.assertEqual(Mini_Morphit.amountonhand,576)

	def test_booitem(self): # pylint:disable=C0103
		"""assert that booitem is equal to 64
		"""

		self.assertEqual(booitem.amountonhand,64)


