#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
int main()
{
	int* p, i, a[10];
	p = a;				//pָ��a[0]		��
	printf("please enter 10 integer numbers:");
	for (i = 0; i < 10; i++)
		scanf("%d", p++);	//����10��������a[0]~a[9]
	for (i = 0; i < 10; i++, p++)
		printf("%d ", *p);	//�����a[0]~a[9]	��
	printf("\n");
	return 0;
}