#define N 7         
#include <stdio.h>  // 1
void main()
{
    int a[N][N];    // 1
    int i, j;
    for (i = 0; i < N; i++) // 1
    {
        a[i][0] = 1;    // 1
        a[i][i] = 1;
    }

    for (i = 2; i < N; i++)     // 1
        for (j = 1; j < i; j++) // 1
            a[i][j] = a[i - 1][j] + a[i - 1][j - 1]; // 1

    for (i = 0; i < N; i++)         // 1
    {
        for (j = 0; j <= i; j++)    // 1
            printf("%6d", a[i][j]); // 1
        printf("\n");
    }
}
