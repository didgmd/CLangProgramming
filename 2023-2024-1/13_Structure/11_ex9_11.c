#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
struct						//���������ṹ������
{
	int num;					//��Աnum(���)
	char name[10];			//��Աname(����)
	char sex;					//��Աsex(�Ա�)
	char job;					//��Աjob(ְҵ)
	union					//������������������
	{
		int clas;				//��Աclas(�༶)
		char position[10];		//��Աposition(ְ��) 
	}category;				//��Աcategory�ǹ��������
}person[2];					//����ṹ������person��������Ԫ��

int main()
{
	int i;
	for (i = 0; i < 2; i++)
	{
		printf("please enter the data of person:\n");
		scanf("%d %s %c %c", &person[i].num, person[i].name, &person[i].sex, &person[i].job);		//����ǰ4��
		if (person[i].job == 's')
			scanf("%d", &person[i].category.clas);										//����ѧ��������༶
		else if (person[i].job == 't')
			scanf("%s", person[i].category.position);										//���ǽ�ʦ������ְ��
		else
			printf("Input error!");													//��job����'s'��'t'����ʾ���������
	}
	printf("\n");
	printf("No.  name\tsex job class/position\n");
	for (i = 0; i < 2; i++)
	{
		if (person[i].job == 's')														//����ѧ��
			printf("%-6d%-10s%-4c%-4c%-10d\n", person[i].num, person[i].name, person[i].sex, person[i].job, person[i].category.clas);
		else																		//���ǽ�ʦ
			printf("%-6d%-10s%-4c%-4c%-10s\n", person[i].num, person[i].name, person[i].sex, person[i].job, person[i].category.position);
	}
	return 0;
}
