// 打印杨辉三角的前n行
#include <stdio.h>
#define N 10
int main() {
    int a[N][N];
    int i, j;
    for (i = 0; i < N; i++) {
        a[i][0] = 1;
        a[i][i] = 1;
    }
    for (i = 2; i < N; i++) {
        for (j = 1; j < i; j++) {
            a[i][j] = a[i - 1][j - 1] + a[i - 1][j];
        }
    }
    for (i = 0; i < N; i++) {
        for (j = 0; j <= i; j++) {
            printf("%d ", a[i][j]);
        }
        printf("\n");
    }
    return 0;
}