"""rework this fit current development progress on V2
- This is a reworked version of the Process Map (Python) V1, use as base for future versions
"""
import math
import sys


class NodeB:
    """class for storing simple data about an item such as its name and how much is needed to create
    its parent
    """
    ingredient: str = ''
    amountonhand: int = 0
    amountneededpercraft: int = 0
    amountmadepercraft: int = 0
    amountresulted: int = 0
    queueamountresulted: dict = {}  # use this to test the math function

    def __init__(self, name: str = '', red: int = 0, blue: int = 1, yellow: int = 1) -> None:
        """_summary_

        Args:
            I (str, optional): name of the item. Defaults to ''.
            red (int, optional): amount of the item you have on hand. Defaults to 0.
            blue (int, optional): amount of the parent item you create each time you craft it.
            Defaults to 1.
            yellow (int, optional): amount of item needed to craft the parent item one time.
            Defaults to 1.
        """
        self.amountonhand = red
        self.amountmadepercraft = blue
        self.amountneededpercraft = yellow
        self.queueamountresulted = {}
        self.ingredient = name
        self.amountresulted = 0


class Node(NodeB):
    """stores identifiable features of an item, such as the parent and children instances
    Args:
        primary (_type_): parent class of item
    """
    parent = None
    children: dict = {}
    generation: int = 0
    instances: int = 0
    instancekey: int = 0

    def __init__(self, name: str = '', par=None, red: int = 0, blue: int = 1, yellow: int = 1) -> None:
        super().__init__(name, red, blue, yellow)
        self.instancekey = Node.instances
        self.children = {}
        self.parent = par
        if self.parent is not None:
            self.parent.children.update({self.instancekey: self})
        Node.instances += 1

    def inputnumerics(self):  # todo rework this method
        """input the numeric data for the node"""
        A = eval(input(
            'How much \x1B[33m' + str(self.ingredient) + '\x1B[37m do you have on hand: '))
        B = 0
        while B == 0:
            B = int(input('How much \x1B[33m' + str(self.ingredient) +
                    '\x1B[37m do you create each time you craft it: '))

        C = 1
        self.amountonhand = A
        self.amountmadepercraft = B
        if self.parent is not None:
            C = int(input('How much \x1B[33m' + str(self.ingredient) +
                    '\x1B[37m do you need to create \x1B[34m' + str(self.parent.ingredient) + '\x1B[37m:'))
            self.amountneededpercraft = C

def recursivearithmetic(current: Node) -> int:
    """figure out the amount resulted of the augment Node instance,
    math function used: D = (B/C)A + (B/C)(min(Dqueue))
    - if there is no values in the queue it will default to 0
    Returns:
        int: returns the amount resulted of augment Node instance
    """
    # check and set minimum if queue is not empty
    tentativeinterger: int = sys.maxsize
    if len(current.queueamountresulted) == 0:
        tentativeinterger = 0
    else:
        for myinterger in current.queueamountresulted.items():
            if myinterger[1] < tentativeinterger:
                tentativeinterger = myinterger[1]
    # tenative arithmetic code
    # red = (current.amountmadepercraft / current.amountneeded)
    # black = (red*current.amountonhand) + (red*tentativeinterger)
    # black = round(math.floor(black))
    # current.amountresulted = black
    current.amountresulted = round(math.floor(((current.amountmadepercraft / current.amountneeded) *
                                               current.amountonhand) + ((current.amountmadepercraft / current.amountneeded)*tentativeinterger)))  # pylint:disable=C0301
    # recursively call the method
    if current.parent is not None:
        current.parent.queueamountresulted.update(
            {current.ingredient: current.amountresulted})
        recursivearithmetic(current.parent)
    return current.amountresulted

def searchforendpoint(cur: Node):
    """looks for endpoint nodes to start the math method from
    """
    if len(cur.children) > 0:
        for child in cur.children.items():
            searchforendpoint(child[1])
    else:
        recursivearithmetic(cur)




def populate(cur: Node):
    """creates new child instances during script runtime

    Args:
        cur (Node): parent instance, creates children instances for this node

    Raises:
        TypeError: this method continues recursively, if the child is not an instance
        of the same class as the augment, this is unintended behavior and will raise an error
        to catch it
    """
    inputqueue: dict = {}
    checkstring: str = cur.ingredient
    # output ingredient trail
    if cur.parent is not None:
        temp: Node = cur
        while temp.parent is not None:
            print('TRAIL: ', end='')
            if temp.parent is not None:
                print(temp.ingredient, end='-> ')
            else:
                print(temp.ingredient)
            temp = temp.parent
        checkstring = temp.ingredient
    # prompt user to input ingredienta
    print('What ingredients do you need to create', cur.ingredient, end=':\n')
    while True:
        myinput = input('')
        myinput = myinput.strip()
        #! input checking
        duplicated: bool = False
        if len(inputqueue) > 0:
            for word in inputqueue.items():
                duplicated = word[1] == checkstring
                if duplicated:
                    break
        if duplicated:
            print('You already typed that in')
        elif myinput == checkstring:
            print('Invalid input, we are trying to make that item!')
        elif myinput == cur.ingredient:
            print('You cannot type that in')
        else:
            break
    # create new child instances
    for newnodename in inputqueue.items():
        newchild: Node = Node(newnodename[1], cur)
        newchild.inputnumerics()
    # continue method runtime
    for child in cur.children.items():
        if isinstance(child[1], Node):
            populate(child[1])
        else:
            raise TypeError


if __name__ == '__main__':
    # prompt user to type in the name of the item they want to create
    """FIXME
    while True:
        itemname = input('What is the name of the item you want to create: ')
        itemname = itemname.strip()
        if len(itemname) == 0:
            print('You must type something in')
        else:
            break
    head = Node(itemname, None)
    # head.inputnumerics()
    # populate(head)
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
    print(focusingarray.amountresulted)
    #print('# resulted of', head.ingredient, end=str(head.amountresulted)+'\n')
