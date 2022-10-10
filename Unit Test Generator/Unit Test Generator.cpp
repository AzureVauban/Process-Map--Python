// Unit Test Generator.cpp : This file contains the 'main' function. Program execution begins and ends there.
// merge changes into Bug Fixing Branch when this is completed
#include "NodeUtility.h"
std::ofstream output("generatedUnitTest.py");
void populate(NodeUtility::Node& object)
{
    
}
int main()
{
    using namespace NodeUtility;
    // prompt the name of the head most ingredient
    auto head = new Node("Head");
    auto bodyA = new Node("Body A", head);
    auto bodyB = new Node("Body B", bodyA);
    auto bodyC = new Node("Body C", bodyB);
    auto bodyD = new Node("Body D", bodyC);

    // prompt subingredients

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
