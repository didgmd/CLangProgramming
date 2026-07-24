/*
 * 例程 ID：EX-C08-031
 * 标题：教材例程 custom-07_arrayoutput
 * 教材位置：第 8 章 / custom-07_arrayoutput
 * 知识点：指针、数组与指针、字符串指针、动态内存
 * 来源：2023-2024-1/11_Pointer/07_ArrayOutput.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>

int main() {

	int a[3] = { 1, 2, 3 };
	// 数组名不加索引时，本质上为地址（指针）
	printf("       a = %p\n", (void *)(a));// &a[0]
	printf("      *a = %d\n",  *a);			//  a[0]
	printf(" (a + 1) = %p\n", (void *)((a + 1)));// &a[1]
	printf("*(a + 1) = %d\n", *(a + 1));	//  a[1]
	printf(" (a + 2) = %p\n", (void *)((a + 2)));// &a[2]
	printf("*(a + 2) = %d\n", *(a + 2));	//  a[2]

	return 0;
}
