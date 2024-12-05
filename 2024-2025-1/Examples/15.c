// 统计一个字符串中的字母、数字、空格和其它字符的个数
#include <stdio.h>
int main()
{
    char a[100];
    int i, letter = 0, digit = 0, space = 0, other = 0;
    printf("Please input the string:\n");
    gets(a);
    for (i = 0; a[i] != '\0'; i++)
    {
        if ((a[i] >= 'a' && a[i] <= 'z') || (a[i] >= 'A' && a[i] <= 'Z'))
            letter++;
        else if (a[i] >= '0' && a[i] <= '9')
            digit++;
        else if (a[i] == ' ')
            space++;
        else
            other++;
    }
    printf("The number of letter is %d\n", letter);
    printf("The number of digit is %d\n", digit);
    printf("The number of space is %d\n", space);
    printf("The number of other is %d\n", other);
    return 0;
}