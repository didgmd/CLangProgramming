#include <stdio.h>
#include <stdlib.h>

int main()
{
	int* a = (int*)malloc(sizeof(int));
	int b = 10;
	a = &b;

	printf("%d\n", *a);
	printf("%p\n", a);

	free(a);

	return 0;
}