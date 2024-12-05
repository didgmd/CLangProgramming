// 递归求整数的阶乘
#include <stdio.h>
int fac(int n)
{
    int f;
    if (n < 0)
        printf("n<0,data error!");
    else if (n == 0 || n == 1)
        f = 1;
    else
        f = fac(n - 1) * n;
    return f;
}

int main()
{
    int n, y;
    printf("input an integer number:");
    scanf("%d", &n);
    y = fac(n);
    printf("%d!=%d\n", n, y);
    return 0;
}