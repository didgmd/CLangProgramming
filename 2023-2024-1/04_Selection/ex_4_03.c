#define _CRT_SECURE_NO_WARNINGS 1

#include <stdio.h>
int main()
{
	float a, b, c, t;
	scanf("%f,%f,%f", &a, &b, &c);
	if (a > b)
	{
		t = a;		//��������t��ʵ�ֱ���a�ͱ���b����ֵ
		a = b;
		b = t;
	}			//������aС�ڻ����b     
	if (a > c)
	{
		t = a;		//��������t��ʵ�ֱ���a�ͱ���c����ֵ
		a = c;
		c = t;
	}			//������aС�ڻ����c       
	if (b > c)		//��Ҫ
	{
		t = b;		//��������t��ʵ�ֱ���b�ͱ���c����ֵ
		b = c;
		c = t;
	}			//������bС�ڻ����c                       
	printf("%5.2f,%5.2f,%5.2f\n", a, b, c); 		//˳�����a,b,c��ֵ
	return 0;
}
