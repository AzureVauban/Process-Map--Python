#include <iostream>
#include <cmath>
int red(const double a, const double b)
{
    return int(std::pow(a, b));
}
void blue(const double x, const double y)
{
    std::cout << x << " ^ " << y << " == " << red(x, y) << std::endl;
}
int main()
{
//    blue((1.00 / 50.00), -1);
    blue((double(1) / double(50)), -1);

    return 0;
}