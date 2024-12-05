// 复制字符串（不使用`string.h`），要求用到数组
#include <stdio.h>
void copy(char s1[], char s2[])
{
    int i = 0;
    while (s1[i])
    {
        s2[i] = s1[i];
        i++;
    }
    s2[i] = '\0';
}

int main()
{
    char a[100], b[100];
    printf("Please input the string:\n");
    gets(a);
    copy(a, b);
    printf("\nThe copied string is %s", b);
    return 0;
}