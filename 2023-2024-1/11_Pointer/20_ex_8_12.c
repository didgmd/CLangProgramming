#include <stdio.h>
int main()
{
	int a[3][4] = { 1,3,5,7,9,11,13,15,17,19,21,23 };
	int* p;							//p是int *型指针变量
	for (p = a[0]; p < a[0] + 12; p++)			//使p依次指向下一个元素
	{
		if ((p - a[0]) % 4 == 0) printf("\n");	//p移动4次后换行
		printf("%4d", *p);				//输出p指向的元素的值 
	}
	printf("\n");
	return 0;
}
