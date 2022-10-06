"""Unit testing code for Python Process Map
	Generated from Unit Test generator
	PLEASE USE THE FORMAT DOCUMENT AND FORMAT IMPORT OPTIONS OF CHOSEN IDE
"""
import unittest

from main import Node, reversearithmetic


class Advanced_alloy(unittest.TestCase):
	"""Unit Testing for a mock tree to create advanced alloy"""

	advanced_alloy    : Node = Node('advanced alloy',None, 0, 1, 1) # key :0
	zerchesium_bar    : Node = Node('zerchesium bar',advanced_alloy, 0, 1, 1) # key :1
	protocite_bar    : Node = Node('protocite bar',advanced_alloy, 0, 1, 1) # key :2
	lead    : Node = Node('lead',advanced_alloy, 0, 1, 1) # key :3
	penumbrite_shard    : Node = Node('penumbrite shard',advanced_alloy, 0, 1, 1) # key :4
	zerchesium_ore    : Node = Node('zerchesium ore',zerchesium_bar, 0, 1, 2) # key :5
	protocite    : Node = Node('protocite',protocite_bar, 0, 1, 2) # key :6
	pixels    : Node = Node('pixels',lead, 0, 1, 50) # key :7
	penumbrite    : Node = Node('penumbrite',penumbrite_shard, 0, 1, 1) # key :8
	pixels1    : Node = Node('pixels',penumbrite, 0, 1, 150) # key :9
	reversearithmetic(advanced_alloy,80) # the resulted amount of head should be equal to or greater than the desired amount

	
def test_advanced_alloy(self):
		"""the asserted value of advanced alloy should be 80
		include additional comments here: 0x1e603b834e0
		"""
		self.assertEqual(self.advanced_alloy.amountonhand, 80)
	
def test_zerchesium_bar(self):
		"""the asserted value of zerchesium bar should be 0
		include additional comments here: 0x1e603b836a0
		"""
		self.assertEqual(self.zerchesium_bar.amountonhand, 0)
	
def test_protocite_bar(self):
		"""the asserted value of protocite bar should be 0
		include additional comments here: 0x1e603b83780
		"""
		self.assertEqual(self.protocite_bar.amountonhand, 0)
	
def test_lead(self):
		"""the asserted value of lead should be 0
		include additional comments here: 0x1e603b83820
		"""
		self.assertEqual(self.lead.amountonhand, 0)
	
def test_penumbrite_shard(self):
		"""the asserted value of penumbrite shard should be 0
		include additional comments here: 0x1e603b83910
		"""
		self.assertEqual(self.penumbrite_shard.amountonhand, 0)
	
def test_zerchesium_ore(self):
		"""the asserted value of zerchesium ore should be nan
		include additional comments here: 0x1e603b83ac0
		"""
		self.assertEqual(self.zerchesium_ore.amountonhand, nan)
	
def test_protocite(self):
		"""the asserted value of protocite should be nan
		include additional comments here: 0x1e603b83b60
		"""
		self.assertEqual(self.protocite.amountonhand, nan)
	
def test_pixels(self):
		"""the asserted value of pixels should be nan
		include additional comments here: 0x1e603b83c00
		"""
		self.assertEqual(self.pixels.amountonhand, nan)
	
def test_penumbrite(self):
		"""the asserted value of penumbrite should be 0
		include additional comments here: 0x1e603b83ca0
		"""
		self.assertEqual(self.penumbrite.amountonhand, 0)
	
def test_pixels1(self):
		"""the asserted value of pixels should be nan
		include additional comments here: 0x1e603b83e30
		"""
		self.assertEqual(self.pixels1.amountonhand, nan)
