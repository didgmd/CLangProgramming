/*
 * 例程 ID：EX-C08-022
 * 标题：教材例程 8.16
 * 教材位置：第 8 章 / 8.16
 * 知识点：指针、数组与指针、字符串指针、动态内存
 * 来源：2024-2025-1/20241112_1115/8.16.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>
int main()
{
    char string[] = "I love China!"; // 定义字符数组sting
    printf("%s\n", string);          // 用%s格式声明输出string，可以输出整个字符串
    printf("%c\n", string[7]);       // 用%c格式输出一个字符数组元素
    return 0;
}
