#include <stdio.h>
int main()
{
    void copy_string(char *from, char *to);
    char *a = "I am a teacher.";                // a是char*型指针变量
    char b[] = "You are a student.";            // b是字符数组
    char *p = b;                                // 使指针变量p指向b数组首元素
    printf("string a=%s\nstring b=%s\n", a, b); // 输出a串和b串
    printf("copy string a to string b:\n");
    copy_string(a, p);                            // 调用copy_string函数，实参为指针变量
    printf("\nstring a=%s\nstring b=%s\n", a, b); // 输出改变后的a串和b串
    return 0;
}
void copy_string(char *from, char *to) // 定义函数，形参为字符指针变量
{
    for (; *from != '\0'; from++, to++)
    {
        *to = *from;
    }
    *to = '\0';
}
