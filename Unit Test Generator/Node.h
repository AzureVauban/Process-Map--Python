#pragma once
#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <algorithm>
const std::string docstringprefix = "\"\"\"";
namespace format
{
    enum formattype
    {
        defaulttype = 0,
        classname = 1
    };
    // todo add funnctions for formatting here
    std::string formatstring(const std::string basestring, const formattype type = defaulttype)
    {
        std::string returnstring = basestring;
        switch (type)
        {
        case classname: // return no spaces, replace spaces with underscore
            for (auto &character : returnstring)
            {
                if (character == ' ')
                {
                    character = '_';
                }
            }
            break;

        default: // find substrings, input them into a vector, recombine with the first character of each substring captial
            for (int i = 0; i < returnstring.size(); i++)
            {
                std::vector<std::string> mystrings = {};
                if (returnstring.at(i) == ' ')
                {
                    returnstring.erase(i);
                    returnstring.shrink_to_fit();
                }
            }
            break;
        }
        return returnstring;
    }
}
namespace write
{
    // create functions for writing onto ostream object here
}