#include <stdio.h>
int main()
{
    int i;
    int f[20] = {1, 1}; // 对最前面两个元素f[0]和f[1]赋初值1
    for (i = 2; i < 20; i++)
        f[i] = f[i - 2] + f[i - 1]; // 先后求出f[2]~f[19]的值
    for (i = 0; i < 20; i++)
    {
        if (i % 5 == 0)
            printf("\n");     // 控制每输出5个数后换行
        printf("%12d", f[i]); // 输出一个数
    }
    printf("\n");
    return 0;
}