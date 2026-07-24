/*
 * 例程 ID：EX-C07-013
 * 标题：教材例程 7.13
 * 教材位置：第 7 章 / 7.13
 * 知识点：函数、参数、递归、变量作用域
 * 来源：2024-2025-1/20241105_1108/7.13.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>
int main()
{
    int max_value(int array[][4]);                                // 函数声明
    int a[3][4] = {{1, 3, 5, 7}, {2, 4, 6, 8}, {15, 17, 34, 12}}; // 对数组元素赋初值
    printf("Max value is %d\n", max_value(a));
    // max_value(a)为函数调用
    return 0;
}

int max_value(int array[][4]) // 函数定义
{
    int i, j, max;
    max = array[0][0];
    for (i = 0; i < 3; i++)
        for (j = 0; j < 4; j++)
            if (array[i][j] > max)
                max = array[i][j]; // 把大者放在max中
    return (max);
}
