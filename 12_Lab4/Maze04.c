#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <conio.h>

#define HEIGHT 10
#define WIDTH 10

char maze[HEIGHT][WIDTH];
int playerX, playerY;
int gameOver = 0;  // ������Ϸ������־

void initializeMaze();
void printMaze();
void generateMaze();
void movePlayer(char direction);

int main() {
    initializeMaze();
    generateMaze();
    playerX = 1; playerY = 0;
    printMaze();

    while (!gameOver) {
        if (_kbhit()) {
            char key = _getch();
            movePlayer(key);
        }
    }

    printf("Congratulations! You've escaped the maze.\n");
    return 0;
}

// ����ƶ�����
void movePlayer(char direction) {
    int newX = playerX, newY = playerY;
    switch (direction) {
    case 'w': newY--; break;
    case 's': newY++; break;
    case 'a': newX--; break;
    case 'd': newX++; break;
    }

    if (newX >= 0 && newX < WIDTH && newY >= 0 && newY < HEIGHT && maze[newY][newX] == ' ') {
        playerX = newX;
        playerY = newY;
        printMaze();

        // ����Ƿ񵽴����
        if (playerX == WIDTH - 1 && playerY == HEIGHT - 2) {
            gameOver = 1;
        }
    }
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
