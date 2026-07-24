/*
 * 例程 ID：EX-C01-007
 * 标题：教材例程 1.5.3
 * 教材位置：第 1 章 / 1.5.3
 * 知识点：程序结构、编译与运行、基本输出
 * 来源：2023-2024-1/01_HelloC/1_5_3_WhileLoop.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>

int main()
{
    printf("Hello World\n");

    int i = 1;
    while (i <= 10)
    {
        printf("This is While loop %d\n", i);
        i++;
    }

    return 0;
}
