/*
 * 例程 ID：PJ-2048-03
 * 标题：2048 渐进项目：步骤 3
 * 教材位置：综合案例
 * 知识点：综合应用、渐进式开发
 * 来源：2023-2024-1/09_Lab3/2048_Step3.c
 * 编译模式：gnu99-textbook
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define GRID_SIZE 4

int grid[GRID_SIZE][GRID_SIZE];
int score;

void initializeGrid() {
    for (int i = 0; i < GRID_SIZE; i++) {
        for (int j = 0; j < GRID_SIZE; j++) {
            grid[i][j] = 0;
        }
    }
    score = 0;
}

void addRandomNumber() {
    int empty = 0;
    for (int i = 0; i < GRID_SIZE; i++)
        for (int j = 0; j < GRID_SIZE; j++)
            if (grid[i][j] == 0)
                empty++;

    if (empty == 0) return; // No empty space

    int randPos = rand() % empty;
    int count = 0;
    for (int i = 0; i < GRID_SIZE; i++) {
        for (int j = 0; j < GRID_SIZE; j++) {
            if (grid[i][j] == 0) {
                if (count == randPos) {
                    grid[i][j] = (rand() % 2 + 1) * 2; // Place 2 or 4
                    return;
                }
                count++;
            }
        }
    }
}

void drawGrid() {
    system("cls");

    for (int i = 0; i < GRID_SIZE; i++) {
        for (int j = 0; j < GRID_SIZE; j++) {
            if (grid[i][j] == 0) printf(".\t");
            else printf("%d\t", grid[i][j]);
        }
        printf("\n");
    }
    printf("Score: %d\n", score);
}

char processInput() {
    char ch;
    ch = getchar();
    while ((ch != 'w') && (ch != 'a') && (ch != 's') && (ch != 'd') && (ch != 'q')) {
        ch = getchar();
    }
    return ch;
}

void updateGame(char direction) {
    (void)direction;
    // 根据方向更新游戏状态
    // 此函数将在后续步骤中实现
}

int main() {
    srand(time(NULL)); // Initialize random seed
    initializeGrid();
    addRandomNumber();
    addRandomNumber();
    drawGrid();

    char input;
    do {
        input = processInput();
        if (input != 'q') {
            updateGame(input);
            addRandomNumber(); // 在有效移动后添加新数字
            drawGrid();
        }
    } while (input != 'q');

    return 0;
}
