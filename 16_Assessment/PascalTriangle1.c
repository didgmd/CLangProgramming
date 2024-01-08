#include <stdio.h>
#define N 7

int main()
{
    int a[N][N];

    for (int i = 2; i <= N - 1; i++)
    {
        for (int j = 1; j <= i + 1; j++)
        {
            if (j == 0 || j == i)
            {
                a[i][j] = 1;
                printf("%d\t", 1);
            }
            else
            {
                a[i][j] = a[i - 1][j - 1] + a[i - 1][j];
                printf("%d\t", a[i][j]);
            }
        }
        printf("\n");
    }
    return 0;
}