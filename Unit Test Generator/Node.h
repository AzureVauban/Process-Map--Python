#pragma once
#include <iostream>
#include <string>
#include <vector>
struct SimpleData
{
    std::string ingredient = "";
    int amountonhand = 0,
        amountneeded = 1,
        amountresulted = 0,
        amountmadepercraft = 1;
    SimpleData(std::string I = "", int A = 0, int B = 1, int C = 1)
    {
        ingredient = I;
        amountonhand = A;
        amountmadepercraft = B;
        amountneeded = C;
    }
};
struct Node : public SimpleData
{
    Node(std::string I2 = "")
    {
        ingredient = I2;
    }
};
namespace NodeUtility
{
    // include functions that are needed to be used with the Node class here here
    // todo create function for formatting ingredient name to be used
    enum format
    {
        white = 0, //variable and method declaration 
        purple = 1, //docstring 
        green = 2, //trailing and leading whitespace
        orange = 3 //
    };
    std::string parsestringformat(Node &red, format MODE = white)
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
        orange, formats string to 
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
        return red.ingredient;
    }
}