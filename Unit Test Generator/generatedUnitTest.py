"""AUTO GENERATED UNIT TEST
"""
import unittest

from main import Node

Block_of_Netherite: Node = Node('Block of Netherite', None, 0, 1, 1)
NetheriteIngott: Node = Node('NetheriteIngott', Block_of_Netherite, 0, 1, 9)


class BlockofNetheritete_unittest(unittest.TestCase): # pylint:disable=C0103
	"""tentative test class, add additional comments here:
	"""

	def test_Block_of_Netherite(self):# pylint:disable=C0103
		"""assert that Block of Netherite is equal to 64
		"""

		self.assertEqual(Block_of_Netherite.amountonhand,64)

	def test_NetheriteIngott(self):# pylint:disable=C0103
		"""assert that NetheriteIngott is equal to 576
		"""

		self.assertEqual(NetheriteIngott.amountonhand,576)


