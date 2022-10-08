#include "Node.h"
int main()
{
    std::ofstream generatedunittest("myfile.py");
    // prompt name of head item
    std::cout << "What is the name of the item:" << std::endl;
    std::string headname = "";
    std::getline(std::cin, headname);
    Node headoflinkedlist(headname);
    // modify ofstream object
    generatedunittest << "\"\"\"Assigned title of Head Node is " << headname << std::endl
                      << "\"\"\"" << std::endl;
    // NodeUtility::create::testclass(head,generatedunittest); // error on this file
    generatedunittest.close();
    return 0;
}
