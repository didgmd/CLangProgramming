#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
// int max(int x, int y);		//��max����������
int main()
{
	int max(int x, int y);		//��max����������
	int a, b, c;
	printf("please enter two integer numbers:");  //��ʾ��������
	scanf("%d,%d", &a, &b);	//������������
	c = max(a, b);	//����max������������ʵ�Ρ�������������c
	printf("max is %d\n", c);	//�������c
	return 0;
}
int max(int x, int y)	//����max����������������
{
	int z;		//������ʱ����z
	z = x > y ? x : y;	//��x��y�д��߸���z
	return(z);		//��z��Ϊmax������ֵ����main����
}