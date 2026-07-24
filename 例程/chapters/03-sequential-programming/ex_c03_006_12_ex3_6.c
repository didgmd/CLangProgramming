/*
 * 例程 ID：EX-C03-006
 * 标题：教材例程 3.6
 * 教材位置：第 3 章 / 3.6
 * 知识点：数据类型、运算符、输入输出
 * 来源：2023-2024-1/03_Sequential/12_ex3_6.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>
int main()
{
	double a = 1.0;

	printf("%f\n", a / 3);
	printf("%20.15f\n", a / 3);

	return 0;
}
