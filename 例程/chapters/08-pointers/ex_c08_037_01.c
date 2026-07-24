/*
 * 例程 ID：EX-C08-037
 * 标题：实验演示 lab5.1
 * 教材位置：第 8 章 / lab5.1
 * 知识点：指针、数组与指针、字符串指针、动态内存
 * 来源：2023-2024-1/14_Lab5/01.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>

int main() {
    int num = 42;
    int* ptr = &num;

    printf("Value of num: %d\n", num);
    printf("Address of num: %p\n", (void *)(&num));
    printf("Value of num using pointer: %d\n", *ptr);

    return 0;
}
