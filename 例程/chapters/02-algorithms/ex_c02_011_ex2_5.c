/*
 * 例程 ID：EX-C02-011
 * 标题：教材例程 2.5
 * 教材位置：第 2 章 / 2.5
 * 知识点：算法、流程控制、问题求解
 * 来源：2023-2024-1/02_Algorithm/ex2_5.c
 * 编译模式：gnu99-textbook
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#include <stdio.h>
#include <math.h>

// 例2.5
int main()
{
	int n;
	printf("Please give a number for calculation: ");
	scanf("%d", &n);		// S1

	int i = 2;		// S2

	int sqrt_value = sqrt(n);

	int r;

	for (; i <= sqrt_value; i++)	// S5, S6
	{
		r = n % i;		// S3

		if (r == 0)		// S4
		{
			printf("%d 不是素数\n", n);
			return 0;
		}
	}

	printf("%d 是素数\n", n);

	return 0;
}
