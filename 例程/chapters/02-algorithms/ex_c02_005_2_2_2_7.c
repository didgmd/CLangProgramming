/*
 * 例程 ID：EX-C02-005
 * 标题：教材例程 2.2_2.7
 * 教材位置：第 2 章 / 2.2_2.7
 * 知识点：算法、流程控制、问题求解
 * 来源：2024-2025-1/20240924/2.2_2.7.c
 * 编译模式：gnu99-textbook
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#include <stdio.h>

int main()
{
    int n[50] = {0}; // n[0]~n[49]
    int g[50] = {0}; // g[0]~g[49]
    int i = 1;

    while (i <= 5)
    {
        scanf("%d", &n[i]);
        scanf("%d", &g[i]);
        printf("Add student number: %d, grade: %d\n", n[i], g[i]);
        i = i + 1;
    }

    i = 1;

    while (i <= 5)
    {
        if (g[i] >= 80)
        {
            printf("Student number: %d, grade: %d\n", n[i], g[i]);
        }
        i = i + 1;
    }

    return 0;
}
