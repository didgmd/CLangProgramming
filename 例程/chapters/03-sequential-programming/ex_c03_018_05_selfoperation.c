/*
 * 例程 ID：EX-C03-018
 * 标题：教材例程 custom-05_selfoperation
 * 教材位置：第 3 章 / custom-05_selfoperation
 * 知识点：数据类型、运算符、输入输出
 * 来源：2023-2024-1/03_Sequential/05_SelfOperation.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>

int main()
{
	int i, j;
	
	for (i = 0; i < 10;)
	{
		printf("i = %d\n", i++);
	}

	for (j = 0; j < 10;)
	{
		printf("j = %d\n", ++j);
	}

	return 0;
}
