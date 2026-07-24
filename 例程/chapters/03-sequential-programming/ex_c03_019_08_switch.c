/*
 * 例程 ID：EX-C03-019
 * 标题：教材例程 custom-08_switch
 * 教材位置：第 3 章 / custom-08_switch
 * 知识点：数据类型、运算符、输入输出
 * 来源：2023-2024-1/03_Sequential/08_Switch.c
 * 编译模式：gnu99-textbook
 * 旧语法：msvc-crt-compat
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>

int main()
{
	int a;

	printf("请问你想去几层？\n");

	scanf("%d", &a);

	switch (a)
	{
		case 1:
			printf("去第一层\n");
			break;
		case 2:
			printf("去第二层\n");
			break;
		case 3:
			printf("去第三层\n");
			break;
		case 4:
			printf("去第四层\n");
			break;
		default:
			printf("没有这个楼层\n");
			break;
	}

	return 0;
}
