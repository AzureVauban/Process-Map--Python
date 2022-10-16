"""unit testing code, test out Mode A and Mode B for the script
   re-add to gitignore when pulling and merging modifications into master
"""
import random
import unittest

from main import Node, SplitEndpoints, findlocalendpoints, reversearithmetic
from main import tentative_formatoutput


class Issue12_single_unique_endpoint(unittest.TestCase):  # pylint:disable=C0103
    """test new formatting and endpoint search methods from main.py module wih only one endpoint

    Args:
        unittest (class): Unit testing framework for python
    """
    # ? Tritanium Bar Mock Tree: https://frackinuniverse.miraheze.org/wiki/Tritanium_Bar
    desiredamount: int = random.randint(1, 100)
    # it should take 6696 pixels to make one tritanium bar
    tritaniumbar: Node = Node('Tritanium Bar')
    lead: Node = Node('Lead', tritaniumbar)
    pixels: Node = Node('Pixels', lead, 0, 1, 200)
    irradiumbar: Node = Node('Irradium Bar', tritaniumbar)
    irradiumore: Node = Node('Irradium Ore', irradiumbar, 0, 1, 2)
    pixels2: Node = Node('Pixels', irradiumore, 0, 1, 600)
    triangliumpyramid: Node = Node('Trianglium Pyramid', tritaniumbar)
    triangliumore: Node = Node('Trianglium Ore', triangliumpyramid, 0, 1, 2)
    pixels3: Node = Node('Pixels', triangliumore, 0, 1, 810)
    prisilitestar: Node = Node('Prisilite Star', tritaniumbar)
    prismshard: Node = Node('Prism Shard', prisilitestar, 0, 1, 2)
    # buy prism shards from geologist NPC ingame
    pixels4: Node = Node('Pixels', prismshard, 0, 1, 1838)
    reversearithmetic(tritaniumbar, desiredamount)
    roots: dict = findlocalendpoints(tritaniumbar, {})
    # should 4 endpoints, but 1 (all the endpoints are pixels) item in its endpoint output

    def test_endpointsdict(self):
        """test to see if the length of the endpoints dictionary
        is 4 elements
        """
        self.assertEqual(len(self.roots), 4)

    def test_endpoints(self):
        """test to see if the item name of each endpoint is Pixels
        """
        iscalledpixels: bool = True
        for instance in self.roots.items():
            if not isinstance(instance[1], Node):
                raise TypeError('endpoint is not an instance of', Node)
            else:
                iscalledpixels = instance[1].ingredient == 'Pixels'
                if not iscalledpixels:
                    break
        self.assertTrue(iscalledpixels)


    def test_sum(self):
        """
        test to see if the sum of the amount on hand of each tuple element within the value of the red dictionary is correct
        and the same as the value of the blue dictionary
        doing the math by hand results in the same number, which means that if the unit test code is correct, the test WILL pass sucessfully
        """
        green: SplitEndpoints = testmethod(self.roots)
        # iterate through red of green and sum the amount on hand of each tuple element
        # the sum of the item values (type should be int) in the blue dictionary
        bluenumber: int = 0
        # sum of the amount on hand of each tuple element within the value of the red dictionary
        yellownumber: int = 0
        for integer in green.blue_dict.items():
            bluenumber += integer[1]
        for yellowtuple in green.red_dict.items():
            for integer in yellowtuple[1]:
                yellownumber += integer[1]
        self.assertEqual(bluenumber, yellownumber)

    def test_betteroutput(self):
        """make sure that the sum of the percentages of the endpoints items is 100%
        #! comments notated in red '!' are to be removed when the test passes,including this one
        """
        testsumfloat: float = 0.00
        pyorange: SplitEndpoints = tentative_formatoutput(self.roots)
        # iterate through the red dictionary and sum the percentages of each tuple element
#!      percentages: dict = {}
#!      percentages = pyorange.red_dict
        # key: ingredient name, value: list of string of percentages
        output_dictionary: dict = {}
        for item in pyorange.red_dict.items():
            orangeinteger: int = 0  # sum of the amount on hand of each tuple element
            for orangenumber in item[1]:
                orangeinteger += orangenumber[1]
#!          for orangetuple in item[1]: # convert the amount on hand of each tuple element to a float
#!              orangetuple = (orangetuple[0], float(orangetuple[1]))
#!            print(item[0],end=' (')
            # create a new dictionary with the key being the ingredient name of the endpoint node and the values being a formatted string of the output that will be printed to the console
            for orangetuple in item[1]:
                if item[0] not in output_dictionary:
                    #outputdictionary.update({item:[str(round((orangetuple[1]/orangeinteger)*100, 2))+'%','used in',orangetuple[0]]})
                    output_dictionary.update({item[0]: [str(round(
                        (orangetuple[1]/orangeinteger)*100, 2))+'% used in '+orangetuple[0]]})  # ? add breakpoint here
                else:  # if item is in the outputdictionary, append the string to the list
                    output_dictionary[item[0]].append(
                        str(round((orangetuple[1]/orangeinteger)*100, 2))+'% used in '+orangetuple[0])
                testsumfloat += round(
                    (orangetuple[1]/orangeinteger)*100, 2)
#!                if index == len(orangetuple):
#!                    print('\x1B[34m'+str(round((orangetuple[1]/orangeinteger)*100, 2))+'% used in',orangetuple[0]+', ',end=' ')
#!                else:
#!                    print('\x1B[36m'+str(round((orangetuple[1]/orangeinteger)*100, 2))+'% used in',orangetuple[0]+', ',end='')
#!            print(')')
        # iterate through the outputdictionary, output the key then iterate through the list of strings and output each string, then output a newline at the last element of the list
        for item in output_dictionary.items():
            print(item[0], end=' (')
            for index, string in enumerate(item[1]):
                if index == len(item[1])-1:
                    print(string, end='')
                else:
                    print(string, end=', ')
            print(')')
        # print the outputdictionary
        print('outputdictionary:', output_dictionary)
        self.assertEqual(testsumfloat, 100.00)
    def test_betteroutput_testmethod(self):
        tentative_formatoutput(self.roots)
        print('terminating test')
        self.assertEqual(1,1)

class Issue12_multiple_unique_endpoint(unittest.TestCase):  # pylint:disable=C0103
    """test new formatting and endpoint search methods from main.py module wih only one endpoint
    """
    pass
