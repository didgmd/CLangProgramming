#define _CRT_SECURE_NO_WARNINGS 1
#pragma warning(disable: 6031)

#include <stdio.h>

int add(int x, int y)
{
	int z;

	z = x + y;

	return z;
}

int max(int x, int y)
{
	int z;
	if (x > y)
	{
		z = x;
		printf("%d is larger than %d\n", x, y);
	}
	else if (x < y)
	{
		z = y;
		printf("%d is smaller than %d\n", x, y);
	}
	else
	{
		z = x;
		printf("%d and %d is the same\n", x, y);
	}

	return z;
}

int calculator(int x, int y, char z)
{
	int res = 0;

	if (z == '+')
	{
		res = x + y;
	}
	else if (z == '-')
	{
		res = x - y;
	}
	else if (z == '*')
	{
		res = x * y;
	}
	else if (z == '/')
	{
		res = x / y;
	}
	else
	{
		printf("The input operator is invalid\n");
	}

	return res;
}

int main()
{
	printf("Hello World\n");

	int a, b, c;
	
	printf("Please input the first number: ");
	scanf("%d", &a);

	printf("Please input the second number: ");
	scanf("%d", &b);

	// c = add(a, b);
	// printf("c = %d\n", c);
	// printf("The sum of %d and %d is %d\n", a, b, c);

	// c = max(a, b);
	// printf("Then max number between %d and %d is %d\n", a, b, c);

	char op;
	printf("Please input the operator: ");
	scanf(" %c", &op);
	
	c = calculator(a, b, op);

	return 0;
}