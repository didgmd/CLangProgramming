/*
 * 例程 ID：EX-C07-022
 * 标题：实验演示 lab5.10
 * 教材位置：第 7 章 / lab5.10
 * 知识点：函数、参数、递归、变量作用域
 * 来源：2023-2024-1/14_Lab5/10.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>

int fibonacci(int n) {
    if (n <= 1) {
        return n;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    int n = 10;
    for (int i = 0; i < n; i++) {
        printf("%d ", fibonacci(i));
    }
    printf("\n");

    return 0;
}
