#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
int main()
{
	int i, a[10], * p = a;	//p�ĳ�ֵ��a��pָ��a[0]
	printf("please enter 10 integer numbers:");
	for (i = 0; i < 10; i++)
		scanf("%d", p++);
	p = a;				//����ʹpָ��a[0]
	for (i = 0; i < 10; i++, p++)
		printf("%d ", *p);
	printf("\n");
	return 0;
}
