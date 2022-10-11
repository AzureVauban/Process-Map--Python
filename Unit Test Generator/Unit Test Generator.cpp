// Unit Test Generator.cpp : This file contains the 'main' function. Program execution begins and ends there.
// merge changes into Bug Fixing Branch when this is completed
#include "NodeUtility.h"
std::ofstream output("generatedUnitTest.py");
void populate(NodeUtility::Node &object)
{
    std::cout << "What do you need to create " << object.ingredient << ":" << std::endl;
}

int main()
{
    using namespace NodeUtility;
    // prompt the name of the head most ingredient
    auto blockofnetherite = new Node("Block of Netherite");
    auto netheriteingot = new Node("Netherite Ingot", blockofnetherite, 0, 1, 9);
    auto goldingot = new Node("Gold Ingot", netheriteingot, 0, 1, 4);
    auto netheritescrap = new Node("Netherite Scrap", netheriteingot, 1, 1, 4);
    auto emerald = new Node("Emerald", netheritescrap, 0, 1, 34);
    Node tentativetest("head", nullptr);
    // prompt subingredients
    //  populate(tentativetest);
    // create and write into file
    // todo create function that determines if an input has been repeated somewhere else and append a number the name to make it unique
    // set assert values - do arithmetic

    
    NodeUtility::setassertvalues(blockofnetherite, 64);
    //  create docstring
    write::docstring::module(output);
    output << std::endl;
    // create variable declarations
    write::tree_declaration(output, blockofnetherite);
    output << std::endl
           << std::endl;
    // create test class
    write::createclass(output, blockofnetherite);
    // create test methods
    write::tree_method(output, blockofnetherite);
    // clean up allocated memory from tree
    // terminate process
    output << std::endl;
    output.close();
    
    massdelete(blockofnetherite);
    return 0;
}
