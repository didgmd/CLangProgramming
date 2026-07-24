/*
 * 例程 ID：EX-C04-004
 * 标题：教材例程 4.4
 * 教材位置：第 4 章 / 4.4
 * 知识点：if、switch、条件表达式
 * 来源：2024-2025-1/20241011_1015/4.4.c
 * 编译模式：gnu99-textbook
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#include <stdio.h>
int main()
{
    char ch;
    scanf("%c", &ch);
    ch = (ch >= 'A' && ch <= 'Z') ? (ch + 32) : ch;
    printf("%c\n", ch);
    return 0;
}
