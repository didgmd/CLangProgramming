#include <stdio.h>
int main()
{
	char* a = "I love China!";
	a = a + 7;			//改变指针变量的值，即改变指针变量的指向
	printf("%s\n", a);	//输出从a指向的字符开始的字符串
	return 0;
}
