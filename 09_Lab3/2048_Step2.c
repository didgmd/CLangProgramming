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

int main() {
    srand(time(NULL)); // Initialize random seed
    initializeGrid();
    addRandomNumber();
    addRandomNumber();
    drawGrid();

    return 0;
}
