/*
 * 例程 ID：EX-C03-017
 * 标题：教材例程 custom-04_complement
 * 教材位置：第 3 章 / custom-04_complement
 * 知识点：数据类型、运算符、输入输出
 * 来源：2023-2024-1/03_Sequential/04_Complement.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>

int main() {
	int num1 = 5;

	for (int i = 31; i >= 0; i--)
	{
		int mask = 1 << i;
		int bit = ((num1 & mask) != 0);
		printf("%d", bit);
	}
	printf("\n");

	int num2 = -5;

	for (int i = 31; i >= 0; i--)
	{
		int mask = 1 << i;
		int bit = ((num2 & mask) != 0);
		printf("%d", bit);
	}
	printf("\n");

	return 0;
}
