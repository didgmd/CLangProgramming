#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
int main()
{
	void swap(int* p1, int* p2);
	int a, b;
	int* pointer_1, * pointer_2;	//pointer_1,pointer_2��int *�ͱ���
	printf("please enter two integer numbers:");
	scanf("%d,%d", &a, &b);
	pointer_1 = &a;
	pointer_2 = &b;
	if (a < b) swap(pointer_1, pointer_2);
	//����swap��������ָ�������ʵ��
	printf("max=%d,min=%d\n", *pointer_1, *pointer_2);
	return 0;
}

void swap(int* p1, int* p2) 	//�β���ָ�����
{
	int* p;
	p = p1;				//����3�н���p1��p2��ָ��
	p1 = p2;
	p2 = p;
}