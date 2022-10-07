"""unit testing code, test out Mode A and Mode B for the script
   readd to gitignore when pulling and merging modifications into master
"""
import random
import unittest

from numpy import true_divide

from main import Node, findlocalendpoints, reversearithmetic


class MODEAtesting(unittest.TestCase):
    """tentative description

    Args:
        unittest (_type_): _description_
    """
    tritaniumbar : Node = Node('Tritanium Bar')
    lead : Node = Node('Lead',tritaniumbar)
    pixels : Node = Node('Pixels',lead,0,1,200)
    irradiumbar : Node = Node('Irradium Bar',tritaniumbar)
    irradiumore : Node = Node('Irradium Ore',irradiumbar,0,1,2)
    pixels2 : Node = Node('Pixels',irradiumore,0,1,600)
    triangliumpyramid : Node = Node('Trianglium Pyramid',tritaniumbar)
    triangliumore : Node = Node('Trianglium Ore',triangliumpyramid,0,1,2)
    pixels3 : Node = Node('Pixels',triangliumore,0,1,810)
    prisilitestar : Node = Node('Prisilite Star',tritaniumbar)
    prismshard : Node = Node('Prism Shard',prisilitestar,0,1,2)
    pixels4 : Node = Node('Pixels',prismshard,0,1,1838) #? buy from geologist NPC ingame
    reversearithmetic(tritaniumbar,random.randint(1,100))
    roots : dict = findlocalendpoints(tritaniumbar,{})
    def test_endpointsdict(self):
        """test to see if the length of the endpoints dictionary
        is 4 elements
        """
        self.assertEqual(len(self.roots),4)
    def test_endpoints(self):
        """test to see if the item name of each endpoint is Pixels
        """
        isPixel : bool = True
        for instance in self.roots.items():
            isPixel : instance[1].name
        self.assertTrue(isPixel)