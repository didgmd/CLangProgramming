/*
 * 例程 ID：PJ-CALC-01
 * 标题：计算器渐进项目：步骤 1
 * 教材位置：综合案例
 * 知识点：综合应用、渐进式开发
 * 来源：2023-2024-1/01_HelloC/1_4_1_Calculator.c
 * 编译模式：gnu99-textbook
 * 旧语法：msvc-warning-pragma、msvc-crt-compat
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
// 由于Visual Studio认为scanf()不够安全，因此须添加如下prefix才能使用scanf()
#define _CRT_SECURE_NO_WARNINGS 1
#pragma warning(disable: 6031)

#include <stdio.h>

// A calculator program that adds, subtracts, multiplies, and divides two numbers with different functions
int main()
{
    // Declare variables
    int a, b, result;
    char operation;

    // Ask for a number
    printf("Enter a number: ");
    scanf("%d", &a);

    // Ask for another number
    printf("Enter another number: ");
    scanf("%d", &b);

    // Ask for an operation
    printf("Enter an operation: ");
    scanf(" %c", &operation);

    // Check if the operation is valid
    if (operation == '+')
    {
        // Add the numbers
        result = a + b;
    }
    else if (operation == '-')
    {
        // Subtract the numbers
        result = a - b;
    }
    else if (operation == '*')
    {
        // Multiply the numbers
        result = a * b;
    }
    else if (operation == '/')
    {
        // Divide the numbers
        result = a / b;
    }
    else
    {
        // Print an error message
        printf("Invalid operation!\n");
        return 1;
    }

    // Print the result
    printf("Result: %d\n", result);

    return 0;
}
