/*
 * 例程 ID：EX-C08-001
 * 标题：教材例程 8.1
 * 教材位置：第 8 章 / 8.1
 * 知识点：指针、数组与指针、字符串指针、动态内存
 * 来源：2024-2025-1/20241112_1115/8.1.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：deterministic
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>
int main()
{
    int a = 100, b = 10;
    // 定义整型变量a,b，并初始化
    int *pointer_1, *pointer_2;
    // 定义指向整型数据的指针变量pointer_1, pointer_2
    pointer_1 = &a;              // 把变量a的地址赋给指针变量pointer_1
    pointer_2 = &b;              // 把变量b的地址赋给指针变量pointer_2
    printf("a=%d,b=%d\n", a, b); // 输出变量a和b的值
    printf("*pointer_1=%d,*pointer_2=%d\n", *pointer_1, *pointer_2);
    // 输出变量a和b的值
    return 0;
}
