/*
 * 例程 ID：PJ-SNAKE-01
 * 标题：贪吃蛇渐进项目：步骤 1
 * 教材位置：综合案例
 * 知识点：综合应用、渐进式开发
 * 来源：2023-2024-1/07_Lab2/Snake_Step1.c
 * 编译模式：gnu99-textbook
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#include <stdio.h>
#include <stdlib.h>

int width = 20;  // 注释
int height = 20;
int gameOver;
int x, y, fruitX, fruitY, score;
int tailX[100], tailY[100];
int nTail;

void Setup() {
    gameOver = 0;
    x = width / 2;
    y = height / 2;
    fruitX = rand() % width;
    fruitY = rand() % height;
    score = 0;
}

int main() {
    Setup();

    return 0;
}
