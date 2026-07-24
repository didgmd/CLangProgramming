/*
 * 例程 ID：EX-C02-004
 * 标题：教材例程 2.2
 * 教材位置：第 2 章 / 2.2
 * 知识点：算法、流程控制、问题求解
 * 来源：2023-2024-1/02_Algorithm/ex2_2.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>

int main()
{
	printf("Hello World\n");

	int n[9] = {231, 232, 233, 234, 235, 236, 237, 238, 239};
	int g[9] = {78, 92, 85, 66, 74, 99, 78, 72, 87};

	int i;
	for (i = 0; i < 9; i++)
	{
		if (g[i] >= 80)
		{
			printf("Student No. is %d, grade is %d\n", n[i], g[i]);
		}
	}

	return 0;
}
