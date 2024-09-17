#include <stdio.h>
#include <stdlib.h>

// �����Թ���С
#define HEIGHT 10
#define WIDTH 10

// �Թ�����
char maze[HEIGHT][WIDTH];

// ��������
void initializeMaze();
void printMaze();

int main() {
    // ��ʼ���Թ�
    initializeMaze();

    // ��ӡ�Թ�
    printMaze();

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

// ��ӡ�Թ�
void printMaze() {
    for (int i = 0; i < HEIGHT; i++) {
        for (int j = 0; j < WIDTH; j++) {
            printf("%c", maze[i][j]);
        }
        printf("\n");
    }
}