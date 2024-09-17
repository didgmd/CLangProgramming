#include <stdio.h>

int main()
{
	int a = 3;
	
	printf("Result of a is %d\n", a += a -= a * a);

	int b = -3;

	printf("Result of b is %d\n", b += b -= b * b);
	
	return 0;
}