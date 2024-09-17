#include <stdio.h>
#define N 7

int main()
{
    int a[N][N];
    int i, j;

    for (i = 0; i < N; i++)
    {
        a[1][0] = 1;
        a[i][i] = 1;
    }

    for (i = 0; i < N; i++)
    {
        for (j = 0; j <= i; j++)
        {
            a[i][j] = a[i][j - 1] + a[i - 1][j - 1];
        }
    }

    for (j = 0; j <= N; j++)
    {
        a[0][j] = 1;
        a[j][j] = 1;
    }

    for (i = 0; i < N; i++)
        for (j = 0; j <= i; j++)
            printf("%4d/t", a[i][j]);

    return 0;
}