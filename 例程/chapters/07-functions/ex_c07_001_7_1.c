/*
 * 例程 ID：EX-C07-001
 * 标题：教材例程 7.1
 * 教材位置：第 7 章 / 7.1
 * 知识点：函数、参数、递归、变量作用域
 * 来源：2024-2025-1/20241105_1108/7.1.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：deterministic
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>
int main()
{
    void print_star();    // 声明print_star函数
    void print_message(); // 声明print_message函数
    print_star();         // 调用print_star函数
    print_message();      // print_message函数
    print_star();         // 调用print_star函数
    return 0;
}

void print_star() // 定义print_star函数
{
    printf("******************\n"); // 输出一行*号
}

void print_message() // 定义print_message函数
{
    printf("How do you do!\n"); // 输出一行文字信息
}
