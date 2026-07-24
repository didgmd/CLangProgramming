/*
 * 例程 ID：EX-C05-011
 * 标题：教材例程 5.9.1
 * 教材位置：第 5 章 / 5.9.1
 * 知识点：while、do-while、for、break、continue
 * 来源：2024-2025-1/20241018_1022/5.9.1.c
 * 编译模式：gnu99-textbook
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#include <stdio.h>
int main()
{
    int n, i;
    printf("please enter a integer number,n=?");
    scanf("%d", &n);
    for (i = 2; i < n; i++)
        if (n % i == 0)
            break;
    if (i < n)
        printf("%d is not a prime number.\n", n);
    else
        printf("%d is a prime number.\n", n);
    return 0;
}
