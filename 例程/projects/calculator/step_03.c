/*
 * 例程 ID：PJ-CALC-03
 * 标题：计算器渐进项目：步骤 3
 * 教材位置：综合案例
 * 知识点：综合应用、渐进式开发
 * 来源：2023-2024-1/01_HelloC/1_5_2_CalcFuncForLoop.c
 * 编译模式：gnu99-textbook
 * 旧语法：msvc-warning-pragma、msvc-crt-compat
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#define _CRT_SECURE_NO_WARNINGS 1
#pragma warning(disable: 6031)

#include <stdio.h>

// 声明/定义计算器函数
int calculator(int x, int y, char op)
{
    int res = 0;    // 初始化计算结果变量

    // 根据输入的运算符进行相应的运算
    if (op == '+')
    {
        res = x + y;
        printf("%d + %d = %d\n", x, y, res);
    }
    else if (op == '-')
    {
        res = x - y;
        printf("%d - %d = %d\n", x, y, res);
    }
    else if (op == '*')
    {
        res = x * y;
        printf("%d * %d = %d\n", x, y, res);
    }
    else if (op == '/')
    {
        // 判断除数是否为0
        if (y != 0)
        {
            res = x / y;
            printf("%d / %d = %d\n", x, y, res);
        }
        else
        {
            printf("The divisor cannot be 0\n");
        }
    }
    else
    {
        printf("The input operator is invalid\n");
    }

    return res;    // 返回计算结果
}

// 主函数
int main()
{
    int i, a, b, result;
    char op;

    for (i = 1; i <= 10; i++)
    {
        printf("This is For loop %d\n", i);

        // scanf("%d %c %d", &a, &op, &b);
        printf("Please input the first number: ");
        scanf("%d", &a);
        printf("Please input the operator: ");
        scanf(" %c", &op);
        printf("Please input the second number: ");
        scanf("%d", &b);

        result = calculator(a, b, op);  // 调用计算器函数

        printf("The result is %d\n", result);
    }

    return 0;
}
