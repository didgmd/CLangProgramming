// 学生的结构体类型包含学号、姓名、成绩，
// 将10个学生的成绩存入数组，然后按照冒泡排序的方法将他们按照从小到大的顺序排列
#include <stdio.h>
int main()
{
    struct student
    {
        int num;
        char name[20];
        float score;
    } a[10], t;
    int i, j;
    for (i = 0; i < 10; i++)
    {
        printf("input the \"num name score\" of student %d:", i + 1);
        scanf("%d %s %f", &a[i].num, a[i].name, &a[i].score);
    }

    // 冒泡排序
    for (i = 0; i < 9; i++)
    {
        for (j = 0; j < 9 - i; j++)
        {
            if (a[j].score > a[j + 1].score)
            {
                t = a[j];
                a[j] = a[j + 1];
                a[j + 1] = t;
            }
        }
    }
    for (i = 0; i < 10; i++)
    {
        printf("%d %s %f\n", a[i].num, a[i].name, a[i].score);
    }
    return 0;
}
