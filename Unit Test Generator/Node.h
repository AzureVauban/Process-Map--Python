#pragma once
#include <iostream>
#include <string>
#include <vector>
struct Node
{
    std::string ingredient = "";
};
namespace NodeUtility
{
    // include functions here
    //todo create function for formatting ingredient name to be used
    std::string parsestringformat(Node &red, const int formattype = 0)
    {
        /* 
        0, default mode, formats string for variable declaration
            input : advanced alloy, output : advancedalloyN
            where N is an integer number used to help make the declaration unique in the event there are multple instances
                the same ingredient name
        1, formats string to be utilized in math asseration method declaration
            input : advanced alloy, output : advancedalloyN
            where N is an integer number used to help make the declaration unique in the event there are multple instances
                the same ingredient name
        2, formats string to be utilized in docstring of math asseration method
            input : advanced alloy, output : Advanced Alloy
        3, ...
        */
        return red.ingredient;
    }
}