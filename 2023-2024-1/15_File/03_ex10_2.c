#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
#include <stdlib.h>
int main()
{
	FILE* in, * out; 						//����ָ��FILE�����ļ���ָ�����
	char ch, infile[10], outfile[10];			//���������ַ����飬�ֱ������������ļ���
	printf("��������ļ�������:");
	scanf("%s", infile);					//����һ�������ļ�������
	printf("��������ļ�������:");
	scanf("%s", outfile); 					//����һ������ļ�������
	if ((in = fopen(infile, "r")) == NULL)		//�������ļ�
	{
		printf("�޷��򿪴��ļ�\n");	exit(0);
	}
	if ((out = fopen(outfile, "w")) == NULL)	//������ļ�
	{
		printf("�޷��򿪴��ļ�\n");	exit(0);
	}
	ch = fgetc(in);          				//�������ļ�����һ���ַ�����������ch
	while (!feof(in))       					//���δ���������ļ��Ľ�����־
	{
		fputc(ch, out);      				//��chд������ļ�
		putchar(ch);        				//��ch��ʾ����Ļ��
		ch = fgetc(in);       				//�ٴ������ļ�����һ���ַ�����������ch
	}
	putchar(10);						//��ʾ��ȫ���ַ�����
	fclose(in); 						//�ر������ļ�
	fclose(out);						//�ر�����ļ�
	return 0;
}
