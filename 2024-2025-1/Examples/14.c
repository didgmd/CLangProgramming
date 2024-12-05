// 求100~200之间的素数
#include <stdio.h>
#include <math.h>
int main()
{
    int i, n, k;
    for (n = 101; n <= 200; n = n + 2)
    {
        k = sqrt(n);
        for (i = 2; i <= k; i++)
            if (n % i == 0)
                break;
        if (i >= k + 1)
            printf("%d ", n);
    }
    return 0;
}