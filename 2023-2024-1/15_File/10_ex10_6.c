#define _CRT_SECURE_NO_WARNINGS 1
#include<stdio.h>
#include <stdlib.h>
struct Student_type	//学生数据类型
{
	char name[10];
	int num;
	int age;
	char addr[15];
}stud[10];
int main()
{
	int i;
	FILE* fp;
	if ((fp = fopen("stu.dat", "rb")) == NULL)	//以只读方式打开二进制文件
	{
		printf("can not open file\n");
		exit(0);
	}
	for (i = 0; i < 10; i += 2)
	{
		fseek(fp, i * sizeof(struct Student_type), 0);	//移动文件位置标记 
		fread(&stud[i], sizeof(struct Student_type), 1, fp);	//读一个数据块到结构体变量 
		printf("%-10s %4d %4d %-15s\n", stud[i].name, stud[i].num, stud[i].age, stud[i].addr);
		//在屏幕输出 
	}
	fclose(fp);
	return 0;
}
