#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
int main()
{
	int max();
	extern int A, B, C;	//���ⲿ����A,B,C����������չ���Ӵ˴���ʼ
	printf("Please enter three integer numbers:");
	scanf("%d %d %d", &A, &B, &C);		//����3��������A,B,C
	printf("max is %d\n", max());
	return 0;
}
int A, B, C;				//�����ⲿ����A,B,C
int max()
{
	int m;
	m = A > B ? A : B;		//��A��B�еĴ��߷���m��
	if (C > m) m = C;		//��A,B,C�����еĴ��߷���m��
	return(m);		//����m��ֵ
}
