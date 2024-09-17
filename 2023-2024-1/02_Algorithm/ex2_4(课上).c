#include <stdio.h>

int main()
{
	printf("Hello World\n");

	int sign = 1;
	float term;			// 当前项的值
	float sum = 0.0;	// 和
	int deno;			// 分母

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