#include "Node.h"
int main()
{
    std::cout << "What is the name of the item:" << std::endl;
    std::string headname = "";
    std::getline(std::cin,headname);
    Node head(headname);
    std::cout << "Formatted String: " << NodeUtility::parsestringformat(head) << std::endl;
    return 0;
}
