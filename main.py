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
    amountresultedqueue: dict = {}  # use this to test the math function

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
        self.amountresultedqueue = {}
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

def arithmetic(cur: Node) -> int:
    """arithmetic method for figuring out the amount resulted of an item

    Args:
        cur (Node): instance
    """
    # ? expected amount on Silicon Board is 1328
    tempnum: int = sys.maxsize  # minimum amount resulted from queue
    if len(cur.amountresultedqueue) > 0:
        for number in cur.amountresultedqueue.items():
            if number[1] < tempnum:
                tempnum = number[1]
    else:
        tempnum = 0
    # main math method
    cur.amountresulted = round(math.floor(
        cur.amountmadepercraft/cur.amountneededpercraft)*cur.amountonhand)
    cur.amountresulted += round(math.floor(cur.amountmadepercraft /
                                cur.amountneededpercraft)*tempnum)
    # pass along data to parent instance
    if isinstance(cur.parent) and cur.parent is not None:
        cur.parent.amountresultedqueue.update(
            {cur.ingredient: cur.amountresulted})
        arithmetic(cur.parent)
    return cur.amountresulted

def searchforendpoint(cur: Node):
    """looks for endpoint nodes to start the math method from
    """
    if len(cur.children) > 0:
        for child in cur.children.items():
            searchforendpoint(child[1])
    else:
        arithmetic(cur)




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
    print('# resulted of', head.ingredient, end=str(head.amountresulted)+'\n')
