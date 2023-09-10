#include <stdio.h>

// 1*3*5*7*9*11
int main()
{
	int p = 1;					// S1
	int i = 3;					// S2

	for (; i <= 11; i = i + 2)	// S4, S5
	{
		p = p * i;				// S3
	}

	/*
	while (i <= 11)				// S5
	{
		p = p * i;				// S3
		i = i + 2;				// S4
	}
	*/

	printf("The result is %d\n", p);

	return 0;
}