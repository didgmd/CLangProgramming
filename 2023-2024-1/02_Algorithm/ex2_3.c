#include <stdio.h>

// ��2.3
int main()
{
	int year = 2000;	// S1

	for (; year <= 2500; year++)	// S6
	{	
		if (year % 4 != 0)	// S2
		{
			printf("%d ��������\n", year);
			continue;
		}
		else if (year % 100 != 0)	// S3
		{
			printf("%d ������\n", year);
			continue;
		}
		else if (year % 400 == 0)	// S4
		{
			printf("%d ������\n", year);
			continue;
		}
		
		printf("%d ��������\n", year);	// S5
	}

	return 0;
}