/*
this script is used to create ingredient mock trees for the Proces Map (Python) Unit test file
the first node will always have an amount made per craft and amount needed of 1 and an amount on hand of 0
*/
#include <iostream>
#include <string>
#include <vector>
struct data
{
    std::string ingredient;                                 // name of the item
    const data *parent;                                     // parent of item
    std::vector<data> *children;                            // subnodes
    data(const std::string name = "", const data *P = NULL) //! PASS PARENT IN BY REFRENCE data(name,&PARENT);
    {
        ingredient = name;
        parent = P;
        if (parent)
        {
            parent->children->emplace_back(this);
        }
    }
    ~data()
    {
        std::cout << "Deleting " << ingredient << " : " << this << std::endl;
    }
};
void populate(data &purple); // creates trees
int main()
{
    std::string headitemname = "HEAD";
    data head(headitemname);
    populate(head);
    return 0;
}
void populate(data &purple)
{
    std::cout << "What ingredients do you need create " << purple.ingredient << ":" << std::endl;
    std::vector<std::string> myinputs;
    // prompt user input
    while (true)
    {
        std::string userinput;
        std::getline(std::cin, userinput);
        if (userinput.empty())
        {
            break;
        }
        else
        {
            myinputs.emplace_back(userinput);
        }
    }
    // create new children instances
    for (auto &i : myinputs)
    {
         
    }
    // continue function recursvely
    for (int i = 0; i < purple.children->size(); i++)
    {
        populate(purple.children->at(i));
    }
    std::cout << "end of function from" << populate << std::endl;
}
