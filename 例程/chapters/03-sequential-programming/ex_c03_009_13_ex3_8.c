/*
 * 例程 ID：EX-C03-009
 * 标题：教材例程 3.8
 * 教材位置：第 3 章 / 3.8
 * 知识点：数据类型、运算符、输入输出
 * 来源：2023-2024-1/03_Sequential/13_ex3_8.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>

int main()
{
	char a = 'B', b = 'O', c = 'Y';	//定义3个字符变量并初始化

	putchar(a);						//向显示器输出字符B
	putchar(b);						//向显示器输出字符O
	putchar(c);						//向显示器输出字符Y
	putchar('\n');					//向显示器输出一个换行符
	
	return 0;
}
