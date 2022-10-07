"""Unit testing code for Python Process Map
	Generated from Unit Test generator
	PLEASE USE THE DOCUMENT FORMATING AND FORMATING IMPORT OPTIONS OF UTILIZED IDE
"""
import unittest

from main import Node, reversearithmetic


class Oji(unittest.TestCase):
	"""Unit Testing for a mock tree to create oji"""

	oji    : Node = Node('oji',None, 0, 1, 1) # key :0
	vgh    : Node = Node('vgh',oji, 0, 5, 6) # key :1
	hjg    : Node = Node('hjg',oji, 0, 5, 7) # key :2
	kjl    : Node = Node('kjl',oji, 0, 5, 8) # key :3
	hui    : Node = Node('hui',oji, 0, 5, 9) # key :4
	hui1    : Node = Node('hui',oji, 0, 5, 6) # key :5
	reversearithmetic(oji,83) # the resulted amount of head should be equal to or greater than the desired amount

	def test_oji(self):
		"""the asserted value of oji should be 83
		include additional comments here: ...
		"""
		self.assertEqual(self.oji.amountonhand, 83)
	def test_vgh(self):
		"""the asserted value of vgh should be 0
		include additional comments here: ...
		"""
		self.assertEqual(self.vgh.amountonhand, 0)
	def test_hjg(self):
		"""the asserted value of hjg should be 0
		include additional comments here: ...
		"""
		self.assertEqual(self.hjg.amountonhand, 0)
	def test_kjl(self):
		"""the asserted value of kjl should be 0
		include additional comments here: ...
		"""
		self.assertEqual(self.kjl.amountonhand, 0)
	def test_hui(self):
		"""the asserted value of hui should be 0
		include additional comments here: ...
		"""
		self.assertEqual(self.hui.amountonhand, 0)
	def test_hui1(self):
		"""the asserted value of hui should be 0
		include additional comments here: ...
		"""
		self.assertEqual(self.hui1.amountonhand, 0)
