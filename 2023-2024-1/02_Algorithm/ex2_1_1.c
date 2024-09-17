#include <stdio.h>

// 1*2*3*4*5
int main()
{
	int p = 1;					// S1
	int i = 2;					// S2
	
	for (; i <= 5; i++)			// S4, S5
	{
		p = p * i;				// S3
	}

	/*
	while (i <= 5)				// S5
	{
		p = p * i;				// S3
		i++;					// S4
	}
	*/

	printf("The result is %d\n", p);

	return 0;
}