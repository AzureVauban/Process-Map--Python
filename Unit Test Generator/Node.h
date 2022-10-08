#pragma once
#include <iostream>
#include <string>
#include <vector>
struct SimpleData
{
    private:
    std::string ingredient = "";
    int amountonhand = 0,
        amountneeded = 1,
        amountresulted = 0,
        amountmadepercraft = 1;
};
struct Node ::public SimpleData
{
    int tempvalue = amountonhand * 2;
    std::cout << tempvalue << std::endl;
};
namespace NodeUtility
{
    // include functions that are needed to be used with the Node class here here
    // todo create function for formatting ingredient name to be used
    std::string parsestringformat(Node &red, const int formattype = 0)
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
        return red.ingredient;
    }
}