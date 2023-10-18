#include <stdio.h>

int main() {
	int num1 = 5;

	for (int i = 31; i >= 0; i--)
	{
		int mask = 1 << i;
		int bit = ((num1 & mask) != 0);
		printf("%d", bit);
	}
	printf("\n");

	int num2 = -5;

	for (int i = 31; i >= 0; i--)
	{
		int mask = 1 << i;
		int bit = ((num2 & mask) != 0);
		printf("%d", bit);
	}
	printf("\n");

	return 0;
}
