#include "Node.h"
int main()
{
    std::cout << "What is the name of the item:" << std::endl;
    std::string headname = "";
    std::getline(std::cin,headname);
    Node head(headname);
    return 0;
}
