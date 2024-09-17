#define _CRT_SECURE_NO_WARNINGS 1

#include <stdio.h>

// 定义图书结构体
struct Book {
    char title[50];
    char author[50];
};

// 显示所有图书信息
void display(struct Book* books, int n) {
    printf("图书信息:\n");
    for (int i = 0; i < n; i++) {
        printf("标题: %s, 作者: %s\n", (books + i)->title, (books + i)->author);
    }
}

int main() {
    struct Book books[10];  // 存储最多10本图书的数组
    int n = 0;  // 图书数量
    int choice;

    while (1) {
        printf("1. 添加图书信息\n");
        printf("2. 显示所有图书信息\n");
        printf("3. 退出\n");
        printf("请输入你的选择: ");
        scanf("%d", &choice);

        if (choice == 1) {
            printf("输入图书标题: ");
            scanf(" %[^\n]", books[n].title);
            printf("输入图书作者: ");
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
            printf("无效选择，请重试。\n");
        }
    }

    return 0;
}
