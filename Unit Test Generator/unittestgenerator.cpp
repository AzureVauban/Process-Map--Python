#include "Node.h"
int main()
{
    std::ofstream generatedunittest("myfile.py");
    //prompt name of head item
    std::cout << "What is the name of the item:" << std::endl;
    std::string headname = "";
    std::getline(std::cin,headname);
    Node head(headname);
    //modify resulted unit test module
    NodeUtility::create::testclass(head,generatedunittest);
    return 0;
}
