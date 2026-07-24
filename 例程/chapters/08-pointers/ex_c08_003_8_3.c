/*
 * 例程 ID：EX-C08-003
 * 标题：教材例程 8.3
 * 教材位置：第 8 章 / 8.3
 * 知识点：指针、数组与指针、字符串指针、动态内存
 * 来源：2024-2025-1/20241112_1115/8.3.c
 * 编译模式：gnu99-textbook
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#include <stdio.h>
int main()
{
    void swap(int *p1, int *p2); // 对swap函数的声明
    int a, b;
    int *pointer_1, *pointer_2; // 定义两个int *型的指针变量
    printf("please enter a and b:");
    scanf("%d,%d", &a, &b); // 输入两个整数
    pointer_1 = &a;         // 使pointer_1指向a
    pointer_2 = &b;         // 使pointer_2指向b
    if (a < b)
        swap(pointer_1, pointer_2);  // 如果a<b，调用swap函数
    printf("max=%d,min=%d\n", a, b); // 输出结果
    return 0;
}

void swap(int *p1, int *p2) // 定义swap函数
{
    int temp;
    temp = *p1; // 使*p1和*p2互换
    *p1 = *p2;
    *p2 = temp;
} // 本例交换a和b的值，而p1和p2的值不变。这恰和例8.2相反
