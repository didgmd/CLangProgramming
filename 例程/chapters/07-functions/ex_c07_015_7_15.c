/*
 * 例程 ID：EX-C07-015
 * 标题：教材例程 7.15
 * 教材位置：第 7 章 / 7.15
 * 知识点：函数、参数、递归、变量作用域
 * 来源：2024-2025-1/20241105_1108/7.15.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>
int a = 3, b = 5; // a,b是全局变量
int main()
{
    int max(int a, int b); // 函数声明。a,b是形参
    int a = 8;             // a是局部变量
    printf("max=%d\n", max(a, b));
    return 0;
}

int max(int a, int b) // a,b是函数形参
{
    int c;
    c = a > b ? a : b; // 把a和b中的大者存放在c中
    return (c);
}
