// 已知一个数字字符串，求对应的整数
#include <stdio.h>
int main()
{
    char a[100];
    int i, sum = 0;
    printf("Please input the string:\n");
    gets(a);
    for (i = 0; a[i] != '\0'; i++)
    {
        sum = sum * 10 + a[i] - '0';
    }
    printf("The number is %d\n", sum);
    return 0;
}