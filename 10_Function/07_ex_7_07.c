#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
int main()
{
	int fac(int n);		//fac函数声明
	int n;
	int y;
	printf("input an integer number:");
	scanf("%d", &n);	//输入要求阶乘的数
	y = fac(n);
	printf("%d!=%d\n", n, y);
	return 0;
}

int fac(int n) 				//定义fac函数
{
	int f;
	if (n < 0)				//n不能小于0
		printf("n<0,data error!");
	else if (n == 0 || n == 1)	//n=0或,1时n!=1
		f = 1;				//递归终止条件
	else
		f = fac(n - 1) * n;	 //n>1时，n!=n*(n-1)
	return(f);
}