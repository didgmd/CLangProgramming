/*
 * 例程 ID：PJ-MAZE-02
 * 标题：迷宫渐进项目：步骤 2
 * 教材位置：综合案例
 * 知识点：综合应用、渐进式开发
 * 来源：2023-2024-1/12_Lab4/Maze02.c
 * 编译模式：gnu99-textbook
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
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
