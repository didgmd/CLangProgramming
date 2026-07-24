/*
 * 例程 ID：EX-C09-003
 * 标题：教材例程 9.3
 * 教材位置：第 9 章 / 9.3
 * 知识点：结构体、枚举、链表、自定义数据类型
 * 来源：2024-2025-1/20241119_1122/9.3.c
 * 编译模式：gnu99-textbook
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#include <string.h>
#include <stdio.h>
struct Person // 声明结构体类型struct Person
{
    char name[20];                             // 候选人姓名
    int count;                                 // 候选人得票数
} leader[3] = {{"Li", 0}, {"Zhang", 0}, {"Sun", 0}}; // 定义结构体数组并初始化

int main()
{
    int i, j;
    char leader_name[20]; // 定义字符数组
    for (i = 1; i <= 10; i++)
    {
        scanf("%s", leader_name); // 输入所选的候选人姓名
        for (j = 0; j < 3; j++)
            if (strcmp(leader_name, leader[j].name) == 0)
                leader[j].count++;
    }
    printf("\nResult:\n");
    for (i = 0; i < 3; i++)
        printf("%5s:%d\n", leader[i].name, leader[i].count);
    return 0;
}
