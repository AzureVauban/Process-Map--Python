"""Unit testing code for Python Process Map
   Auto Generated
"""
import unittest

from main import Node


class Head(unittest.TestCase):
	"""Unit Testing for a mock tree to create head"""

	head	: Node = Node('head',None, 0, 1, 1)
	tail	: Node = Node('tail',head, 0, 1, 1)
	tail2	: Node = Node('tail2',head, 0, 1, 1)
	tail3	: Node = Node('tail3',head, 0, 1, 1)
	def test_head(self):
		"""the amount resulted of head should be 0"""
		self.assertEqual(self.head.amountonhand, 0)
	def test_tail(self):
		"""the amount resulted of tail should be 0"""
		self.assertEqual(self.tail.amountonhand, 0)
	def test_tail2(self):
		"""the amount resulted of tail2 should be 0"""
		self.assertEqual(self.tail2.amountonhand, 0)
	def test_tail3(self):
		"""the amount resulted of tail3 should be 0"""
		self.assertEqual(self.tail3.amountonhand, 0)
