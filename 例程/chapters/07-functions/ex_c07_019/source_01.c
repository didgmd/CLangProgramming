/*
 * 例程 ID：EX-C07-019
 * 标题：教材例程 7.19
 * 教材位置：第 7 章 / 7.19
 * 知识点：函数、参数、递归、变量作用域
 * 来源：2024-2025-1/20241105_1108/7.19.file1.c, 2024-2025-1/20241105_1108/7.19.file2.c
 * 编译模式：gnu99-textbook
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#include <stdio.h>
int A; // 定义外部变量
int main()
{
    int power(int); // 函数声明
    int b = 3, c, d, m;
    printf("enter the number a and its power m:\n");
    scanf("%d,%d", &A, &m);
    c = A * b;
    printf("%d*%d=%d\n", A, b, c);
    d = power(m);
    printf("%d**%d=%d\n", A, m, d);
    return 0;
}
