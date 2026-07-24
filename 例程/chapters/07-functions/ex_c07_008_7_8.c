/*
 * 例程 ID：EX-C07-008
 * 标题：教材例程 7.8
 * 教材位置：第 7 章 / 7.8
 * 知识点：函数、参数、递归、变量作用域
 * 来源：2024-2025-1/20241105_1108/7.8.c
 * 编译模式：gnu99-textbook
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#include <stdio.h>
int main()
{
    void hanoi(int n, char one, char two, char three);
    // 对hanoi函数的声明
    int m;
    printf("input the number of diskes:");
    scanf("%d", &m);
    printf("The step to move %d diskes:\n", m);
    hanoi(m, 'A', 'B', 'C');
}

void hanoi(int n, char one, char two, char three) // 定义hanoi函数
// 将n个盘从one座借助two座,移到three座
{
    void move(char x, char y); // 对move函数的声明
    if (n == 1)
        move(one, three);
    else
    {
        hanoi(n - 1, one, three, two);
        move(one, three);
        hanoi(n - 1, two, one, three);
    }
}
void move(char x, char y) // 定义move函数
{
    printf("%c->%c\n", x, y);
}
