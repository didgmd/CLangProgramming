#include <stdio.h>
#define N 7

int main()
{
    int n;
    int a[N][N];
    int i, j;

    for (i = 0; i < N; i++)
    {
        for (j = 0; j < N; j++)
        {
            if (i == 0)
            {
                printf("1\n");
            }
            else if (j == 0)
            {
                printf("1 ");
            }
            else
            {
                a[i][j] = a[i - 1][j - 1] + a[i - 1][j];
            }
        }
    }
    printf("%4d", a[i][j]);

    return 0;
}