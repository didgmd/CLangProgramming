#include <stdio.h>
int main()
{
	int fac(int n);
	int i;
	for (i = 1; i <= 5; i++)	//先后5次调用fac函数
		printf("%d!=%d\n", i, fac(i));	//每次计算并输出i!的值
	return 0;
}
int fac(int n)
{
	static int f = 1;		//f保留了上次调用结束时的值
	f = f * n;			//在上次的f值的基础上再乘以n
	return(f);			//返回值f是n!的值
}
