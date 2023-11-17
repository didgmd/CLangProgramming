#include <stdio.h>
int main()
{
	int max_value(int array[][4]);		//函数声明
	int a[3][4] = { {1,3,5,7},{2,4,6,8},{15,17,34,12} };	 //对数组元素赋初值
	printf("Max value is %d\n", max_value(a));
	//max_value(a)为函数调用
	return 0;
}

int max_value(int array[][4])	//函数定义
{
	int i, j, max;
	max = array[0][0];
	for (i = 0; i < 3; i++)
		for (j = 0; j < 4; j++)
			if (array[i][j] > max) max = array[i][j];	//把大者放在max中
	return(max);
}
