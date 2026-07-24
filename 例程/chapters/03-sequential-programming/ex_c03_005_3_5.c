/*
 * 例程 ID：EX-C03-005
 * 标题：教材例程 3.5
 * 教材位置：第 3 章 / 3.5
 * 知识点：数据类型、运算符、输入输出
 * 来源：2024-2025-1/20240927_1008/3.5.c
 * 编译模式：gnu99-textbook
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#include <stdio.h>
#include <math.h> //程序中要调用求平方根函数sqrt
int main()
{
    double a, b, c, disc, x1, x2, p, q; // disc用来存放判别式(bb-4ac)的值
    scanf("%lf%lf%lf", &a, &b, &c);     // 输入双精度型变量的值要用格式声明″%lf″
    disc = b * b - 4 * a * c;
    p = -b / (2.0 * a);
    q = sqrt(disc) / (2.0 * a);
    x1 = p + q;
    x2 = p - q;                             // 求出方程的两个根
    printf("x1=%7.2f\nx2=%7.2f\n", x1, x2); // 输出方程的两个根
    return 0;
}
