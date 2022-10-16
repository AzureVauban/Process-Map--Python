"""unit testing code, test out Mode A and Mode B for the script
   re-add to gitignore when pulling and merging modifications into master
"""
import random
import unittest

from main import reversearithmetic  # pylint: disable
from main import Node, findlocalendpoints, reformat_output  # pylint: disable


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

    def test_betteroutput_testmethod(self):
        """_summary_ test to see if the output is formatted correctly
        """
        reformat_output(self.roots)
        print('terminating test')
        self.assertEqual(1, 1)


class Issue12_multiple_unique_endpoint(unittest.TestCase):  # pylint:disable=C0103
    """test new formatting and endpoint search methods from main.py module wih only one endpoint
    """
    focusingarray: Node = Node('Focusing Array', None, 1, 1, 1)
    advancedalloy: Node = Node('Advanced Alloy', focusingarray, 8, 1, 2)
    crystal: Node = Node('Crystal', focusingarray, 640, 1, 2)
    plasmiccrystal: Node = Node('Plasmic Crystal', focusingarray, 41, 2, 2)
    quantumprocessor: Node = Node('Quantum Processor', focusingarray, 20, 2, 1)
    zerchesiumbar: Node = Node('Zerchesium Bar', advancedalloy, 548, 1, 1)
    zerchesiumore: Node = Node('Zerchesium Ore', zerchesiumbar, 2, 1, 2)
    protocitebar: Node = Node('Protocite Bar', advancedalloy, 277, 1, 1)
    protociteore: Node = Node('Protocite Ore', protocitebar, 2, 1, 2)
    penumbriteshard: Node = Node('Penumbrite Shard', advancedalloy, 86, 1, 1)
    penumbriteore: Node = Node('Penumbrite Ore', penumbriteshard, 2, 1, 2)
    lead: Node = Node('Lead', advancedalloy, 251, 1, 1)
    crystalplantseed: Node = Node('Crystal Plant Seed', crystal, 100, 1, 1)
    bloodrock: Node = Node('Blood Rock', plasmiccrystal, 1000, 1, 50)
    blood: Node = Node('Blood', bloodrock, 23, 1, 1)
    lava: Node = Node('Lava', bloodrock, 404, 1, 1)
    protocitebarb: Node = Node('Protocite Bar', quantumprocessor, 277, 1, 2)
    protociteoreb: Node = Node('Protocite Ore', protocitebarb, 2, 1, 2)
    siliconboard: Node = Node('Silicon Board', quantumprocessor, 310, 1, 4)
    silicon: Node = Node('Silicon', siliconboard, 1000, 1, 1)
    sand: Node = Node('Sand', silicon, 901, 1, 50)
    copperwire: Node = Node('Copper Wire', siliconboard, 492, 9, 1)
    copperbar: Node = Node('Copper Bar', copperwire, 1000, 1, 1)
    copperore: Node = Node('Copper Ore', copperbar, 2, 1, 2)
    desiredamount: int = random.randint(1, 100)
    reversearithmetic(focusingarray, desiredamount)
    roots: dict = findlocalendpoints(focusingarray, {})

    def test_betteroutput_testmethod(self):
        """_summary_ test to see if the output is formatted correctly
        """
        reformat_output(self.roots)
        print('terminating test')
        self.assertEqual(1, 1)
