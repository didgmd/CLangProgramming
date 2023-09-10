#include <stdio.h>
#include <math.h>

// 例2.5
int main()
{
	int n;
	printf("Please give a number for calculation: ");
	scanf_s("%d", &n);		// S1

	int i = 2;		// S2

	int sqrt_value = sqrt(n);

	int r;

	for (; i <= sqrt_value; i++)	// S5, S6
	{
		r = n % i;		// S3

		if (r == 0)		// S4
		{
			printf("%d 不是素数\n", n);
			return 0;
		}
	}

	printf("%d 是素数\n", n);

	return 0;
}