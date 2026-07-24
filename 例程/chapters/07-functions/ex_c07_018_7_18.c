/*
 * 例程 ID：EX-C07-018
 * 标题：教材例程 7.18
 * 教材位置：第 7 章 / 7.18
 * 知识点：函数、参数、递归、变量作用域
 * 来源：2024-2025-1/20241105_1108/7.18.c
 * 编译模式：gnu99-textbook
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#include <stdio.h>
int main()
{
    int max();
    extern int A, B, C; // 把外部变量A,B,C的作用域扩展到从此处开始
    printf("Please enter three integer numbers:");
    scanf("%d %d %d", &A, &B, &C); // 输入3个整数给A,B,C
    printf("max is %d\n", max());
    return 0;
}
int A, B, C; // 定义外部变量A,B,C
int max()
{
    int m;
    m = A > B ? A : B; // 把A和B中的大者放在m中
    if (C > m)
        m = C;  // 将A,B,C三者中的大者放在m中
    return (m); // 返回m的值
}
