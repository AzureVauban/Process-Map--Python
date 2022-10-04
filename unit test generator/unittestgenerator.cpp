/*
This file is used to create big mock ingredient trees for the Process Map (Python) versions
*/
#include <iostream>
#include <fstream>
#include <algorithm> //for alphabetlically sorting the input
#include <string>
#include <vector>
#include <sstream> //for converting strings into interger
#include <thread>
struct mockNode
{
public:
    std::vector<mockNode> *child = {};
    std::string ingredient;

private:
    mockNode *parent;
    int amountonhand = 0,
        amountneeded = 1,
        amountmadepercraft = 1;

    // setters
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
    // getters
    std::string itemname()
    {
        return ingredient;
    }

    mockNode(std::string red = nullptr, mockNode *blue = nullptr)
    {
        ingredient = red;
        parent = blue;
        if (parent)
        {
            parent->child->emplace_back(this);
        }
        promptnumber();
    }
    ~mockNode()
    {
    }
};
//! bool outputrepeated(std::vector<std::string> &mystrvector, std::string &mystring); // checks to see if the output is repeated and if it is append how many times its been repeated to make it unique
void populate(mockNode &cur);                                 // same method from the main solution python file, just in C++
void createoutputfile(std::vector<std::string> &methodnames); // outputs a .py file for the unit tests
void mass_delete(mockNode &black);
void terminateprogram(int seconds);
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
    mockNode head(CLASSNAME);
    // prompt the user to input test names
    populate(head);
    // create file object and output items
    std::cout << "file outputted" << std::endl;
    // destroy node data
    std::cout << "terminating process" << std::endl;
    mass_delete(head);
    return 0;
}
void populate(mockNode &cur)
{
    std::cout << "What do you need to create " << cur.itemname() << ":" << std::endl;
    // output the trail if parent of the augment instance is not null
    std::vector<std::string> myinputs = {};
    // prompt input
    while (true)
    {
        std::string input;
        std::getline(std::cin, input);
        if (input.empty())
        {
            break;
        }
        else
        {
            myinputs.emplace_back(input);
        }
    }
    // create new nodes and emplace them into the childrens vector of their parent
    for (const auto &i : myinputs)
    {
        mockNode childnode(i);
    }
    // continue function recursively
    // auto j = cur.child->begin();
    for (int i = 0; i < cur.child->size(); i++)
    {
        populate(cur.child->at(i));
    }
}
void createoutputfile(mockNode &white)
{ // todo get file code from old project
}
void mass_delete(mockNode &black)
{
    for (int i = 0; i < black.child->size(); i++)
    {
        mass_delete(black.child->at(i));
    }
    //! std::cout << "Deconstructor was called on " << &black << ":" << &black << std::endl;
    std::cout << "Deconstructor was called on " << &black.ingredient << std::endl;
    delete &black;
}
void terminateprogram(int seconds)
{
    using namespace std::this_thread;
    using namespace std::chrono_literals;
    std::cout << "Shutting down program in " << seconds << " seconds\n";
    for (int s = seconds; s > 0; s--)
    {
        sleep_for(1s);
        std::cout << s << std::endl;
    }
    std::cout << "TERMINATING PROCESS" << std::endl;
}