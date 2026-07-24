/*
 * 例程 ID：EX-C06-009
 * 标题：教材例程 6.9
 * 教材位置：第 6 章 / 6.9
 * 知识点：一维数组、二维数组、字符数组、字符串
 * 来源：2024-2025-1/20241025_1029/6.9.c
 * 编译模式：gnu99-textbook
 * 旧语法：gets
 * 交互方式：manual
 * 兼容性：教材/考试兼容例程：保留 gets() 以识别教材旧写法。仅允许受控短输入；该接口已从 C11 移除，不应用于生产程序。
 */
#include <stdio.h>
#include <string.h>
int main()
{
    char str[3][20]; // 定义二维字符数组
    char string[20];
    // 定义一维字符数组，作为交换字符串时的临时字符数组
    int i;
    for (i = 0; i < 3; i++)
        gets(str[i]);                                 // 读入3个字符串，分别给str[0],str[1],str[2]
    if (strcmp(str[0], str[1]) > 0)                   // 若str[0]大于str[1]
        strcpy(string, str[0]);                       // 把str[0]的字符串赋给字符数组string
    else                                              // 若str[0]小于等于str[1]
        strcpy(string, str[1]);                       // 把str[1]的字符串赋给字符数组string
    if (strcmp(str[2], string) > 0)                   // 若str[2]大于string
        strcpy(string, str[2]);                       // 把str[2]的字符串赋给字符数组string
    printf("\nthe largest string is:\n%s\n", string); // 输出string
    return 0;
}
