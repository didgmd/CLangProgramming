#include <stdio.h>
#include <math.h>

int main()
{
	int n;
	printf("Please give a number for prime number determination: ");
    scanf("%d", &n); // S1

    int i = 2; // S2
    int sqrt_value = sqrt(n);
	int r;

	while (i <= sqrt_value)	// S6
	{
		r = n % i;		// S3

		if (r == 0)		// S4
		{
			printf("%d is not a prime number due to the remainder of %d divided by %d is %d\n", n, n, i, r);
			return 0;
		}

        i = i + 1; // S5
	}

	printf("%d is a prime number\n", n);

	return 0;
}