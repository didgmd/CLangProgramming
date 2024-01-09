#include <stdio.h>
#define N 7

int main()
{
    int a[N][N];
    int i, j;

    for (i = 0; i < N - 1; i++)
    {
        a[i][0] = 1;
        for (j = 0; j <= i; j++)
        {
            a[i][j] = a[i - 1][j - 1] + a[i - 1][j];
            if (j == i)
            {
                a[i][j] = 1;
            }
            printf("%4d\n", a[i][j]);
        }
    }

    return 0;
}