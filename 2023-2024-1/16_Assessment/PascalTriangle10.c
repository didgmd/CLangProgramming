#include <stdio.h>
#define N 7

int main()
{
    int a[N][N];
    int i, j;

    for (i = 0; i < N; i++)
    {
        for (j = 0; j <= i; j++)
        {
            a[i][1] = 1;
            a[i][i] = 1;
            if (j >= 1 && j < i - 1)
            {
                a[i][j] = a[i - 1][j - 1] + a[i - 1][j];
            }

            if (j > i)
            {
                a[i][j] = "/t";
            }
            printf("%4d/t", a[i][j]);

            if (i == j)
                printf("\n");
        }
    }

    return 0;
}