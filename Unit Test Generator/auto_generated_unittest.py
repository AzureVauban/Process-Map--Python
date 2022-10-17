"""AUTO GENERATED UNIT TEST
"""
import unittest

from main import Node, reversearithmetic

Focusing_Array: Node = Node('Focusing Array', None, 0, 1, 1)
Advanced_Alloy: Node = Node('Advanced Alloy', Focusing_Array, 0, 1, 2)
Zerchesium_Bar: Node = Node('Zerchesium Bar', Advanced_Alloy, 0, 1, 1)
Zerchesium_Ore: Node = Node('Zerchesium Ore', Zerchesium_Bar, 0, 1, 2)
Pixels: Node = Node('Pixels', Zerchesium_Ore, 0, 1, 1400)
Protocite_Bar: Node = Node('Protocite Bar', Advanced_Alloy, 0, 1, 1)
Protocite: Node = Node('Protocite', Protocite_Bar, 0, 1, 2)
Pixels_B: Node = Node('Pixels B', Protocite, 0, 1, 390)
Penumbrite_Shard: Node = Node('Penumbrite Shard', Advanced_Alloy, 0, 1, 1)
Penumbrite_Ore: Node = Node('Penumbrite Ore', Penumbrite_Shard, 0, 1, 2)
Pixels_C: Node = Node('Pixels C', Penumbrite_Ore, 0, 1, 390)
Lead: Node = Node('Lead', Advanced_Alloy, 0, 1, 1)
Pixels_D: Node = Node('Pixels D', Lead, 0, 1, 60)
Crystal: Node = Node('Crystal', Focusing_Array, 0, 1, 2)
Prism_Shard: Node = Node('Prism Shard', Crystal, 0, 3, 1)
Pixels_E: Node = Node('Pixels E', Prism_Shard, 0, 1, 1838)
Plasmic_Crystal: Node = Node('Plasmic Crystal', Focusing_Array, 0, 1, 2)
Bloody_Rock: Node = Node('Bloody Rock', Plasmic_Crystal, 0, 1, 50)
Blood: Node = Node('Blood', Bloody_Rock, 0, 1, 1)
Teratomato: Node = Node('Teratomato', Blood, 0, 3, 1)
Teratomato_Seed: Node = Node('Teratomato Seed', Teratomato, 0, 1, 3)
Mercury: Node = Node('Mercury', Bloody_Rock, 0, 1, 1)
Cinnabar: Node = Node('Cinnabar', Mercury, 0, 2, 2)
Pixels_F: Node = Node('Pixels F', Cinnabar, 0, 1, 70)
Quantum_Processor: Node = Node('Quantum Processor', Focusing_Array, 0, 1, 1)
Silicon_Board: Node = Node('Silicon Board', Quantum_Processor, 0, 2, 4)
Silicon_: Node = Node('Silicon ', Silicon_Board, 0, 1, 1)
Sand_: Node = Node('Sand ', Silicon_, 0, 1, 50)
Cobblestone: Node = Node('Cobblestone', Sand_, 0, 3, 50)
Rockroot: Node = Node('Rockroot', Cobblestone, 0, 2, 1)
Rockroot_Seed: Node = Node('Rockroot Seed', Rockroot, 0, 1, 3)
Copper_Wire: Node = Node('Copper Wire', Silicon_Board, 0, 1, 1)
Copper_Bar: Node = Node('Copper Bar', Copper_Wire, 0, 9, 1)
Copper_Ore: Node = Node('Copper Ore', Copper_Bar, 0, 1, 2)
Pixels_G: Node = Node('Pixels G', Copper_Ore, 0, 1, 88)
Protocite_Bar_B: Node = Node('Protocite Bar B', Quantum_Processor, 0, 2, 2)
Protocite_B: Node = Node('Protocite B', Protocite_Bar_B, 0, 1, 2)
Pixels_H: Node = Node('Pixels H', Protocite_B, 0, 1, 390)
reversearithmetic(Focusing_Array, 1)


class FOCUSINGARRAYY_unittest(unittest.TestCase): # pylint:disable=C0103
	"""tentative test class, add additional comments here:
	"""

	def test_Focusing_Array(self): # pylint:disable=C0103
		"""assert that Focusing Array is equal to 1
		"""

		self.assertEqual(Focusing_Array.amountonhand,1)

	def test_Advanced_Alloy(self): # pylint:disable=C0103
		"""assert that Advanced Alloy is equal to 2
		"""

		self.assertEqual(Advanced_Alloy.amountonhand,2)

	def test_Zerchesium_Bar(self): # pylint:disable=C0103
		"""assert that Zerchesium Bar is equal to 2
		"""

		self.assertEqual(Zerchesium_Bar.amountonhand,2)

	def test_Zerchesium_Ore(self): # pylint:disable=C0103
		"""assert that Zerchesium Ore is equal to 4
		"""

		self.assertEqual(Zerchesium_Ore.amountonhand,4)

	def test_Pixels(self): # pylint:disable=C0103
		"""assert that Pixels is equal to 5600
		"""

		self.assertEqual(Pixels.amountonhand,5600)

	def test_Protocite_Bar(self): # pylint:disable=C0103
		"""assert that Protocite Bar is equal to 2
		"""

		self.assertEqual(Protocite_Bar.amountonhand,2)

	def test_Protocite(self): # pylint:disable=C0103
		"""assert that Protocite is equal to 4
		"""

		self.assertEqual(Protocite.amountonhand,4)

	def test_Pixels_B(self): # pylint:disable=C0103
		"""assert that Pixels B is equal to 1560
		"""

		self.assertEqual(Pixels_B.amountonhand,1560)

	def test_Penumbrite_Shard(self): # pylint:disable=C0103
		"""assert that Penumbrite Shard is equal to 2
		"""

		self.assertEqual(Penumbrite_Shard.amountonhand,2)

	def test_Penumbrite_Ore(self): # pylint:disable=C0103
		"""assert that Penumbrite Ore is equal to 4
		"""

		self.assertEqual(Penumbrite_Ore.amountonhand,4)

	def test_Pixels_C(self): # pylint:disable=C0103
		"""assert that Pixels C is equal to 1560
		"""

		self.assertEqual(Pixels_C.amountonhand,1560)

	def test_Lead(self): # pylint:disable=C0103
		"""assert that Lead is equal to 2
		"""

		self.assertEqual(Lead.amountonhand,2)

	def test_Pixels_D(self): # pylint:disable=C0103
		"""assert that Pixels D is equal to 120
		"""

		self.assertEqual(Pixels_D.amountonhand,120)

	def test_Crystal(self): # pylint:disable=C0103
		"""assert that Crystal is equal to 2
		"""

		self.assertEqual(Crystal.amountonhand,2)

	def test_Prism_Shard(self): # pylint:disable=C0103
		"""assert that Prism Shard is equal to 0
		"""

		self.assertEqual(Prism_Shard.amountonhand,0)

	def test_Pixels_E(self): # pylint:disable=C0103
		"""assert that Pixels E is equal to 0
		"""

		self.assertEqual(Pixels_E.amountonhand,0)

	def test_Plasmic_Crystal(self): # pylint:disable=C0103
		"""assert that Plasmic Crystal is equal to 2
		"""

		self.assertEqual(Plasmic_Crystal.amountonhand,2)

	def test_Bloody_Rock(self): # pylint:disable=C0103
		"""assert that Bloody Rock is equal to 100
		"""

		self.assertEqual(Bloody_Rock.amountonhand,100)

	def test_Blood(self): # pylint:disable=C0103
		"""assert that Blood is equal to 100
		"""

		self.assertEqual(Blood.amountonhand,100)

	def test_Teratomato(self): # pylint:disable=C0103
		"""assert that Teratomato is equal to 33
		"""

		self.assertEqual(Teratomato.amountonhand,33)

	def test_Teratomato_Seed(self): # pylint:disable=C0103
		"""assert that Teratomato Seed is equal to 99
		"""

		self.assertEqual(Teratomato_Seed.amountonhand,99)

	def test_Mercury(self): # pylint:disable=C0103
		"""assert that Mercury is equal to 100
		"""

		self.assertEqual(Mercury.amountonhand,100)

	def test_Cinnabar(self): # pylint:disable=C0103
		"""assert that Cinnabar is equal to 100
		"""

		self.assertEqual(Cinnabar.amountonhand,100)

	def test_Pixels_F(self): # pylint:disable=C0103
		"""assert that Pixels F is equal to 7000
		"""

		self.assertEqual(Pixels_F.amountonhand,7000)

	def test_Quantum_Processor(self): # pylint:disable=C0103
		"""assert that Quantum Processor is equal to 1
		"""

		self.assertEqual(Quantum_Processor.amountonhand,1)

	def test_Silicon_Board(self): # pylint:disable=C0103
		"""assert that Silicon Board is equal to 2
		"""

		self.assertEqual(Silicon_Board.amountonhand,2)

	def test_Silicon_(self): # pylint:disable=C0103
		"""assert that Silicon  is equal to 2
		"""

		self.assertEqual(Silicon_.amountonhand,2)

	def test_Sand_(self): # pylint:disable=C0103
		"""assert that Sand  is equal to 100
		"""

		self.assertEqual(Sand_.amountonhand,100)

	def test_Cobblestone(self): # pylint:disable=C0103
		"""assert that Cobblestone is equal to 1666
		"""

		self.assertEqual(Cobblestone.amountonhand,1666)

	def test_Rockroot(self): # pylint:disable=C0103
		"""assert that Rockroot is equal to 833
		"""

		self.assertEqual(Rockroot.amountonhand,833)

	def test_Rockroot_Seed(self): # pylint:disable=C0103
		"""assert that Rockroot Seed is equal to 2499
		"""

		self.assertEqual(Rockroot_Seed.amountonhand,2499)

	def test_Copper_Wire(self): # pylint:disable=C0103
		"""assert that Copper Wire is equal to 2
		"""

		self.assertEqual(Copper_Wire.amountonhand,2)

	def test_Copper_Bar(self): # pylint:disable=C0103
		"""assert that Copper Bar is equal to 0
		"""

		self.assertEqual(Copper_Bar.amountonhand,0)

	def test_Copper_Ore(self): # pylint:disable=C0103
		"""assert that Copper Ore is equal to 0
		"""

		self.assertEqual(Copper_Ore.amountonhand,0)

	def test_Pixels_G(self): # pylint:disable=C0103
		"""assert that Pixels G is equal to 0
		"""

		self.assertEqual(Pixels_G.amountonhand,0)

	def test_Protocite_Bar_B(self): # pylint:disable=C0103
		"""assert that Protocite Bar B is equal to 1
		"""

		self.assertEqual(Protocite_Bar_B.amountonhand,1)

	def test_Protocite_B(self): # pylint:disable=C0103
		"""assert that Protocite B is equal to 2
		"""

		self.assertEqual(Protocite_B.amountonhand,2)

	def test_Pixels_H(self): # pylint:disable=C0103
		"""assert that Pixels H is equal to 780
		"""

		self.assertEqual(Pixels_H.amountonhand,780)

