"""Unit testing code for Python Process Map
   Generated from Unit Test generator
   PLEASE USE THE FORMAT DOCUMENT AND FORMAT IMPORT OPTIONS OF CHOSEN IDE
"""
import unittest

from main import Node, reversearithmetic


class Random_alloy(unittest.TestCase):
    """Unit Testing for a mock tree to create random alloy"""

    random_alloy: Node = Node('random alloy', None, 0, 1, 1)
    metal_a0_1: Node = Node('metal a', random_alloy, 0, 0, 0)
    metal_b0_2: Node = Node('metal b', random_alloy, 0, 0, 0)
    metal_c0_3: Node = Node('metal c', random_alloy, 0, 0, 0)
    metal_d0_4: Node = Node('metal d', random_alloy, 0, 0, 0)
    metal_e0_5: Node = Node('metal e', random_alloy, 0, 0, 0)
    pixels0_6: Node = Node('pixels', metal_a0_1, 0, 0, 0)
    pixels1_7: Node = Node('pixels', metal_b0_2, 0, 0, 0)
    pixels2_8: Node = Node('pixels', metal_c0_3, 0, 0, 0)
    pixels3_9: Node = Node('pixels', metal_d0_4, 0, 0, 0)
    pixels4_10: Node = Node('pixels', metal_e0_5, 0, 0, 0)
    # the resulted amount of head should be equal to or greater than the desired amount
    reversearithmetic(random_alloy, 0)


def test_random_alloy(self):
    """the asserted value of random alloy should be 0
       include additional comments here: 0x1bd56ae24b0
    """
    self.assertEqual(self.random_alloy.amountonhand, 0)


def test_metal_a0(self):
    """the asserted value of metal a should be 0
       include additional comments here: 0x1bd56ae2530
    """
    self.assertEqual(self.metal_a0.amountonhand, 0)


def test_metal_b0(self):
    """the asserted value of metal b should be 0
       include additional comments here: 0x1bd56ae25b0
    """
    self.assertEqual(self.metal_b0.amountonhand, 0)


def test_metal_c0(self):
    """the asserted value of metal c should be 0
       include additional comments here: 0x1bd56ae2780
    """
    self.assertEqual(self.metal_c0.amountonhand, 0)


def test_metal_d0(self):
    """the asserted value of metal d should be 0
       include additional comments here: 0x1bd56ae2800
    """
    self.assertEqual(self.metal_d0.amountonhand, 0)


def test_metal_e0(self):
    """the asserted value of metal e should be 0
       include additional comments here: 0x1bd56ae28f0
    """
    self.assertEqual(self.metal_e0.amountonhand, 0)


def test_pixels0(self):
    """the asserted value of pixels should be 0
       include additional comments here: 0x1bd56ae29e0
    """
    self.assertEqual(self.pixels0.amountonhand, 0)


def test_pixels1(self):
    """the asserted value of pixels should be 0
       include additional comments here: 0x1bd56ae2a60
    """
    self.assertEqual(self.pixels1.amountonhand, 0)


def test_pixels2(self):
    """the asserted value of pixels should be 0
       include additional comments here: 0x1bd56ae2ae0
    """
    self.assertEqual(self.pixels2.amountonhand, 0)


def test_pixels3(self):
    """the asserted value of pixels should be 0
       include additional comments here: 0x1bd56ae2c50
    """
    self.assertEqual(self.pixels3.amountonhand, 0)


def test_pixels4(self):
    """the asserted value of pixels should be 0
       include additional comments here: 0x1bd56ae2cd0
    """
    self.assertEqual(self.pixels4.amountonhand, 0)
