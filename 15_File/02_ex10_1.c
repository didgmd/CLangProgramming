#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
#include <stdlib.h>
int main()
{
	FILE* fp;                     				//定义文件指针fp
	char ch, filename[10];
	printf("请输入所用的文件名: ");
	scanf("%s", filename);        			//输入文件名
	getchar();                  		 		//用来消化最后输入的回车符
	if ((fp = fopen(filename, "w")) == NULL)	//打开输出文件并使fp指向此文件
	{
		printf("cannot open file\n");  	//如果打开出错就输出“打不开”
		exit(0);                       			//终止程序
	}
	printf("请输入一个准备存储到磁盘的字符串(以#结束): ");
	ch = getchar();        					//接收从键盘输入的第一个字符
	while (ch != '#')        					//当输入′#′时结束循环
	{
		fputc(ch, fp); 					//向磁盘文件输出一个字符
		putchar(ch);					//将输出的字符显示在屏幕上
		ch = getchar(); 					//再接收从键盘输入的一个字符
	}
	fclose(fp);						//关闭文件
	putchar(10); 						//向屏幕输出一个换行符 
	return 0;
}
