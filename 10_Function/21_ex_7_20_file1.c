#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
int main()
{
	extern void enter_string(char str[]);			//�Ժ���������
	extern void delete_string(char str[], char ch); 	//�Ժ���������
	extern void print_string(char str[]);			//�Ժ���������
	//����3���������ڱ������н�Ҫ���õ����������ļ��ж����3������
	char c, str[80];
	enter_string(str); 		//�����������ļ��ж����enter_string����
	scanf("%c", &c); 		//����Ҫ��ɾȥ���ַ�
	delete_string(str, c);		//�����������ļ��ж����delete_string���� 
	print_string(str);		//�����������ļ��ж����print_string����
	return 0;
}
