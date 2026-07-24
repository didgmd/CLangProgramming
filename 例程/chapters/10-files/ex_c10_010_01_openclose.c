/*
 * 例程 ID：EX-C10-010
 * 标题：教材例程 custom-01_openclose
 * 教材位置：第 10 章 / custom-01_openclose
 * 知识点：文件、顺序读写、随机读写、错误检测
 * 来源：2023-2024-1/15_File/01_OpenClose.c
 * 编译模式：gnu99-textbook
 * 旧语法：msvc-crt-compat
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
#include <stdlib.h>

int main() {

	FILE* fp;
	
	fp = fopen("test.txt", "w");
	if (fp == NULL) {
		printf("Cannot open file\n");
		exit(0);
	}

	printf("Please enter a string to store in the disk (end with #): ");
	char ch = getchar();	// Get the first char
	while (ch != '#') {		// When input is not '#'
		fputc(ch, fp);		// Write the first char to the file
		ch = getchar();		// Get the next char
	}
	fclose(fp);

	fp = fopen("test.txt", "r");
	if (fp == NULL) {
		printf("Cannot open file\n");
		exit(0);
	}

	printf("The content of the file is: ");
	ch = fgetc(fp);			// Get the first char
	while (ch != EOF) {		// When input is not EOF
		putchar(ch);		// Print the first char
		ch = fgetc(fp);		// Get the next char
	}
	fclose(fp);

	return 0;
}
