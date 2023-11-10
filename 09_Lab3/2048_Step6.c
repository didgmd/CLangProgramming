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
    printf("欢迎来到2048游戏！\n使用 W, A, S, D 控制数字的移动。\n按 Q 退出游戏。\n");

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

void shiftLeft() {
    for (int i = 0; i < GRID_SIZE; i++) {
        int temp[GRID_SIZE] = { 0 };  // 临时存储合并结果的数组
        int tempIndex = 0;  // 临时数组的索引
        // 遍历当前行
        for (int j = 0; j < GRID_SIZE; j++) {
            if (grid[i][j] != 0) {
                if (temp[tempIndex] == 0) {
                    temp[tempIndex] = grid[i][j];
                }
                else if (temp[tempIndex] == grid[i][j]) {
                    temp[tempIndex++] *= 2;
                    score += temp[tempIndex - 1];  // 更新分数
                }
                else {
                    temp[++tempIndex] = grid[i][j];
                }
            }
        }
        // 使用临时数组更新网格的当前行
        for (int j = 0; j < GRID_SIZE; j++) {
            grid[i][j] = temp[j];
        }
    }
}

void shiftRight() {
    for (int i = 0; i < GRID_SIZE; i++) {
        int temp[GRID_SIZE] = { 0 };
        int tempIndex = GRID_SIZE - 1;
        for (int j = GRID_SIZE - 1; j >= 0; j--) {
            if (grid[i][j] != 0) {
                if (temp[tempIndex] == 0) {
                    temp[tempIndex] = grid[i][j];
                }
                else if (temp[tempIndex] == grid[i][j]) {
                    temp[tempIndex--] *= 2;
                    score += temp[tempIndex + 1];
                }
                else {
                    temp[--tempIndex] = grid[i][j];
                }
            }
        }
        for (int j = 0; j < GRID_SIZE; j++) {
            grid[i][j] = temp[j];
        }
    }
}

void shiftUp() {
    for (int j = 0; j < GRID_SIZE; j++) {
        int temp[GRID_SIZE] = { 0 };
        int tempIndex = 0;
        for (int i = 0; i < GRID_SIZE; i++) {
            if (grid[i][j] != 0) {
                if (temp[tempIndex] == 0) {
                    temp[tempIndex] = grid[i][j];
                }
                else if (temp[tempIndex] == grid[i][j]) {
                    temp[tempIndex++] *= 2;
                    score += temp[tempIndex - 1];
                }
                else {
                    temp[++tempIndex] = grid[i][j];
                }
            }
        }
        for (int i = 0; i < GRID_SIZE; i++) {
            grid[i][j] = temp[i];
        }
    }
}

void shiftDown() {
    for (int j = 0; j < GRID_SIZE; j++) {
        int temp[GRID_SIZE] = { 0 };
        int tempIndex = GRID_SIZE - 1;
        for (int i = GRID_SIZE - 1; i >= 0; i--) {
            if (grid[i][j] != 0) {
                if (temp[tempIndex] == 0) {
                    temp[tempIndex] = grid[i][j];
                }
                else if (temp[tempIndex] == grid[i][j]) {
                    temp[tempIndex--] *= 2;
                    score += temp[tempIndex + 1];
                }
                else {
                    temp[--tempIndex] = grid[i][j];
                }
            }
        }
        for (int i = 0; i < GRID_SIZE; i++) {
            grid[i][j] = temp[i];
        }
    }
}

void updateGame(char direction) {
    // 根据方向更新游戏状态
    switch (direction) {
    case 'a':
        shiftLeft();
        break;
    case 'd':
        shiftRight();
        break;
    case 'w':
        shiftUp();
        break;
    case 's':
        shiftDown();
        break;
    }
}

int isGameOver() {
    // 检查是否还有空位
    for (int i = 0; i < GRID_SIZE; i++) {
        for (int j = 0; j < GRID_SIZE; j++) {
            if (grid[i][j] == 0) {
                return 0; // 还有空位，游戏继续
            }
        }
    }

    // 检查是否还有可合并的相邻数字
    for (int i = 0; i < GRID_SIZE; i++) {
        for (int j = 0; j < GRID_SIZE; j++) {
            if (j < GRID_SIZE - 1 && grid[i][j] == grid[i][j + 1]) {
                return 0; // 水平方向上可合并，游戏继续
            }
            if (i < GRID_SIZE - 1 && grid[i][j] == grid[i + 1][j]) {
                return 0; // 垂直方向上可合并，游戏继续
            }
        }
    }

    return 1; // 没有空位且无法合并，游戏结束
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
            if (isGameOver()) {
                printf("游戏结束！您的得分是：%d\n", score);
                break;
            }
        }
    } while (input != 'q');

    printf("感谢您的游戏，再见！\n");
    return 0;
}
