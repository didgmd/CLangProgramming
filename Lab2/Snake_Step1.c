#include <stdio.h>
#include <stdlib.h>

int width = 20;  // ×¢ÊÍ
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