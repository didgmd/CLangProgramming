// 求解一元二次方程
#include <stdio.h>
#include <math.h>
int main()
{
    double a, b, c, d, x1, x2;
    printf("Please input the coefficients of the equation:\n");
    scanf("%lf %lf %lf", &a, &b, &c);
    d = b * b - 4 * a * c;
    if (d < 0)
        printf("The equation has no real roots.\n");
    else if (d == 0)
    {
        x1 = -b / (2 * a);
        printf("The equation has one root: x=%lf\n", x1);
    }
    else
    {
        x1 = (-b + sqrt(d)) / (2 * a);
        x2 = (-b - sqrt(d)) / (2 * a);
        printf("The equation has two roots: x1=%lf, x2=%lf\n", x1, x2);
    }
    return 0;
}