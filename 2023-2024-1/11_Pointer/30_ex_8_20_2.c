#include <stdio.h>
int main()
{
	void copy_string(char from[], char to[]);	//��������
	char a[] = "I am a teacher.";		//�����ַ�����a����ʼ��
	char b[] = "You are a student.";	//�����ַ�����b����ʼ��
	char* from = a, * to = b;	//fromָ��a������Ԫ�أ�toָ��b������Ԫ�� 
	printf("string a=%s\nstring b=%s\n", a, b);
	printf("copy string a to string b:\n");
	copy_string(from, to);	//ʵ��Ϊ�ַ�ָ�����
	printf("\nstring a=%s\nstring b=%s\n", a, b);
	return 0;
}
void copy_string(char from[], char to[]) 		//�β�Ϊ�ַ�����
{
	int i = 0;
	while (from[i] != '\0')
	{
		to[i] = from[i]; i++;
	}
	to[i] = '\0';
}
