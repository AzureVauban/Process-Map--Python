"""rework this fit current development progress on V2
- This is a reworked version of the Process Map (Python) V1, use as base for future versions
- Mode A : The user figures out how much of item A can they make given the their supply of item
B,C,D...
- Mode B: The user figures out how much of item B,C,D... they need to get their desired amount of A
"""
import math
import sys

PROGRAMMODETYPE: int = 0


class NodeB:
    """class for storing simple data about an item such as its name and how much is needed to create
    its parent
    """
    ingredient: str = ''
    amountonhand: int = 0
    amountneeded: int = 0
    amountmadepercraft: int = 0
    amountresulted: int = 0
    queueamountresulted: dict = {}

    def __init__(self, name: str = '', red: int = 0, blue: int = 1, yellow: int = 1) -> None:
        """_summary_

        Args:
            name (str, optional): name of the item. Defaults to ''.
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
        NobeB (class): parent class of item
    """
    parent = None
    children: dict = {}
    generation: int = 0
    instances: int = 0
    instancekey: int = 0
    askmadepercraftquestion: bool = False

    def __init__(self, name: str = '', par=None, red: int = 0, blue: int = 1, yellow: int = 1, green: bool = False) -> None:  # pylint:disable=C0301
        """default constructor for Node instance, stores identifying features of an item's
        information

        Args:
            name (str, optional): name of the item. Defaults to ''.
            pare (class, optional): parent instance of declared Node. Defaults to None
            red (int, optional): amount of the item you have on hand. Defaults to 0.
            blue (int, optional): amount of the parent item you create each time you craft it.
            Defaults to 1.
            yellow (int, optional): amount of item needed to craft the parent item one time.
            Defaults to 1.
            green (bool,optional): boolean variable, checks if one of the Node's sibiling
            instances was prompted to input the amount made per craft (blue)
        """
        super().__init__(name, red, blue, yellow)
        self.instancekey = Node.instances
        self.children = {}
        self.parent = par
        if self.parent is not None:
            self.generation = self.parent.generation + 1
            self.parent.children.update({self.instancekey: self})
        else:
            self.generation = 0
        self.askmadepercraftquestion = green
        Node.instances += 1
        if __name__ == '__main__':
            self.__inputnumerics()

    def __inputnumerics(self):
        """prompt input of the numeric data for the instance from the user"""
        #prompt amount on hand
        while True and PROGRAMMODETYPE == 0:
            print('How much', self.ingredient, 'do you have on hand: ')
            self.amountonhand = promptint()
            if self.amountonhand < 0:
                print('That number is not valid')
            else:
                break
            #prompt amount needed
        if self.parent is not None:
            # prompt amount made per craft
            while True and self.askmadepercraftquestion:
                print('How much', self.parent.ingredient,
                      'do you create each time you craft it: ')
                self.amountmadepercraft = promptint()
                if self.amountmadepercraft < 1:
                    print('That number is not valid')
                else:
                    self.askmadepercraftquestion = False
                    break
            while True:
                print('How much', self.ingredient, 'do you need to craft',
                      self.parent.ingredient, '1 time: ')
                self.amountneeded = promptint()
                if self.amountneeded < 1:
                    print('That number is not valid')
                else:
                    break
    def clearamountresulted(self):
        """clear amount resulted for all subnodes below this instance
        """
        self.queueamountresulted.clear()
        if len(self.children) > 0:
            for childinstance in self.children.items():
                if not isinstance(childinstance[1],Node):
                    raise TypeError('Child is not an instance of',Node)
                childinstance[1].clearamountresulted()
def findlocalendpoints(cur: Node, testdict: dict) -> dict:
    """look for endpoints connected to the tree at this node
        after this method is finished running, please clear its utilized dictionaryy
    """
    if testdict is None:
        testdict: dict = {}
    # ! unit testing failing
    if len(cur.children) > 0:
        for childinstance in cur.children.items():
            if isinstance(childinstance[1], Node):
                findlocalendpoints(childinstance[1], testdict)
    else:
        testdict.update({cur.instancekey: cur})
    returndict: dict = testdict
    return returndict


def promptint() -> int:
    """prompt the user to input a returnable integer

    Returns:
        int: an interger that is used to set the amountneeded, amount on hand, and
        the amount made per craft for a Node instance
    """
    mynum: int = 0
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
    #else:
    #    cur.clearamountresulted()
    return cur.amountresulted


def reversearithmetic(cur: Node, desiredamount: int = 0) -> int:
    """recursive arithmetic method that figures out how much of the endpoint items you
    need to get a desired amount of the head item
    """
    # create temp instance and set it to the head Node of the argument instance
    temp: Node = cur
    while temp.parent is not None:
        temp = temp.parent
    endpointsoftree: dict = findlocalendpoints(temp, {})
    # check to see if each item is the approrpiate type
    for endpoint in endpointsoftree.items():
        if not isinstance(endpoint[1], Node):
            raise TypeError('Endpoint is not an instance of', Node)
    # while amount resulted is less than the desired amount,
    # iterate through each Node in the dictionary and add its amount on hand by 1
    while temp.amountresulted < desiredamount: #todo comment - reverse arithmetic runtime bug
        #! debug this section/interaction with section, block of netherite mock tree should
        #! resulted in 2304 for both endpoints, unit test passes but during real world
        #! runtime infinite loop occurs, the amount on hand of the iterated endpoint
        #! infinitely increases, main suspect for bug is this for-loop below these comment lines
        #! another possibility is the input method for these nodes, since all unit tests pass
        #! completely possible solution, change method to loop until EACH individual item can give
        #! the amount resulted
        for endpoint in endpointsoftree.items():
            tempbaz :int = recursivearithmetic(endpoint[1])
            if temp.amountresulted > desiredamount:
                break
            endpoint[1].amountonhand += 1
            # recursively clear the amount resulted queue once the recursive arithmetic
            # reaches the head instance
    return temp.amountresulted


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
        print('TRAIL: ', end='')
        while True:
            if temp.parent is not None:
                print(temp.ingredient, '-> ', end='')
                temp = temp.parent
            else:
                print(temp.ingredient)
                break
        checkstring = temp.ingredient
    # prompt user to input ingredients
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
        elif len(myinput) == 0:
            break
        else:
            inputqueue.update({len(inputqueue): myinput})
    # create new child instances
    tempbool: bool = True
    for newnodename in inputqueue.items():
        newchild: Node = Node(newnodename[1], cur, 0, 0, 0, tempbool)  # pylint:disable=W0612
        tempbool = False
    # continue method runtime
    for childinstance in cur.children.items():
        if isinstance(childinstance[1], Node):
            populate(childinstance[1])
        else:
            raise TypeError('child is not an instance of', Node)


def printprompt():
    """prints out introduction
    """
    print('Which mode do you want to use:')
    print('Mode A - You are trying to figure out how much of your desired item you can make with the current supply of materials (Type in A)')  # pylint:disable=C0301
    print('Mode B - You are trying to figure out how much base materials you need to create a certain amount of your desired item, (Type in B)')  # pylint:disable=C0301
    print("Type in 'H' if you need a reminder of the prompt\n")


if __name__ == '__main__':
    print('Welcome to Process Map (Python) v1.1!\n')
    while True:  # main runtime loop
        # Mode B: How much of Item B,C,D (endpoint instances), would I need to make X amount of
        # item A
        # prompt user which mode they want to run the program in
        printprompt()
        while True:
            userinput = (input(''))
            userinput = userinput.strip()
            userinput = userinput.upper()
            if userinput not in ('A', 'B', 'H'):
                print("That input is not valid, please type in 'A' or 'B'")
            elif len(userinput) > 1:
                print('Your input is too long, please only type in one character')
            elif userinput == 'B':
                PROGRAMMODETYPE = 1
                break
            elif userinput == 'H':
                printprompt()
            else:
                PROGRAMMODETYPE = 0
                break
        # prompt user to type in the name of the item they want to create
        while True:
            itemname = input(
                'What is the name of the item you want to create: ')
            itemname = itemname.strip()
            if len(itemname) == 0:
                print('You must type something in')
            else:
                break
        head = Node(itemname, None)
        if PROGRAMMODETYPE == 0:  # ? normal program mode
            populate(head)
            for child in findlocalendpoints(head, {}).items():
                recursivearithmetic(child[1])
            print('# resulted of', head.ingredient, '',
                  end=str(head.amountresulted)+'\n')
        else:  # ? Mode B
            print('How much', head.ingredient, 'do you want to create:')
            desirednumber: int = promptint()
            populate(head)
            reversearithmetic(head, desirednumber)
            # output resulted numbers for endpoints
            print('To get', str(str(desirednumber)+'x'),
                  head.ingredient, 'you need the following:')
            # print amount needed of endpoint items
            mango: dict = findlocalendpoints(head, {})
            for itemnode in findlocalendpoints(head, {}).items():
                if not isinstance(itemnode[1], Node):
                    raise TypeError('child is not an instance of', Node)
                print(itemnode[1].ingredient, ':',
                      itemnode[1].amountonhand, end='x\n')
        # prompt the user to see if they want to input another tree
        print("\nDo you want to run the program again with another item tree? (Y/N) type in 'H' if you need to be reminded of the prompt")
        while True:
            userinput = (input(''))
            userinput = userinput.strip()
            userinput = userinput.upper()
            if userinput not in ('Y', 'N', 'H'):
                print("That input is not valid, please type in 'Y' or 'N'")
            elif len(userinput) > 1:
                print('Your input is too long, please only type in one character')
            elif userinput == 'N' or userinput == 'Y':
                break
        head.clearamountresulted()
    print('terminating process')
