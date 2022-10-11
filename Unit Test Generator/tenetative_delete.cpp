#include <iostream>
#include <cmath>
int test_power(const double a, const double b)
{
    return int(std::pow(a, b));
}
void test(const double x, const double y)
{
    std::cout << x << "^" << y << " " << test_power(x, y);
}
int main()
{
    test((1 / 50), -1);
    return 0;
}