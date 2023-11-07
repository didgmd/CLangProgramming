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