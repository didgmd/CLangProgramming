/*
 * 例程 ID：EX-C03-015
 * 标题：教材例程 custom-02_decocthex
 * 教材位置：第 3 章 / custom-02_decocthex
 * 知识点：数据类型、运算符、输入输出
 * 来源：2023-2024-1/03_Sequential/02_DecOctHex.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>

int main()
{
	int a = 10;		// 十进制
	int b = 010;	// 八进制
	int c = 0x10;	// 十六进制

	printf("a = %d, b = %d, c = %d\n", a, b, c);

	return 0;
}
