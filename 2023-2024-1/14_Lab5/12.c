#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
#include <string.h>

// ����ѧ���ṹ��
struct Student {
    char name[50];
    int id;
    float score;
};

// ��������
void addStudent(struct Student students[], int* count);
void findStudent(struct Student students[], int count);
void displayAllStudents(struct Student students[], int count);
float calculateAverageScore(struct Student students[], int count);

int main() {
    struct Student students[100]; // ѧ�����飬���洢100��ѧ����Ϣ
    int count = 0; // ѧ������

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

// ���ѧ����Ϣ
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

// ����ѧ����Ϣ
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

// ��ʾ����ѧ����Ϣ
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

// ����ƽ���ɼ�
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
