"""
- This is a reworked version of the Process Map (Python) V1, use as base for forking future versions
- Mode A : The user figures out how much of item A can they make given the their supply of item
B,C,D...
- Mode B: The user figures out how much of item B,C,D... they need to get their desired amount of A
"""
import math
import sys
import time

PROGRAMMODETYPE: int = 0


class NodeB:
    """
    class for storing simple data about an item such as its name and how much is needed to create
    its parent
    """
    ingredient: str = ''
    amountonhand: int = 0
    amountneeded: int = 0
    amountmadepercraft: int = 0
    amountresulted: int = 0
    queueamountresulted: dict = {}

    def __init__(self, name: str = '', red: int = 0, blue: int = 1, yellow: int = 1) -> None:
        """
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
    """
    stores identifiable features of an item, such as the parent and children instances
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
        """
        default constructor for Node instance, stores identifying features of an item's
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
        """
        prompt input of the numeric data for the instance from the user
        """
        # prompt amount on hand
        while True and PROGRAMMODETYPE == 0:
            print('How much', self.ingredient, 'do you have on hand: ')
            self.amountonhand = promptint()
            if self.amountonhand < 0:
                print('That number is not valid')
            else:
                break
            # prompt amount needed
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
        """
        clear amount resulted for all subnodes below this instance
        """
        self.queueamountresulted.clear()
        if len(self.children) > 0:
            for child in self.children.items():
                if not isinstance(child[1], Node):
                    raise TypeError('Child is not an instance of', Node)
                child[1].clearamountresulted()


def findlocalendpoints(cur: Node, foundendpoints: dict) -> dict:
    """
    look for endpoints connected to the tree at this node
    after this method is finished running, please clear its utilized dictionaryy
    """
    if foundendpoints is None:
        myendpoints: dict = {}
    else:
        myendpoints: dict = foundendpoints
    if len(cur.children) > 0:
        for child in cur.children.items():
            if isinstance(child[1], Node):
                findlocalendpoints(child[1], myendpoints)
    else:
        myendpoints.update({cur.instancekey: cur})
    returndict: dict = myendpoints
    return returndict


def promptint() -> int:
    """
    prompt the user to input a returnable integer

    Returns:
        int: an interger that is used to set the amountneeded, amount on hand, and
        the amount made per craft for a Node instance
    """
    mynum: int = 0
    while True:
        myinput = input('')
        if not myinput.isdigit():
            print('you can only type in a postive interger')
        else:
            mynum = int(myinput)
            break
    return mynum


def recursivearithmetic(cur: Node) -> int:
    """
    figure out the amount resulted of the augment Node instance,
    math function used: D = (B/C)A + (B/C)(min(Dqueue))
    - If there is no values in the queue it will default to 0
    Returns:
        int: returns the amount resulted of augment Node instance
    """
    # check and set minimum resulted if queue is not empty
    tentativeinterger: int = sys.maxsize
    if len(cur.queueamountresulted) == 0:
        tentativeinterger = 0
    else:
        for myinterger in cur.queueamountresulted.items():
            if myinterger[1] < tentativeinterger:
                tentativeinterger = myinterger[1]
    red = (cur.amountmadepercraft / cur.amountneeded)
    blue = (red*cur.amountonhand) + (red*tentativeinterger)
    blue = round(math.floor(blue))
    cur.amountresulted = blue
    # recursively call the method
    if cur.parent is not None:
        cur.parent.queueamountresulted.update(
            {cur.ingredient: cur.amountresulted})
        recursivearithmetic(cur.parent)
    return cur.amountresulted


def reversearithmetic(cur: Node, desiredamount: int = 0) -> int:
    """find how much of a material you will need get a particular amount of an item you want

    Args:
        cur (Node): stores information about an ingredient
        desiredamount (int, optional): what the amount resulted should be given the
        returned value of this method. Defaults to 0.

    Raises:
        TypeError: child is not an instance of Node

    Returns:
        int: the amount on hand of the current Node's item needed to get the desired amount
    """
    cur.amountresulted = desiredamount
    red: float = ((cur.amountmadepercraft/cur.amountneeded)
                  ** -1)*cur.amountresulted
    green: float = round(math.ceil(red))
    cur.amountonhand = int(max(red, green))
    traceback: bool = green > red
    if traceback:  # go back through the higher up nodes and increase the amount on hand by 1
        temp: Node = cur
        while temp.parent is not None:
            temp = temp.parent
            temp.amountonhand += 1
    # continue method recursively
    if len(cur.children) > 0:
        for childnode in cur.children.items():
            if not isinstance(childnode[1], Node):
                raise TypeError('child is not an instance of', Node)
            reversearithmetic(childnode[1], cur.amountonhand)
    return cur.amountonhand


def populate(cur: Node):
    """
    creates new child instances during script runtime

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
        tempinstance: Node = cur
        print('TRAIL: ', end='')
        while True:
            if tempinstance.parent is not None:
                print(tempinstance.ingredient, '-> ', end='')
                tempinstance = tempinstance.parent
            else:
                print(tempinstance.ingredient)
                break
        checkstring = tempinstance.ingredient
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
        Node(newnodename[1], cur, 0, 1, 1, tempbool)
        tempbool = False
    # continue method runtime
    for child in cur.children.items():
        if isinstance(child[1], Node):
            populate(child[1])
        else:
            raise TypeError('child is not an instance of', Node)


def printprompt():
    """
    prints out introduction to program, prompts the user which Mode they want to utilize
    """
    print('Which mode do you want to use:')
    print('Mode A - You are trying to figure out how much of your desired item you can make with the current supply of materials (Type in A)')  # pylint:disable=C0301
    print('Mode B - You are trying to figure out how much base materials you need to create a certain amount of your desired item, (Type in B)')  # pylint:disable=C0301
    print("Type in 'H' if you need a reminder of the prompt\n")



class SplitEndpoints:
    """subclass of Node, used to store dictionaries that split the endpoints of the tree
    """
    red_dict : dict = {}
    blue_dict : dict = {}
    def __init__(self, red : dict, blue : dict) -> None:
        # type check for the parameter of red and blue
        # red must be a dictionary with string keys and a list of tuple of str and integer values
        for key, value in red.items():
            if not isinstance(key,str):
                raise TypeError('key is not a string')
            elif not isinstance(value,list):
                raise TypeError('value is not a list')
            for item in value:
                if not isinstance(item,tuple):
                    raise TypeError('item is not a tuple')
                if not isinstance(item[0],str):
                    raise TypeError('item[0] is not a string')
                if not isinstance(item[1],int):
                    raise TypeError('item[1] is not an integer')
        self.red_dict = red
        # blue must be a dictionary with string keys and an integer value
        for key,value in blue.items():
            if not isinstance(key,str):
                raise TypeError('key is not a string')
            if not isinstance(value,int):
                raise TypeError('value is not an integer')
        self.blue_dict = blue
def tentative_formatoutput(endpoints: dict)-> dict:
    """peusdocode for reformatting the output
    split endpoints into two dictionaries called red_dict and blue_dict
    * red_dict will have the key as the ingredient name, and the value as a list of tuples which
    consists of the parent node's ingredient name and the amount on hand

    * blue_dict will have the key as the ingredient name, and the value as the sum of the amount on
    hand from nodes with the same ingredient name
    return the two dictionaries as an instance of the class SplitEndpoints

    * the class SplitEndpoints will have two attributes, red_dict and blue_dict, which are the same
    as the two dictionaries from this method, this class must have an init method with these two
    dictionaries

    take the red_dict and blue_dict from the instance of SplitEndpoints and print output by
    iterating through the red_dict's. print the key, then iterate through the list of tuples, which
    will be referred to as purple, iterate through the purple list by printing the product of
    amountonhand divided by the value of the same key in blue_dict multipled by 100 and the parent
    node's ingredient name output will look like this: (ingredient name) (percentage of amount on
    hand composed in the total amount on hand in the entire tree)% used in
    (parent node's ingredient name) , ...<keep going>...,
    """
    red_dict : dict = {}
    blue_dict : dict = {}
    for key,value in endpoints:
        if key not in red_dict:
            ingredient :str = 'None'
            if isinstance(value.parent,Node):
                ingredient = value.parent.ingredient
            red_dict.update({value[1].ingredient:[(ingredient,value[1].amountonhand)]})
        else:
            pass
    return red_dict


if __name__ == '__main__':
    print('Welcome to Process Map (Python) v1.1!\n')
    while True:
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
            for subnode in findlocalendpoints(head, {}).items():
                recursivearithmetic(subnode[1])
            print('# resulted of', head.ingredient, '',
                  end=str(head.amountresulted)+'\n')
        else:  # ? Mode B
            print('How much', head.ingredient, 'do you want to create:')
            desirednumber: int = promptint()
            populate(head)
            reversearithmetic(head, desirednumber)
            # output the results
            print('To get', str(str(desirednumber)+'x'),
                  head.ingredient, 'you need the following:')
            results: dict = findlocalendpoints(head, {})
            # iterate through the dictionary and output the amounts on hand
            for itemnode in results.items():
                if not isinstance(itemnode[1], Node):
                    raise TypeError('child is not an instance of', Node)
                # only do this if there 2 or more children for the head node,
                # get the second to last node
                if len(head.children) > 1:
                    tempnode: Node = itemnode[1]
                    while tempnode.parent.parent is not None:  # type: ignore
                        tempnode = tempnode.parent  # type: ignore
                    temporarystring: str = tempnode.ingredient
                    print(itemnode[1].ingredient, ':',
                          itemnode[1].amountonhand, end='x')
                    print(' ->', temporarystring)
                else:
                    print(itemnode[1].ingredient, ':',
                          itemnode[1].amountonhand, end='x\n')
        # prompt the user to see if they want to input another tree
        print("\nDo you want to run the program again with another item tree? (Y/N)")
        print("type in 'H' if you need to be reminded of the prompt")
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
        if userinput == 'N':
            break
    # terminate the program
    print('terminating process in 10 seconds')
    # close program in 10 seconds
    NANI = 10
    while NANI > 0:
        time.sleep(1)
        NANI -= 1
