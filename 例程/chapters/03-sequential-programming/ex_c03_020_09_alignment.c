/*
 * 例程 ID：EX-C03-020
 * 标题：教材例程 custom-09_alignment
 * 教材位置：第 3 章 / custom-09_alignment
 * 知识点：数据类型、运算符、输入输出
 * 来源：2023-2024-1/03_Sequential/09_Alignment.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>

int main()
{
	int a = 10;

	printf("a = %4d, a = %-4d,\n", a, a);
	printf("a = %-4d, a = %4d\n", a, a);
	
	printf("a = %d, a = %-d\n", a, a);
	printf("a = %-d, a = %d\n", a, a);

	return 0;
}
