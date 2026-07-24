/*
 * 例程 ID：EX-C08-010
 * 标题：教材例程 8.7.2
 * 教材位置：第 8 章 / 8.7.2
 * 知识点：指针、数组与指针、字符串指针、动态内存
 * 来源：2024-2025-1/20241112_1115/8.7.2.c
 * 编译模式：gnu99-textbook
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#include <stdio.h>
int main()
{
    int i, a[10], *p = a; // p的初值是a，p指向a[0]
    printf("please enter 10 integer numbers:");
    for (i = 0; i < 10; i++)
        scanf("%d", p++);
    p = a; // 重新使p指向a[0]
    for (i = 0; i < 10; i++, p++)
        printf("%d ", *p);
    printf("\n");
    return 0;
}
