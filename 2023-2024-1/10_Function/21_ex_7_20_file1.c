#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
int main()
{
	extern void enter_string(char str[]);			//对函数的声明
	extern void delete_string(char str[], char ch); 	//对函数的声明
	extern void print_string(char str[]);			//对函数的声明
	//以上3行声明了在本函数中将要调用的已在其他文件中定义的3个函数
	char c, str[80];
	enter_string(str); 		//调用在其他文件中定义的enter_string函数
	scanf("%c", &c); 		//输入要求删去的字符
	delete_string(str, c);		//调用在其他文件中定义的delete_string函数 
	print_string(str);		//调用在其他文件中定义的print_string函数
	return 0;
}
