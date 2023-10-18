#include <stdio.h>

int main()
{
	int a = 10;
	short int b = 20;
	long int c = 30;
	long long int d = 40;

	printf("Size of a is %d\n", sizeof(a));
	printf("Size of b is %d\n", sizeof(b));
	printf("Size of c is %d\n", sizeof(c));
	printf("Size of d is %d\n", sizeof(d));

	return 0;	
}