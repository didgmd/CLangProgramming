#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <conio.h>  // 用于检测键盘输入

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
    playerX = 1; playerY = 0; // 设置玩家初始位置为迷宫入口
    printMaze(); // 初始打印迷宫

    while (1) { // 游戏主循环
        if (_kbhit()) { // 检查键盘输入
            char key = _getch();
            movePlayer(key);
        }
    }

    return 0;
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

void movePlayer(char direction) {
    // 计算新位置
    int newX = playerX, newY = playerY;
    switch (direction) {
        case 'w': newY--; break;
        case 's': newY++; break;
        case 'a': newX--; break;
        case 'd': newX++; break;
    }

    // 检查新位置是否有效
    if (newX >= 0 && newX < WIDTH && newY >= 0 && newY < HEIGHT && maze[newY][newX] == ' ') {
        playerX = newX;
        playerY = newY;
        printMaze(); // 在玩家移动后更新迷宫显示
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
