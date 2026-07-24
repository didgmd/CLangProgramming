/*
 * 例程 ID：EX-C08-021
 * 标题：教材例程 8.15
 * 教材位置：第 8 章 / 8.15
 * 知识点：指针、数组与指针、字符串指针、动态内存
 * 来源：2023-2024-1/11_Pointer/24_ex_8_15.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>
int main()
{
	void search(float(*p)[4], int n);	//函数声明
	float score[3][4] = { {65,57,70,60},{58,87,90,81},{90,99,100,98} };
	//定义二维数组函数score
	search(score, 3);				//调用search函数
	return 0;
}

void search(float(*p)[4], int n)
//形参p是指向包含4个float型元素的一维数组的指针变量
{
	int i, j, flag;
	for (j = 0; j < n; j++)
	{
		flag = 0;
		for (i = 0; i < 4; i++)
			if (*(*(p + j) + i) < 60) flag = 1;
		//*(*(p+j)+i)就是score[j][i]
		if (flag == 1)
		{
			printf("No.%d fails,his scores are:\n", j + 1);
			for (i = 0; i < 4; i++)
				printf("%5.1f ", *(*(p + j) + i));
			//输出*(*(p+j)+i)就是输出score[j][i]的值
			printf("\n");
		}
	}
}
