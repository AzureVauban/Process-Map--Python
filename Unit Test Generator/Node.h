#pragma once
#include <iostream>
#include <string>
#include <vector>
#include <fstream>
const std::string docstringprefix = "\"\"\"";
namespace format
{
    enum formattingtype
    {
        docstring = 0
    }
    // todo add funnctions for formatting here
    std::string tentative(std::string basestring, formattingtype type)
    {
        std::string returnstring = basestring;
        return returnstring;
    }
}
namespace write
{
    // create functions for writing onto ostream object here
}