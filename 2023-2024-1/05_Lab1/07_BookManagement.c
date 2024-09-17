#define _CRT_SECURE_NO_WARNINGS 1

#include <stdio.h>

// ����ͼ��ṹ��
struct Book {
    char title[50];
    char author[50];
};

// ��ʾ����ͼ����Ϣ
void display(struct Book* books, int n) {
    printf("ͼ����Ϣ:\n");
    for (int i = 0; i < n; i++) {
        printf("����: %s, ����: %s\n", (books + i)->title, (books + i)->author);
    }
}

int main() {
    struct Book books[10];  // �洢���10��ͼ�������
    int n = 0;  // ͼ������
    int choice;

    while (1) {
        printf("1. ���ͼ����Ϣ\n");
        printf("2. ��ʾ����ͼ����Ϣ\n");
        printf("3. �˳�\n");
        printf("���������ѡ��: ");
        scanf("%d", &choice);

        if (choice == 1) {
            printf("����ͼ�����: ");
            scanf(" %[^\n]", books[n].title);
            printf("����ͼ������: ");
            scanf(" %[^\n]", books[n].author);
            n++;
        }
        else if (choice == 2) {
            display(books, n);
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
