#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define HEIGHT 10
#define WIDTH 10

char maze[HEIGHT][WIDTH];

void initializeMaze();
void printMaze();
void generateMaze();

int main() {
    // ��ʼ���Թ�
    initializeMaze();
    // �����Թ�·��
    generateMaze();
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
