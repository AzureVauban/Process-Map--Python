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
    /* Complier Error
    C:/msys64/mingw64/include/c++/12.1.0/fstream:853:7: note: declared here
    853 |       basic_ofstream(const basic_ofstream&) = delete;
        |       ^~~~~~~~~~~~~~
    
    Node.h:97:58: note:   initializing argument 2 of 'void NodeUtility::create::testclass(const Node&, std::ofstream)'
    97 |         void testclass(const Node &purple, std::ofstream pymodule)
       |                                            ~~~~~~~~~~~~~~^~~~~~~~

    */
    generatedunittest.close();
    return 0;
}
