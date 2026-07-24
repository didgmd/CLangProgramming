/*
 * 例程 ID：EX-C06-012
 * 标题：教材例程 custom-10_string
 * 教材位置：第 6 章 / custom-10_string
 * 知识点：一维数组、二维数组、字符数组、字符串
 * 来源：2023-2024-1/08_Array/10_String.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>

int main() {
	char a[5] = "China";
	char b[6] = "China";

	for (int i = 0; i <= 4; i++) {
		printf("%c", a[i]);
	}

	printf("\n");

	printf("a: %s\n", a);
	printf("b: %s\n", b);

	return 0;
}
