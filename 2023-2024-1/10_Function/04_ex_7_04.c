#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
int main()
{
	float add(float x, float y);		//��add����������
	float a, b, c;
	printf("Please enter a and b:");	//��ʾ����
	scanf("%f,%f", &a, &b);			//��������ʵ��
	c = add(a, b); 					//����add����
	printf("sum is %f\n", c);			//�������֮��
	return 0;
}

float add(float x, float y)		//����add����
{
	float z;
	z = x + y;
	return(z); 			//�ѱ���z��ֵ��Ϊ����ֵ����
}
