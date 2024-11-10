#include <stdio.h>
int main()
{
    int *p, i, a[10];
    p = a; // p指向a[0]		①
    printf("please enter 10 integer numbers:");
    for (i = 0; i < 10; i++)
        scanf("%d", p++); // 输入10个整数给a[0]~a[9]
    for (i = 0; i < 10; i++, p++)
        printf("%d ", *p); // 想输出a[0]~a[9]	②
    printf("\n");
    return 0;
}
