/*
 * 例程 ID：EX-C06-008
 * 标题：教材例程 6.8
 * 教材位置：第 6 章 / 6.8
 * 知识点：一维数组、二维数组、字符数组、字符串
 * 来源：2024-2025-1/20241025_1029/6.8.c
 * 编译模式：gnu99-textbook
 * 旧语法：gets
 * 交互方式：manual
 * 兼容性：教材/考试兼容例程：保留 gets() 以识别教材旧写法。仅允许受控短输入；该接口已从 C11 移除，不应用于生产程序。
 */
#include <stdio.h>
int main()
{
    char string[81];
    int i, num = 0, word = 0;
    char c;
    gets(string);                             // 输入一个字符串给字符数组string
    for (i = 0; (c = string[i]) != '\0'; i++) // 只要字符不是'\0'就循环
        if (c == ' ')
            word = 0;       // 若是空格字符，使word置0
        else if (word == 0) // 如果不是空格字符且word原值为0
        {
            word = 1; // 使word置1
            num++;    // num累加1，表示增加一个单词
        }
    printf("There are %d words in this line.\n", num); // 输出单词数
    return 0;
}
