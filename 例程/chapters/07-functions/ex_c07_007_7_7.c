/*
 * 例程 ID：EX-C07-007
 * 标题：教材例程 7.7
 * 教材位置：第 7 章 / 7.7
 * 知识点：函数、参数、递归、变量作用域
 * 来源：2024-2025-1/20241105_1108/7.7.c
 * 编译模式：gnu99-textbook
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#include <stdio.h>
int main()
{
    int fac(int n); // fac函数声明
    int n;
    int y;
    printf("input an integer number:");
    scanf("%d", &n); // 输入要求阶乘的数
    y = fac(n);
    printf("%d!=%d\n", n, y);
    return 0;
}

int fac(int n) // 定义fac函数
{
    int f;
    if (n < 0) // n不能小于0
        printf("n<0,data error!");
    else if (n == 0 || n == 1) // n=0或,1时n!=1
        f = 1;                 // 递归终止条件
    else
        f = fac(n - 1) * n; // n>1时，n!=n*(n-1)
    return (f);
}
