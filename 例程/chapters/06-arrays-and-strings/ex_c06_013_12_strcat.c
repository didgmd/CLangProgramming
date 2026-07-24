/*
 * 例程 ID：EX-C06-013
 * 标题：教材例程 custom-12_strcat
 * 教材位置：第 6 章 / custom-12_strcat
 * 知识点：一维数组、二维数组、字符数组、字符串
 * 来源：2023-2024-1/08_Array/12_strcat.c
 * 编译模式：gnu99-textbook
 * 旧语法：msvc-crt-compat
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
#include <string.h>

int main() {

	char str1[30] = { "People's Republic of " };
	char str2[] = { "China" };
	strcat(str1, str2);
	printf("%s\n", str1);
	// printf("%s\n", strcat(str1, str2));


	return 0;
}
