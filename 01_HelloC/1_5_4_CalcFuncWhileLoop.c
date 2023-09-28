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

    i = 1;
    while (1)
    {
        printf("This is For loop %d\n", i);

        // scanf("%d %c %d", &a, &op, &b);
        printf("Please input the operator (Input ! to exit): ");
        scanf(" %c", &op);

        // 根据输入 op 判断是否退出
        if (op == '!')
        {
            printf("Bye!\n");
            break;
        }

        printf("Please input the first number: ");
        scanf("%d", &a);
        printf("Please input the second number: ");
        scanf("%d", &b);

        result = calculator(a, b, op);  // 调用计算器函数

        printf("The result is %d\n", result);

        i++;
    }

    return 0;
}