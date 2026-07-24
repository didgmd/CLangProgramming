/*
 * 例程 ID：EX-C07-009
 * 标题：教材例程 7.9
 * 教材位置：第 7 章 / 7.9
 * 知识点：函数、参数、递归、变量作用域
 * 来源：2024-2025-1/20241105_1108/7.9.c
 * 编译模式：gnu99-textbook
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#include <stdio.h>
int main()
{
    int max(int x, int y); // 函数声明
    int a[10], m, n, i;
    printf("enter 10 integer numbers:");
    for (i = 0; i < 10; i++) // 输入10个数给a[0]~a[9]
        scanf("%d", &a[i]);
    printf("\n");
    for (i = 1, m = a[0], n = 0; i < 10; i++)
    {
        if (max(m, a[i]) > m) // 若max函数返回的值大于m
        {
            m = max(m, a[i]); // max函数返回的值取代m原值
            n = i;            // 把此数组元素的序号记下来，放在n中
        }
    }
    printf("The largest number is %d\nit is the %dth number.\n", m, n + 1);
}

int max(int x, int y) // 定义max函数
{
    return (x > y ? x : y); // 返回x和y中的大者
}
