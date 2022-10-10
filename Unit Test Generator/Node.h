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
    for (auto child : obj->children)
    {
        massdelete(child);
    }
    delete obj;
}
// functions for writting and creating the unit test module
namespace format
{
    enum formattype
    {
        defaulttype = 0,
        docstring = 1,
        classname = 2
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
        case classname: // return no spaces
            std::remove(returnstring.begin(), returnstring.end(), ' ');
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
    namespace docstring
    {

        void module(std::ofstream &tentativename)
        {
            tentativename << write::docstringprefix << "AUTO GENERATED UNIT TEST" << std::endl
                          << write::docstringprefix << std::endl;
            /*
            std::vector<std::string> moduleimportnames = {"unittest", "random", "math", "main"};
            std::sort(moduleimportnames.begin(), moduleimportnames.end());
            */

            tentativename << "import unittest" << std::endl
                          << std::endl;
            tentativename << "from main import Node" << std::endl;
        }
        void classdoc(std::ofstream &tentativename)
        {
            tabbing(tentativename, 1);
            tentativename << docstringprefix << "tentative test class, add additional comments here: " << std::endl;
            tabbing(tentativename, 1);
            tentativename << docstringprefix << std::endl;
        }
    }
    void declaration(std::ofstream &module, const Node *object)
    {
        std::string parentstring = "None";
        if (object->parent)
        {
            parentstring = format::formatstring(object->parent->ingredient);
        }
        module << format::formatstring(object->ingredient) << ": Node = Node('" << object->ingredient << "', " << parentstring << ", " << 0 << ", " << object->amountmadepercraft << ", " << object->amountneeded << ")" << std::endl;
    }
    void method(std::ofstream &module, const Node *object)
    {
        std::string parentstring = "None";
    }
    void tree_declaration(std::ofstream &module, const Node *object)
    {
        write::declaration(module, object);
        for (auto miniobject : object->children)
        {
            tree_declaration(module, miniobject);
        }
    }
    void tree_method(std::ofstream &module, const Node *object)
    {
    }
    void createclass(std::ofstream &module, Node *object)
    {
        Node *temp = object;
        while (temp->parent)
        {
            temp = temp->parent;
        }
        module << "class " << format::formatstring(temp->ingredient, format::classname) << "_unittest"
               << "(unittest.TestCase): #pylint:disable" << std::endl;
        docstring::classdoc(module);
        // call docstring function for class
    }
}