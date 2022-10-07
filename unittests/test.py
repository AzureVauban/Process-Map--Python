"""unit testing code, test out Mode A and Mode B for the script
"""
import random
import unittest

from Process_Mao import reversearithmetic  # pylint:disable=E0401
from main import Node, findlocalendpoints  # pylint:disable=E0401

# To get 9999x Solar Array you need the following:
# Tungsten Ore : 399960x #! append this output to the end:   (second generation (from head) item)
# Silver Ore : 399960x
# Sand : 24997500x
# Sand : 999900x
# Copper Ore : 4444x
# Copper Ore : 22220x
# Titanium Ore : 119988x
# Gold Ore : 199980x
# Coal : 399960x
# Pixels : 3999600x
# Sulphur : 79992x
# Hydrogen : 79992x
# Water : 159984x
# Sand : 999900x
# Copper Ore : 4444x
# Gold Ore : 79992x


def resetsupplyvalues(cur: Node):
    """
    resets the amount on hand attribute of all nodes into a tree to 0 for
    use in Mode B unit testing

    Args:
        cur (Node): Node instance with information about an ingredient
    """
    while cur.parent is not None:
        cur = cur.parent
    roots: dict = findlocalendpoints(cur, {})
    # find endpoints
    for endnode in roots.items():
        endnode[1].amountonhand = 0
        tempnode: Node = endnode[1]
        # traverse upward and reset amount on hand 0
        while tempnode.parent is not None:
            tempnode.amountonhand = 0
            tempnode = tempnode.parent


class FocusingArray(unittest.TestCase):
    """
    converted mode A mock tree into mode B mock tree, resets all amounts on hand of each item
    into 0
    """
    focusingarray       : Node = Node('Focusing Array', None, 0, 1, 1)
    advancedalloy       : Node = Node('Advanced Alloy', focusingarray, 8, 1, 2)
    crystal             : Node = Node('Crystal', focusingarray, 640, 1, 2)
    plasmiccrystal      : Node = Node('Plasmic Crystal', focusingarray, 41, 1, 2)
    quantumprocessor    : Node = Node('Quantum Processor', focusingarray, 20, 1, 1)
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
    protocitebarb       : Node = Node('Protocite Bar', quantumprocessor, 277, 2, 2)
    protociteoreb       : Node = Node('Protocite Ore', protocitebarb, 2, 1, 2)
    siliconboard        : Node = Node('Silicon Board', quantumprocessor, 310, 2, 4)
    silicon             : Node = Node('Silicon', siliconboard, 1000, 1, 1)
    sand                : Node = Node('Sand', silicon, 901, 1, 50)
    copperwire          : Node = Node('Copper Wire', siliconboard, 492, 1, 1)
    copperbar           : Node = Node('Copper Bar', copperwire, 1000, 9, 1)
    copperore           : Node = Node('Copper Ore', copperbar, 2, 1, 2)
    resetsupplyvalues(sand)  # reset all amounts on hand of each node to 0
    reversearithmetic(focusingarray, 9999)
    # resulted amount of focusing array should be equal to or greater than 9999

    def test_focusingarray(self):
        """amount resulted of focusing array should be 9999
        """
        self.assertGreaterEqual(self.focusingarray.amountonhand, 9999)
    # ? tests for advanced alloy branch

    def test_advancedalloy(self):
        """amount resulted of advanced alloy should be 19998, which comes from 9999*2
        """
        self.assertEqual(self.advancedalloy.amountonhand, 19998)

    def test_zerchesiumbar(self):
        """amount resulted of zerchesium bar should be 19998
        """
        self.assertEqual(self.zerchesiumbar.amountonhand, 19998)

    def test_zerchesiumore(self):
        """amount resulted of zerchesium ore should be 39996
        """
        self.assertEqual(self.zerchesiumore.amountonhand, 39996)

    def test_penumbriteshard(self):
        """amount resulted of penumbrite shard should be 19998
        """
        self.assertEqual(self.penumbriteshard.amountonhand, 19998)

    def test_penumbriteore(self):
        """amount resulted of penumbrite ore should be 39996
        """
        self.assertEqual(self.penumbriteore.amountonhand, 39996)

    def test_protocitebar(self):
        """amount resulted of protocite bar should be 19998
        """
        self.assertEqual(self.protocitebar.amountonhand, 19998)

    def test_protociteore(self):
        """amount resulted of protocite should be 39996
        """
        self.assertEqual(self.protociteore.amountonhand, 39996)

    def test_lead(self):
        """amount resulted of lead should be 19998
        """
        self.assertEqual(self.lead.amountonhand, 19998)
    # ? tests for crystal branch

    def test_crystal(self):
        """amount resulted of crystal should be 9999
        """
        self.assertEqual(self.crystal.amountonhand, 9999*2)

    def test_crystalplant(self):
        """amount resulted of crystal plant should be 19998
        """
        self.assertEqual(self.crystalplantseed.amountonhand, 19998)
    # ? tests for plasmic crystal branch

    def test_plasmiccrystal(self):
        """amount resulted of plasmic crystal should be 19998
        """
        self.assertEqual(self.plasmiccrystal.amountonhand, 9999*2)

    def test_bloodrock(self):
        """amount resulted of blood rock should be 999900
        """
        self.assertEqual(self.bloodrock.amountonhand, 9999*2*50)

    def test_blood(self):
        """amount resulted of blood should be 999900
        """
        self.assertEqual(self.blood.amountonhand, 9999*2*50)

    def test_lava(self):
        """amount resulted of blood should be 999900
        """
        self.assertEqual(self.lava.amountonhand, 9999*2*50)
    # ? tests for quantaum processor branch

    def test_quantumprocessor(self):
        """amount resulted of quantuam processor should be 9999
        """
        self.assertEqual(self.quantumprocessor.amountonhand, 9999)

    def test_protocitebarb(self):
        """amount resulted of protocite bar should be 9999
        """
        self.assertEqual(self.protocitebarb.amountonhand, 9999)

    def test_protociteoreb(self):
        """amount resulted of protocite should be 19998
        """
        self.assertEqual(self.protociteoreb.amountonhand, 19998)

    def test_siliconboard(self):
        """amount resulted of silicon board should be 19998
        """
        self.assertEqual(self.siliconboard.amountonhand, 19998)

    def test_silicon(self):
        """amount resulted of silicon should be 19998"""
        self.assertEqual(self.silicon.amountonhand, 19998)

    def test_sand(self):
        """amount resulted of sand 999900"""
        self.assertEqual(self.sand.amountonhand, 19998*50)

    def test_copperwire(self):
        """amount resulted of copper wire 19998"""
        self.assertEqual(self.copperwire.amountonhand, 19998)

    def test_copperbar(self):
        """amount resulted of copper bar 179982"""
        self.assertEqual(self.copperbar.amountonhand, 2222)

    def test_copperore(self):
        """amount resulted of copper ore 359964"""
        self.assertEqual(self.copperore.amountonhand, 4444)


class BlockOfNetherite(unittest.TestCase):
    """unit testing the recursive arithmetic method under Mode B's runtime condition

    Args:
        unittest (class): unit testing
    """
    blockofnetherite    : Node = Node('block of netherite', None, 0, 1, 1)
    netherite           : Node = Node('netherite ingot', blockofnetherite, 0, 1, 9)
    goldingot           : Node = Node('gold ingot', netherite, 0, 1, 4)
    netheritescrap      : Node = Node('netherite scrap', netherite, 0, 1, 4)
    testdesiredamount : int = random.randint(1,100)
    reversearithmetic(blockofnetherite, testdesiredamount)
    # endpoints are gold ingot and netherite scrap

    def test_blockofnetherite(self):
        """amount on hand of block of netherite should be 64
        """
        self.assertEqual(self.blockofnetherite.amountonhand, self.testdesiredamount)

    def test_netherite(self):
        """amount on hand of netherite should be 576
        """
        self.assertEqual(self.netherite.amountonhand, self.testdesiredamount*9)

    def test_netheritescrap(self):
        """amount on hand of netherite scrap should be 2304
        """
        #!self.assertEqual(reversearithmetic(self.netheritescrap,2304),2304)
        self.assertEqual(self.netheritescrap.amountonhand, self.testdesiredamount*36)

    def test_goldingot(self):
        """amount on hand of gold ingot should be 2304
        """
        #!self.assertEqual(reversearithmetic(self.goldingot,2304),2304)
        self.assertEqual(self.goldingot.amountonhand, self.testdesiredamount*36)
class randomitem(unittest.TestCase):
    """test to see if the amount resulted of Stick of Ram would correct itself

    Args:
        unittest (class): Unit Test framework
    """
    testdesiredamount : int = random.randint(0,100)
    purple : Node = ('Purple',None,0,1,1)
