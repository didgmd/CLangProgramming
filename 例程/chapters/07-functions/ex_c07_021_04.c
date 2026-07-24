/*
 * 例程 ID：EX-C07-021
 * 标题：实验演示 lab5.4
 * 教材位置：第 7 章 / lab5.4
 * 知识点：函数、参数、递归、变量作用域
 * 来源：2023-2024-1/14_Lab5/04.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>

int factorial(int n) {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

int main() {
    int n = 5;
    int result = factorial(n);
    printf("%d! = %d\n", n, result);

    return 0;
}
