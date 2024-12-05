// 求平方根的整数部分，要求不用`math.h`
#include <stdio.h>
int main()
{
    int n, i;
    printf("Please input the number:\n");
    scanf("%d", &n);
    for (i = 0; i * i <= n; i++)
        ;
    printf("The integer part of the square root is %d\n", i - 1);
    return 0;
}