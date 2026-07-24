/*
 * 例程 ID：EX-C08-036
 * 标题：实验演示 lab1-04_pointeranalysis
 * 教材位置：第 8 章 / lab1-04_pointeranalysis
 * 知识点：指针、数组与指针、字符串指针、动态内存
 * 来源：2023-2024-1/05_Lab1/04_PointerAnalysis.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>

struct sContext_t {
	int a;
	char b;
	char* c;
	int d;
	short e;
};

int main() {

	int a = 10;
	int *p = &a;	// 传统格式
	//int* p = &a;	// 新版Visual Studio格式

	printf("value   of a is %d\n", a);
	printf("address of a is %p\n", (void *)(&a));
	printf("content of p is %d\n", *p);
	printf("value   of p is %p\n", (void *)(p));
	printf("address of p is %p\n", (void *)(&p));

	printf("\n");

	int array[10];
	printf("address of array    is %p\n", (void *)(&array));
	printf("address of array[0] is %p\n", (void *)(&array[0]));
	printf("address of array[1] is %p\n", (void *)(&array[1]));
	printf("address of array[2] is %p\n", (void *)(&array[2]));
	printf("address of array[3] is %p\n", (void *)(&array[3]));
	printf("address of array[5] is %p\n", (void *)(&array[5]));
	printf("address of array[7] is %p\n", (void *)(&array[7]));
	printf("address of array[9] is %p\n", (void *)(&array[9]));

	printf("\n");

	struct sContext_t sContext;
	printf("size of sContext           is %lu\n", (unsigned long)sizeof(sContext));
	printf("size of sContext.a (int)   is %lu\n", (unsigned long)sizeof(sContext.a));
	printf("size of sContext.b (char)  is %lu\n", (unsigned long)sizeof(sContext.b));
	printf("size of sContext.c (char*) is %lu\n", (unsigned long)sizeof(sContext.c));
	printf("size of sContext.d (int)   is %lu\n", (unsigned long)sizeof(sContext.d));
	printf("size of sContext.e (short) is %lu\n", (unsigned long)sizeof(sContext.e));

	printf("\n");

	printf("address of sContext           is %p\n", (void *)(&sContext));
	printf("address of sContext.a (int)   is %p\n", (void *)(&sContext.a));
	printf("address of sContext.b (char)  is %p\n", (void *)(&sContext.b));
	printf("address of sContext.c (char*) is %p\n", (void *)(&sContext.c));
	printf("address of sContext.d (int)   is %p\n", (void *)(&sContext.d));
	printf("address of sContext.e (short) is %p\n", (void *)(&sContext.e));

	return 0;

}
