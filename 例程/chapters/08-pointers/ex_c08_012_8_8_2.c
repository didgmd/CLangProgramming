/*
 * 例程 ID：EX-C08-012
 * 标题：教材例程 8.8.2
 * 教材位置：第 8 章 / 8.8.2
 * 知识点：指针、数组与指针、字符串指针、动态内存
 * 来源：2024-2025-1/20241112_1115/8.8.2.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>
int main()
{
    void inv(int *x, int n);
    int i, a[10] = {3, 7, 9, 11, 0, 6, 7, 5, 4, 2};
    printf("The original array:\n");
    for (i = 0; i < 10; i++)
        printf("%d ", a[i]);
    printf("\n");
    inv(a, 10);
    printf("The array has been inverted:\n");
    for (i = 0; i < 10; i++)
        printf("%d ", a[i]);
    printf("\n");
    return 0;
}

void inv(int *x, int n) // 形参x是指针变量
{
    int *p, temp, *i, *j, m = (n - 1) / 2;
    i = x;
    j = x + n - 1;
    p = x + m;
    for (; i <= p; i++, j--)
    {
        temp = *i;
        *i = *j;
        *j = temp;
    } //*i与*j交换
    return;
}
