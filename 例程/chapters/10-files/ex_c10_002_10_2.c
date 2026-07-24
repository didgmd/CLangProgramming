/*
 * 例程 ID：EX-C10-002
 * 标题：教材例程 10.2
 * 教材位置：第 10 章 / 10.2
 * 知识点：文件、顺序读写、随机读写、错误检测
 * 来源：2024-2025-1/20241129/10.2.c
 * 编译模式：gnu99-textbook
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#include <stdio.h>
#include <stdlib.h>
int main()
{
    FILE *in, *out;                   // 定义指向FILE类型文件的指针变量
    char ch, infile[10], outfile[10]; // 定义两个字符数组，分别存放两个数据文件名
    printf("输入读入文件的名字:");
    scanf("%s", infile); // 输入一个输入文件的名字
    printf("输入输出文件的名字:");
    scanf("%s", outfile);                  // 输入一个输出文件的名字
    if ((in = fopen(infile, "r")) == NULL) // 打开输入文件
    {
        printf("无法打开此文件\n");
        exit(0);
    }
    if ((out = fopen(outfile, "w")) == NULL) // 打开输出文件
    {
        printf("无法打开此文件\n");
        exit(0);
    }
    ch = fgetc(in);   // 从输入文件读入一个字符，赋给变量ch
    while (!feof(in)) // 如果未遇到输入文件的结束标志
    {
        fputc(ch, out); // 将ch写到输出文件
        putchar(ch);    // 将ch显示到屏幕上
        ch = fgetc(in); // 再从输入文件读入一个字符，赋给变量ch
    }
    putchar(10); // 显示完全部字符后换行
    fclose(in);  // 关闭输入文件
    fclose(out); // 关闭输出文件
    return 0;
}
