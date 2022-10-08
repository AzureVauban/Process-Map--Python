#include "Node.h"
int main()
{
    std::ofstream generatedunittest("myfile.py");
    // prompt name of head item
    std::cout << "Name of Linked List:" << std::endl;
    std::string headname = "";
    std::getline(std::cin, headname);
    Node headoflinkedlist(headname);
    // modify ofstream object
    generatedunittest << "\"\"\"Tentative Description: " << headname << std::endl
                      << "\"\"\"" << std::endl;
     NodeUtility::create::testclass(headoflinkedlist,generatedunittest); // error on this line
    generatedunittest.close();
    return 0;
}
