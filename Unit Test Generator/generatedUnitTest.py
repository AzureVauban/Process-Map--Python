"""AUTO GENERATED UNIT TEST
"""
import unittest

from main import Node

Head_Node : Node = Node('Head Node', None, 0, 1, 1)
Body_A : Node = Node('Body A', Head_Node, 0, 1, 1)
Body_B : Node = Node('Body B', Body_A, 0, 1, 1)
Body_C : Node = Node('Body C', Body_B, 0, 1, 1)
Body_D : Node = Node('Body D', Body_C, 0, 1, 1)

class HeadNodee_unittest(unittest.TestCase): #pylint:disable
	"""tentative test class, add additional comments here: 
	"""

