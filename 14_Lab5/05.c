#include <stdio.h>

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
