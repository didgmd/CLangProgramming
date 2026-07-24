/*
 * 例程 ID：EX-C06-005
 * 标题：教材例程 6.5
 * 教材位置：第 6 章 / 6.5
 * 知识点：一维数组、二维数组、字符数组、字符串
 * 来源：2024-2025-1/20241025_1029/6.5.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>
int main()
{
    int i, j, row = 0, colum = 0, max;
    int a[3][4] = {{1, 2, 3, 4}, {9, 8, 7, 6}, {-10, 10, -5, 2}}; // 定义数组并赋初值
    max = a[0][0];                                                // 先认为a[0][0]最大
    for (i = 0; i <= 2; i++)
        for (j = 0; j <= 3; j++)
            if (a[i][j] > max) // 如果某元素大于max，就取代max的原值
            {
                max = a[i][j];
                row = i;   // 记下此元素的行号
                colum = j; // 记下此元素的列号
            }
    printf("max=%d\nrow=%d\ncolum=%d\n", max, row, colum);
    return 0;
}
