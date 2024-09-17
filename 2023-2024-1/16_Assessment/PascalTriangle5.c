#include <stdio.h>
#define N 7

int main()
{
    int a[N][N];
    int i, j;

    a[0][0] = 1;

    for (i = 0; i < N; i++)
    {
        for (j = 0; j <= i; j++)
        {
            if (i >= 2 && j >= 1) {
                a[i][j] = a[i - 1][j - 1] + a[i - 1][j];
            }
            else
            {
                a[i][j] = 1;
            }
        }
    }
    for (i = 0; i < N; i++)
        for (j = 0; j <= i; j++)
            printf("%4d\n", a[i][j]);

    return 0;
}