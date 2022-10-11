"""AUTO GENERATED UNIT TEST
"""
import unittest

from main import Node

Block_of_Netherite: Node = Node('Block of Netherite', None, 0, 1, 1)
Netherite_Ingot: Node = Node('Netherite Ingot', Block_of_Netherite, 0, 10, 100)
Gold_Ingot: Node = Node('Gold Ingot', Netherite_Ingot, 0, 1, 4)
Netherite_Scrap: Node = Node('Netherite Scrap', Netherite_Ingot, 0, 1, 4)
Emerald: Node = Node('Emerald', Netherite_Scrap, 0, 1, 34)


class BlockofNetheritete_unittest(unittest.TestCase): # pylint:disable=C0103
	"""tentative test class, add additional comments here:
	"""

	def test_Block_of_Netherite(self):# pylint:disable=C0103
		"""assert that Block of Netherite is equal to 9
		"""

		self.assertEqual(Block_of_Netherite.amountonhand,9)

	def test_Netherite_Ingot(self):# pylint:disable=C0103
		"""assert that Netherite Ingot is equal to 90
		"""

		self.assertEqual(Netherite_Ingot.amountonhand,90)

	def test_Gold_Ingot(self):# pylint:disable=C0103
		"""assert that Gold Ingot is equal to 360
		"""

		self.assertEqual(Gold_Ingot.amountonhand,360)

	def test_Netherite_Scrap(self):# pylint:disable=C0103
		"""assert that Netherite Scrap is equal to 360
		"""

		self.assertEqual(Netherite_Scrap.amountonhand,360)

	def test_Emerald(self):# pylint:disable=C0103
		"""assert that Emerald is equal to 12240
		"""

		self.assertEqual(Emerald.amountonhand,12240)


