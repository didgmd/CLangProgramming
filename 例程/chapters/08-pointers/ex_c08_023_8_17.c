/*
 * 例程 ID：EX-C08-023
 * 标题：教材例程 8.17
 * 教材位置：第 8 章 / 8.17
 * 知识点：指针、数组与指针、字符串指针、动态内存
 * 来源：2024-2025-1/20241112_1115/8.17.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>
int main()
{
    char *string = "I love China!"; // 定义字符指针变量string并初始化
    printf("%s\n", string);         // 输出字符串
    return 0;
}
