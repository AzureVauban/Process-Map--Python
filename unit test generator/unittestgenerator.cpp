/*
this script is used to create ingredient mock trees for the Proces Map (Python) Unit test file
the first node will always have an amount made per craft and amount needed of 1 and an amount on hand of 0
*/
#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include <thread>
#include <cmath>
#include <utility> //modify traversal check method to return a pair, a bool and the number of times the name is repeated
enum programmode
{
    red = 0, // solve for the possible amount you can create of your desired amount, primary
    blue = 1 // solve for how much of the raw-most ingredient you would need to create your desired amount of a particular item, secondary
};
programmode MODE = blue;                               //! for now manually change the mode until code its prompt can be added properly
long long int DESIREDAMOUNT = 0; //! only used in Mode B
std::ofstream resultfile("autogenerated_unittest.py"); // resulted file
static int instances = 0;
struct Node
{
    std::string ingredient;
    Node *parent;
    std::vector<Node *> children;
    long long int amountmadepercraft, amountneeded, amountonhand, instancekey;
    Node(std::string name = "", Node *par = nullptr, long long int a = 0,long long int b = 1,long long int c = 1)
    {
        instancekey = instances;
        children = {};
        ingredient = name;
        parent = par;
        amountonhand = a;
        amountmadepercraft = b;
        amountneeded = c;
        // todo create function that prompts the user to input values for the numeric data
        if (parent)
        {
            parent->children.emplace_back(this);
        }
        prompt_numbericdata();
        instances += 1;
    }
    ~Node()
    {
        std::cout << "Removing " << ingredient << " from " << this << std::endl;
    }
    void prompt_numbericdata()
    {
        /*
        if there is a parent prompt amount made per craft and amount needed
        if mode B, do not prompt the amount on hand, keep it as its default value,
        else prompt amount on hand for EVERY node in the ingredient tree!
        */

        if (not MODE == blue)
        {
            // prompt amount on hand
            std::cout << "What is the amount of " << ingredient << " you have on hand:" << std::endl;
            amountonhand = integersetter();
        }
        if (parent)
        {
            // prompt amount needed to craft parent once
            do
            {
                std::cout << "How much " << ingredient << " do you need to craft " << parent->ingredient << " once:" << std::endl;
                amountneeded = integersetter();
                if (amountneeded < 1)
                {
                    std::cout << "Only intergers values equal to or above one will be acccepted" << std::endl;
                }
            } while (amountneeded < 1);
            // prompt amount made per craft
            do
            {
                std::cout << "What is the amount of " << parent->ingredient << " you create each craft: " << std::endl;
                amountmadepercraft = integersetter();
                if (amountmadepercraft < 1)
                {
                    std::cout << "Only intergers values equal to or above one will be acccepted" << std::endl;
                }
            } while (amountmadepercraft < 1);
        }
    }
    int desiredamountsetter()
    {
        std::cout << "What is your desired amount " << ingredient << ":" << std::endl;
        return integersetter();
    }

private:
    long long int integersetter()
    {
        std::string myinput = "";
        long long int integer = 1;
        while (true)
        {
            std::getline(std::cin, myinput);
            // strip trailing whitespace of input
            //! comment back in this code if the correct code doesn't work
            /*while (myinput.size() > 0 && myinput.back() == ' ')
            {
                myinput.pop_back();
                myinput.shrink_to_fit();
            }*/
            if (myinput.size() > 0)
            {

                for (int i = 0; i < myinput.length(); i++)
                {
                    if (myinput[i] == ' ')
                    {
                        // using in-built function to erase element
                        myinput.erase(myinput.begin() + i);
                        i--;
                    }
                }
            }
            if (not myinput.empty())
            {
                break;
            }
            else if (not checkchar(myinput))
            {
                std::cout << "Please type in a postive integer" << std::endl;
            }
        }
        std::stringstream ssbuffer;
        ssbuffer << myinput;
        ssbuffer >> integer;
        return integer;
    }
    bool checkchar(std::string somestring)
    { // strings always fail validation input, could this function be the reason why?
        bool isadigit = true;
        for (const auto &character : somestring)
        {
            isadigit = (int)character <= 57 and (int) character >= 48;
            if (not isadigit)
            {
                break;
            }
        }
        return isadigit;
    }
};
std::vector<Node *> allnodes = {};
// clean up allocated memory using during runtime
void collectgarbage(Node *current);
// create node instances
void populate(Node *current);
// write Node declarations onto output file
void createnodedeclarations(Node *current);
// write test methods onto output file
void createtestmethods(Node *currentnode);
// returns a formatted string
std::string parseformatter(std::string somestring, int formattype = 0, Node *object = nullptr);
// closes program after a certain about of seconds
void terminateprocess(int seconds);
// traverse upward, emplacing names into it, double "for" check for duplicates, clear afterwards
bool checkfornamingduplicates(Node *purple);
// parse traverse through the global list of nodes, return a count of all nodes that have the same ingredient before reaching the same node in the vector
int subappend(Node *orange, std::vector<Node *> purple);
int main()
{
    // prompt program mode
    // prompt tree title (which is the name of the mock ingredient tree)
    std::string treetitle = "";
    do
    {
        std::cout << "What is the name of the head node: ";
        std::getline(std::cin, treetitle);
        if (treetitle.empty())
        {
            std::cout << "Please type in something\n";
        }
    } while (treetitle.empty());

    // create tree using Nodes linked to each other
    auto head = new Node(treetitle);
    allnodes.emplace_back(head);
    populate(head);
    //todo prompt desired amount here instead
    if (MODE = blue){
        DESIREDAMOUNT = head->desiredamountsetter();
    }
    // write to file its docstring
    resultfile << "\"\"\"Unit testing code for Python Process Map" << std::endl;
    resultfile << "\tGenerated from Unit Test generator" << std::endl;
    resultfile << "\tPLEASE USE THE FORMAT DOCUMENT AND FORMAT IMPORT OPTIONS OF CHOSEN IDE" << std::endl;
    resultfile << "\"\"\"\n";
    // write module imports
    resultfile << "import unittest\n"
               << std::endl
               << "from main import Node, reversearithmetic\n"
               << std::endl
               << std::endl;
    // create unit test class
    std::string classname = head->ingredient;
    classname.at(0) = std::toupper(classname.at(0));
    // parse through the string and convert whitespaces to underscores
    for (auto &i : classname)
    {
        if (i == ' ')
        {
            i = '_';
        }
    }
    resultfile << "class " << classname << "(unittest.TestCase):" << std::endl;
    resultfile << "\t\"\"\""
               << "Unit Testing for a mock tree to create " << head->ingredient << "\"\"\"\n"
               << std::endl;
    // write node declarations onto of the file at the top of the Unit Test class
    for (int i = 0; i < allnodes.size(); i++)
    {

        createnodedeclarations(allnodes.at(i));
    }
    // write import methods onto the file object
    if (MODE = blue) //?MODE B
    {
        //!long long int DESIREDAMOUNT = head->desiredamountsetter();
        resultfile << "\treversearithmetic(" << parseformatter(head->ingredient, 0) << "," << DESIREDAMOUNT << ") # the resulted amount of head should be equal to or greater than the desired amount\n";

    }
    // write test methods declarations onto the file below, after all declarations of been created
    resultfile << std::endl;
    for (int i = 0; i < allnodes.size(); i++)
    {

        createtestmethods(allnodes.at(i));
    }

    resultfile.close();
    // destroy nodes and reset used memory
    collectgarbage(head);
    // destory nodes in all nodes vector
    // delete allnodes[allnodes.size()];
    terminateprocess(5);
    return 0;
}
void collectgarbage(Node *current)
{
    for (auto &i : current->children)
    {
        collectgarbage(i);
    }
    delete current;
}
void populate(Node *current)
{
    // prompt if the current node has a parent, loop through its parents and output the trail
    if (current->parent)
    {
        Node *temp = current;
        while (temp->parent)
        {
            if (temp->parent)
            {
                std::cout << temp->ingredient << " -> ";
            }
            else
            {
                std::cout << temp->ingredient << std::endl;
                break;
            }
            temp = temp->parent;
        }
    }
    // prompt user to input nodes
    std::vector<std::string> userinputs = {};
    std::cout << "What do you need to create " << current->ingredient << ":" << std::endl;
    while (true)
    {
        bool namealreadytyped = false, duplicated = false;
        std::string myinput;
        std::getline(std::cin, myinput);
        // strip the input of leading whitespace
        while (myinput.size() > 0 and myinput.front() == ' ')
        {
            myinput.erase(0);
            myinput.shrink_to_fit();
        }
        // strip the input of trailing whitespace
        while (myinput.size() > 0 and myinput.back() == ' ')
        {
            myinput.pop_back();
            myinput.shrink_to_fit();
        }
        // check to see if the user already typed their input into the input vector
        if (not userinputs.empty())
        {

            for (const auto &c : userinputs)
            {
                duplicated = myinput == c;
                if (duplicated)
                {
                    break;
                }
            }
        }
        if (not myinput.empty())
        {
            userinputs.emplace_back(myinput);
        }
        else if (duplicated)
        {
            std::cout << "You have already typed in this input, can you please type in something else..." << std::endl;
        }
        else
        {
            break;
        }
    }
    // create new nodes
    for (const auto &str : userinputs)
    {
        auto child = new Node(str, current);
        allnodes.emplace_back(child);
    }
    // continue function recursively
    for (auto &childinstance : current->children)
    {
        populate(childinstance);
    }
}
void createnodedeclarations(Node *current)
{
    /*
    example of a Node declared in the python unit test file
    focusingarray       : Node = Node('Focusing Array', None, 0, 1, 1)
    */
    long long int assertedvalue = 0;
    // parse nodename
    std::vector<std::string> tempstrings = {}; //?traverse upward, emplacing names into it, double "for" check for duplicates, clear afterwards
    //! std::string nodeinstancename = parseformatter(current->ingredient); recomment this back in if the case 1 logic doesn't work
    std::string nodeinstancename = parseformatter(current->ingredient, 1, current);
    //? check to see how many times this has been repeated, if the amount if greater than 1, append (total +2) onto it
    //! dont append the instance key, only append the duplicate number
    /*
    auto tempinstance = current;
    std::string strvar = "";
    while (tempinstance->parent)
    {
        if (tempinstance->ingredient == current->ingredient)
        {

            strvar = std::to_string(tempinstance->instancekey);
            nodeinstancename.append("_" + strvar);
            break;
        }
        tempinstance->parent;
    }
    */
    //  setter code for the parent instances of the parameter
    std::string parentinstancename = "None";
    if (current->parent)
    {
        //! parentinstancename = parseformatter(current->parent->ingredient, 0); recomment this back in if the case 1 logic for the parsestring function does not work
        parentinstancename = parseformatter(current->parent->ingredient, 1, current->parent);
        //?check to see how many times this has been repeated, if the amount if greater than 1, append (total +2) onto it
        //! dont append the instance key, only append the duplicate number
        /*
        auto tempinstance = current->parent;
        while (tempinstance->parent)
        {
            if (tempinstance->ingredient == current->parent->ingredient)
            {

                strvar = std::to_string(tempinstance->instancekey);
                parentinstancename.append("_" + strvar);
                break;
            }
            tempinstance->parent;
        }
        */
    }
    // write data onto it
    //?create class declaration, make a copy of the ingredient name and parse through it captializing it then removing whitespace
    resultfile << "\t" << nodeinstancename << std::right << "    : Node = Node('" << current->ingredient << "',";
    resultfile << parentinstancename << ", ";
    resultfile << current->amountonhand << ", " << current->amountmadepercraft << ", " << current->amountneeded << ")";
    resultfile << " # key :" << current->instancekey << std::endl;
}
void createtestmethods(Node *current)
{

    /*
    in mode B, the assert value is the product amountonhand of the parent and the inverse of the quotient between its amount made per craft and amount needed per craft
    */
    auto assertedvalue = 0.00;
    if (MODE == blue and not current->parent)
    {
        assertedvalue = DESIREDAMOUNT;
    } else if (MODE == blue and current->parent)
    {
    //todo DEBUG THIS
    int a = current->amountmadepercraft;
    int b = current->amountneeded;
    auto ratio = ceil(pow(double((current->amountmadepercraft/current->amountneeded)),-1));
    assertedvalue = ceil(current->parent->amountonhand * ratio);
    }
    // make copy and modify string to be used as a declaration
    //! recomment this code if the parsemethod case 1 doesn't work
    /*
    std::string nodeinstancename = parseformatter(current->ingredient);
    if (checkfornamingduplicates(current))
    {
        nodeinstancename.append(std::to_string(subappend(current,allnodes)));
    }
    */
    std::string nodeinstancename = parseformatter(current->ingredient, 1, current);
    // write data onto the file
    resultfile << "\t\ndef test_" << nodeinstancename << "(self):" << std::endl;
    resultfile << "\t\t\"\"\"the asserted value of " << current->ingredient << " should be " << assertedvalue << std::endl;
    resultfile << "\t\tinclude additional comments here: " << current << std::endl;
    resultfile << "\t\t\"\"\"" << std::endl;
    if (MODE = blue)
    {
        resultfile << "\t\tself.assertEqual(self." << nodeinstancename << ".amountonhand, " << assertedvalue << ")" << std::endl;
    }
    else
    {
        resultfile << "\t\tself.assertEqual(self." << nodeinstancename << ".amountresulted, " << assertedvalue << ")" << std::endl;
    }
}
std::string parseformatter(std::string somestring, int formattype, Node *nodeobject)
{
    /* formatting types:
    type 1: declaration syntax of an instance of Node (remove whitespace)
    default : declaration syntax of an instance of Node (replace whitespace with underscore)
    */
    std::string myreturnedstring = somestring;
    switch (formattype)
    {
    case 0: // declaration syntax of an instance of Node (remove whitespace)
        for (int i = 0; i < myreturnedstring.size(); i++)
        {
            if (myreturnedstring.at(i) == ' ')
            {
                myreturnedstring.at(i) = '_';
            }
        }
        break;
    case 1: // modified declaration node name, appended with an interger (the number duplicates are above itself) to be unique
        myreturnedstring = parseformatter(somestring);
        if (checkfornamingduplicates(nodeobject) and nodeobject)
        {
            if (subappend(nodeobject,allnodes) > 0)
            {
            myreturnedstring.append(std::to_string(subappend(nodeobject, allnodes)));
            }
        }
        break;
    default: // declaration syntax of an instance of Node (replace whitespace with underscore)
        for (int i = 0; i < myreturnedstring.size(); i++)
        {
            if (myreturnedstring.at(i) == ' ')
            {
                myreturnedstring.erase(i);
                myreturnedstring.shrink_to_fit();
            }
        }
        break;
    }
    return myreturnedstring;
}
void terminateprocess(int seconds)
{
    using namespace std::this_thread;
    using namespace std::chrono_literals;
    std::cout << "Shutting down program in " << seconds << " seconds\n";
    for (int s = seconds; s > 0; s--)
    {
        sleep_for(1s);
        std::cout << s << std::endl;
    }
    std::cout << "TERMINATING PROGRAM\n";
}
bool checkfornamingduplicates(Node *purple)
{
    bool isduplicate = false;
    std::vector<std::string> nodenames = {};
    // emplace string variables into the vector
    while (purple->parent)
    {
        nodenames.emplace_back(purple->ingredient);
        purple = purple->parent;
    }
    // check to see if duplicate is present
    for (const auto &a : nodenames)
    {
        for (const auto &b : nodenames)
        {
            isduplicate = a == b;
            if (isduplicate)
            { //! if the node is a duplicate, append its instance key to the formatted name in the output formatter functions
                break;
            }
        }
    }
    return isduplicate;
}
//
int subappend(Node *orange, std::vector<Node *> purple)
{
    // todo find better variable names
    // stop when orange's instancekey is the same as purple
    //?returns the amount of duplicates of orange's ingredient name there is before reaching to itself in the vector
    int count = 0;
    for (const auto &instance : purple)
    {
        bool booleanbreak = orange->instancekey == instance->instancekey;
        if (booleanbreak)
        {
            break;
        }
        if (orange->ingredient == instance->ingredient and not booleanbreak)
        {
            count += 1;
        }
    }
    return count; // append this number to the string in the filewrite functions
}
// end of code