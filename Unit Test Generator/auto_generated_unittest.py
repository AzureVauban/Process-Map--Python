"""AUTO GENERATED UNIT TEST
"""
import unittest

from main import Node, reversearithmetic

Scorched_Core: Node = Node('Scorched Core', None, 0, 1, 1)
Thanatite_Crystal: Node = Node('Thanatite Crystal', Scorched_Core, 0, 1, 10)
Thanatite_Crystal_Seed_2: Node = Node('Thanatite Crystal Seed 2', Thanatite_Crystal, 0, 1, 3)
Thanatite_Crystal_Seed: Node = Node('Thanatite Crystal Seed', Scorched_Core, 0, 1, 5)
Crystal: Node = Node('Crystal', Thanatite_Crystal_Seed, 0, 5, 2)
Pixels: Node = Node('Pixels', Crystal, 0, 1, 122)
Iron_Ore: Node = Node('Iron Ore', Thanatite_Crystal_Seed, 0, 5, 1)
Pixels_2: Node = Node('Pixels 2', Iron_Ore, 0, 1, 175)
Core_Fragment: Node = Node('Core Fragment', Thanatite_Crystal_Seed, 0, 5, 2)
Pixels_3: Node = Node('Pixels 3', Core_Fragment, 0, 1, 250)
reversearithmetic(Scorched_Core, 9999)


class SCORCHEDCOREE_unittest(unittest.TestCase): # pylint:disable=C0103
	"""tentative test class, add additional comments here:
	"""

	def test_Scorched_Core(self): # pylint:disable=C0103
		"""assert that Scorched Core is equal to 9999
		"""

		self.assertEqual(Scorched_Core.amountonhand,9999)

	def test_Thanatite_Crystal(self): # pylint:disable=C0103
		"""assert that Thanatite Crystal is equal to 99990
		"""

		self.assertEqual(Thanatite_Crystal.amountonhand,99990)

	def test_Thanatite_Crystal_Seed_2(self): # pylint:disable=C0103
		"""assert that Thanatite Crystal Seed 2 is equal to 299970
		"""

		self.assertEqual(Thanatite_Crystal_Seed_2.amountonhand,299970)

	def test_Thanatite_Crystal_Seed(self): # pylint:disable=C0103
		"""assert that Thanatite Crystal Seed is equal to 49995
		"""

		self.assertEqual(Thanatite_Crystal_Seed.amountonhand,49995)

	def test_Crystal(self): # pylint:disable=C0103
		"""assert that Crystal is equal to 19998
		"""

		self.assertEqual(Crystal.amountonhand,19998)

	def test_Pixels(self): # pylint:disable=C0103
		"""assert that Pixels is equal to 2439756
		"""

		self.assertEqual(Pixels.amountonhand,2439756)

	def test_Iron_Ore(self): # pylint:disable=C0103
		"""assert that Iron Ore is equal to 9999
		"""

		self.assertEqual(Iron_Ore.amountonhand,9999)

	def test_Pixels_2(self): # pylint:disable=C0103
		"""assert that Pixels 2 is equal to 1749825
		"""

		self.assertEqual(Pixels_2.amountonhand,1749825)

	def test_Core_Fragment(self): # pylint:disable=C0103
		"""assert that Core Fragment is equal to 19998
		"""

		self.assertEqual(Core_Fragment.amountonhand,19998)

	def test_Pixels_3(self): # pylint:disable=C0103
		"""assert that Pixels 3 is equal to 4999500
		"""

		self.assertEqual(Pixels_3.amountonhand,4999500)

