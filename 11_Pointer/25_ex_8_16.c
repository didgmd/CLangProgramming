#include <stdio.h>
int main()
{
	char string[] = "I love China!";	//�����ַ�����sting
	printf("%s\n", string);		//��%s��ʽ�������string��������������ַ���
	printf("%c\n", string[7]);		//��%c��ʽ���һ���ַ�����Ԫ�� 

	char *p = string;			//�����ַ�ָ��p��ָ���ַ�����string
	printf("%s\n", p);			//��%s��ʽ�������p��������������ַ���
	printf("%c\n", p[5]);
	return 0;
}
