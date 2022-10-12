"""AUTO GENERATED UNIT TEST
"""
import unittest

from main import Node, reversearithmetic

Block_of_Emerald: Node = Node('Block of Emerald', None, 0, 1, 1)
Emerald: Node = Node('Emerald', Block_of_Emerald, 0, 1, 9)
Wooden_Stck: Node = Node('Wooden Stck', Emerald, 0, 1, 31)
Oak_Planks: Node = Node('Oak Planks', Wooden_Stck, 0, 4, 2)
Oak_Wood: Node = Node('Oak Wood', Oak_Planks, 0, 4, 1)
reversearithmetic(Block_of_Emerald, 64)


class BLOCKOFEMERALDLD_unittest(unittest.TestCase): # pylint:disable=C0103
	"""tentative test class, add additional comments here:
	"""

	def test_Block_of_Emerald(self): # pylint:disable=C0103
		"""assert that Block of Emerald is equal to 64
		"""

		self.assertEqual(Block_of_Emerald.amountonhand,64)

	def test_Emerald(self): # pylint:disable=C0103
		"""assert that Emerald is equal to 576
		"""

		self.assertEqual(Emerald.amountonhand,576)

	def test_Wooden_Stck(self): # pylint:disable=C0103
		"""assert that Wooden Stck is equal to 17856
		"""

		self.assertEqual(Wooden_Stck.amountonhand,17856)

	def test_Oak_Planks(self): # pylint:disable=C0103
		"""assert that Oak Planks is equal to 8928
		"""

		self.assertEqual(Oak_Planks.amountonhand,8928)

	def test_Oak_Wood(self): # pylint:disable=C0103
		"""assert that Oak Wood is equal to 2232
		"""

		self.assertEqual(Oak_Wood.amountonhand,2232)

