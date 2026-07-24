/*
 * 例程 ID：EX-C04-003
 * 标题：教材例程 4.3
 * 教材位置：第 4 章 / 4.3
 * 知识点：if、switch、条件表达式
 * 来源：2024-2025-1/20241011_1015/4.3.c
 * 编译模式：gnu99-textbook
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#include <stdio.h>
int main()
{
    float a, b, c, t;
    scanf("%f,%f,%f", &a, &b, &c);
    if (a > b)
    {
        t = a; // 借助变量t，实现变量a和变量b互换值
        a = b;
        b = t;
    } // 互换后，a小于或等于b
    if (a > c)
    {
        t = a; // 借助变量t，实现变量a和变量c互换值
        a = c;
        c = t;
    } // 互换后，a小于或等于c
    if (b > c) // 还要
    {
        t = b; // 借助变量t，实现变量b和变量c互换值
        b = c;
        c = t;
    } // 互换后，b小于或等于c
    printf("%5.2f,%5.2f,%5.2f\n", a, b, c); // 顺序输出a,b,c的值
    return 0;
}
