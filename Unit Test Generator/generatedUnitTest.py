"""AUTO GENERATED UNIT TEST
"""
import unittest

from main import Node

Block_of_Netherite: Node = Node('Block of Netherite', None, 0, 1, 1)
Netherite_Ingot: Node = Node('Netherite Ingot', Block_of_Netherite, 0, 1, 9)
Gold_Ingot: Node = Node('Gold Ingot', Netherite_Ingot, 0, 1, 4)
Netherite_Scrap: Node = Node('Netherite Scrap', Netherite_Ingot, 0, 1, 4)
Emerald: Node = Node('Emerald', Netherite_Scrap, 0, 1, 34)


class BlockofNetheritete_unittest(unittest.TestCase): # pylint:disable=C0103
	"""tentative test class, add additional comments here:
	"""

	def test_Block_of_Netherite(self):# pylint:disable=C0103
		"""assert that Block of Netherite is equal to 89
		"""

		self.assertEqual(Block_of_Netherite.amountonhand,89)

	def test_Netherite_Ingot(self):# pylint:disable=C0103
		"""assert that Netherite Ingot is equal to 801
		"""

		self.assertEqual(Netherite_Ingot.amountonhand,801)

	def test_Gold_Ingot(self):# pylint:disable=C0103
		"""assert that Gold Ingot is equal to 3204
		"""

		self.assertEqual(Gold_Ingot.amountonhand,3204)

	def test_Netherite_Scrap(self):# pylint:disable=C0103
		"""assert that Netherite Scrap is equal to 3204
		"""

		self.assertEqual(Netherite_Scrap.amountonhand,3204)

	def test_Emerald(self):# pylint:disable=C0103
		"""assert that Emerald is equal to 108936
		"""

		self.assertEqual(Emerald.amountonhand,108936)


