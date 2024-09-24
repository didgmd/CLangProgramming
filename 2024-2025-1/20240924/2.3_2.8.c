#include <stdio.h>

int main()
{
	int year = 2000; // S1

	while (year <= 2500)
	{
		if (year % 4 != 0) // S2
		{
			printf("%d is not a leap year\n", year); // Go to S6
		}
		else if (year % 100 != 0) // S3
		{
			printf("%d is a leap year\n", year); // Go to S6
		}
		else if (year % 400 == 0) // S4
		{
			printf("%d is a leap year\n", year); // Go to S6
		}
		else
		{
			// S5
			printf("%d is a not a leap year\n", year); // Go to S6
		}

		year = year + 1; // S6
	}

	return 0;
}