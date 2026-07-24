/*
 * 例程 ID：EX-C08-004
 * 标题：教材例程 8.4
 * 教材位置：第 8 章 / 8.4
 * 知识点：指针、数组与指针、字符串指针、动态内存
 * 来源：2024-2025-1/20241112_1115/8.4.c
 * 编译模式：gnu99-textbook
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#include <stdio.h>
int main()
{
    void swap(int *p1, int *p2);
    int a, b;
    int *pointer_1, *pointer_2; // pointer_1,pointer_2是int *型变量
    printf("please enter two integer numbers:");
    scanf("%d,%d", &a, &b);
    pointer_1 = &a;
    pointer_2 = &b;
    if (a < b)
        swap(pointer_1, pointer_2);
    // 调用swap函数，用指针变量作实参
    printf("max=%d,min=%d\n", *pointer_1, *pointer_2);
    return 0;
}

void swap(int *p1, int *p2) // 形参是指针变量
{
    int *p;
    p = p1; // 下面3行交换p1和p2的指向
    p1 = p2;
    p2 = p;
}
