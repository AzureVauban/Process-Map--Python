// Unit Test Generator.cpp : This file contains the 'main' function. Program execution begins and ends there.
#include "Node.h"
#include <cmath>
void populate(Node *current);
//! void recursivearithmetic(Node *current);
long long int inverserecursivearithmetic(Node *current, long long int desiredamount);
int main()
{
    std::ofstream generatedunittest("autogeneratedtest.py");
    // prompt name of head item
    std::cout << "Name of Linked List:" << std::endl;
    std::string headname = "";
    std::getline(std::cin, headname);
    auto head = new Node(headname, nullptr);
    // prompt ingredients
    populate(head);
    // prompt amount desired
    long long int desiredamount = 0;
    std::cout << "How much " << headname << " do you want to create? " << std::endl;
    std::cin >> desiredamount;
    // set assert values
    inverserecursivearithmetic(head, desiredamount);
    // cleanup and terminate process
    NodeUtility::generatateunittest(head, generatedunittest);
    NodeUtility::destroy(head);
    return 0;
}
void populate(Node *current)
{
    std::vector<std::string> userinputs;
    std::cout << "What do you need to create " << current->ingredient << ":" << std::endl;
    std::string myinput = "";
    std::string headnode = current->ingredient;
    Node *temp = current;
    while (temp->parent)
    {
        temp = temp->parent;
    }
    headnode = temp->ingredient;
    // prompt inputs
    do
    {
        std::getline(std::cin, myinput);
        bool duplicatedinput = false;
        for (const auto &u : userinputs)
        {
            duplicatedinput = u == myinput;
        }
        if (duplicatedinput)
        {
            std::cout << "You already typed something else" << std::endl;
        }
        else if (myinput == current->ingredient)
        {
            std::cout << "You cannot type that in" << std::endl;
        }
        else if (myinput == headnode)
        {
            std::cout << "You cannot type that in, you are trying to create that item" << std::endl;
        }
        else if (not myinput.empty())
        {
            userinputs.emplace_back(myinput);
        }
    } while (not myinput.empty());
    // create Nodes
    for (const auto &child : userinputs)
    {
        auto childnode = new Node(child, current);
    }
    // continue function recursively
    for (const auto &childnode : current->children)
    {
        populate(childnode);
    }
}
long long int inverserecursivearithmetic(Node *current, long long int desiredamount = 0)
{
    std::cout << "SETTING ASSERT VALUE FOR " << current->ingredient << std::endl;
    current->amountresulted = desiredamount;
    auto red = current->amountmadepercraft;
    auto blue = current->amountneeded;
    // create assert values
    current->amountonhand = std::pow(red / blue, -1) * current->amountresulted;
    for (const auto &child : current->children)
    {
        inverserecursivearithmetic(child);
    }
    return current->amountonhand;
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
