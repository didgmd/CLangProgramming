#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
int main()
{
	int a[10];
	int i;
	printf("please enter 10 integer numbers:");
	for (i = 0; i < 10; i++)
		scanf("%d", &a[i]);
	for (i = 0; i < 10; i++)
		printf("%d ", a[i]);
	//����Ԫ�������������±��ʾ
	printf("%\n");
	return 0;
}
