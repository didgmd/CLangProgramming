/*
 * 例程 ID：EX-C06-011
 * 标题：教材例程 custom-09_diamondspause
 * 教材位置：第 6 章 / custom-09_diamondspause
 * 知识点：一维数组、二维数组、字符数组、字符串
 * 来源：2023-2024-1/08_Array/09_DiamondsPause.c
 * 编译模式：gnu99-textbook
 * 旧语法：system-pause
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#include <stdio.h>
#include <stdlib.h>

int main() {

	char diamonds[5][5] = { 
		{' ', ' ', '*'},
		{' ', '*', ' ', '*'},
		{'*', ' ', ' ', ' ', '*'},
		{' ', '*', ' ', '*'},
		{' ', ' ', '*'}};

	for (int i = 0; i <= 4; i++) {
		for (int j = 0; j <= 4; j++) {
			printf("%c", diamonds[i][j]);
		}
		printf("\n");
	}

	system("pause");

	return 0;
}
