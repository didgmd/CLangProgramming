#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
int A;				//�����ⲿ����
int main()
{
	int power(int);		//��������
	int b = 3, c, d, m;
	printf("enter the number a and its power m:\n");
	scanf("%d,%d", &A, &m);
	c = A * b;
	printf("%d*%d=%d\n", A, b, c);
	d = power(m);
	printf("%d**%d=%d\n", A, m, d);
	return 0;
}
