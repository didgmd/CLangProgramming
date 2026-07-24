/*
 * 例程 ID：EX-C07-012
 * 标题：教材例程 7.12
 * 教材位置：第 7 章 / 7.12
 * 知识点：函数、参数、递归、变量作用域
 * 来源：2024-2025-1/20241105_1108/7.12.c
 * 编译模式：gnu99-textbook
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#include <stdio.h>
int main()
{
    void sort(int array[], int n);
    int a[10], i;
    printf("enter array:\n");
    for (i = 0; i < 10; i++)
        scanf("%d", &a[i]);
    sort(a, 10); // 调用sort函数,a为数组名，大小为10
    printf("The sorted array:\n");
    for (i = 0; i < 10; i++)
        printf("%d ", a[i]);
    printf("\n");
    return 0;
}

void sort(int array[], int n)
{
    int i, j, k, t;
    for (i = 0; i < n - 1; i++)
    {
        k = i;
        for (j = i + 1; j < n; j++)
            if (array[j] < array[k])
                k = j;
        t = array[k];
        array[k] = array[i];
        array[i] = t;
    }
}
