/*
 * 例程 ID：PJ-DATA-04
 * 标题：数据管理案例：步骤 4
 * 教材位置：综合案例
 * 知识点：综合应用、渐进式开发
 * 来源：2023-2024-1/14_Lab5/12.c
 * 编译模式：gnu99-textbook
 * 旧语法：msvc-crt-compat
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
#include <string.h>

// 定义学生结构体
struct Student {
    char name[50];
    int id;
    float score;
};

// 函数声明
void addStudent(struct Student students[], int* count);
void findStudent(struct Student students[], int count);
void displayAllStudents(struct Student students[], int count);
float calculateAverageScore(struct Student students[], int count);

int main() {
    struct Student students[100]; // 学生数组，最多存储100个学生信息
    int count = 0; // 学生数量

    int choice;
    do {
        printf("\nStudent Grade Management System\n");
        printf("1. Add Student\n");
        printf("2. Find Student\n");
        printf("3. Display All Students\n");
        printf("4. Calculate Average Score\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
        case 1:
            addStudent(students, &count);
            break;
        case 2:
            findStudent(students, count);
            break;
        case 3:
            displayAllStudents(students, count);
            break;
        case 4:
            printf("Average Score: %.2f\n", calculateAverageScore(students, count));
            break;
        case 5:
            printf("Exiting program.\n");
            break;
        default:
            printf("Invalid choice. Please try again.\n");
            break;
        }
    } while (choice != 5);

    return 0;
}

// 添加学生信息
void addStudent(struct Student students[], int* count) {
    if (*count < 100) {
        struct Student newStudent;
        printf("Enter student name: ");
        scanf("%s", newStudent.name);
        printf("Enter student ID: ");
        scanf("%d", &newStudent.id);
        printf("Enter student score: ");
        scanf("%f", &newStudent.score);

        students[*count] = newStudent;
        (*count)++;
        printf("Student added successfully.\n");
    }
    else {
        printf("Cannot add more students. Student database is full.\n");
    }
}

// 查找学生信息
void findStudent(struct Student students[], int count) {
    int searchId;
    printf("Enter student ID to find: ");
    scanf("%d", &searchId);

    for (int i = 0; i < count; i++) {
        if (students[i].id == searchId) {
            printf("Student found:\n");
            printf("Name: %s\n", students[i].name);
            printf("ID: %d\n", students[i].id);
            printf("Score: %.2f\n", students[i].score);
            return;
        }
    }

    printf("Student not found.\n");
}

// 显示所有学生信息
void displayAllStudents(struct Student students[], int count) {
    if (count == 0) {
        printf("No students in the database.\n");
    }
    else {
        printf("All students:\n");
        for (int i = 0; i < count; i++) {
            printf("Student %d:\n", i + 1);
            printf("Name: %s\n", students[i].name);
            printf("ID: %d\n", students[i].id);
            printf("Score: %.2f\n", students[i].score);
        }
    }
}

// 计算平均成绩
float calculateAverageScore(struct Student students[], int count) {
    if (count == 0) {
        return 0.0;
    }

    float totalScore = 0.0;
    for (int i = 0; i < count; i++) {
        totalScore += students[i].score;
    }

    return totalScore / count;
}
