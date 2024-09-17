#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
int main()
{
	float add(float x, float y);		//对add函数作声明
	float a, b, c;
	printf("Please enter a and b:");	//提示输入
	scanf("%f,%f", &a, &b);			//输入两个实数
	c = add(a, b); 					//调用add函数
	printf("sum is %f\n", c);			//输出两数之和
	return 0;
}

float add(float x, float y)		//定义add函数
{
	float z;
	z = x + y;
	return(z); 			//把变量z的值作为函数值返回
}
