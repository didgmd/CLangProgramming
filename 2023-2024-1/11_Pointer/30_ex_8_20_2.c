#include <stdio.h>
int main()
{
	void copy_string(char from[], char to[]);	//函数声明
	char a[] = "I am a teacher.";		//定义字符数组a并初始化
	char b[] = "You are a student.";	//定义字符数组b并初始化
	char* from = a, * to = b;	//from指向a数组首元素，to指向b数组首元素 
	printf("string a=%s\nstring b=%s\n", a, b);
	printf("copy string a to string b:\n");
	copy_string(from, to);	//实参为字符指针变量
	printf("\nstring a=%s\nstring b=%s\n", a, b);
	return 0;
}
void copy_string(char from[], char to[]) 		//形参为字符数组
{
	int i = 0;
	while (from[i] != '\0')
	{
		to[i] = from[i]; i++;
	}
	to[i] = '\0';
}
