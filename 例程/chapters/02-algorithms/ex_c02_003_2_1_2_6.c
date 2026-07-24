/*
 * 例程 ID：EX-C02-003
 * 标题：教材例程 2.1_2.6
 * 教材位置：第 2 章 / 2.1_2.6
 * 知识点：算法、流程控制、问题求解
 * 来源：2024-2025-1/20240924/2.1_2.6.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：deterministic
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>

int main()
{
    // 1 * 2 * 3 * 4 * 5
    int p = 1;
    int i = 2;

    while (i <= 5) 
    {
        printf("p is %d, i is %d\n", p, i);
        p = p * i;  // S3
        i = i + 1;  // S4
    }

    return 0;
}
