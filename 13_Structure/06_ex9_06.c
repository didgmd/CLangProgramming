#include <stdio.h>
struct Student				//声明结构体类型struct Student
{
	int num;
	char name[20];
	char sex;
	int age;
};
struct Student stu[3] = { {10101,"Li Lin",'M',18},{10102,"Zhang Fang",'M',19},{10104,"Wang Min",'F',20} };
//定义结构体数组并初始化 
int main()
{
	struct Student* p;		//定义指向struct Student结构体变量的指针变量 
	printf(" No. Name        sex age\n");
	for (p = stu; p < stu + 3; p++)
		printf("%5d %-20s %2c %4d\n", p->num, p->name, p->sex, p->age);	//输出结果
	return 0;
}
