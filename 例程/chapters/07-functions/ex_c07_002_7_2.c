/*
 * 例程 ID：EX-C07-002
 * 标题：教材例程 7.2
 * 教材位置：第 7 章 / 7.2
 * 知识点：函数、参数、递归、变量作用域
 * 来源：2024-2025-1/20241105_1108/7.2.c
 * 编译模式：gnu99-textbook
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#include <stdio.h>
int main()
{
    int max(int x, int y); // 对max函数的声明
    int a, b, c;
    printf("please enter two integer numbers:"); // 提示输入数据
    scanf("%d,%d", &a, &b);                      // 输入两个整数
    c = max(a, b);                               // 调用max函数，有两个实参。大数赋给变量c
    printf("max is %d\n", c);                    // 输出大数c
    return 0;
}
int max(int x, int y) // 定义max函数，有两个参数
{
    int z;             // 定义临时变量z
    z = x > y ? x : y; // 把x和y中大者赋给z
    return (z);        // 把z作为max函数的值带回main函数
}
