#include <stdio.h>
int main()
{
	char string[] = "I love China!";	//定义字符数组sting
	printf("%s\n", string);		//用%s格式声明输出string，可以输出整个字符串
	printf("%c\n", string[7]);		//用%c格式输出一个字符数组元素 

	char *p = string;			//定义字符指针p，指向字符数组string
	printf("%s\n", p);			//用%s格式声明输出p，可以输出整个字符串
	printf("%c\n", p[5]);
	return 0;
}
