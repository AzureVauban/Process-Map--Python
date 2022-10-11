"""AUTO GENERATED UNIT TEST
"""
import unittest

from main import Node

Block_of_Netherite: Node = Node('Block of Netherite', None, 0, 1, 1)
Netherite_Ingot: Node = Node('Netherite Ingot', Block_of_Netherite, 0, 1, 9)
Gold_Ingot: Node = Node('Gold Ingot', Netherite_Ingot, 0, 1, 4)
Netherite_Scrap: Node = Node('Netherite Scrap', Netherite_Ingot, 0, 1, 4)
Emerald: Node = Node('Emerald', Netherite_Scrap, 0, 1, 34)


class BlockofNetheritete_unittest(unittest.TestCase): #pylint:disable=C0103
	"""tentative test class, add additional comments here: 
	"""

	def test_Block_of_Netherite(self):
		"""assert that Block of Netherite is equal to 0
		"""
		self.assertEqual(Block_of_Netherite.amountonhand,0)
	def test_Netherite_Ingot(self):
		"""assert that Netherite Ingot is equal to 0
		"""
		self.assertEqual(Netherite_Ingot.amountonhand,0)
	def test_Gold_Ingot(self):
		"""assert that Gold Ingot is equal to 0
		"""
		self.assertEqual(Gold_Ingot.amountonhand,0)
	def test_Netherite_Scrap(self):
		"""assert that Netherite Scrap is equal to 1
		"""
		self.assertEqual(Netherite_Scrap.amountonhand,1)
	def test_Emerald(self):
		"""assert that Emerald is equal to 0
		"""
		self.assertEqual(Emerald.amountonhand,0)

