#include <stdio.h>
int main()
{
	int a[2][3] = { {1,2,3},{4,5,6} };
	int b[3][2], i, j;
	printf("array a:\n");
	for (i = 0; i <= 1; i++)			//处理a数组中的一行中各元素
	{
		for (j = 0; j <= 2; j++)		//处理a数组中某一列中各元素
		{
			printf("%5d", a[i][j]);	//输出a数组的一个元素
			b[j][i] = a[i][j];	//将a数组元素的值赋给b数组相应元素
		}
		printf("\n");
	}
	printf("array b:\n");				//输出b数组各元素
	for (i = 0; i <= 2; i++)				//处理b数组中一行中各元素
	{
		for (j = 0; j <= 1; j++)			//处理b数组中一列中各元素
			printf("%5d", b[i][j]);		//输出b数组的一个元素
		printf("\n");
	}
	return 0;
}
