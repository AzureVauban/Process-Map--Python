/*
this script is used to create ingredient mock trees for the Proces Map (Python) Unit test file
the first node will always have an amount made per craft and amount needed of 1 and an amount on hand of 0
*/
#include <iostream>
#include <string>
#include <vector>
#include <fstream>
std::ofstream resultfile("generatedunittest.py"); // resulted file
std::vector<std::string> allnodenames = {};
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
        // check to see if there is a node in the global node name vector with this exact name
        for (const auto &a : allnodenames)
        {
            for (const auto &b : allnodenames)
            {
                namealreadytyped = a == b;
                if (namealreadytyped)
                {
                    break;
                }
            }
        }
        // check to see if the user already typed their input into the input vector
        for (const auto &c : userinputs)
        {
            duplicated = myinput == c;
            if (duplicated)
            {
                break;
            }
        }
        if (not myinput.empty())
        {
            userinputs.emplace_back(myinput);
        }
        else if (namealreadytyped)
        {
            std::cout << "You have already typed in this input, please type in the input with a different notation" << std::endl;
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
    }
    // continue function recursively
    for (auto &childinstance : current->children)
    {
        populate(childinstance);
    }
}
void createdeclarations(Node *head)
{
    /*
    example of a Node declared in the python unit test file
    focusingarray       : Node = Node('Focusing Array', None, 0, 1, 1)
    */
    // convert any whitespace
    int assertedvalue = 0;
    for (auto &nodetitle : allnodenames)
    {

        std::string nodename = nodetitle;
        for (int i = 0; i < nodename.size(); i++)
        {
            if (nodename.at(i) == ' ')
            {
                nodename.erase(i);
                nodename.shrink_to_fit();
            }
        }
        // write data onto it
        //?create class declaration, make a copy of the ingredient name and parse through it captializing it then removing whitespace
        std::string classname = head->ingredient;
        classname.at(0) = std::toupper(classname.at(0));
        resultfile << "class " << classname << "(unittest.TestCase):" << std::endl;
        resultfile << "\t" << nodename << ": Node = Node('" << head->ingredient << "',";
        if (head->parent)
        {
            resultfile << nodename << ",";
        }
        else
        {
            resultfile << "None"
                       << ",";
        }
        resultfile << "0," << head->amountmadepercraft << "," << head->amountneeded << ")" << std::endl;
    }
}
void createtestfile(Node *head)
{
    std::string nodename = head->ingredient;
    int assertedvalue = 0;
    // make copy and modify string to be used as a declaration
    for (int i = 0; i < nodename.size(); i++)
    {
        if (nodename.at(i) == ' ')
        {
            nodename.erase(i);
            nodename.shrink_to_fit();
        }
    }
    // write data onto the file
    resultfile << "\tdef test_" << nodename << "(self):" << std::endl;
    resultfile << "\t\t\"\"\"the amount resulted of " << nodename << " should be " << assertedvalue << "\"\"\"" << std::endl;
    resultfile << "\t\tself.assertEqual(self." << nodename << ".amountonhand," << assertedvalue << ")" << std::endl;
}
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
    populate(head);
    // output mock unit test file
    std::string doctstring = "\"\"\"unit testing code for Python Process Map\"\"\"\n";
    resultfile << doctstring;
    // write node declarations onto of the file at the top
    createdeclarations(head);
    // write unit test declarations onto the file below, after all declarations of been created
    createtestfile(head);

    // destroy nodes and reset used memory
    collectgarbage(head);
    resultfile.close();
    return 0;
}