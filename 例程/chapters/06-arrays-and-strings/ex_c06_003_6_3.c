/*
 * 例程 ID：EX-C06-003
 * 标题：教材例程 6.3
 * 教材位置：第 6 章 / 6.3
 * 知识点：一维数组、二维数组、字符数组、字符串
 * 来源：2024-2025-1/20241025_1029/6.3.c
 * 编译模式：gnu99-textbook
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#include <stdio.h>
int main()
{
    int a[10];
    int i, j, t;
    printf("input 10 numbers :\n");
    for (i = 0; i < 10; i++)
        scanf("%d", &a[i]);
    printf("\n");
    for (j = 0; j < 9; j++)         // 进行9次循环，实现9趟比较
        for (i = 0; i < 9 - j; i++) // 在每一趟中进行9-j次比较
            if (a[i] > a[i + 1])    // 相邻两个数比较
            {
                t = a[i];
                a[i] = a[i + 1];
                a[i + 1] = t;
            }
    printf("the sorted numbers :\n");
    for (i = 0; i < 10; i++)
        printf("%d ", a[i]);
    printf("\n");
    return 0;
}
