// Unit Test Generator.cpp : This file contains the 'main' function. Program execution begins and ends there.
#include "Node.h"
#include <cmath>
void populate(Node *current);
void recursivearithmetic(Node *current);
void inverserecursivearithmetic(Node *current);
int main()
{
    std::ofstream generatedunittest("autogeneratedtest.py");
    // prompt name of head item
    std::cout << "Name of Linked List:" << std::endl;
    std::string headname = "";
    std::getline(std::cin, headname);
    auto head = new Node(headname);
    // prompt ingredient
    populate(head);
    // set assert values
    inverserecursivearithmetic(head);
    // cleanup and terminate process
    NodeUtility::generatateunittest(head, generatedunittest);
    NodeUtility::destroy(head);
    return 0;
}
void populate(Node *current)
{
    std::cout << "What ingredients do you need to create " << current->ingredient << ":" << std::endl;
    // create input loop
    std::string myinput = "";
    std::vector<std::string> userinputs = {};
    do
    {
        std::getline(std::cin, myinput);
        // strip leading and trailing whitespace
        // validate string
        bool duplicatedstring = false;
        if (!myinput.empty())
        {
            userinputs.emplace_back(myinput);
        } else if (duplicatedstring)
        {
            std::cout << "You already typed that in " << std::endl;
        } else if (){
            
        }
        else
        {
            break;
        }
    } while (!myinput.empty());
    // create new node instances
    // continue function recursively by iterating itself onto children instances
    for (auto &child : current->children)
    {
        populate(child);
    }
}
void inverserecursivearithmetic(Node *current)
{
    // create assert values
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started:
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
