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
    auto head = new Node("Block of Netherite");
    auto bodyA = new Node("Netherite Ingot", head);
    auto bodyB = new Node("Gold Ingot", bodyA);
    auto bodyC = new Node("Netherite Scrap", bodyA);
    auto bodyD = new Node("Emerald", bodyC);
    Node tentativetest("head", nullptr);
    // prompt subingredients
    populate(tentativetest);
    // create and write into file
    auto test = "Visual Studio Code";
    // todo create function that determines if an input has been repeated somewhere else and append a number the name to make it unique
    //  create docstring
    write::docstring::module(output);
    output << std::endl;
    // create variable declarations
    write::tree_declaration(output, head);
    output << std::endl
           << std::endl;
    // create test class
    write::createclass(output, head);
    // create test methods
    write::tree_method(output, head);
    // clean up allocated memory from tree
    massdelete(head);
    // terminate process
    output << std::endl;
    output.close();
    return 0;
}
