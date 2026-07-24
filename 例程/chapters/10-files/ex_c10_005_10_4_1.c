/*
 * 例程 ID：EX-C10-005
 * 标题：教材例程 10.4.1
 * 教材位置：第 10 章 / 10.4.1
 * 知识点：文件、顺序读写、随机读写、错误检测
 * 来源：2024-2025-1/20241129/10.4.1.c
 * 编译模式：gnu99-textbook
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#include <stdio.h>
#define SIZE 10
struct Student_type
{
    char name[10];
    int num;
    int age;
    char addr[15];
} stud[SIZE]; // 定义全局结构体数组stud，包含10个学生数据

void save() // 定义函数save，向文件输出SIZE个学生的数据
{
    FILE *fp;
    int i;
    if ((fp = fopen("stu.dat", "wb")) == NULL) // 打开输出文件stu.dat
    {
        printf("cannot open file\n");
        return;
    }
    for (i = 0; i < SIZE; i++)
        if (fwrite(&stud[i], sizeof(struct Student_type), 1, fp) != 1)
            printf("file write error\n");
    fclose(fp);
}

int main()
{
    int i;
    printf("Please enter data of students:\n");
    for (i = 0; i < SIZE; i++)
        // 输入SIZE个学生的数据，存放在数组stud中
        scanf("%s%d%d%s", stud[i].name, &stud[i].num,
              &stud[i].age, stud[i].addr);
    save();
    return 0;
}
