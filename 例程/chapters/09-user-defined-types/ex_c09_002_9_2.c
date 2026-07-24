/*
 * 例程 ID：EX-C09-002
 * 标题：教材例程 9.2
 * 教材位置：第 9 章 / 9.2
 * 知识点：结构体、枚举、链表、自定义数据类型
 * 来源：2024-2025-1/20241119_1122/9.2.c
 * 编译模式：gnu99-textbook
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#include <stdio.h>
int main()
{
    struct Student // 声明结构体类型struct Student
    {
        int num;
        char name[20];
        float score;
    } student1, student2;                                           // 定义两个结构体变量student1,student2
    scanf("%d%s%f", &student1.num, student1.name, &student1.score); // 输入学生1的数据
    scanf("%d%s%f", &student2.num, student2.name, &student2.score); // 输入学生1的数据
    printf("The higher score is:\n");
    if (student1.score > student2.score)
        printf("%d  %s  %6.2f\n", student1.num, student1.name, student1.score);
    else if (student1.score < student2.score)
        printf("%d  %s  %6.2f\n", student2.num, student2.name, student2.score);
    else
    {
        printf("%d  %s  %6.2f\n", student1.num, student1.name, student1.score);
        printf("%d  %s  %6.2f\n", student2.num, student2.name, student2.score);
    }
    return 0;
}
