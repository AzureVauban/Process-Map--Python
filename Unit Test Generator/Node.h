#pragma once
#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <algorithm>
struct Node
{
    std::string ingredient = "";
    long long int amountonhand, amountneeded, amountmadepercraft, amountresulted;
    Node *parent;
    std::vector<Node *> children;
    Node(std::string name = "", Node *par = nullptr, long long int A = 0, long long int B = 1, long long int C = 1)
    {
        ingredient = name;
        parent = par;
        if (parent)
        {
            parent->children.emplace_back(this);
        }
        amountonhand = A;
        amountmadepercraft = B;
        amountneeded = C;
    }
    ~Node()
    {
        std::cout << "DEALLOCATING " << ingredient << " : " << this << std::endl;
    }
};
void massdelete(Node *obj)
{
    for (const auto child : obj->children)
    {
        massdelete(obj);
    }
    delete obj;
}
// functions for writting and creating the unit test module
namespace format
{
    enum formattype
    {
        defaulttype = 0,
        docstring = 1
    };
    // todo add funnctions for formatting here
    std::string formatstring(const std::string basestring, const formattype type = defaulttype)
    {
        std::string returnstring = basestring;
        switch (type)
        {
        case docstring: // return no spaces, replace spaces with underscore
            for (auto &character : returnstring)
            {
                if (character == ' ')
                {
                    character = '_';
                }
            }
            break;

        default: // return no spaces, replace spaces with underscore
            for (auto &character : returnstring)
            {
                if (character == ' ')
                {
                    character = '_';
                }
            }
        }
        return returnstring;
    }
}
namespace write
{
    const std::string docstringprefix = "\"\"\"";
    // create functions for writing onto ostream object here
    void tabbing(std::ofstream &module, const int tablevel = 1)
    {
        for (int i = 0; i < tablevel; i++)
        {
            module << "\t";
        }
    }
    void moduledocstring(std::ofstream &module)
    {
        module << write::docstringprefix << "AUTO GENERATED UNIT TEST" << std::endl
               << write::docstringprefix << std::endl;
        std::vector<std::string> moduleimportnames = {"unittest", "random", "math", "main"};
        std::sort(moduleimportnames.begin(), moduleimportnames.end());
        for (const auto &import : moduleimportnames)
        {
            module << "import " << import << std::endl;
        }
    }
    void variabledeclaration(std::ofstream &module, const Node *object)
    {
        module << format::formatstring(object->ingredient) << 
    }
}