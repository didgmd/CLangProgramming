#include <stdio.h>

int main()
{
	printf("Hello World\n");

	int n[9] = {231, 232, 233, 234, 235, 236, 237, 238, 239};
	int g[9] = {78, 92, 85, 66, 74, 99, 78, 72, 87};

	int i;
	for (i = 0; i < 9; i++)
	{
		if (g[i] >= 80)
		{
			printf("Student No. is %d, grade is %d\n", n[i], g[i]);
		}
	}

	return 0;
}