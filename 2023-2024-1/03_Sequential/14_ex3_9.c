#include <stdio.h>

int main()
{
	char a, b, c;	//�����ַ�����a,b,c

	a = getchar();	//�Ӽ�������һ���ַ����͸��ַ�����a
	b = getchar();	//�Ӽ�������һ���ַ����͸��ַ�����b
	c = getchar();	//�Ӽ�������һ���ַ����͸��ַ�����c

	putchar(a); 	//������a��ֵ���
	putchar(b); 	//������b��ֵ��� 
	putchar(c); 	//������c��ֵ���
	putchar('\n');	//����
	
	return 0;
}
