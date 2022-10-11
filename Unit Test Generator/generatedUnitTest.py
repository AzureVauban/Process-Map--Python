"""AUTO GENERATED UNIT TEST
"""
import unittest

from main import Node

Block_of_Netherite: Node = Node('Block of Netherite', None, 0, 1, 1)
morphite: Node = Node('morphite', Block_of_Netherite, 0, 1, 5)


class BlockofNetheritete_unittest(unittest.TestCase): # pylint:disable=C0103
	"""tentative test class, add additional comments here:
	"""

	def test_Block_of_Netherite(self):# pylint:disable=C0103
		"""assert that Block of Netherite is equal to 5
		"""

		self.assertEqual(Block_of_Netherite.amountonhand,5)

	def test_morphite(self):# pylint:disable=C0103
		"""assert that morphite is equal to 25
		"""

		self.assertEqual(morphite.amountonhand,25)


