// 求字符串的长度（100以下），要求用到指针
#include <stdio.h>
int length(char *s)
{
    char *p = s;
    while (*p)
        p++;
    return (p - s);
}

int length2(char *s)
{
    int j = 0;
    while (*s)
    {
        s++;
        j++;
    }
    return j;
}

int main()
{
    char a[100];
    int i;
    printf("Please input the string:\n");
    gets(a);
    i = length(a);
    printf("\nThe length of string is %d", i);

    return 0;
}