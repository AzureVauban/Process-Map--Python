"""AUTO GENERATED UNIT TEST
"""
import unittest

from main import Node

Block_of_Emeralds: Node = Node('Block of Emeralds', None, 0, 1, 1)
Emerald: Node = Node('Emerald', Block_of_Emeralds, 0, 1, 9)


class BlockofEmeraldsds_unittest(unittest.TestCase): # pylint:disable=C0103
	"""tentative test class, add additional comments here:
	"""

	def test_Block_of_Emeralds(self):# pylint:disable=C0103
		"""assert that Block of Emeralds is equal to 64
		"""

		self.assertEqual(Block_of_Emeralds.amountonhand,64)

	def test_Emerald(self):# pylint:disable=C0103
		"""assert that Emerald is equal to 576
		"""

		self.assertEqual(Emerald.amountonhand,576)


