/*
this script is used to create ingredient mock trees for the Proces Map (Python) Unit test file
the first node will always have an amount made per craft and amount needed of 1 and an amount on hand of 0
*/
#include <iostream>
#include <string>
#include <vector>
#include <fstream>
std::ofstream resultfile("generatedunittest.py"); // resulted file
struct Node
{
    std::string ingredient;
    Node *parent;
    std::vector<Node *> children;
    int amountmadepercraft, amountneeded;
    Node(std::string name = "", Node *par = nullptr)
    {
        children = {};
        ingredient = name;
        parent = par;
        amountmadepercraft = 1;
        amountneeded = 1;
        if (parent)
        {
            parent->children.emplace_back(this);
        }
    }
    ~Node()
    {
        std::cout << "Removing " << ingredient << " from " << this << std::endl;
    }
};
std::vector<Node *> allnodes = {};
void collectgarbage(Node *cur);
void populate(Node *current);
void createnodedeclarations(Node *head);   //? create node instances
void createtestmethods(Node *currentnode); //? create test methods
std::string parseformatter(std::string somestring, int formattype = 0);
int main()
{
    // prompt tree title (which is the name of the mock ingredient tree)
    std::string treetitle = "";
    do
    {
        std::cout << "What is the name of the head node: ";
        std::getline(std::cin, treetitle);
        if (treetitle.empty())
        {
            std::cout << "Please type in something\n";
        }
    } while (treetitle.empty());
    // create tree using Nodes linked to each other
    auto head = new Node(treetitle);
    allnodes.emplace_back(head);
    populate(head);
    // output mock unit test file
    std::string doctstring = "\"\"\"Unit testing code for Python Process Map\n   Auto Generated from Unit Test generator\n\"\"\"\n";
    resultfile << doctstring;
    resultfile << "import unittest\n"
               << std::endl
               << "from main import Node\n"
               << std::endl
               << "from main import reversearithmetic()\n"
               << std::endl
               << std::endl;
    // create unit test class
    std::string classname = head->ingredient;
    classname.at(0) = std::toupper(classname.at(0));
    // parse through the string and convert whitespaces to underscores
    for (auto &i : classname)
    {
        if (i == ' ')
        {
            i = '_';
        }
    }
    resultfile << "class " << classname << "(unittest.TestCase):" << std::endl;
    resultfile << "\t\"\"\""
               << "Unit Testing for a mock tree to create " << head->ingredient << "\"\"\"\n"
               << std::endl;
    // write node declarations onto of the file at the top of the Unit Test class
    for (int i = 0; i < allnodes.size(); i++)
    {

        createnodedeclarations(allnodes.at(i));
    }
    // write test methods declarations onto the file below, after all declarations of been created
    for (int i = 0; i < allnodes.size(); i++)
    {

        createtestmethods(allnodes.at(i));
    }

    resultfile.close();
    // destroy nodes and reset used memory
    collectgarbage(head);
    return 0;
}
void collectgarbage(Node *cur)
{
    for (auto &i : cur->children)
    {
        collectgarbage(i);
    }
    delete cur;
}
void populate(Node *current)
{
    // prompt if the current node has a parent, loop through its parents and output the trail
    if (current->parent)
    {
        // todo finish code here
    }
    // prompt user to input nodes
    std::vector<std::string> userinputs = {};
    std::cout << "What do you need to create " << current->ingredient << ":" << std::endl;
    while (true)
    {
        bool namealreadytyped = false, duplicated = false;
        std::string myinput;
        std::getline(std::cin, myinput);

        // check to see if the user already typed their input into the input vector
        if (not userinputs.empty())
        {

            for (const auto &c : userinputs)
            {
                duplicated = myinput == c;
                if (duplicated)
                {
                    break;
                }
            }
        }
        if (not myinput.empty())
        {
            userinputs.emplace_back(myinput);
        }
        else if (duplicated)
        {
            std::cout << "You have already typed in this input, can you please type in something else..." << std::endl;
        }
        else
        {
            break;
        }
    }
    // create new nodes
    for (const auto &str : userinputs)
    {
        auto child = new Node(str, current);
        allnodes.emplace_back(child);
    }
    // continue function recursively
    for (auto &childinstance : current->children)
    {
        populate(childinstance);
    }
}
void createnodedeclarations(Node *ari)
{
    /*
    example of a Node declared in the python unit test file
    focusingarray       : Node = Node('Focusing Array', None, 0, 1, 1)
    */
    int assertedvalue = 0;
    // parse nodename
    std::string nodeinstancename = parseformatter(ari->ingredient);
    // setter code for the parent instances of the parameter
    std::string parentinstancename = "None";
    if (ari->parent)
    {
        parentinstancename = parseformatter(ari->parent->ingredient, 0);
    }
    // write data onto it
    //?create class declaration, make a copy of the ingredient name and parse through it captializing it then removing whitespace
    resultfile << "\t" << nodeinstancename << std::right << "\t: Node = Node('" << nodeinstancename << "',";
    resultfile << parentinstancename << ", ";
    resultfile << "0, " << ari->amountmadepercraft << ", " << ari->amountneeded << ")" << std::endl;
}
void createtestmethods(Node *ari)
{

    std::string nodeinstancename = parseformatter(ari->ingredient);
    int assertedvalue = 0;
    // make copy and modify string to be used as a declaration
    // write data onto the file
    resultfile << "\tdef test_" << nodeinstancename << "(self):" << std::endl;
    resultfile << "\t\t\"\"\"the amount resulted of " << nodeinstancename << " should be " << assertedvalue << "\"\"\"" << std::endl;
    resultfile << "\t\tself.assertEqual(self." << nodeinstancename << ".amountonhand, " << assertedvalue << ")" << std::endl;
}
std::string parseformatter(std::string somestring, int formattype)
{
    /* formatting types:
    type 1: declaration syntax of an instance of Node (remove whitespace)
    default : declaration syntax of an instance of Node (replace whitespace with underscore)
    */
    std::string myreturnedstring = somestring;
    switch (formattype)
    {
    case 0: // declaration syntax of an instance of Node (remove whitespace)
        for (int i = 0; i < myreturnedstring.size(); i++)
        {
            if (myreturnedstring.at(i) == ' ')
            {
                myreturnedstring.at(i) = '_';
            }
        }
        break;

    default: // declaration syntax of an instance of Node (replace whitespace with underscore)
        for (int i = 0; i < myreturnedstring.size(); i++)
        {
            if (myreturnedstring.at(i) == ' ')
            {
                myreturnedstring.erase(i);
                myreturnedstring.shrink_to_fit();
            }
        }
        break;
    }
    return myreturnedstring;
}