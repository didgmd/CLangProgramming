#include <stdio.h>

// 例2.3
int main()
{
	int year = 2000;	// S1

	for (; year <= 2500; year++)	// S6
	{	
		if (year % 4 != 0)	// S2
		{
			printf("%d 不是闰年\n", year);
			continue;
		}
		else if (year % 100 != 0)	// S3
		{
			printf("%d 是闰年\n", year);
			continue;
		}
		else if (year % 400 == 0)	// S4
		{
			printf("%d 是闰年\n", year);
			continue;
		}
		
		printf("%d 不是闰年\n", year);	// S5
	}

	return 0;
}