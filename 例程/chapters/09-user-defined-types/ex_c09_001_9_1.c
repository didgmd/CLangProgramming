/*
 * 例程 ID：EX-C09-001
 * 标题：教材例程 9.1
 * 教材位置：第 9 章 / 9.1
 * 知识点：结构体、枚举、链表、自定义数据类型
 * 来源：2024-2025-1/20241119_1122/9.1.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：deterministic
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>
int main()
{
    struct Student // 声明结构体类型struct Student
    {
        long int num; // 以下4行为结构体的成员
        char name[20];
        char sex;
        char addr[20];
    } a = {10101, "Li Lin", 'M', "123 Beijing Road"}; // 定义结构体变量a并初始化
    printf("NO.:%ld\nname:%s\nsex:%c\naddress:%s\n", a.num, a.name, a.sex, a.addr);
    return 0;
}
