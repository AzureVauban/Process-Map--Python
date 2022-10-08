#pragma once
#include <iostream>
#include <string>
#include <vector>
#include <fstream>
enum MODE
{
    red = 0,
    blue = 1
};
struct SimpleData
{
    std::string ingredient = "";
    long long int amountonhand = 0,
        amountneeded = 1,
        amountresulted = 0,
        amountmadepercraft = 1;
    SimpleData(std::string I = "", long long int A = 0, long long int B = 1, long long int C = 1)
    {
        ingredient = I;
        amountonhand = A;
        amountmadepercraft = B;
        amountneeded = C;
    }
};
struct Node : public SimpleData
{
    Node *parent;
    std::vector <Node*> children = {};
    Node(std::string I2 = "", Node *parentinstance = nullptr, long long int A2 = 0, long long int B2 = 1, long long int C2 = 1)
    {
        std::cout << "ALLOCATING " << I2 << " : " << this << std::endl;
        ingredient = I2;
        amountonhand = A2;
        amountmadepercraft = B2;
        amountneeded = C2;
        parent = parentinstance;
        if (parent)
        {
            parent->children.emplace_back(this);
        }
    }
};

namespace NodeUtility
{

    // include functions that are needed to be used with the Node class here here
    enum format
    {
        white = 0,  // variable and method declaration
        purple = 1, // docstring
        green = 2,  // trailing and leading whitespace
        orange = 3  // all lowercase
    };
    // return head node/parent most of a particular Node instance
    Node *origin(Node *current)
    {
        while (current->parent)
        {
            current = current->parent;
        }
        return current;
    }
    // todo finish function for formatting ingredient name to be used - use Visual Studio to Unit Test
    std::string parsestringformat(const Node &Nani, format MODE = white)
    {
        /*
        white, default mode, formats string for variable declaration and to be utilized
        in math asseration method declaration.
            input: advanced alloy, output : advancedalloyN
            where N is an integer number used to help make the declaration unique in the event there are multple instances
                the same ingredient name.
        purple, formats string to be utilized in docstring of math asseration method.
            input: advanced alloy, output : Advanced Alloy
        green formats string to exclude leading and trailing whitespace
            input:   advanced alloy    , output: advanced alloy
        orange, formats string to be only lowercase characters
        */
        switch (MODE)
        {
        case purple:
            std::cout << "Purple" << std::endl;
            break;
        case green:
            std::cout << "Green" << std::endl;
            break;
        case orange:
            std::cout << "Orange" << std::endl;
            break;
        default:
            std::cout << "Default" << std::endl;
            break;
        }
        return Nani.ingredient;
    }
    // create function to delete all node pointers
    void destroy(const Node *nodeobject)
    {
        std::cout << "DEALLOCATING " << nodeobject->ingredient << " : " << nodeobject << std::endl;
        for (const auto &i : nodeobject->children)
        {
            destroy(i);
        }
        delete nodeobject;
    }
    void tabbing(std::ofstream &pymodule, const int TABLEVEL)
    {
        std::cout << "SETTING INDENTATION..." << std::endl;
        for (int i = 0; i < TABLEVEL; i++) {
            pymodule << "\t";
        }
    }
    // todo create function to get assert values for test methods
    namespace create
    {
        namespace docstring
        {

            // todo create function for outputting docstring for class
            void testclass(const Node &nodeobject, std::ofstream &pymodule)
            {
                //pymodule << "Writing Docstring for " << parsestringformat(blue) << << std::endl;
                // todo add code
            }
            // todo create function for outtputting docstring for method
            void method(const Node &nodeobject, std::ofstream &pymodule)
            {
                std::cout << "Writing Docstring for " << parsestringformat(nodeobject) << " test method" << std::endl;
                // todo add code
            }
            // create function for outtputting module docstring
            void module(std::ofstream &pymodule)
            {
                std::cout << "GENERATING UNITTEST DOCSTRING" << std::endl;
                pymodule << "\"\"\"" << "AUTO GENERATED UNIT TEST FILE" << std::endl 
                << "   USE FORMATTING FUNCTIONS OF UTILIZED IDE TO CLEANUP AND FINALIZE ANY MISTAKES REGARDING\nFORMATTING THAT COULD BE MADE" 
                << std::endl << "\"\"\"" << std::endl;
            }
        }
        // todo create function for outtputting test class to output .py file
        void testclass(const Node &nodeobject, std::ofstream &pymodule)
        {
            // todo add code
            docstring::testclass(nodeobject, pymodule);
        }
        // todo create function for outputitng test method declaration of definition
        void method(const Node &nodeobject, MODE type, std::ofstream &pymodule)
        {
            // todo add code
            docstring::method(nodeobject, pymodule);
        }

        // todo create function for creating variable declarations
        void declaration(const Node &nodeobject, std::ofstream &pymodule)
        {
            // todo add code
        }
    }
    // create function for generating the unit test file
    void generatateunittest(Node *head, std::ofstream &outputfile)
    {
        create::docstring::module(outputfile);
        outputfile << "import unittest" << std::endl << "import random" << std::endl << std::endl;
        outputfile << "from main import (Node, findlocalendpoints, reversearithmetic, tentative_formatoutput)" << std::endl;
        //NodeUtility::tabbing(outputfile, 3);
        //outputfile << "Tentative Description : " << head << std::endl;
        //NodeUtility::tabbing(outputfile, 3);
        // loop until all classes have been written onto the file
        // generate module docstring
        // generate unit test class
        // generate unit test methods based on program mode
        outputfile << std::endl;
        // close file
        outputfile.close();
    }
}