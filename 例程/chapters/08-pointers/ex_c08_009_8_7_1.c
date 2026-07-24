/*
 * 例程 ID：EX-C08-009
 * 标题：教材例程 8.7.1
 * 教材位置：第 8 章 / 8.7.1
 * 知识点：指针、数组与指针、字符串指针、动态内存
 * 来源：2024-2025-1/20241112_1115/8.7.1.c
 * 编译模式：gnu99-textbook
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#include <stdio.h>
int main()
{
    int *p, i, a[10];
    p = a; // p指向a[0]		①
    printf("please enter 10 integer numbers:");
    for (i = 0; i < 10; i++)
        scanf("%d", p++); // 输入10个整数给a[0]~a[9]
    for (i = 0; i < 10; i++, p++)
        printf("%d ", *p); // 想输出a[0]~a[9]	②
    printf("\n");
    return 0;
}
