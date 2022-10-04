/*
This file is used to create big mock ingredient trees for the Process Map (Python) versions
*/
#include <iostream>
#include <fstream>
#include <algorithm> //for alphabetlically sorting the input
#include <string>
#include <vector>
#include <sstream> //for converting strings into interger
class mockNode
{
    std::string *ingredient;
    mockNode *parent;
    std::vector<mockNode> *children = {};
    int amountonhand = 0,
        amountneeded = 1,
        amountmadepercraft = 1;
    void promptnumber()
    {
        // prompt user to input the numeric data
        // always prompt amount on hand
        // if there is a parent instance, prompt amount on needed and amount made per craft
    }
    int intergersetter()
    {
        // use this to return validated interger for the prompt numeric data function
        return 0;
    }

public:
    mockNode(std::string *red = nullptr, mockNode *blue = nullptr)
    {
        ingredient = red;
        parent = blue;
        promptnumber();
    }
    ~mockNode()
    {
    }
};
bool outputrepeated(std::vector<std::string> &mystrvector, std::string &mystring); // checks to see if the output is repeated and if it is append how many times its been repeated to make it unique
void populate(mockNode &cur);                                                      // same method from the main solution python file, just in C++
void createoutputfile(std::vector<std::string> &methodnames);                      // outputs a .py file for the unit tests
int main()
{
    // prompt the user to input the class
    std::string CLASSNAME = "";
    while (true)
    {
        std::cout << "What is the name of the Unit Test class: ";
        std::getline(std::cin, CLASSNAME);
        // strip trailing and leading whitespace from user input
        if (not CLASSNAME.empty())
        {
            break;
        }
    }
    // prompt the user to input test names
    std::vector<std::string> testmethodsname = {};
    std::cout << "Input the name of your test methods:" << std::endl;
    while (true)
    {
        std::string myinput = "";
        std::getline(std::cin, myinput);
        if (myinput.empty())
        {
            break;
        }
        else if (true) // todo insert duplicate checker function
        {
            // check to see if the input has been repeated, if so append a number onto the name input
        }
        else
        {
            testmethodsname.emplace_back(myinput);
        }
    }
    return 0;
}
bool outputrepeated(std::vector<std::string> &mystrvector, std::string &mystring)
{
    bool repeated = false;
    return repeated;
}
void populate(mockNode &cur)
{
}
void createoutputfile(std::vector<std::string> &methodnames)
{
}