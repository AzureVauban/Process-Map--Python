# Process Map (Python v1.1f)

This is an item process map console application, type in the name of the items that you want to use to create an even more important item and caculate how much of that item you can make with your current amount on hand, amount needed to create desirable item, and amount of item made per craft. The purpose of this is to see how my python programming styles and habits differs from my c++ programming styles and habits. Another goal of this project is to make teach my self problem solving through the use of recursion (making a function call itself until a certain condition is met, in which case the function would complete its runtime)

## Changes

### Reworked Old Arithmetic Method

In this new verison of the Process Map, the arithmetic method has been reworked. The arithmetic method is supposed to figure out how much of an item a user can create given the amount of ingredients they have for it, during the program's runtime it is referred to as Mode A.

### Created New Arithmetic Method and New Program Mode

Mode B is another mode the user has the option of utilizing in the program. The purpose of Mode B is to figure out how much of the base materials you will need to get a particular about of an item you want. In normal situations this one can consider these base materials to be raw ingredients of manufactured items. How amount needed is determined is through multiplying the quotient of the amount of the parent made per craft and the amount needed to create the parent once, by the amount on hand currently. If these product is less than the desired amount, it will look again and increase the amount on hand until so.

### Finally used Unit Testing for parts of the code

To improve the quality of the arithmetic methods utilized in the solution, Unit Tests using the Unit Test framework were used. To make this work both of the recursive methods had to be modified to return an interger, which is the amount resulted for Mode A's method and the amount on hand for Mode B's method.

## Planned Features of Process Map (Python v2.0)

### Being able to search and copy Nodes you already typed in

In this current iteration of the Process Map, the user must type in one ingredient one by one at a time. There are many ingredient trees in which the end user will input the same ingredient more than once. Process Map v2.0 will improve upon this by giving the user the option to copy and paste a node they already typed out.

Being able to edit or change what you typed before continuing to the next set of inputs
