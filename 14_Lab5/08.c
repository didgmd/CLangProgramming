#include <stdio.h>

int printMatrix(int* ptr, int rows, int cols) {
    int sum = 0;
    int k = 0;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            printf("%d ", ptr[k]);
            sum += ptr[k];
            k++;
        }
        printf("\n");
    }
    return sum;
}

int main() {
    int matrix[3][3] = { {1, 2, 3}, {4, 5, 6}, {7, 8, 9} };
    int* ptr = matrix;
    int res = printMatrix(ptr, 3, 3);
    printf("Sum of all elements: %d\n", res);

    return 0;
}
