/*
 * 例程 ID：EX-C08-024
 * 标题：教材例程 8.18
 * 教材位置：第 8 章 / 8.18
 * 知识点：指针、数组与指针、字符串指针、动态内存
 * 来源：2024-2025-1/20241112_1115/8.18.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>
int main()
{
    char a[] = "I am a student.", b[20]; // 定义字符数组
    int i;
    for (i = 0; *(a + i) != '\0'; i++)
        *(b + i) = *(a + i);       // 将a[i]的值赋给b[i]
    *(b + i) = '\0';               // 在b数组的有效字符之后加'\0'
    printf("string a is:%s\n", a); // 输出a数组中全部有效字符
    printf("string b is:");
    for (i = 0; b[i] != '\0'; i++)
        printf("%c", b[i]); // 逐个输出b数组中全部有效字符
    printf("\n");
    return 0;
}
