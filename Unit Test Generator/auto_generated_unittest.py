"""AUTO GENERATED UNIT TEST
"""
import unittest

from main import Node, reversearithmetic

Morphite: Node = Node('Morphite', None, 0, 1, 1)
Irradium_Bar: Node = Node('Irradium Bar', Morphite, 0, 1, 1)
Irradium_Ore: Node = Node('Irradium Ore', Irradium_Bar, 0, 1, 2)
Pixels: Node = Node('Pixels', Irradium_Ore, 0, 1, 600)
Liquid_Protocite: Node = Node('Liquid Protocite', Morphite, 0, 1, 1)
Liquid_Protocite_B: Node = Node('Liquid Protocite B', Liquid_Protocite, 0, 2, 1)
Pus: Node = Node('Pus', Liquid_Protocite, 0, 2, 1)
Blister_Sack: Node = Node('Blister Sack', Pus, 0, 1, 1)
Phase_Matter: Node = Node('Phase Matter', Morphite, 0, 1, 1)
Pixels_B: Node = Node('Pixels B', Phase_Matter, 0, 1, 150)
Sulphuric_Acid: Node = Node('Sulphuric Acid', Morphite, 0, 1, 2)
Whitespine: Node = Node('Whitespine', Sulphuric_Acid, 0, 2, 1)
reversearithmetic(Morphite, 9999)


class MORPHITE_unittest(unittest.TestCase): # pylint:disable=C0103
	"""tentative test class, add additional comments here:
	"""

	def test_Morphite(self): # pylint:disable=C0103
		"""assert that Morphite is equal to 9999
		"""

		self.assertEqual(Morphite.amountonhand,9999)

	def test_Irradium_Bar(self): # pylint:disable=C0103
		"""assert that Irradium Bar is equal to 9999
		"""

		self.assertEqual(Irradium_Bar.amountonhand,9999)

	def test_Irradium_Ore(self): # pylint:disable=C0103
		"""assert that Irradium Ore is equal to 19998
		"""

		self.assertEqual(Irradium_Ore.amountonhand,19998)

	def test_Pixels(self): # pylint:disable=C0103
		"""assert that Pixels is equal to 11998800
		"""

		self.assertEqual(Pixels.amountonhand,11998800)

	def test_Liquid_Protocite(self): # pylint:disable=C0103
		"""assert that Liquid Protocite is equal to 9999
		"""

		self.assertEqual(Liquid_Protocite.amountonhand,9999)

	def test_Liquid_Protocite_B(self): # pylint:disable=C0103
		"""assert that Liquid Protocite B is equal to 4999
		"""

		self.assertEqual(Liquid_Protocite_B.amountonhand,4999)

	def test_Pus(self): # pylint:disable=C0103
		"""assert that Pus is equal to 4999
		"""

		self.assertEqual(Pus.amountonhand,4999)

	def test_Blister_Sack(self): # pylint:disable=C0103
		"""assert that Blister Sack is equal to 4999
		"""

		self.assertEqual(Blister_Sack.amountonhand,4999)

	def test_Phase_Matter(self): # pylint:disable=C0103
		"""assert that Phase Matter is equal to 9999
		"""

		self.assertEqual(Phase_Matter.amountonhand,9999)

	def test_Pixels_B(self): # pylint:disable=C0103
		"""assert that Pixels B is equal to 1499850
		"""

		self.assertEqual(Pixels_B.amountonhand,1499850)

	def test_Sulphuric_Acid(self): # pylint:disable=C0103
		"""assert that Sulphuric Acid is equal to 19998
		"""

		self.assertEqual(Sulphuric_Acid.amountonhand,19998)

	def test_Whitespine(self): # pylint:disable=C0103
		"""assert that Whitespine is equal to 9999
		"""

		self.assertEqual(Whitespine.amountonhand,9999)

