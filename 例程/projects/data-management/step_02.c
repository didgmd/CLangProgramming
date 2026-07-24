/*
 * 例程 ID：PJ-DATA-02
 * 标题：数据管理案例：步骤 2
 * 教材位置：综合案例
 * 知识点：综合应用、渐进式开发
 * 来源：2023-2024-1/05_Lab1/06_StudentManagement.c
 * 编译模式：gnu99-textbook
 * 旧语法：msvc-crt-compat
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#define _CRT_SECURE_NO_WARNINGS 1

#include <stdio.h>

// 定义学生结构体
struct Student {
    char name[52];
    int score;
};

// 显示所有学生信息
void display(struct Student* students, int n) {
    printf("学生信息:\n");
    for (int i = 0; i < n; i++) {
        printf("姓名: %s, 成绩: %d\n", (students + i)->name, (students + i)->score);
        // printf("%p\n", students);
        // printf("%p, %p\n", &(students + i)->name, &(students + i)->score);
    }
}

int main() {
    struct Student students[10];  // 存储最多10名学生的数组
    int n = 0;  // 学生数量
    int choice;

    while (1) {
        printf("1. 添加学生信息\n");
        printf("2. 显示所有学生信息\n");
        printf("3. 退出\n");
        printf("请输入你的选择: ");
        scanf("%d", &choice);

        if (choice == 1) {
            printf("输入学生姓名: ");
            scanf(" %[^\n]", students[n].name);
            printf("输入学生成绩: ");
            scanf("%d", &students[n].score);
            n++;
        }
        else if (choice == 2) {
            display(students, n);
        }
        else if (choice == 3) {
            break;
        }
        else {
            printf("无效选择，请重试。\n");
        }
    }

    return 0;
}
