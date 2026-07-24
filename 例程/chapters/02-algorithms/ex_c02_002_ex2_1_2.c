/*
 * 例程 ID：EX-C02-002
 * 标题：教材例程 2.1.2
 * 教材位置：第 2 章 / 2.1.2
 * 知识点：算法、流程控制、问题求解
 * 来源：2023-2024-1/02_Algorithm/ex2_1_2.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>

// 1*3*5*7*9*11
int main()
{
	int p = 1;					// S1
	int i = 3;					// S2

	for (; i <= 11; i = i + 2)	// S4, S5
	{
		p = p * i;				// S3
	}

	/*
	while (i <= 11)				// S5
	{
		p = p * i;				// S3
		i = i + 2;				// S4
	}
	*/

	printf("The result is %d\n", p);

	return 0;
}
