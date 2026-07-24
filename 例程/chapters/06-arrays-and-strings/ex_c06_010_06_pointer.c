/*
 * 例程 ID：EX-C06-010
 * 标题：教材例程 custom-06_pointer
 * 教材位置：第 6 章 / custom-06_pointer
 * 知识点：一维数组、二维数组、字符数组、字符串
 * 来源：2023-2024-1/08_Array/06_Pointer.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>

int main() {
	int a[5] = { 1, 2, 3, 4, 5 };

	// 取址符 &
	// 输出数组 a 中所有元素的首地址
	printf("a[0] %p %d\n", (void *)(&(a[0])), *(&(a[0])));
	printf("a[1] %p\n", (void *)(&(a[1])));
	printf("a[2] %p\n", (void *)(&(a[2])));
	printf("a[3] %p\n", (void *)(&(a[3])));
	printf("a[4] %p\n", (void *)(&(a[4])));

	int b[3][3] = { {1, 2, 3,},{4, 5, 6},{7, 8, 9} };
	
	for (int i = 0; i <= 2; i++) {
		for (int j = 0; j <= 2; j++) {
			printf("b[%d][%d] %p %d\n", i, j, (void *)(&(b[i][j])), b[i][j]);
		}
	}

	return 0;
}
