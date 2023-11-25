#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <conio.h>

#define HEIGHT 10
#define WIDTH 10

char maze[HEIGHT][WIDTH];
int playerX, playerY;
int gameOver = 0;  // 新增游戏结束标志

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

// 玩家移动函数
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

        // 检查是否到达出口
        if (playerX == WIDTH - 1 && playerY == HEIGHT - 2) {
            gameOver = 1;
        }
    }
}

// 初始化迷宫
void initializeMaze() {
    for (int i = 0; i < HEIGHT; i++) {
        for (int j = 0; j < WIDTH; j++) {
            maze[i][j] = '#';  // 初始全部设置为墙壁
        }
    }
    // 设置入口和出口
    maze[1][0] = ' ';
    maze[HEIGHT - 2][WIDTH - 1] = ' ';
}

void generateMaze() {
    // 随机打开一些墙壁来形成路径
    srand(time(NULL));  // 初始化随机数生成器

    for (int i = 1; i < HEIGHT - 1; i++) {
        for (int j = 1; j < WIDTH - 1; j++) {
            if (rand() % 4 == 0) {  // 随机决定是否打开墙壁
                maze[i][j] = ' ';
            }
        }
    }
}

void printMaze() {
    system("cls"); // 清屏
    for (int i = 0; i < HEIGHT; i++) {
        for (int j = 0; j < WIDTH; j++) {
            if (i == playerY && j == playerX)
                printf("P");  // 显示玩家位置
            else
                printf("%c", maze[i][j]);
        }
        printf("\n");
    }
}
