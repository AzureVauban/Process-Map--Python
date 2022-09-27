"""unit tesint module for Process Map (Python v1.1)
"""
import unittest

from solution import Node, searchforendpoint

# test tree - Focusing Array
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
searchforendpoint(focusingarray)


class tests(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """
    def test1(self):
        """_summary_
        """
        self.assertTrue(focusingarray, not None)
        