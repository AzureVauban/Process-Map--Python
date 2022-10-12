// Unit Test Generator.cpp : This file contains the 'main' function. Program execution begins and ends there.
// merge changes into Bug Fixing Branch when this is completed
#include "NodeUtility.h"

std::ofstream output("auto_generated_unittest.py");
void populate(NodeUtility::Node *object)
{
    std::cout << "What do you need to create " << object->ingredient << ":" << std::endl;
    std::string userinput = "";
    std::vector<std::string> userinputs = {};
    // prompt inputs
    do
    {
        std::getline(std::cin, userinput);
        while (userinput.size() > 0 and userinput.back() == ' ')
        {
            userinput.pop_back();
            userinput.shrink_to_fit();
        }
        bool isalreadypresent = false;
        for (const auto &mystring : userinputs)
        {
            isalreadypresent = mystring == userinput;
            if (isalreadypresent)
            {
                break;
            }
        }
        if (not userinput.empty())
        {
            userinputs.emplace_back(userinput);
        }
        else if (isalreadypresent)
        {
            std::cout << "You already typed that in!" << std::endl;
        }
        else if (userinput == object->ingredient)
        {
            std::cout << "You cannot type that in..." << std::endl;
        }
    } while (!userinput.empty());
    // create child node instances
    bool promptbool = true;
    int amountmadepercraft = 0;
    for (const auto &childname : userinputs)
    {
        if (promptbool)
        {
            auto childinstance = new NodeUtility::Node(childname, object, 0, 1, 1, promptbool);
            promptbool = false;
            amountmadepercraft = childinstance->amountmadepercraft;
        }
        else
        {
            auto childinstance = new NodeUtility::Node(childname, object, 0, amountmadepercraft, 1);
        }
    }
    // recursive runtime
    for (auto childnode : object->children)
    {
        populate(childnode);
    }
}
int main()
{
    using namespace NodeUtility;
    // prompt the name of the head most ingredient
    std::string head_node_name = "";
    do
    {
        std::cout << "What is the name of the item you want to create?" << std::endl;
        std::getline(std::cin, head_node_name);
        if (head_node_name.empty())
        {
            std::cout << "Please type in something!" << std::endl;
        }
    } while (head_node_name.empty());
    auto head = new Node(head_node_name);
    // prompt subingredients
    populate(head);
    // make ingredient names unique
    /// test this function below the comment
    format::unique::parsetree(head);
    // prompt desired amount
    std::cout << "How much " << head->ingredient << " do you want to create? " << std::endl;
    int desirednumofhead = integer_input();
    // set assert values - do arithmetic
    NodeUtility::setassertvalues(head, desirednumofhead);
    // create and write into file
    //  create docstring
    write::docstring::module(output);
    output << std::endl;
    // create variable declarations
    write::tree_declaration(output, head);
    output << "reversearithmetic(" << format::formatstring(head->ingredient, format::instance_declaration) << ", " << desirednumofhead << ")" << std::endl;
    output << std::endl
           << std::endl;
    // create test class
    write::createclass(output, head);
    // create test methods
    write::tree_method(output, head);
    // clean up allocated memory from tree
    // terminate process
    massdelete(head);
    output.close();
    return 0;
}
