/*
 * 例程 ID：EX-C08-027
 * 标题：教材例程 8.20.2
 * 教材位置：第 8 章 / 8.20.2
 * 知识点：指针、数组与指针、字符串指针、动态内存
 * 来源：2024-2025-1/20241112_1115/8.20.2.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>
int main()
{
    void copy_string(char from[], char to[]); // 函数声明
    char a[] = "I am a teacher.";             // 定义字符数组a并初始化
    char b[] = "You are a student.";          // 定义字符数组b并初始化
    char *from = a, *to = b;                  // from指向a数组首元素，to指向b数组首元素
    printf("string a=%s\nstring b=%s\n", a, b);
    printf("copy string a to string b:\n");
    copy_string(from, to); // 实参为字符指针变量
    printf("\nstring a=%s\nstring b=%s\n", a, b);
    return 0;
}
void copy_string(char from[], char to[]) // 形参为字符数组
{
    int i = 0;
    while (from[i] != '\0')
    {
        to[i] = from[i];
        i++;
    }
    to[i] = '\0';
}
