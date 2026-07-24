/*
 * 例程 ID：EX-C07-005
 * 标题：教材例程 7.5
 * 教材位置：第 7 章 / 7.5
 * 知识点：函数、参数、递归、变量作用域
 * 来源：2024-2025-1/20241105_1108/7.5.c
 * 编译模式：gnu99-textbook
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#include <stdio.h>
int main()
{
	int max4(int a, int b, int c, int d); // 对max4的函数声明
	int a, b, c, d, max;
	printf("Please enter 4 interger numbers:"); // 提示输入4个数
	scanf("%d %d %d %d", &a, &b, &c, &d);		// 输入4个数
	max = max4(a, b, c, d);						// 调用max4函数，得到4个数中的最大者
	printf("max=%d \n", max);					// 输出4个数中的最大者
	return 0;
}

int max4(int a, int b, int c, int d) // 定义max4函数
{
	int max2(int a, int b); // 对max2的函数声明
	int m;
	m = max2(a, b); // 调用max2函数，得到a和b中的大者，放在m中
	m = max2(m, c); // 调用max2函数，得到a,b,c中的大者，放在m中
	m = max2(m, d); // 调用max2函数，得到a,b,c,d中的大者，放在m中
	return (m);		// 把m作为函数值带回main函数
}

int max2(int a, int b) // 定义max2函数
{
	if (a >= b)
		return a; // 若a≥b，将a作为函数返回值
	else
		return b; // 若a<b，将b作为函数返回值
}
