// Unit Test Generator.cpp : This file contains the 'main' function. Program execution begins and ends there.
// merge changes into Bug Fixing Branch when this is completed
#include "NodeUtility.h"
#include <sstream>
std::ofstream output("generatedUnitTest.py");
void populate(NodeUtility::Node &object)
{
    std::cout << "What do you need to create " << object.ingredient << ":" << std::endl;
}
bool isdigit_check(const std::string basestring = "")
{
    bool isdigit = false;
    for (const auto &character : basestring)
    {
        isdigit = (int)character <= 57 and (int) character >= 48;
        if (not isdigit)
        {
            break;
        }
    }
    return isdigit;
}
int integer_input()
{
    int returnint = 0;
    std::string desiredamount_str = "";
    std::stringstream buffer;
    do
    {
        std::getline(std::cin, desiredamount_str);
        std::remove(desiredamount_str.begin(), desiredamount_str.end(), ' ');
        if (not isdigit_check(desiredamount_str))
        {
            std::cout << "Please type in an interger" << std::endl;
        }
    } while (not isdigit_check(desiredamount_str));
    buffer << desiredamount_str;
    buffer >> returnint;
    return returnint;
}
int main()
{
    using namespace NodeUtility;
    // prompt the name of the head most ingredient
    auto blockofnetherite = new Node("Block of Netherite");
    // prompt subingredients
    auto netheriteingot = new Node("Netherite Ingot", blockofnetherite, 0, 1, 9);
    auto goldingot = new Node("Gold Ingot", netheriteingot, 0, 1, 4);
    auto netheritescrap = new Node("Netherite Scrap", netheriteingot, 1, 1, 4);
    auto emerald = new Node("Emerald", netheritescrap, 0, 1, 34);
    //  populate(tentativetest);

    // todo create function that determines if an input has been repeated somewhere else and append a number the name to make it unique
    // prompt desired amount
    std::cout << "How much " << blockofnetherite->ingredient << " do you want to create? " << std::endl;
    int desirednumofhead = integer_input();
    // set assert values - do arithmetic
    NodeUtility::setassertvalues(blockofnetherite, desirednumofhead);
    // create and write into file
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
    massdelete(blockofnetherite);
    output.close();
    return 0;
}
