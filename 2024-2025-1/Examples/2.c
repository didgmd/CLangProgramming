// 二维数组矩阵转换
#include <stdio.h>
#define N 3
int main()
{
    int a[N][N], b[N][N];
    int i, j;
    printf("Please input the matrix:\n");
    for (i = 0; i < N; i++)
        for (j = 0; j < N; j++)
            scanf("%d", &a[i][j]);
    for (i = 0; i < N; i++)
        for (j = 0; j < N; j++)
            b[j][i] = a[i][j];
    printf("The transposed matrix is:\n");
    for (i = 0; i < N; i++)
    {
        for (j = 0; j < N; j++)
            printf("%d ", b[i][j]);
        printf("\n");
    }
    return 0;
}