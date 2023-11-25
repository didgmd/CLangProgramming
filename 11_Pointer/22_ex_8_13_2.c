#include <stdio.h>
int main()
{
	int a[4] = { 1,3,5,7 };		//定义一维数组a，包含4个元素
	int(*p)[4];			//定义指向包含4个元素的一维数组的指针变量中
	p = &a;				//使p指向一维数组
	printf("%d\n", (*p)[3]);	//输出a[3]，输出整数7
	return 0;
}
