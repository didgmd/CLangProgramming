#include <stdio.h>

int addTwoNumbers(int x, int y)  // x �� y ���β�
{
	int z;
	z = x + y;

	return z;
}

int main()
{
	int a, b, c;  // �������ͱ���
	a = 3;     // ������ֵ
	b = 5;
	// c = a + b;
	c = addTwoNumbers(a, b);  // a �� b ��ʵ��

	int d, e, f;
	d = 4;
	e = 7;
	// f = d + e;
	f = addTwoNumbers(d, e);

	printf("This is the first number: %d\n", a);
	printf("This is the second number: %d\n", b);
	printf("The sum of two numbers is: %d\n", c);

	printf("This is the first number: %d\n", d);
	printf("This is the second number: %d\n", e);
	printf("The sum of two numbers is: %d\n", f);

	return 0;
}
