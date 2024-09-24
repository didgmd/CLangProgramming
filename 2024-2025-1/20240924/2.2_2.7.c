#include <stdio.h>

int main()
{
    int n[50] = {0}; // n[0]~n[49]
    int g[50] = {0}; // g[0]~g[49]
    int i = 1;

    while (i <= 5)
    {
        scanf("%d", &n[i]);
        scanf("%d", &g[i]);
        printf("Add student number: %d, grade: %d\n", n[i], g[i]);
        i = i + 1;
    }

    i = 1;

    while (i <= 5)
    {
        if (g[i] >= 80)
        {
            printf("Student number: %d, grade: %d\n", n[i], g[i]);
        }
        i = i + 1;
    }

    return 0;
}