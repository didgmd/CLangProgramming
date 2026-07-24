/*
 * 例程 ID：EX-C09-014
 * 标题：实验演示 lab5.5
 * 教材位置：第 9 章 / lab5.5
 * 知识点：结构体、枚举、链表、自定义数据类型
 * 来源：2023-2024-1/14_Lab5/05.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>

#include <string.h>
// 定义一个结构体类型 Student
struct Student {
    char name[50];  // 学生姓名
    int age;        // 学生年龄
    float score;    // 学生成绩
};

int main() {
    // 创建一个 Student 结构体变量并初始化
    struct Student student1;
    strcpy(student1.name, "Alice");
    student1.age = 20;
    student1.score = 85.5;

    // 打印学生信息
    printf("学生姓名: %s\n", student1.name);
    printf("学生年龄: %d\n", student1.age);
    printf("学生成绩: %.2f\n", student1.score);

    return 0;
}
