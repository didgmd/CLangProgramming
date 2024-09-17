#include <stdio.h>
#define N 7

int main()
{
    int a[N][N];
    int i, j;

    for (i = 0; i < N; i++)
    {
        j = N - i;
        while (j--)
        {
            printf(" ");
        }
        a[i][0] = 1;
        for (j = 0; j <= i; j++)
        {
            if (j == i)
            {
                a[i][j] = 1;
            }
            if (i > 1 && j >= 1)
            {
                a[i][j] = a[i - 1][j - 1] + a[i - 1][j];
            }
            printf("%4d\t", a[i][j]);
        }
        printf("\n");
    }

    return 0;
}