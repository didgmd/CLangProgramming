/*
 * 例程 ID：EX-C07-017
 * 标题：教材例程 7.17
 * 教材位置：第 7 章 / 7.17
 * 知识点：函数、参数、递归、变量作用域
 * 来源：2024-2025-1/20241105_1108/7.17.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>
int main()
{
    int fac(int n);
    int i;
    for (i = 1; i <= 5; i++)           // 先后5次调用fac函数
        printf("%d!=%d\n", i, fac(i)); // 每次计算并输出i!的值
    return 0;
}
int fac(int n)
{
    static int f = 1; // f保留了上次调用结束时的值
    f = f * n;        // 在上次的f值的基础上再乘以n
    return (f);       // 返回值f是n!的值
}
