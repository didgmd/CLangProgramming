#define _CRT_SECURE_NO_WARNINGS 1
#include<stdio.h>
int main()
{
	char ch;
	FILE* fp1, * fp2;
	fp1 = fopen("file1.dat", "r");	//�������ļ�
	fp2 = fopen("file2.dat", "w");	//������ļ�
	ch = getc(fp1);				//��file1.dat�ļ������һ���ַ�
	while (!feof(fp1))			//��δ��ȡ�ļ�β��־
	{
		putchar(ch);			//����Ļ���һ���ַ�
		ch = getc(fp1);			//�ٴ�file1.dat�ļ�����һ���ַ�
	}
	putchar(10);				//����Ļִ�л���
	rewind(fp1);				//ʹ�ļ�λ�ñ�Ƿ����ļ���ͷ
	ch = getc(fp1);				//��file1.dat�ļ������һ���ַ�
	while (!feof(fp1))			//��δ��ȡ�ļ�β��־
	{
		fputc(ch, fp2);			//��file2.dat�ļ����һ���ַ�
		ch = fgetc(fp1);			//�ٴ�file1.dat�ļ�����һ���ַ�
	}
	fclose(fp1); fclose(fp2);
	return 0;
}