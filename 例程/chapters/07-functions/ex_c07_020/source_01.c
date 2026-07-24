/*
 * 例程 ID：EX-C07-020
 * 标题：教材例程 7.20
 * 教材位置：第 7 章 / 7.20
 * 知识点：函数、参数、递归、变量作用域
 * 来源：2024-2025-1/20241105_1108/7.20.file1.c, 2024-2025-1/20241105_1108/7.20.file2.c, 2024-2025-1/20241105_1108/7.20.file3.c, 2024-2025-1/20241105_1108/7.20.file4.c
 * 编译模式：gnu99-textbook
 * 旧语法：gets
 * 交互方式：manual
 * 兼容性：教材/考试兼容例程：保留 gets() 以识别教材旧写法。仅允许受控短输入；该接口已从 C11 移除，不应用于生产程序。
 */
#include <stdio.h>
int main()
{
    extern void enter_string(char str[]);           // 对函数的声明
    extern void delete_string(char str[], char ch); // 对函数的声明
    extern void print_string(char str[]);           // 对函数的声明
    // 以上3行声明了在本函数中将要调用的已在其他文件中定义的3个函数
    char c, str[80];
    enter_string(str);     // 调用在其他文件中定义的enter_string函数
    scanf("%c", &c);       // 输入要求删去的字符
    delete_string(str, c); // 调用在其他文件中定义的delete_string函数
    print_string(str);     // 调用在其他文件中定义的print_string函数
    return 0;
}
