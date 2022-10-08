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
        white = 0,
        orange = 1,
        green = 2,
        purple = 3
    };
    // format MODE = white;
    std::string parsestringformat(Node &red, format MODE = white)
    {
        /*
        0, default mode, formats string for variable declaration and to be utilized
        in math asseration method declaration.
            input: advanced alloy, output : advancedalloyN
            where N is an integer number used to help make the declaration unique in the event there are multple instances
                the same ingredient name.
        1, formats string to be utilized in docstring of math asseration method.
            input: advanced alloy, output : Advanced Alloy
        2, formats string to exclude leading and trailing whitespace
            input:   advanced alloy    , output: advanced alloy
        3, formats string to
        */
        switch (MODE)
        {
        case orange:
            std::cout << "Orange" << std::endl;
            break;
        case green:
            std::cout << "Green" << std::endl;
            break;
        case purple:
            std::cout << "Purple" << std::endl;
            break;
        default:
            std::cout << "Default" << std::endl;
            break;
        }
        return red.ingredient;
    }
}