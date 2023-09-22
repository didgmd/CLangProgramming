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
	int res;

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
	// 这行代码使用了 %c 格式化字符，它会读取一个字符，包括空格、制表符和换行符。
	// 如果前面有其他输入，例如一个数字，那么这个字符会读取前面输入时留下的换行符，导致 scanf 函数不会等待输入。
	// 可以在 %c 前面加一个空格，这样 scanf 函数会跳过前面的空白字符，等待输入。
	scanf(" %c", &op);

	c = calculator(a, b, op);

	return 0;
}