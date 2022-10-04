/*
this script is used to create ingredient mock trees for the Proces Map (Python) Unit test file
the first node will always have an amount made per craft and amount needed of 1 and an amount on hand of 0
*/
#include <iostream>
#include <string>
#include <vector>
#include <fstream>
std::ifstream resultfile("generatedunittest.py"); //resulted file
struct Node
{
    std::string ingredient;
    Node *parent;
    std::vector<Node *> children;
    Node(std::string name = "", Node *par = nullptr)
    {
        children = {};
        ingredient = name;
        parent = par;
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
        std::string myinput;
        std::getline(std::cin, myinput);
        if (not myinput.empty())
        {
            userinputs.emplace_back(myinput);
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
void outputfile(Node *head)
{
    /*
    example of a Node declared in the python unit test file
    focusingarray       : Node = Node('Focusing Array', None, 0, 1, 1)
    */
    //convert any whitespace 
    for (int i = 0; i < head->ingredient.size();i++)
    {
        if (head->ingredient.at(i) == ' ')
        {
            head->ingredient.erase(i);
            head->ingredient.shrink_to_fit();
        }
    } 
    resultfile.open("generatedunittest.py");
    //write data to it
    resultfile.close();
}
int main()
{
    // prompt tree title (which is the name of the mock ingredient tree)
    std::string treetitle = "";
    do
    {
        std::cout << "What is the name of the head node: ";
        std::getline(std::cin, treetitle);
    } while (treetitle.empty());
    // create tree using Nodes linked to each other
    auto head = new Node(treetitle);
    populate(head);
    // output mock unit test file
        //write node declarations onto of the file at the top
        //write unit test declarations onto the file below, after all declarations of been created
    // destroy nodes and reset used memory
    collectgarbage(head);
    return 0;
}