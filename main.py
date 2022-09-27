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
    amountneeded: int = 0
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
        self.amountneeded = yellow
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
        self.inputnumerics()


    def inputnumerics(self):
        """prompt input of the numeric data for the instance from the user"""
        print('How much',self.ingredient,'do you have on hand: ')
        self.amountonhand = self.__promptint()
        if self.parent is not None:
            print('How much',self.ingredient,'do you need to craft ',self.parent.ingredient,'one time: ')
            self.amountneeded = self.__promptint()
            print('How much ',self.parent,'do you create each time you craft it: ')
            self.amountmadepercraft = self.__promptint()
    def __promptint(self) -> int:
        """prompt the user to input a returnable integer

        Returns:
            int: an interger that is used to set the amountneeded, amount on hand, and
            the amount made per craft for a Node instance
        """
        mynum : int = 0
        while True:
            temp = input('')
            if not temp.isdigit():
                print('you can only type in a postive interger')
            else:
                mynum = int(temp)
                break
        return mynum
def recursivearithmetic(cur: Node) -> int:
    """figure out the amount resulted of the augment Node instance,
    math function used: D = (B/C)A + (B/C)(min(Dqueue))
    - if there is no values in the queue it will default to 0
    Returns:
        int: returns the amount resulted of augment Node instance
    """
    # check and set minimum if queue is not empty
    tentativeinterger: int = sys.maxsize
    if len(cur.queueamountresulted) == 0:
        tentativeinterger = 0
    else:
        for myinterger in cur.queueamountresulted.items():
            if myinterger[1] < tentativeinterger:
                tentativeinterger = myinterger[1]
    # tenative arithmetic code
    red = (cur.amountmadepercraft / cur.amountneeded)
    black = (red*cur.amountonhand) + (red*tentativeinterger)
    black = round(math.floor(black))
    cur.amountresulted = black
    # recursively call the method
    if cur.parent is not None:
        cur.parent.queueamountresulted.update(
            {cur.ingredient: cur.amountresulted})
        recursivearithmetic(cur.parent)
    return cur.amountresulted

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
    while True:
        itemname = input('What is the name of the item you want to create: ')
        itemname = itemname.strip()
        if len(itemname) == 0:
            print('You must type something in')
        else:
            break
    head = Node(itemname, None)
    head.inputnumerics()
    populate(head)
    print('# resulted of', head.ingredient, end=str(head.amountresulted)+'\n')
