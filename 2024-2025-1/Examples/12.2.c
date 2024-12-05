// 学生的结构体类型包含学号、姓名、成绩，
// 将10个学生的成绩存入数组，然后按照选择排序的方法将他们按照从小到大的顺序排列
#include <stdio.h>
int main()
{
    struct student
    {
        int num;
        char name[20];
        float score;
    } a[10], t;
    int i, j, k;
    for (i = 0; i < 10; i++)
    {
        printf("input the \"num name score\" of student %d:", i + 1);
        scanf("%d %s %f", &a[i].num, a[i].name, &a[i].score);
    }

    // 选择排序
    for (i = 0; i < 9; i++)
    {
        k = i;
        for (j = i + 1; j < 10; j++)
        {
            if (a[j].score < a[k].score)
                k = j;
        }
        if (k != i)
        {
            t = a[i];
            a[i] = a[k];
            a[k] = t;
        }
    }
    for (i = 0; i < 10; i++)
    {
        printf("%d %s %f\n", a[i].num, a[i].name, a[i].score);
    }
    return 0;
}