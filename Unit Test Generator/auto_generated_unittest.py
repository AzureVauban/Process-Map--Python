"""AUTO GENERATED UNIT TEST
"""
import unittest

from main import Node, reversearithmetic

Gold_Bar: Node = Node('Gold Bar', None, 0, 1, 1)
Gold_Ore_: Node = Node('Gold Ore ', Gold_Bar, 0, 1, 2)
Pixels: Node = Node('Pixels', Gold_Ore_, 0, 1, 200)
reversearithmetic(Gold_Bar, 1)


class GOLDBARR_unittest(unittest.TestCase): # pylint:disable=C0103
	"""tentative test class, add additional comments here:
	"""

	def test_Gold_Bar(self): # pylint:disable=C0103
		"""assert that Gold Bar is equal to 1
		"""

		self.assertEqual(Gold_Bar.amountonhand,1)

	def test_Gold_Ore_(self): # pylint:disable=C0103
		"""assert that Gold Ore  is equal to 2
		"""

		self.assertEqual(Gold_Ore_.amountonhand,2)

	def test_Pixels(self): # pylint:disable=C0103
		"""assert that Pixels is equal to 400
		"""

		self.assertEqual(Pixels.amountonhand,400)

