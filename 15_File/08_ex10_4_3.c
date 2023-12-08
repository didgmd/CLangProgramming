#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
#define SIZE 3
struct Student_type
{
	char name[10];
	int num;
	int age;
	char addr[15];
}stud[SIZE];	//定义全局结构体数组stud，包含10个学生数据

void load()
{
	FILE* fp;
	int i;
	if ((fp = fopen("stu.dat", "rb")) == NULL) //打开输入文件stu.dat
	{
		printf("cannot open infile\n");
		return;
	}
	for (i = 0; i < SIZE; i++)
		if (fread(&stud[i], sizeof(struct Student_type), 1, fp) != 1)
			//从stu.dat文件中读数据
		{
			if (feof(fp))	//如果文件结束，则关闭文件并返回
			{
				fclose(fp);
				return;
			}
			printf("file read error\n");
		}
	fclose(fp);
}

void save()	//定义函数save，向文件输出SIZE个学生的数据
{
	FILE* fp;
	int i;
	if ((fp = fopen("stu2.dat", "wb")) == NULL)	//打开输出文件stu2.dat
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
	load();
	save();
	return 0;
}
