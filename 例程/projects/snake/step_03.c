/*
 * 例程 ID：PJ-SNAKE-03
 * 标题：贪吃蛇渐进项目：步骤 3
 * 教材位置：综合案例
 * 知识点：综合应用、渐进式开发
 * 来源：2023-2024-1/07_Lab2/Snake_Step3.c
 * 编译模式：gnu99-textbook
 * 旧语法：conio、getch
 * 交互方式：manual
 * 兼容性：Windows 专属例程：依赖 conio.h 或即时按键接口。
 */
#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

int width = 20;
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

void Draw() {
    system("cls");
    for (int i = 0; i < width + 2; i++)
        printf("#");
    printf("\n");

    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
            if (j == 0)
                printf("#");
            if (i == y && j == x)
                printf("O");
            else if (i == fruitY && j == fruitX)
                printf("*");
            else {
                int print = 0;
                for (int k = 0; k < nTail; k++) {
                    if (tailX[k] == j && tailY[k] == i) {
                        printf("o");
                        print = 1;
                    }
                }
                if (!print)
                    printf(" ");
            }

            if (j == width - 1)
                printf("#");
        }
        printf("\n");
    }

    for (int i = 0; i < width + 2; i++)
        printf("#");
    printf("\n");
    printf("Score: %d\n", score);
}

void Input() {
    if (_kbhit()) {
        switch (_getch()) {
        case 'a':
            x--;
            break;
        case 'd':
            x++;
            break;
        case 'w':
            y--;
            break;
        case 's':
            y++;
            break;
        case 'x':
            gameOver = 1;
            break;
        }
    }
}

int main() {
    Setup();
    while (!gameOver) {
        Draw();
        Input();
    }

    return 0;
}
