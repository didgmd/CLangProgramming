#define _CRT_SECURE_NO_WARNINGS 1

#include <stdio.h>
int main()
{
	char c;
	c = getchar();				//����һ���ַ����ַ�����c
	while (c != '\n')				//���c��ֵ�Ƿ�Ϊ���з�'\n'  
	{
		if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z'))	//c�������ĸ
		{
			if (c >= 'W' && c <= 'Z' || c >= 'w' && c <= 'z') c = c - 22;
			//�����26����ĸ�����4����ĸ֮һ��ʹc-22
			else c = c + 4;		//�����ǰ��22����ĸ֮һ����ʹc��4�����������4����ĸ
		}
		printf("%c", c);			//����Ѹı���ַ�
		c = getchar(); 			//��������һ���ַ����ַ�����c
	}
	printf("\n");
	return 0;
}