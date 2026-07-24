/*
 * 例程 ID：EX-C01-006
 * 标题：教材例程 1.5.1
 * 教材位置：第 1 章 / 1.5.1
 * 知识点：程序结构、编译与运行、基本输出
 * 来源：2023-2024-1/01_HelloC/1_5_1_ForLoop.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>

int main()
{
    printf("Hello World\n");

    int i;
    for (i = 1; i <= 10; i++)
    {
        printf("This is For loop %d\n", i);
    }

    return 0;
}
