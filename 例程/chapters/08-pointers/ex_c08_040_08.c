/*
 * 例程 ID：EX-C08-040
 * 标题：实验演示 lab5.8
 * 教材位置：第 8 章 / lab5.8
 * 知识点：指针、数组与指针、字符串指针、动态内存
 * 来源：2023-2024-1/14_Lab5/08.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
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
    int* ptr = &matrix[0][0];
    int res = printMatrix(ptr, 3, 3);
    printf("Sum of all elements: %d\n", res);

    return 0;
}
