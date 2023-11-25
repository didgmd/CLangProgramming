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
    // 初始化迷宫
    initializeMaze();
    // 生成迷宫路径
    generateMaze();
    // 打印迷宫
    printMaze();

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

// 打印迷宫
void printMaze() {
    for (int i = 0; i < HEIGHT; i++) {
        for (int j = 0; j < WIDTH; j++) {
            printf("%c", maze[i][j]);
        }
        printf("\n");
    }
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
