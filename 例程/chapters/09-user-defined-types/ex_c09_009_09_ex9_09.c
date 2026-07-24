/*
 * 例程 ID：EX-C09-009
 * 标题：教材例程 9.9
 * 教材位置：第 9 章 / 9.9
 * 知识点：结构体、枚举、链表、自定义数据类型
 * 来源：2023-2024-1/13_Structure/09_ex9_09.c
 * 编译模式：gnu99-textbook
 * 旧语法：msvc-crt-compat
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
#include <stdlib.h>
#define LEN sizeof(struct Student)
struct Student
{
	long num;
	float score;
	struct Student* next;
};
int n; 	//n为全局变量，本文件模块中各函数均可使用它
struct Student* creat(void)
	//定义函数。此函数返回一个指向链表头的指针
{
	struct Student* head;
	struct Student* p1, * p2;
	n = 0;
	p1 = p2 = (struct Student*)malloc(LEN);  //开辟一个新单元
	scanf("%ld,%f", &p1->num, &p1->score);
	//输入第1个学生的学号和成绩
	head = NULL;
	while (p1->num != 0)
	{
		n = n + 1;
		if (n == 1) head = p1;
		else p2->next = p1;
		p2 = p1;
		p1 = (struct Student*)malloc(LEN);
		//开辟动态存储区，把起始地址赋给p1
		scanf("%ld,%f", &p1->num, &p1->score);
		//输入其他学生的学号和成绩
	}
	p2->next = NULL;
	return(head);
}
int main()
{
	struct Student* pt;
	pt = creat(); 	//函数返回链表第一个结点的地址 
	printf("\nnum:%ld\nscore:%5.1f\n", pt->num, pt->score);
	//输出第1个结点的成员值
	return 0;
}
