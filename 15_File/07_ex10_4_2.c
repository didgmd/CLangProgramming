#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
#include <stdlib.h>
#define SIZE 3
struct Student_type
{
	char name[10];
	int num;
	int age;
	char addr[15];
}stud[SIZE];

int main()
{
	int i;
	FILE* fp;
	if ((fp = fopen("stu.dat", "rb")) == NULL)	//打开输入文件stu.dat
	{
		printf("cannot open file\n");
		exit(0);
	}
	for (i = 0; i < SIZE; i++)
	{
		fread(&stud[i], sizeof(struct Student_type), 1, fp);	//从fp指向的文件读入一组数据
		printf("%-10s %4d %4d %-15s\n", stud[i].name, stud[i].num, stud[i].age, stud[i].addr);
		//在屏幕上输出这组数据 
	}
	fclose(fp);						//关闭文件stu_list
	return 0;
}
