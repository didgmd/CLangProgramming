#include <stdio.h>

//求两个整数中的较大者的max函数
int max(int x, int y)		                	//定义max函数,函数值为整型, 形式参数x和y为整型 
{
    int z;					                	//max函数中的声明部分，定义本函数中用到的变量z为整型

    if (x > y)
    {
        printf("The max of two number is: ");
        z = x;					                //若x>y成立，将x的值赋给变量z
    }
    else
    {
        printf("The max of two number is: ");
        z = y;				                	//否则(即x>y不成立)，将y的值赋给变量z
    }

    return z; 				                	//将z的值作为max函数值，返回到调用max函数的位置
}

//主函数
int main()					                	//定义主函数
{								                //主函数体开始
    int a, b, c;				                //定义变量a，b，c

    printf("The first number: ");
    scanf_s("%d", &a);                          //输入变量a的值
    printf("The second number: ");
    scanf_s("%d", &b);                          //输入变量b的值
    c = max(a, b);			                	//调用max函数，将得到的值赋给c

    printf("max = %d\n", c);                	//输出c的值
    return 0;				                	//返回函数值为0
} //主函数体结束