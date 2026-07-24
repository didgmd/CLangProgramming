/*
 * 例程 ID：EX-C02-006
 * 标题：教材例程 2.3
 * 教材位置：第 2 章 / 2.3
 * 知识点：算法、流程控制、问题求解
 * 来源：2023-2024-1/02_Algorithm/ex2_3.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>

// 例2.3
int main()
{
	int year = 2000;	// S1

	for (; year <= 2500; year++)	// S6
	{	
		if (year % 4 != 0)	// S2
		{
			printf("%d 不是闰年\n", year);
			continue;
		}
		else if (year % 100 != 0)	// S3
		{
			printf("%d 是闰年\n", year);
			continue;
		}
		else if (year % 400 == 0)	// S4
		{
			printf("%d 是闰年\n", year);
			continue;
		}
		
		printf("%d 不是闰年\n", year);	// S5
	}

	return 0;
}
