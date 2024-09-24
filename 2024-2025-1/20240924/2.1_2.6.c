#include <stdio.h>

int main()
{
    // 1 * 2 * 3 * 4 * 5
    int p = 1;
    int i = 2;

    while (i <= 5) 
    {
        printf("p is %d, i is %d\n", p, i);
        p = p * i;  // S3
        i = i + 1;  // S4
    }

    return 0;
}