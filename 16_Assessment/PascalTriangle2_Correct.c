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
            if (j == 0 || j == i)
            {
                a[i][j] = 1;
            }
            else
            {
                a[i][j] = a[i - 1][j - 1] + a[i - 1][j];
            }
        }
    }

    for (i = 0; i < N; i++)
    {
        for (j = 0; j <= i; j++)
        {
            printf("%4d", a[i][j]);
        }
        printf("\n");
    }
    return 0;
}