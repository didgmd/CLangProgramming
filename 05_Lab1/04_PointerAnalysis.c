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
	printf("address of a is %p\n", &a);
	printf("content of p is %d\n", *p);
	printf("value   of p is %p\n", p);
	printf("address of p is %p\n", &p);

	printf("\n");

	int array[10];
	printf("address of array    is %p\n", &array);
	printf("address of array[0] is %p\n", &array[0]);
	printf("address of array[1] is %p\n", &array[1]);
	printf("address of array[2] is %p\n", &array[2]);
	printf("address of array[3] is %p\n", &array[3]);
	printf("address of array[5] is %p\n", &array[5]);
	printf("address of array[7] is %p\n", &array[7]);
	printf("address of array[9] is %p\n", &array[9]);

	printf("\n");

	struct sContext_t sContext;
	printf("size of sContext           is %d\n", sizeof(sContext));
	printf("size of sContext.a (int)   is %d\n", sizeof(sContext.a));
	printf("size of sContext.b (char)  is %d\n", sizeof(sContext.b));
	printf("size of sContext.c (char*) is %d\n", sizeof(sContext.c));
	printf("size of sContext.d (int)   is %d\n", sizeof(sContext.d));
	printf("size of sContext.e (short) is %d\n", sizeof(sContext.e));

	printf("\n");

	printf("address of sContext           is %p\n", &sContext);
	printf("address of sContext.a (int)   is %p\n", &sContext.a);
	printf("address of sContext.b (char)  is %p\n", &sContext.b);
	printf("address of sContext.c (char*) is %p\n", &sContext.c);
	printf("address of sContext.d (int)   is %p\n", &sContext.d);
	printf("address of sContext.e (short) is %p\n", &sContext.e);

	return 0;

}