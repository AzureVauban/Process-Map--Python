// Unit Test Generator.cpp : This file contains the 'main' function. Program execution begins and ends there.
// merge changes into Bug Fixing Branch when this is completed
#include "Node.h"
std::ofstream output("generatedUnitTest.py");
int main()
{
    // prompt the name of the head most ingredient
    auto head = new Node("Head Node");
    // prompt subingredients

    // create and write into file
    auto test = "Visual Studio Code";
    // create docstring
    write::moduledocstring(output);
    output << std::endl;
    // create class
    // clean up allocated memory from tree
    massdelete(head);
    // terminate process
    output << std::endl;
    output.close();
    return 0;
}