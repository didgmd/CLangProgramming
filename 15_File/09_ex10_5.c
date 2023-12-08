#define _CRT_SECURE_NO_WARNINGS 1
#include<stdio.h>
int main()
{
	char ch;
	FILE* fp1, * fp2;
	fp1 = fopen("file1.dat", "r");	//打开输入文件
	fp2 = fopen("file2.dat", "w");	//打开输出文件
	ch = getc(fp1);				//从file1.dat文件读入第一个字符
	while (!feof(fp1))			//当未读取文件尾标志
	{
		putchar(ch);			//在屏幕输出一个字符
		ch = getc(fp1);			//再从file1.dat文件读入一个字符
	}
	putchar(10);				//在屏幕执行换行
	rewind(fp1);				//使文件位置标记返回文件开头
	ch = getc(fp1);				//从file1.dat文件读入第一个字符
	while (!feof(fp1))			//当未读取文件尾标志
	{
		fputc(ch, fp2);			//向file2.dat文件输出一个字符
		ch = fgetc(fp1);			//再从file1.dat文件读入一个字符
	}
	fclose(fp1); fclose(fp2);
	return 0;
}
