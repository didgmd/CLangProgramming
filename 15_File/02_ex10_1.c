#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
#include <stdlib.h>
int main()
{
	FILE* fp;                     				//�����ļ�ָ��fp
	char ch, filename[10];
	printf("���������õ��ļ���: ");
	scanf("%s", filename);        			//�����ļ���
	getchar();                  		 		//���������������Ļس���
	if ((fp = fopen(filename, "w")) == NULL)	//������ļ���ʹfpָ����ļ�
	{
		printf("cannot open file\n");  	//����򿪳����������򲻿���
		exit(0);                       			//��ֹ����
	}
	printf("������һ��׼���洢�����̵��ַ���(��#����): ");
	ch = getchar();        					//���մӼ�������ĵ�һ���ַ�
	while (ch != '#')        					//�������#��ʱ����ѭ��
	{
		fputc(ch, fp); 					//������ļ����һ���ַ�
		putchar(ch);					//��������ַ���ʾ����Ļ��
		ch = getchar(); 					//�ٽ��մӼ��������һ���ַ�
	}
	fclose(fp);						//�ر��ļ�
	putchar(10); 						//����Ļ���һ�����з� 
	return 0;
}
