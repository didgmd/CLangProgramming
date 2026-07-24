/*
 * 例程 ID：EX-C08-013
 * 标题：教材例程 8.9.1
 * 教材位置：第 8 章 / 8.9.1
 * 知识点：指针、数组与指针、字符串指针、动态内存
 * 来源：2024-2025-1/20241112_1115/8.9.1.c
 * 编译模式：gnu99-textbook
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#include <stdio.h>
int main()
{
    void inv(int *x, int n);  // inv函数声明
    int i, arr[10], *p = arr; // 指针变量p指向arr[0]
    printf("The original array:\n");
    for (i = 0; i < 10; i++, p++)
        scanf("%d", p); // 输入arr数组的元素
    printf("\n");
    p = arr;    // 指针变量p重新指向arr[0]
    inv(p, 10); // 调用inv函数，实参p是指针变量
    printf("The array has been inverted:\n");
    for (p = arr; p < arr + 10; p++)
        printf("%d ", *p);
    printf("\n");
    return 0;
}

void inv(int *x, int n) // 定义inv函数，形参x是指针变量
{
    int *p, m, temp, *i, *j;
    m = (n - 1) / 2;
    i = x;
    j = x + n - 1;
    p = x + m;
    for (; i <= p; i++, j--)
    {
        temp = *i;
        *i = *j;
        *j = temp;
    }
    return;
}
