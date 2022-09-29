"""unit testing code
"""
import unittest

from main import PROGRAMMODETYPE, Node, findlocalendpoints, searchforendpoint
from main import reversearithmetic

class MODEAtesting(unittest.TestCase):
    """Unit Testing

    Args:
        unittest (_type_): test case 
    """
    focusingarray       : Node = Node('Focusing Array', None, 1, 1, 1)
    advancedalloy       : Node = Node('Advanced Alloy', focusingarray, 8, 1, 2)
    crystal             : Node = Node('Crystal', focusingarray, 640, 1, 2)
    plasmiccrystal      : Node = Node('Plasmic Crystal', focusingarray, 41, 2, 2)
    quantumprocessor    : Node = Node('Quantum Processor', focusingarray, 20, 2, 1)
    zerchesiumbar       : Node = Node('Zerchesium Bar', advancedalloy, 548, 1, 1)
    zerchesiumore       : Node = Node('Zerchesium Ore', zerchesiumbar, 2, 1, 2)
    protocitebar        : Node = Node('Protocite Bar', advancedalloy, 277, 1, 1)
    protociteore        : Node = Node('Protocite Ore', protocitebar, 2, 1, 2)
    penumbriteshard     : Node = Node('Penumbrite Shard', advancedalloy, 86, 1, 1)
    penumbriteore       : Node = Node('Penumbrite Ore', penumbriteshard, 2, 1, 2)
    lead                : Node = Node('Lead', advancedalloy, 251, 1, 1)
    crystalplantseed    : Node = Node('Crystal Plant Seed', crystal, 100, 1, 1)
    bloodrock           : Node = Node('Blood Rock', plasmiccrystal, 1000, 1, 50)
    blood               : Node = Node('Blood', bloodrock, 23, 1, 1)
    lava                : Node = Node('Lava', bloodrock, 404, 1, 1)
    protocitebarb       : Node = Node('Protocite Bar', quantumprocessor, 277, 1, 2)
    protociteoreb       : Node = Node('Protocite Ore', protocitebarb, 2, 1, 2)
    siliconboard        : Node = Node('Silicon Board', quantumprocessor, 310, 1, 4)
    silicon             : Node = Node('Silicon', siliconboard, 1000, 1, 1)
    sand                : Node = Node('Sand', silicon, 901, 1, 50)
    copperwire          : Node = Node('Copper Wire', siliconboard, 492, 9, 1)
    copperbar           : Node = Node('Copper Bar', copperwire, 1000, 1, 1)
    copperore           : Node = Node('Copper Ore', copperbar, 2, 1, 2)
    searchforendpoint(focusingarray)
    @classmethod
    def test1(cls):
        """test to see if the amount resulted of focusing array is 48
        """
        cls.assertTrue(cls.focusingarray.amountresulted,48)
class MODEBtesting(unittest.TestCase):
    """unit testing class for Mode B, which is trying to figure out what should be the amount on
       hand of the endpoint items to get a desired amount of the headmost item crafted

    Args:
        unittest (class): Unit Testing Module/Class
    """
    blockofgold : Node = Node('Block of Gold',None,0,1,1)
    goldingot : Node = Node('Gold Ingot',blockofgold,0,1,9)
    goldore : Node = Node('Gold Ore',goldingot,0,1,1)
    PROGRAMMODETYPE = 1
    #blockofgold.findlocalendpoints()
    def test(self):
        """test reverse arithmetic method
        """
        self.assertEqual(reversearithmetic(self.blockofgold,100),100)
    def test_tentative1(self):
        """test simple upward traversal
        """
        cur : Node = self.goldore
        while cur.parent is not None:
            cur = cur.parent
        self.assertTrue(cur,self.blockofgold)
    def test_tentative2(self):
        """check to see if the endpoints of this mock ingredient tree are correctly found
        """
        cur : Node = self.goldore
        while cur.parent is not None:
            cur = cur.parent
        reddict : dict = findlocalendpoints(cur)
        bluedict : dict = {}
        bluedict.update({self.goldore.instancekey:self.goldore})
        self.assertEqual(reddict,bluedict)
