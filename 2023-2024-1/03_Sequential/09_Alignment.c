#include <stdio.h>

int main()
{
	int a = 10;

	printf("a = %4d, a = %-4d,\n", a, a);
	printf("a = %-4d, a = %4d\n", a, a);
	
	printf("a = %d, a = %-d\n", a, a);
	printf("a = %-d, a = %d\n", a, a);

	return 0;
}