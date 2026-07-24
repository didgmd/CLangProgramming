/*
 * 例程 ID：EX-C08-018
 * 标题：教材例程 8.13.1
 * 教材位置：第 8 章 / 8.13.1
 * 知识点：指针、数组与指针、字符串指针、动态内存
 * 来源：2023-2024-1/11_Pointer/21_ex_8_13_1.c
 * 编译模式：gnu99-textbook
 * 旧语法：msvc-crt-compat
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
int main()
{
	int a[3][4] = {{1, 3, 5, 7}, {9, 11, 13, 15}, {17, 19, 21, 23}};		//定义二维数组a并初始化
	int(*p)[4], i, j;			//指针变量p指向包含4个整型元素的一维数组
	p = a;					//p指向二维数组的0行
	printf("please enter row and colum:");
	scanf("%d,%d", &i, &j);	//输入要求输出的元素的行列号
	printf("a[%d,%d]=%d\n", i, j, *(*(p + i) + j));			//输出a[i][j]的值
	return 0;
}
