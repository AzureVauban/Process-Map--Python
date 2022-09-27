"""rework this fit current development progress on V2
- This is a reworked version of the Process Map (Python) V1, use as base for future versions
"""
class primary:
    """class for storing simple data about an item such as its name and how much is needed to create its parent
    """
    ingredient :str = ''
    amountonhand :int = 0
    amountneededpercraft :int = 0
    amountmadepercraft :int = 0
    amountresulted :int = 0
    amountresultedqueue :dict = {}  # use this to test the math function
    def __init__(self,name :str = '',red : int = 0, blue: int = 1, yellow : int = 1) -> None:
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
        self.amountresultedqueue: dict = {}
        self.ingredient = name
        self.amountresulted = 0
class secondary(primary):
    """stores identifiable features of an item, such as the parent and children instances
    Args:
        primary (_type_): parent class of item
    """
    parent = None
    children :dict = {}
    generation : int = 0
    instances : int = 0
    instancekey : int = 0
    def __init__(self, name: str = '',par = None, red: int = 0, blue: int = 0, yellow: int = 0) -> None:
        super().__init__(name, red, blue, yellow)
        self.instancekey = secondary.instances
        self.children = {}
        self.ingredient = name
        if par is not None and isinstance(par,secondary):
            self.parent = par
            self.parent.children.update({self.instancekey:self})
        else:
            self.parent = None
        secondary.instances += 1
    def inputnumerics(self): #todo rework this method
        """input the numeric data for the node"""
        A = eval(input('How much \x1B[33m' +  str(self.ingredient) + '\x1B[37m do you have on hand: '))
        B = 0
        while B == 0:
            B = int(input('How much \x1B[33m' +  str(self.ingredient) + '\x1B[37m do you create each time you craft it: ')) 
            
        C = 1
        self.amountonhand = A
        self.amountmadepercraft = B
        if self.parent is not None:
            C = int(input('How much \x1B[33m' + str(self.ingredient) + '\x1B[37m do you need to create \x1B[34m' + str(self.parent.ingredient) +'\x1B[37m:'))
            self.amountneededpercraft = C
    def traceback(self, output: bool =False):
        """output trail"""
        if output is True:
            print('TRAIL: ', end='')
        if self.parent is not None:
            print(self.ingredient, '-> ', end='')
        else:
            print('\x1B[35m', self.ingredient, '\x1B[37m')

        if self.parent is not None:
            self.parent.traceback()
    def searchforendpoints(self):
        """search for endpoint nodes"""
        if len(self.children) > 0:
            for childNode in self.children:
                childNode.searchforendpoints()
        else:
            arithmetic(self)


def arithmetic(cur: secondary): #todo update code to be new math method
    """ 
    A = amount on hand
    B = amount made per craft
    C = amount needed
    D = amount on hand for new node (D^P = E^C + A^P)
    E = amount resulted
    Equation for when B = 1: D = A/(B*C)
    Equation for when B > 1: = D^P = D^C * B^P + A^P (C,child & P,parent) 
    #? expected amount on Silicon Board is 1328
    if (cur.parentNode is not None):
        arithmetic(cur.parentNode)
    cur.amountresulted = D


def populate(currentNode=Node):
    """populate each node with subnodes"""
    inputqueue = []
    if currentNode.parentNode != None:
        currentNode.traceback(True)
    print('What ingredients do you need to create',currentNode.ingredient,': ')
    while True:
        i = input('')
        if (len(i) > 0):
            inputqueue.append(i)
        else:
            break
    if len(inputqueue) > 0:
        for nodeName in inputqueue:
            temp = Node(nodeName,currentNode)
            temp.inputnumerics()
    if len(currentNode.childrenNodes) > 0:
        """recursive function call"""
        for newNode in currentNode.childrenNodes:
            populate(newNode)


if __name__ == '__main__':
    print('\x1B[32mbeginning process\x1B[37m')
    itemname = input('What is the name of the item you want to create: ')
    head = Node(itemname, None)
    head.inputnumerics()
    populate(head)
    print('The amount of',head.ingredient,'possible for you to create with all these values is: \x1B[32m',head.returnresultedamount())
    """terminating process"""
    print('\x1B[31mterminating process\x1B[37m')
