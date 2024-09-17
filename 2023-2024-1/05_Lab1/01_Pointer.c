#include <stdio.h>

int main()
{
	int a = 10;

	printf("%d\n", a);
	printf("%p\n", &a);

	int* b = &a;

	printf("%p\n", b);
	printf("%p\n", &b);
	printf("%d\n", *b);

	return 0;
}