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

void shiftLeft() {
    for (int i = 0; i < GRID_SIZE; i++) {
        int temp[GRID_SIZE] = { 0 };  // ��ʱ�洢�ϲ����������
        int tempIndex = 0;  // ��ʱ���������
        // ������ǰ��
        for (int j = 0; j < GRID_SIZE; j++) {
            if (grid[i][j] != 0) {
                if (temp[tempIndex] == 0) {
                    temp[tempIndex] = grid[i][j];
                }
                else if (temp[tempIndex] == grid[i][j]) {
                    temp[tempIndex++] *= 2;
                    score += temp[tempIndex - 1];  // ���·���
                }
                else {
                    temp[++tempIndex] = grid[i][j];
                }
            }
        }
        // ʹ����ʱ�����������ĵ�ǰ��
        for (int j = 0; j < GRID_SIZE; j++) {
            grid[i][j] = temp[j];
        }
    }
}

void updateGame(char direction) {
    // ���ݷ��������Ϸ״̬
    switch (direction) {
    case 'a':
        shiftLeft();
        break;
        // ʵ������������߼�
    }
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
            addRandomNumber(); // ����Ч�ƶ������������
            drawGrid();
        }
    } while (input != 'q');

    return 0;
}
