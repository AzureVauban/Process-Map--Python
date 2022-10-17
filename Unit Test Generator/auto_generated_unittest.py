"""AUTO GENERATED UNIT TEST
"""
import unittest

from main import Node, reversearithmetic

Block_of_Diamond: Node = Node('Block of Diamond', None, 0, 1, 1)
Diamond: Node = Node('Diamond', Block_of_Diamond, 0, 1, 9)
reversearithmetic(Block_of_Diamond, 64)


class BLOCKOFDIAMONDND_unittest(unittest.TestCase): # pylint:disable=C0103
	"""tentative test class, add additional comments here:
	"""

	def test_Block_of_Diamond(self): # pylint:disable=C0103
		"""assert that Block of Diamond is equal to 64
		"""

		self.assertEqual(Block_of_Diamond.amountonhand,64)

	def test_Diamond(self): # pylint:disable=C0103
		"""assert that Diamond is equal to 576
		"""

		self.assertEqual(Diamond.amountonhand,576)

