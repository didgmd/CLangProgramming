/*
 * 例程 ID：EX-C02-008
 * 标题：教材例程 2.4
 * 教材位置：第 2 章 / 2.4
 * 知识点：算法、流程控制、问题求解
 * 来源：2023-2024-1/02_Algorithm/ex2_4.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>

// 例2.4
int main()
{
	int sign = 1;	// S1
	int sum = 1;	// S2
	int deno = 2;	// S3
	int term;

	while (deno <= 100)
	{
		sign = (-1) * sign;		// S4
		term = sign * (1 / deno);	// S5
		sum = sum + term;		// S6
		deno = deno + 1;		// S7
	}

	printf("Final sum is %d\n", sum);

	return 0;
}
