/*
 * 例程 ID：EX-C09-016
 * 标题：实验演示 lab5.7
 * 教材位置：第 9 章 / lab5.7
 * 知识点：结构体、枚举、链表、自定义数据类型
 * 来源：2023-2024-1/14_Lab5/07.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>

#include <string.h>
struct Student {
    char name[50];
    int id;
    float score;
};

void printStudentInfo(struct Student* s) {
    printf("Name: %s\n", s->name);
    printf("ID: %d\n", s->id);
    printf("Score: %.2f\n", s->score);
}

int main() {
    struct Student student1;
    struct Student* ptr = &student1;

    strcpy(student1.name, "Alice");
    student1.id = 12345;
    student1.score = 95.5;

    printStudentInfo(ptr);

    return 0;
}
