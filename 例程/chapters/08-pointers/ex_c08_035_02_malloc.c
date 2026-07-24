/*
 * 例程 ID：EX-C08-035
 * 标题：实验演示 lab1-02_malloc
 * 教材位置：第 8 章 / lab1-02_malloc
 * 知识点：指针、数组与指针、字符串指针、动态内存
 * 来源：2023-2024-1/05_Lab1/02_Malloc.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>
#include <stdlib.h>

int main()
{
	int* a = (int*)malloc(sizeof(int));
	int b = 10;
	a = &b;

	printf("%d\n", *a);
	printf("%p\n", (void *)(a));

	free(a);

	return 0;
}
