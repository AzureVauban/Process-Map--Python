"""unit testing code, test out Mode A and Mode B for the script
   re-add to gitignore when pulling and merging modifications into master
"""
import random
import unittest

from main import Node, findlocalendpoints, reversearithmetic


class Issue12_single_unique_endpoint(unittest.TestCase):  # pylint:disable=C0103
    """test new formatting and endpoint search methods from main.py module wih only one endpoint

    Args:
        unittest (class): Unit testing framework for python
    """
    # ? Tritanium Bar Mock Tree: https://frackinuniverse.miraheze.org/wiki/Tritanium_Bar
    desiredamount: int = random.randint(1, 100)
    # it should take 6696 pixels to make one tritanium bar
    tritaniumbar: Node = Node('Tritanium Bar')
    lead: Node = Node('Lead', tritaniumbar)
    pixels: Node = Node('Pixels', lead, 0, 1, 200)
    irradiumbar: Node = Node('Irradium Bar', tritaniumbar)
    irradiumore: Node = Node('Irradium Ore', irradiumbar, 0, 1, 2)
    pixels2: Node = Node('Pixels', irradiumore, 0, 1, 600)
    triangliumpyramid: Node = Node('Trianglium Pyramid', tritaniumbar)
    triangliumore: Node = Node('Trianglium Ore', triangliumpyramid, 0, 1, 2)
    pixels3: Node = Node('Pixels', triangliumore, 0, 1, 810)
    prisilitestar: Node = Node('Prisilite Star', tritaniumbar)
    prismshard: Node = Node('Prism Shard', prisilitestar, 0, 1, 2)
    # buy prism shards from geologist NPC ingame
    pixels4: Node = Node('Pixels', prismshard, 0, 1, 1838)
    reversearithmetic(tritaniumbar, desiredamount)
    roots: dict = findlocalendpoints(tritaniumbar, {})
    # should 4 endpoints, but 1 (all the endpoints are pixels) item in its endpoint output

    def test_endpointsdict(self):
        """test to see if the length of the endpoints dictionary
        is 4 elements
        """
        self.assertEqual(len(self.roots), 4)

    def test_endpoints(self):
        """test to see if the item name of each endpoint is Pixels
        """
        iscalledpixels: bool = True
        for instance in self.roots.items():
            if not isinstance(instance[1], Node):
                raise TypeError('endpoint is not an instance of', Node)
            else:
                iscalledpixels = instance[1].ingredient == 'Pixels'
                if not iscalledpixels:
                    break
        self.assertTrue(iscalledpixels)

    def test_temptest(self):
        """test to see if the total sum of the endpoint node's % compostion correctly
           rounds towards 1 (100%)
        """
        blue: list = []
        red : dict = {} #? {itemname,list [amountonhand of each endpoint]}
        # set the secondary dict
        for crimson in self.roots.items():
            ispresent : bool = crimson[1].ingredi
            red.update({crimson[1].ingredient:[crimson[1].amountonhand]})
        # set the return dictionary to be a list and have no keys
        for nodeinstance in self.roots.items():
            blue.append(nodeinstance[1])
        # todo make return dictionary/list have unique nodes
        for firuzeh in blue:
            indexpos: int = 0
            if not isinstance(firuzeh, Node):
                raise TypeError('firuzeh is not an instance of', Node)
            for azure in blue:
                if not isinstance(azure, Node):
                    raise TypeError('azure is not an instance of', Node)
                if azure.instancekey != firuzeh.instancekey and azure.ingredient == firuzeh.ingredient:
                    firuzeh.amountonhand += azure.amountonhand
                    blue.pop(indexpos)
                    #check to see if the dictionary has the item inputted, if it is, update the list witin the dictionary
                    isstored: bool = False
                    for tentative in red.items():
                        if not isinstance(tentative[1],list):
                            raise TypeError('the dictionary is supposed to store an instance of',list,'not an instance of',type(tentative[1]))
            indexpos += 1
        # make sure only one ingredient type is there, in this test class it should be pixels
        # desired output Pixels : 147312x (2.99 % used in Lead, 17.92 % used in Irradium Ore, 24.19 % used in Trianglium Ore, 54.9 % used in Prism Shard)
        self.assertEqual(len(blue), 1)


class Issue12_multiple_unique_endpoint(unittest.TestCase):  # pylint:disable=C0103
    """test new formatting and endpoint search methods from main.py module wih only one endpoint
    """
    pass
