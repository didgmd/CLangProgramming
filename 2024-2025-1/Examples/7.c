// 将字符串里小写字母改成大写字母，大写字母改成小写字母（eg：`6.2.2-4`）
#include <stdio.h>
void change(char *s)
{
    while (*s)
    {
        if (*s >= 'a' && *s <= 'z')
            *s = *s - 32;
        else if (*s >= 'A' && *s <= 'Z')
            *s = *s + 32;
        s++;
    }
}
int main()
{
    char a[100];
    printf("Please input the string:\n");
    gets(a);
    change(a);
    printf("\nThe changed string is %s", a);
    return 0;
}