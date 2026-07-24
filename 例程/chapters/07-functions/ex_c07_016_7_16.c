/*
 * 例程 ID：EX-C07-016
 * 标题：教材例程 7.16
 * 教材位置：第 7 章 / 7.16
 * 知识点：函数、参数、递归、变量作用域
 * 来源：2024-2025-1/20241105_1108/7.16.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>
int main()
{
    int f(int);   // 函数声明
    int a = 2, i; // 自动局部变量
    for (i = 0; i < 3; i++)
        printf("%d\n", f(a)); // 输出f(a)的值
    return 0;
}

int f(int a)
{
    auto int b = 0;   // 自动局部变量
    static int c = 3; // 静态局部变量
    b = b + 1;
    c = c + 1;
    return (a + b + c);
}
