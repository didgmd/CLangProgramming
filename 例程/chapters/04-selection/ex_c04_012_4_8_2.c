/*
 * 例程 ID：EX-C04-012
 * 标题：教材例程 4.8.2
 * 教材位置：第 4 章 / 4.8.2
 * 知识点：if、switch、条件表达式
 * 来源：2024-2025-1/20241011_1015/4.8.2.c
 * 编译模式：gnu99-textbook
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#include <stdio.h>
int main()
{
    int year, leap;
    printf("enter year:");
    scanf("%d", &year);

    if (year % 4 != 0)
        leap = 0;
    else if (year % 100 != 0)
        leap = 1;
    else if (year % 400 != 0)
        leap = 0;
    else
        leap = 1;

    if (leap)
        printf("%d is ", year);
    else
        printf("%d is not ", year);
    printf("a leap year.\n");
    return 0;
}
