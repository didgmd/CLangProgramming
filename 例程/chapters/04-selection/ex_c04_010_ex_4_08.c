/*
 * 例程 ID：EX-C04-010
 * 标题：教材例程 4.8
 * 教材位置：第 4 章 / 4.8
 * 知识点：if、switch、条件表达式
 * 来源：2023-2024-1/04_Selection/ex_4_08.c
 * 编译模式：gnu99-textbook
 * 旧语法：msvc-crt-compat
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#define _CRT_SECURE_NO_WARNINGS 1

#include <stdio.h>
int main()
{
	int year, leap;
	printf("enter year:");
	scanf("%d", &year);

	///* 第一种
	if (year % 4 == 0)
	{
		if (year % 100 == 0)
		{
			if (year % 400 == 0)
				leap = 1;
			else
				leap = 0;
		}
		else
			leap = 1;
	}
	else
		leap = 0;
	//*/

	/* 第二种
	if (year % 4 != 0)
		leap = 0;
	else if (year % 100 != 0)
		leap = 1;
	else if (year % 400 != 0)
		leap = 0;
	else
		leap = 1;
	*/

	/* 第三种
	if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0))
		leap = 1;
	else
		leap = 0;
	*/

	if (leap)
		printf("%d is ", year);
	else
		printf("%d is not ", year);
	printf("a leap year.\n");
	return 0;
}
