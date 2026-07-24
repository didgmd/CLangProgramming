/*
 * 例程 ID：EX-C07-004
 * 标题：教材例程 7.4
 * 教材位置：第 7 章 / 7.4
 * 知识点：函数、参数、递归、变量作用域
 * 来源：2024-2025-1/20241105_1108/7.4.c
 * 编译模式：gnu99-textbook
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#include <stdio.h>
int main()
{
	float add(float x, float y); // 对add函数作声明
	float a, b, c;
	printf("Please enter a and b:"); // 提示输入
	scanf("%f,%f", &a, &b);			 // 输入两个实数
	c = add(a, b);					 // 调用add函数
	printf("sum is %f\n", c);		 // 输出两数之和
	return 0;
}

float add(float x, float y) // 定义add函数
{
	float z;
	z = x + y;
	return (z); // 把变量z的值作为函数值返回
}
