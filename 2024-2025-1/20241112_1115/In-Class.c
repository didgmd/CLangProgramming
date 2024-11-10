#include <stdio.h>

void main()
{
    int c[4][5] = {{1, 2, 3, 4, 5}, {6, 7, 8, 9, 10}, {11, 12, 13, 14, 15}, {16, 17, 18, 19, 20}};
    int(*cp)[5];
    cp = c;
    printf("%d\n", *cp[2] + 3);   // 14
    printf("%d\n", *(c + 2)[0]);  // 11
    printf("%d\n", *(cp + 2)[0]); // 11
    printf("%d\n", *cp[2]);       // 11
    printf("%d\n", (*cp)[2]);     // 3
    printf("%d\n", (*cp)[12]);    // 13
    printf("%d\n", *(*cp + 2));   // 3
}