/*
 * 例程 ID：EX-C04-005
 * 标题：教材例程 4.5
 * 教材位置：第 4 章 / 4.5
 * 知识点：if、switch、条件表达式
 * 来源：2023-2024-1/04_Selection/ex_4_05.c
 * 编译模式：gnu99-textbook
 * 旧语法：msvc-crt-compat
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#define _CRT_SECURE_NO_WARNINGS 1

#include <stdio.h>
int main()
{
	int x, y;
	scanf("%d", &x);
	if (x < 0)
		y = -1;
	else
		if (x == 0) y = 0;
		else y = 1;
	printf("x=%d,y=%d\n", x, y);
	return 0;
}
