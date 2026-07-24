/*
 * 例程 ID：EX-C03-012
 * 标题：教材例程 3.9
 * 教材位置：第 3 章 / 3.9
 * 知识点：数据类型、运算符、输入输出
 * 来源：2024-2025-1/20240927_1008/3.9.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>
int main()
{
    char a, b, c;  // 定义字符变量a,b,c
    a = getchar(); // 从键盘输入一个字符，送给字符变量a
    b = getchar(); // 从键盘输入一个字符，送给字符变量b
    c = getchar(); // 从键盘输入一个字符，送给字符变量c
    putchar(a);    // 将变量a的值输出
    putchar(b);    // 将变量b的值输出
    putchar(c);    // 将变量c的值输出
    putchar('\n'); // 换行
    return 0;
}
