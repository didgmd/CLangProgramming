/*
 * 例程 ID：EX-C10-001
 * 标题：教材例程 10.1
 * 教材位置：第 10 章 / 10.1
 * 知识点：文件、顺序读写、随机读写、错误检测
 * 来源：2024-2025-1/20241129/10.1.c
 * 编译模式：gnu99-textbook
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#include <stdio.h>
#include <stdlib.h>
int main()
{
    FILE *fp; // 定义文件指针fp
    char ch, filename[10];
    printf("请输入所用的文件名: ");
    scanf("%s", filename);                   // 输入文件名
    getchar();                               // 用来消化最后输入的回车符
    if ((fp = fopen(filename, "w")) == NULL) // 打开输出文件并使fp指向此文件
    {
        printf("cannot open file\n"); // 如果打开出错就输出“打不开”
        exit(0);                      // 终止程序
    }
    printf("请输入一个准备存储到磁盘的字符串(以#结束): ");
    ch = getchar();   // 接收从键盘输入的第一个字符
    while (ch != '#') // 当输入′#′时结束循环
    {
        fputc(ch, fp);  // 向磁盘文件输出一个字符
        putchar(ch);    // 将输出的字符显示在屏幕上
        ch = getchar(); // 再接收从键盘输入的一个字符
    }
    fclose(fp);  // 关闭文件
    putchar(10); // 向屏幕输出一个换行符
    return 0;
}
