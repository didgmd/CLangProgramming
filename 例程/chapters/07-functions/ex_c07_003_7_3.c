/*
 * 例程 ID：EX-C07-003
 * 标题：教材例程 7.3
 * 教材位置：第 7 章 / 7.3
 * 知识点：函数、参数、递归、变量作用域
 * 来源：2024-2025-1/20241105_1108/7.3.c
 * 编译模式：gnu99-textbook
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#include <stdio.h>
int main()
{
    int max(float x, float y);
    float a, b;
    int c;
    scanf("%f,%f", &a, &b);
    c = max(a, b);
    printf("max is %d\n", c);
    return 0;
}
int max(float x, float y)
{
    float z; // z为实型变量
    z = x > y ? x : y;
    return (z);
}
