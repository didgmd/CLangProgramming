#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <conio.h>  // ���ڼ���������

#define HEIGHT 10
#define WIDTH 10

char maze[HEIGHT][WIDTH];
int playerX, playerY;

void initializeMaze();
void printMaze();
void generateMaze();
void movePlayer(char direction);

int main() {
    initializeMaze();
    generateMaze();
    playerX = 1; playerY = 0; // ������ҳ�ʼλ��Ϊ�Թ����
    printMaze(); // ��ʼ��ӡ�Թ�

    while (1) { // ��Ϸ��ѭ��
        if (_kbhit()) { // ����������
            char key = _getch();
            movePlayer(key);
        }
    }

    return 0;
}

// ��ʼ���Թ�
void initializeMaze() {
    for (int i = 0; i < HEIGHT; i++) {
        for (int j = 0; j < WIDTH; j++) {
            maze[i][j] = '#';  // ��ʼȫ������Ϊǽ��
        }
    }
    // ������ںͳ���
    maze[1][0] = ' ';
    maze[HEIGHT - 2][WIDTH - 1] = ' ';
}

void generateMaze() {
    // �����һЩǽ�����γ�·��
    srand(time(NULL));  // ��ʼ�������������

    for (int i = 1; i < HEIGHT - 1; i++) {
        for (int j = 1; j < WIDTH - 1; j++) {
            if (rand() % 4 == 0) {  // ��������Ƿ��ǽ��
                maze[i][j] = ' ';
            }
        }
    }
}

void movePlayer(char direction) {
    // ������λ��
    int newX = playerX, newY = playerY;
    switch (direction) {
        case 'w': newY--; break;
        case 's': newY++; break;
        case 'a': newX--; break;
        case 'd': newX++; break;
    }

    // �����λ���Ƿ���Ч
    if (newX >= 0 && newX < WIDTH && newY >= 0 && newY < HEIGHT && maze[newY][newX] == ' ') {
        playerX = newX;
        playerY = newY;
        printMaze(); // ������ƶ�������Թ���ʾ
    }
}

void printMaze() {
    system("cls"); // ����
    for (int i = 0; i < HEIGHT; i++) {
        for (int j = 0; j < WIDTH; j++) {
            if (i == playerY && j == playerX)
                printf("P");  // ��ʾ���λ��
            else
                printf("%c", maze[i][j]);
        }
        printf("\n");
    }
}
