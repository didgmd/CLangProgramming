/*
 * 例程 ID：EX-C02-009
 * 标题：教材例程 2.4-class
 * 教材位置：第 2 章 / 2.4-class
 * 知识点：算法、流程控制、问题求解
 * 来源：2023-2024-1/02_Algorithm/ex2_4(课上).c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>

int main()
{
	printf("Hello World\n");

	int sign = 1;
	float term;			// 当前项的值
	float sum = 0.0;	// 和
	int deno;			// 分母

	for (deno = 1; deno <= 10; deno++)
	{
		term = 1.0 / deno;
		//printf("Term is %f\n", term);
		sum = sum + sign * term;
		//printf("sum is %f\n", sum);
		sign = (-1) * sign;
		printf("Deno is %d, Sum is %f\n", deno, sum);
	}

	printf("Sum is %f\n", sum);

	return 0;
}
