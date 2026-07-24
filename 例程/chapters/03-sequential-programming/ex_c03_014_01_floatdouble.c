/*
 * 例程 ID：EX-C03-014
 * 标题：教材例程 custom-01_floatdouble
 * 教材位置：第 3 章 / custom-01_floatdouble
 * 知识点：数据类型、运算符、输入输出
 * 来源：2023-2024-1/03_Sequential/01_FloatDouble.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>

int main()
{
	double a = 2e-3;
	double b = 2e3;
	double c = 2e+3;
	float f = 3.5;

	printf("Size of a is %lu\n", (unsigned long)sizeof(a));
	printf("Size of f is %lu\n", (unsigned long)sizeof(f));

	printf("a = %lf, b = %lf, c = %lf, f = %f\n", a, b, c, f);

	double d = 3.1415926535897932384;
	float e = 3.1415926535897932384;

	printf("d = %lf, e = %f\n", d, e);

	return 0;
}
