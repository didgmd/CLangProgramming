#include <stdio.h>
int main()
{
    void print_star();    // 声明print_star函数
    void print_message(); // 声明print_message函数
    print_star();         // 调用print_star函数
    print_message();      // print_message函数
    print_star();         // 调用print_star函数
    return 0;
}

void print_star() // 定义print_star函数
{
    printf("******************\n"); // 输出一行*号
}

void print_message() // 定义print_message函数
{
    printf("How do you do!\n"); // 输出一行文字信息
}
