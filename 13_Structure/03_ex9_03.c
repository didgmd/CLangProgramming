#define _CRT_SECURE_NO_WARNINGS 1
#include <string.h>
#include <stdio.h>
struct Person						//�����ṹ������struct Person
{
	char name[20];				//��ѡ������
	int count;						//��ѡ�˵�Ʊ�� 
}leader[3] = { "Li",0,"Zhang",0,"Sun",0 };	//����ṹ�����鲢��ʼ��

int main()
{
	int i, j;
	char leader_name[20];			//�����ַ����� 
	for (i = 1; i <= 10; i++)
	{
		scanf("%s", leader_name);	//������ѡ�ĺ�ѡ������
		for (j = 0; j < 3; j++)
			if (strcmp(leader_name, leader[j].name) == 0) leader[j].count++;
	}
	printf("\nResult:\n");
	for (i = 0; i < 3; i++)
		printf("%5s:%d\n", leader[i].name, leader[i].count);
	return 0;
}