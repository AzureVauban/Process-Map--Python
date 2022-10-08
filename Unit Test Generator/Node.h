#pragma once
#include <iostream>
#include <string>
#include <vector>
class Node
{
    std::string ingredient = "";
    public:
    std::string name()
    {
        return ingredient;
    }
};
namespace NodeUtility
{
    // include functions here
    //todo make function for formatting the name of the ingredient, should have 3 modes
    std::string parsestringformat(Node &red)
    {
        return red.name();
    }
}