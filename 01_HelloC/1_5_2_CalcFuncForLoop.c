#define _CRT_SECURE_NO_WARNINGS 1
#pragma warning(disable: 6031)

#include <stdio.h>

// ����/�������������
int calculator(int x, int y, char op)
{
    int res = 0;    // ��ʼ������������

    // ��������������������Ӧ������
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
        // �жϳ����Ƿ�Ϊ0
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

    return res;    // ���ؼ�����
}

// ������
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

        result = calculator(a, b, op);  // ���ü���������

        printf("The result is %d\n", result);
    }

    return 0;
}