/*
 * 例程 ID：EX-C02-012
 * 标题：教材例程 2.5_2.10
 * 教材位置：第 2 章 / 2.5_2.10
 * 知识点：算法、流程控制、问题求解
 * 来源：2024-2025-1/20240924/2.5_2.10.c
 * 编译模式：gnu99-textbook
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#include <stdio.h>
#include <math.h>

int main()
{
	int n;
	printf("Please give a number for prime number determination: ");
    scanf("%d", &n); // S1

    int i = 2; // S2
    int sqrt_value = sqrt(n);
	int r;

	while (i <= sqrt_value)	// S6
	{
		r = n % i;		// S3

		if (r == 0)		// S4
		{
			printf("%d is not a prime number due to the remainder of %d divided by %d is %d\n", n, n, i, r);
			return 0;
		}

        i = i + 1; // S5
	}

	printf("%d is a prime number\n", n);

	return 0;
}
