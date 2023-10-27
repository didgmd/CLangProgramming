#define _CRT_SECURE_NO_WARNINGS 1

#include <stdio.h>
int main()
{
	float a, b, c, t;
	scanf("%f,%f,%f", &a, &b, &c);
	if (a > b)
	{
		t = a;		//借助变量t，实现变量a和变量b互换值
		a = b;
		b = t;
	}			//互换后，a小于或等于b     
	if (a > c)
	{
		t = a;		//借助变量t，实现变量a和变量c互换值
		a = c;
		c = t;
	}			//互换后，a小于或等于c       
	if (b > c)		//还要
	{
		t = b;		//借助变量t，实现变量b和变量c互换值
		b = c;
		c = t;
	}			//互换后，b小于或等于c                       
	printf("%5.2f,%5.2f,%5.2f\n", a, b, c); 		//顺序输出a,b,c的值
	return 0;
}
