#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
int main()
{
	void swap(int* p1, int* p2);	//��swap���������� 
	int a, b;
	int* pointer_1, * pointer_2;	//��������int *�͵�ָ�����
	printf("please enter a and b:");
	scanf("%d,%d", &a, &b);		//������������
	pointer_1 = &a;			//ʹpointer_1ָ��a
	pointer_2 = &b;			//ʹpointer_2ָ��b 
	if (a < b) swap(pointer_1, pointer_2); //���a<b������swap����
	printf("max=%d,min=%d\n", a, b); 	//������
	return 0;
}

void swap(int* p1, int* p2)			//����swap����
{
	int temp;
	temp = *p1;					//ʹ*p1��*p2����
	*p1 = *p2;
	*p2 = temp;
}	//��������a��b��ֵ����p1��p2��ֵ���䡣��ǡ����8.2�෴
