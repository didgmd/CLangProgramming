/*
 * 例程 ID：EX-C04-014
 * 标题：教材例程 4.9
 * 教材位置：第 4 章 / 4.9
 * 知识点：if、switch、条件表达式
 * 来源：2024-2025-1/20241011_1015/4.9.c
 * 编译模式：gnu99-textbook
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#include <stdio.h>
#include <math.h>
int main()
{
    double a, b, c, disc, x1, x2, realpart, imagpart;
    scanf("%lf,%lf,%lf", &a, &b, &c);
    printf("The equation ");
    if (fabs(a) <= 1e-6)
        printf("is not a quadratic\n");
    else
    {
        disc = b * b - 4 * a * c;
        if (fabs(disc) <= 1e-6)
            printf("has two equal roots:%8.4f\n", -b / (2 * a));
        else if (disc > 1e-6)
        {
            x1 = (-b + sqrt(disc)) / (2 * a);
            x2 = (-b - sqrt(disc)) / (2 * a);
            printf("has distinct real roots:%8.4f and %8.4f\n", x1, x2);
        }
        else
        {
            realpart = -b / (2 * a);          // realpart是复根的实部
            imagpart = sqrt(-disc) / (2 * a); // imagpart是复根的虚部
            printf("has complex roots:\n");
            printf("%8.4f+%8.4fi\n", realpart, imagpart); // 输出一个复数
            printf("%8.4f-%8.4fi\n", realpart, imagpart); // 输出另一个复数
        }
    }
    return 0;
}
