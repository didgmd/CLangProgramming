/*
 * 例程 ID：EX-C08-002
 * 标题：教材例程 8.2
 * 教材位置：第 8 章 / 8.2
 * 知识点：指针、数组与指针、字符串指针、动态内存
 * 来源：2024-2025-1/20241112_1115/8.2.c
 * 编译模式：gnu99-textbook
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#include <stdio.h>
int main()
{
    int *p1, *p2, *p, a, b; // p1,p2的类型是int *类型
    printf("please enter two integer numbers:");
    scanf("%d,%d", &a, &b); // 输入两个整数
    p1 = &a;                // 使p1指向变量a
    p2 = &b;                // 使p2指向变量b
    if (a < b)              // 如果a<b
    {
        p = p1;
        p1 = p2;
        p2 = p;
    }                                    // 使p1与p2的值互换
    printf("a=%d,b=%d\n", a, b);         // 输出a,b
    printf("max=%d,min=%d\n", *p1, *p2); // 输出p1和p2所指向的变量的值
    return 0;
}
