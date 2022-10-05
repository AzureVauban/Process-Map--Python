"""Unit testing code for Python Process Map
   Generated from Unit Test generator
   PLEASE USE THE FORMAT DOCUMENT AND FORMAT IMPORT OPTIONS OF CHOSEN IDE
"""
import unittest

from main import Node, reversearithmetic


class Test_item(unittest.TestCase):
    """Unit Testing for a mock tree to create test item"""

    test_item: Node = Node('test item', None, 0, 1, 1)
    perfectly_generic_item: Node = Node(
        'perfectly generic item', test_item, 0, 1, 1)
    item_a: Node = Node('item a', perfectly_generic_item, 0, 1, 1)
    item_b: Node = Node('item b', perfectly_generic_item, 0, 1, 1)
    item_c: Node = Node('item c', perfectly_generic_item, 0, 1, 1)
    item_d: Node = Node('item d', perfectly_generic_item, 0, 1, 1)
    # the resulted amount of head should be equal to or greater than the desired amount
    reversearithmetic(test_item, 9999)


def test_test_item(self):
    """the asserted value of test item should be 0
       include additional comments here: 0x2572d1824b0
    """
    self.assertEqual(self.test_item.amountonhand, 0)


def test_perfectly_generic_item(self):
    """the asserted value of perfectly generic item should be 0
       include additional comments here: 0x2572d182580
    """
    self.assertEqual(self.perfectly_generic_item.amountonhand, 0)


def test_item_a(self):
    """the asserted value of item a should be 0
       include additional comments here: 0x2572d182690
    """
    self.assertEqual(self.item_a.amountonhand, 0)


def test_item_b(self):
    """the asserted value of item b should be 0
       include additional comments here: 0x2572d182850
    """
    self.assertEqual(self.item_b.amountonhand, 0)


def test_item_c(self):
    """the asserted value of item c should be 0
       include additional comments here: 0x2572d1828d0
    """
    self.assertEqual(self.item_c.amountonhand, 0)


def test_item_d(self):
    """the asserted value of item d should be 0
       include additional comments here: 0x2572d1829c0
    """
    self.assertEqual(self.item_d.amountonhand, 0)
