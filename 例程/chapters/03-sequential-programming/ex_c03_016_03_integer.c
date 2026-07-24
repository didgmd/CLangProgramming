/*
 * 例程 ID：EX-C03-016
 * 标题：教材例程 custom-03_integer
 * 教材位置：第 3 章 / custom-03_integer
 * 知识点：数据类型、运算符、输入输出
 * 来源：2023-2024-1/03_Sequential/03_Integer.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>

int main()
{
	int a = 10;
	short int b = 20;
	long int c = 30;
	long long int d = 40;

	printf("Size of a is %lu\n", (unsigned long)sizeof(a));
	printf("Size of b is %lu\n", (unsigned long)sizeof(b));
	printf("Size of c is %lu\n", (unsigned long)sizeof(c));
	printf("Size of d is %lu\n", (unsigned long)sizeof(d));

	char f = 'a';
	printf("f is %c\n", f);
	printf("f is %d\n", f);

	return 0;	
}
