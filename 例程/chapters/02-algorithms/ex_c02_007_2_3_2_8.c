/*
 * 例程 ID：EX-C02-007
 * 标题：教材例程 2.3_2.8
 * 教材位置：第 2 章 / 2.3_2.8
 * 知识点：算法、流程控制、问题求解
 * 来源：2024-2025-1/20240924/2.3_2.8.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>

int main()
{
	int year = 2000; // S1

	while (year <= 2500)
	{
		if (year % 4 != 0) // S2
		{
			printf("%d is not a leap year\n", year); // Go to S6
		}
		else if (year % 100 != 0) // S3
		{
			printf("%d is a leap year\n", year); // Go to S6
		}
		else if (year % 400 == 0) // S4
		{
			printf("%d is a leap year\n", year); // Go to S6
		}
		else
		{
			// S5
			printf("%d is a not a leap year\n", year); // Go to S6
		}

		year = year + 1; // S6
	}

	return 0;
}
