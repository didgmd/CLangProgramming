/*
 * 例程 ID：EX-C04-009
 * 标题：教材例程 4.7
 * 教材位置：第 4 章 / 4.7
 * 知识点：if、switch、条件表达式
 * 来源：2024-2025-1/20241011_1015/4.7.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>
int main()
{
    void action1(int, int), action2(int, int); // 函数声明
    char ch;
    int a = 15, b = 23;
    ch = getchar();
    switch (ch)
    {
    case 'a':
    case 'A':
        action1(a, b);
        break; // 调用action1函数，执行A操作
    case 'b':
    case 'B':
        action2(a, b);
        break;                     // 调用action2函数，执行B操作
    default:
        putchar('\a'); // 如果输入其他字符，发出警告
    }
    return 0;
}

void action1(int x, int y) // 执行加法的函数
{
    printf("x+y=%d\n", x + y);
}

void action2(int x, int y) // 执行乘法的函数
{
    printf("x*y=%d\n", x * y);
}
