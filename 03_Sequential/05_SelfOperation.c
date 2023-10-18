#include <stdio.h>

int main()
{
	int i, j;
	
	for (i = 0; i < 10;)
	{
		printf("i = %d\n", i++);
	}

	for (j = 0; j < 10;)
	{
		printf("j = %d\n", ++j);
	}

	return 0;
}