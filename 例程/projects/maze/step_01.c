/*
 * 例程 ID：PJ-MAZE-01
 * 标题：迷宫渐进项目：步骤 1
 * 教材位置：综合案例
 * 知识点：综合应用、渐进式开发
 * 来源：2023-2024-1/12_Lab4/Maze01.c
 * 编译模式：gnu99-textbook
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#include <stdio.h>
#include <stdlib.h>

// 定义迷宫大小
#define HEIGHT 10
#define WIDTH 10

// 迷宫数组
char maze[HEIGHT][WIDTH];

// 函数声明
void initializeMaze();
void printMaze();

int main() {
    // 初始化迷宫
    initializeMaze();

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
