#include <stdio.h>
int main()
{
	void copy_string(char* from, char* to);
	char* a = "I am a teacher.";		//a��char*��ָ�����
	char b[] = "You are a student.";	//b���ַ�����
	char* p = b;		//ʹָ�����pָ��b������Ԫ��
	printf("string a=%s\nstring b=%s\n", a, b);	//���a����b��
	printf("copy string a to string b:\n");
	copy_string(a, p);	//����copy_string������ʵ��Ϊָ�����
	printf("\nstring a=%s\nstring b=%s\n", a, b);	//����ı���a����b��
	return 0;
}
void copy_string(char* from, char* to)	//���庯�����β�Ϊ�ַ�ָ�����
{
	for (; *from != '\0'; from++, to++)
	{
		*to = *from;
	}
	*to = '\0';
}

// ����Ϊ�Ľ�����
/*
void copy_string(char *from, char *to)
{	for(;(*to++=* from++)!='\0';);
	//��for(;*to++=* from++;);
}
*/
/*
void copy_string(char *from, char *to)
{	while((*to=*from)!='\0')
	//��while(*to=*from)
	{	to++; from++;}
}
*/
/*
void copy_string(char *from, char *to)
{	while(*from!='\0')
	//��while(*from) ����Ϊ'\0'��ASCII��Ϊ0
		*to++=*from++;
	*to='\0';
}
*/
/*
void copy_string(char *from, char *to)
{	while((*to++=*from++)!='\0');
	//��while(*to++=*from++)
}
*/
/*
void copy_string��char from[]��char to[]��
{	char *p1, *p2;
	p1=from;p2=to;
	while((*p2++=*p1++)!='\0');
}
*/