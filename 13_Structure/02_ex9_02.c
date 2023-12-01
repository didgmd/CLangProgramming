#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
int main()
{
	struct Student			//声明结构体类型struct Student 
	{
		int num;
		char name[20];
		float score;
	}student1, student2;	//定义两个结构体变量student1,student2 
	scanf("%d%s%f", &student1.num, student1.name, &student1.score);	//输入学生1的数据
	scanf("%d%s%f", &student2.num, student2.name, &student2.score);	//输入学生1的数据
	printf("The higher score is:\n");
	if (student1.score > student2.score)
		printf("%d  %s  %6.2f\n", student1.num, student1.name, student1.score);
	else if (student1.score < student2.score)
		printf("%d  %s  %6.2f\n", student2.num, student2.name, student2.score);
	else
	{
		printf("%d  %s  %6.2f\n", student1.num, student1.name, student1.score);
		printf("%d  %s  %6.2f\n", student2.num, student2.name, student2.score);
	}
	return 0;
}
