"""unit testing code, test out Mode A and Mode B for the script
"""
import random
import unittest

from main import (Node, findlocalendpoints, recursivearithmetic,
                  reversearithmetic)


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
    #searchforendpoint(focusingarray)
    tentativedict = findlocalendpoints(advancedalloy,{})
    def test1(self):
        """test to see if the amount resulted of focusing array is 48
        """
        for node in self.tentativedict.items():
            recursivearithmetic(node[1])
        self.assertEqual(self.focusingarray.amountresulted,48)
class MODEBtesting(unittest.TestCase):
    """unit testing class for Mode B, which is trying to figure out what should be the amount on
       hand of the endpoint items to get a desired amount of the headmost item crafted

    Args:
        unittest (class): Unit Testing Module/Class
    """
    purple  : Node = Node('Purple',None,0,random.randint(1,100),1)
    green   : Node = Node('Green',purple,0,random.randint(1,100),1)
    orange  : Node = Node('Orange',green,0,random.randint(1,100),1)
    #orange should be the only endpoint present in the endpoint search method
    def testreversearithmetic(self):
        """test reverse arithmetic method
        """
        tempassertint : int = random.randint(1,100)
        self.assertGreaterEqual(reversearithmetic(self.purple,tempassertint),tempassertint)
    def testhead(self):
        """test simple upward traversal
        """
        cur : Node = self.orange
        while cur.parent is not None:
            cur = cur.parent
        self.assertTrue(cur,self.purple)
    def testendpoints(self):
        """check to see if the endpoints of this mock ingredient tree are correctly found
        """
        cur : Node = self.orange
        while cur.parent is not None:
            cur = cur.parent
        reddict : dict = findlocalendpoints(cur,{})
        #reddict : dict = cur.tentative_findlocalendpoints()
        bluedict : dict = {}
        bluedict.update({self.orange.instancekey:self.orange})
        self.assertEqual(reddict,bluedict)
class MODEBtesting2(unittest.TestCase):
    """unit testing the recursive arithmetic method under Mode B's runtime condition

    Args:
        unittest (class): unit testing
    """
    amethyst: Node = Node('Amethyst',None,random.randint(1,100),1,1)
    benitoite : Node = Node('Benitoite',amethyst,0,random.randint(1,100),1)
    carnelian : Node = Node('Carnelian',amethyst,0,random.randint(1,100),1)
    dioptase : Node = Node('Dioptase',benitoite,0,random.randint(1,100),1)
    #endpoints are carnelian and dioptase
    def testhead(self):
        """test simple upward traversal
        """
        cur : Node = self.dioptase
        while cur.parent is not None:
            cur = cur.parent
        self.assertTrue(cur,self.amethyst)
    def testendpoints(self):
        """check to see if the endpoints of this mock ingredient tree are correctly found
        """
        cur : Node = self.dioptase
        while cur.parent is not None:
            cur = cur.parent
        reddict : dict = findlocalendpoints(cur,{})
        bluedict : dict = {}
        # manually input endpoints into the dictionary
        bluedict.update({self.carnelian.instancekey:self.carnelian})
        bluedict.update({self.dioptase.instancekey:self.dioptase})
        self.assertEqual(reddict,bluedict)
    def testreversearithmetic(self):
        """reverse arithmetic testing with many endpoints
        """
        testvalue = random.randint(1, 100)
        self.assertGreaterEqual(reversearithmetic(self.amethyst, testvalue), testvalue)
