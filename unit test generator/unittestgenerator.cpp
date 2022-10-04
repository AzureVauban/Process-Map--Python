/*
this script is used to create ingredient mock trees for the Proces Map (Python) Unit test file
the first node will always have an amount made per craft and amount needed of 1 and an amount on hand of 0
*/
#include <iostream>
#include <string>
struct data{
    std::string ingredient;
    data(std::string name = "")
    {
        ingredient = name;
    }
};
void populate(data &purple); //make input trees
int main()
{
    std::string headitemname = "\x1B[31mHEAD\x1B[37m";
    data head(headitemname);
    populate(head);
    return 0;
}
void populate(data &purple)
{
    std::cout << "What ingredients do you need create " << purple.ingredient << ":" << std::endl;
}
