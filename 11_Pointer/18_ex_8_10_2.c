#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
int main()
{
	void sort(int x[], int n);	//sort函数声明
	int i, * p, a[10];
	p = a;					//指针变量p指向a[0]
	printf("please enter 10 integer numbers:");
	for (i = 0; i < 10; i++)
		scanf("%d", p++);	//输入10个整数
	p = a;	//指针变量p重新指向a[0]
	sort(p, 10);			//调用sort函数
	for (p = a, i = 0; i < 10; i++)
	{
		printf("%d ", *p);	//输出排序后的10个数组元素
		p++;
	}
	printf("\n");
	return 0;
}

void sort(int* x, int n)				//形参x是指针变量
{
	int i, j, k, t;
	for (i = 0; i < n - 1; i++)
	{
		k = i;
		for (j = i + 1; j < n; j++)
			if (*(x + j) > *(x + k)) k = j;	//*(x+j)就是x[j]，其他亦然
		if (k != i)
		{
			t = *(x + i); *(x + i) = *(x + k); *(x + k) = t;
		}
	}
}
