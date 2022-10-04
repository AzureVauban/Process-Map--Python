/*
this script is used to create ingredient mock trees for the Proces Map (Python) Unit test file
the first node will always have an amount made per craft and amount needed of 1 and an amount on hand of 0
*/
#include <iostream>
#include <string> 
#include <vector>
struct data
{
    std::string ingredient; //name of the item
    data *parent;
    data(std::string name = "",data *P = NULL) //!PASS PARENT IN BY REFRENCE data(name,&PARENT);
    {
        ingredient = name;
        parent = P;
    }
    ~data()
    {
        std::cout << "Deleting " << ingredient << " : " << this << std::endl;
    }
};
void populate(data &purple); //creates trees
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
    data test("test",&purple);
    std::cout << "end of function from" << populate << std::endl;
}
