// 递归求斐波那契数列并保存至数组
#include <stdio.h>
int fib(int n)
{
    if (n >= 2)
        return fib(n - 1) + fib(n - 2);
    else
        return 1;
}
int main()
{
    int i, f[20] = {1, 1};
    for (i = 2; i <= 19; i++)
    {
        f[i] = fib(i);
        printf("第%d个斐波那契数为%d\n", i + 1, f[i]);
    }
    return 0;
}