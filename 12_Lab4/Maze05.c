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

int breakWallCount = 0; // 全局变量，用于记录破墙次数
char lastMoveDirection = ' '; // 记录玩家最后一次移动的方向

void breakWall() {
    int wallX = playerX, wallY = playerY;
    // 根据玩家当前面对的方向来确定破墙位置
    switch (lastMoveDirection) {
    case 'w': wallY--; break;
    case 's': wallY++; break;
    case 'a': wallX--; break;
    case 'd': wallX++; break;
    default: return; // 如果没有移动方向，不执行破墙操作
    }

    // 检查并执行破墙操作
    if (wallX >= 0 && wallX < WIDTH && wallY >= 0 && wallY < HEIGHT && maze[wallY][wallX] == '#') {
        maze[wallY][wallX] = ' ';
        breakWallCount++; // 增加破墙次数
    }
}

// 玩家移动函数
void movePlayer(char direction) {
    int newX = playerX, newY = playerY;
    if (direction != ' ') { // 记录除空格键外的最后一次移动方向
        lastMoveDirection = direction;
    }

    switch (direction) {
    case 'w': newY--; break;
    case 's': newY++; break;
    case 'a': newX--; break;
    case 'd': newX++; break;
    case ' ': // 破墙操作
        breakWall();
        printMaze(); // 更新迷宫显示
        return; // 直接返回，不移动玩家位置
    }

    // 检查新位置是否有效
    if (newX >= 0 && newX < WIDTH && newY >= 0 && newY < HEIGHT && maze[newY][newX] == ' ') {
        playerX = newX;
        playerY = newY;
        printMaze(); // 更新迷宫显示

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
    printf("破墙次数: %d\n", breakWallCount); // 显示破墙次数
}