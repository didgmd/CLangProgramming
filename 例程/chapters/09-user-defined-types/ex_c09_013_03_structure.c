/*
 * 例程 ID：EX-C09-013
 * 标题：实验演示 lab1-03_structure
 * 教材位置：第 9 章 / lab1-03_structure
 * 知识点：结构体、枚举、链表、自定义数据类型
 * 来源：2023-2024-1/05_Lab1/03_Structure.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>
#include <stdlib.h>

struct student
{
    int id;
    char name;
    char sex;
    int age;
    int score;
};	// 注意最后有一个分号

int main()
{
    struct student stu;
    struct student *pStu;

    pStu = (struct student *)malloc(sizeof(struct student));
    if (pStu == NULL) {
		printf("Memory allocation failed\n");
		exit(1);
    }

    printf("%p\n", (void *)(&stu));
    stu.id = 123;
    stu.name = 'a';
    stu.sex = 'm';
    stu.age = 20;
    stu.score = 95;

    printf("%p\n", (void *)(pStu));
    pStu->id = 321;
    pStu->name = 'A';
    pStu->sex = 'f';
    pStu->age = 20;
    pStu->score = 96;

    free(pStu);

    return 0;
}
