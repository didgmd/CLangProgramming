#include <stdio.h>

int main()
{
	printf("Hello World\n");

	int sign = 1;
	float term;			// ��ǰ���ֵ
	float sum = 0.0;	// ��
	int deno;			// ��ĸ

	for (deno = 1; deno <= 10; deno++)
	{
		term = 1.0 / deno;
		//printf("Term is %f\n", term);
		sum = sum + sign * term;
		//printf("sum is %f\n", sum);
		sign = (-1) * sign;
		printf("Deno is %d, Sum is %f\n", deno, sum);
	}

	printf("Sum is %f\n", sum);

	return 0;
}