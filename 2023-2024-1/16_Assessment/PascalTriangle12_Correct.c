#include <stdio.h>
#define N 7

int main()
{
    int coef = 1, i, j;

    for (i = 0; i < N; i++)
    {
        for (j = 0; j < i; j++)
        {
            if (j == 0 || i == 0)
            {
                coef = 1;
            }
            else
            {
                coef = coef * (i - j) / j;
            }
            printf("%4d", coef);
        }
        printf("\n");
    }

    return 0;
}