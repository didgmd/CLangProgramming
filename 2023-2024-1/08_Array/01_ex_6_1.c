#include<stdio.h>
int main()
{
	int i, a[10];
	for (i = 0; i <= 9; i++)	//������Ԫ��a[0]~a[9]��ֵ
		a[i] = i;
	for (i = 9; i >= 0; i--)	//���a[9]~a[0]��10������Ԫ��
		printf("%d ", a[i]);
	printf("\n");
	return 0;
}
