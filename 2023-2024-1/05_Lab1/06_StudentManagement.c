#define _CRT_SECURE_NO_WARNINGS 1

#include <stdio.h>

// ����ѧ���ṹ��
struct Student {
    char name[52];
    int score;
};

// ��ʾ����ѧ����Ϣ
void display(struct Student* students, int n) {
    printf("ѧ����Ϣ:\n");
    for (int i = 0; i < n; i++) {
        printf("����: %s, �ɼ�: %d\n", (students + i)->name, (students + i)->score);
        // printf("%p\n", students);
        // printf("%p, %p\n", &(students + i)->name, &(students + i)->score);
    }
}

int main() {
    struct Student students[10];  // �洢���10��ѧ��������
    int n = 0;  // ѧ������
    int choice;

    while (1) {
        printf("1. ���ѧ����Ϣ\n");
        printf("2. ��ʾ����ѧ����Ϣ\n");
        printf("3. �˳�\n");
        printf("���������ѡ��: ");
        scanf("%d", &choice);

        if (choice == 1) {
            printf("����ѧ������: ");
            scanf(" %[^\n]", students[n].name);
            printf("����ѧ���ɼ�: ");
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
            printf("��Чѡ�������ԡ�\n");
        }
    }

    return 0;
}
