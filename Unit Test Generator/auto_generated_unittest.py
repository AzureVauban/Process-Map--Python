"""AUTO GENERATED UNIT TEST
"""
import unittest

from main import Node, reversearithmetic

Block_of_Emerald: Node = Node('Block of Emerald', None, 0, 1, 1)
Emerald: Node = Node('Emerald', Block_of_Emerald, 0, 1, 9)
Stick: Node = Node('Stick', Emerald, 0, 1, 32)
Oak_Planks: Node = Node('Oak Planks', Stick, 0, 4, 2)
Oak_Wood: Node = Node('Oak Wood', Oak_Planks, 0, 4, 1)
reversearithmetic(Block_of_Emerald, 1)


class BLOCKOFEMERALDLD_unittest(unittest.TestCase): # pylint:disable=C0103
	"""tentative test class, add additional comments here:
	"""

	def test_Block_of_Emerald(self): # pylint:disable=C0103
		"""assert that Block of Emerald is equal to 1
		"""

		self.assertEqual(Block_of_Emerald.amountonhand,1)

	def test_Emerald(self): # pylint:disable=C0103
		"""assert that Emerald is equal to 9
		"""

		self.assertEqual(Emerald.amountonhand,9)

	def test_Stick(self): # pylint:disable=C0103
		"""assert that Stick is equal to 288
		"""

		self.assertEqual(Stick.amountonhand,288)

	def test_Oak_Planks(self): # pylint:disable=C0103
		"""assert that Oak Planks is equal to 144
		"""

		self.assertEqual(Oak_Planks.amountonhand,144)

	def test_Oak_Wood(self): # pylint:disable=C0103
		"""assert that Oak Wood is equal to 36
		"""

		self.assertEqual(Oak_Wood.amountonhand,36)

