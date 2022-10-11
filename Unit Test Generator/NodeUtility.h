#pragma once
#include <iostream>
#include <string>
#include <cmath>
#include <vector>
#include <fstream>
#include <algorithm>
namespace NodeUtility
{

    struct Node
    {
        //! using namespace NodeUtility;
        std::string ingredient;
        int amountonhand, amountneeded, amountmadepercraft, amountresulted;
        Node *parent;
        std::vector<Node *> children;
        Node(std::string name = "", Node *par = nullptr, int amount_on_hand = 0,int amount_parent_madepercraft = 1,int amount_needed = 1)
        {
            ingredient = name;
            parent = par;
            if (parent)
            {
                parent->children.emplace_back(this);
            }
            amountonhand = amount_on_hand;
            amountmadepercraft = amount_parent_madepercraft;
            amountneeded = amount_needed;
        }
        ~Node()
        {
            std::cout << "DEALLOCATING " << ingredient << " : " << this << std::endl;
        }
    };
    // set the amount on hand to the desired amount/assertvalue
    long long int setassertvalues(Node *object, const int desiredamount = 0)
    {
        std::cin.clear();
        object->amountresulted = desiredamount;
        float A = object->amountresulted;
        float B = object->amountmadepercraft;
        float C = object->amountneeded;
        float D = object->amountresulted;
        int E = D * 1/((A/B));
        float amountonhand_local = E;
        for (auto child : object->children)
        {
            setassertvalues(child,E);
        }
        std::cout << "FINISH SETTING ASSERT VALUE FOR " << object->ingredient << std::endl;
        return amountonhand_local;
    }
}

void massdelete(NodeUtility::Node *obj)
{
    for (auto child : obj->children)
    {
        massdelete(child);
    }
    delete obj;
}
// functions for writting and creating the unit test module
namespace format // todo modify these functions in a string subclass
{
    enum formattype
    {
        defaulttype = 0,
        docstring = 1,
        classname = 2,
        method = 3,
        instance_declaration = 4
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
        case instance_declaration:
            for (auto &character : returnstring)
            {
                if (character == ' ')
                {
                    character = '_';
                }
            }
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
    std::string modifytitle(const std::string basestring)
    {
        std::string newstring = basestring;
        return newstring;
    }
}
namespace write
{
    using namespace NodeUtility;
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

        void module(std::ofstream &module)
        {
            module << write::docstringprefix << "AUTO GENERATED UNIT TEST" << std::endl
                   << write::docstringprefix << std::endl;
            /*
            std::vector<std::string> moduleimportnames = {"unittest", "random", "math", "main"};
            std::sort(moduleimportnames.begin(), moduleimportnames.end());
            */

            module << "import unittest" << std::endl
                   << std::endl;
            module << "from main import Node" << std::endl;
        }
        void classdoc(std::ofstream &module)
        {
            tabbing(module, 1);
            module << docstringprefix << "tentative test class, add additional comments here: " << std::endl;
            tabbing(module, 1);
            module << docstringprefix << std::endl;
        }
        void method(std::ofstream &module, const Node *object)
        {
            // docstring for test method
            tabbing(module, 2);
            module << docstringprefix << "assert that " << object->ingredient << " is equal to " << object->amountonhand << std::endl;
            tabbing(module, 2);
            module << docstringprefix;
            module << std::endl;
        }
    }
    void declaration(std::ofstream &module, const Node *object)
    {
        std::string parentstring = "None";
        if (object->parent)
        {
            parentstring = format::formatstring(object->parent->ingredient, format::instance_declaration);
        }
        module << format::formatstring(object->ingredient, format::instance_declaration) << ": Node = Node('" << object->ingredient << "', " << parentstring << ", " << 0 << ", " << object->amountmadepercraft << ", " << object->amountneeded << ")" << std::endl;
    }
    void method(std::ofstream &module, const Node *object)
    {
        tabbing(module, 1);
        module << "def test_" << format::formatstring(object->ingredient, format::method) << "(self):" << std::endl;
        write::docstring::method(module, object);
        tabbing(module, 2);
        module << "self.assertEqual(" << format::formatstring(object->ingredient, format::instance_declaration) << ".amountonhand," << object->amountonhand << ")" << std::endl;
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
        write::method(module, object);
        // std::vector<Node*> copy_of_children = {};
        for (const auto miniobject : object->children)
        {
            tree_method(module, miniobject);
        }
    }
    void createclass(std::ofstream &module, Node *object)
    {
        Node *temp = object;
        while (temp->parent)
        {
            temp = temp->parent;
        }
        module << "class " << format::formatstring(temp->ingredient, format::classname) << "_unittest"
               << "(unittest.TestCase): #pylint:disable=C0103" << std::endl;
        docstring::classdoc(module);
        module << std::endl;
        // call docstring function for class
    }
}