// 已知某一天的年月日，求是当年的第几天，注意闰年问题
#include <stdio.h>
int main()
{
    int year, month, day, sum = 0;
    int monthday[13] = {0, 31, 28, 31, 30, 31, 30,
                        31, 31, 30, 31, 30, 31};
    printf("Please input the \"year month day\":\n");
    scanf("%d %d %d", &year, &month, &day);
    if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0)
        monthday[2] = 29;
    for (int i = 1; i < month; i++)
        sum += monthday[i];
    sum += day;
    printf("The day is the %dth day of the year.\n", sum);
    return 0;
}