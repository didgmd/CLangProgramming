#include <stdio.h>
int main()
{
	int f(int);				//函数声明
	int a = 2, i;				//自动局部变量
	for (i = 0; i < 3; i++)
		printf("%d\n", f(a));	//输出f(a)的值
	return 0;
}

int f(int a)
{
	auto int b = 0;			//自动局部变量
	static int c = 3;			//静态局部变量
	b = b + 1;
	c = c + 1;
	return(a + b + c);
}
