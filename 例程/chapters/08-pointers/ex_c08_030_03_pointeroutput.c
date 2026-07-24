/*
 * 例程 ID：EX-C08-030
 * 标题：教材例程 custom-03_pointeroutput
 * 教材位置：第 8 章 / custom-03_pointeroutput
 * 知识点：指针、数组与指针、字符串指针、动态内存
 * 来源：2023-2024-1/11_Pointer/03_PointerOutput.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>

int main() {

	int a = 10;
	int* p = &a;
	printf("八进制   Octonary    (OCT) 0o%o\n", *p);
	printf("八进制   Octonary    (OCT) 0o%16o\n", *p);
	printf("八进制   Octonary    (OCT) 0o%016o\n", *p);
	printf("十六进制 Hexadecimal (HEX) 0x%x\n", *p);
	printf("十六进制 Hexadecimal (HEX) 0x%16x\n", *p);
	printf("十六进制 Hexadecimal (HEX) 0x%016x\n", *p);
	printf("指针形式 Pointer           %p\n", (void *)p);

	return 0;
}
