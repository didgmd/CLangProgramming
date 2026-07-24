/*
 * 例程 ID：EX-C08-014
 * 标题：教材例程 8.10.1
 * 教材位置：第 8 章 / 8.10.1
 * 知识点：指针、数组与指针、字符串指针、动态内存
 * 来源：2024-2025-1/20241112_1115/8.10.1.c
 * 编译模式：gnu99-textbook
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#include <stdio.h>
int main()
{
    void sort(int x[], int n); // sort函数声明
    int i, *p, a[10];
    p = a; // 指针变量p指向a[0]
    printf("please enter 10 integer numbers:");
    for (i = 0; i < 10; i++)
        scanf("%d", p++); // 输入10个整数
    p = a;                // 指针变量p重新指向a[0]
    sort(p, 10);          // 调用sort函数
    for (p = a, i = 0; i < 10; i++)
    {
        printf("%d ", *p); // 输出排序后的10个数组元素
        p++;
    }
    printf("\n");
    return 0;
}
void sort(int x[], int n) // 定义sort函数，x是形参数组名
{
    int i, j, k, t;
    for (i = 0; i < n - 1; i++)
    {
        k = i;
        for (j = i + 1; j < n; j++)
            if (x[j] > x[k])
                k = j;
        if (k != i)
        {
            t = x[i];
            x[i] = x[k];
            x[k] = t;
        }
    }
}
