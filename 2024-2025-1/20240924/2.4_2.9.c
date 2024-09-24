#include <stdio.h>

int main()
{
    int sign = 1; // S1
    int sum = 1;  // S2
    int deno = 2; // S3
    int term;

    while (deno <= 100)
    {
        sign = (-1) * sign;       // S4
        term = sign * (1 / deno); // S5
        sum = sum + term;         // S6
        deno = deno + 1;          // S7
    }

    printf("Final sum is %d\n", sum);

    return 0;
}