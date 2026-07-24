/*
 * 例程 ID：EX-C07-023
 * 标题：实验演示 lab5.11
 * 教材位置：第 7 章 / lab5.11
 * 知识点：函数、参数、递归、变量作用域
 * 来源：2023-2024-1/14_Lab5/11.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>

double estimatePI(int n) {
    double pi = 0;
    int sign = 1;

    for (int i = 0; i < n; i++) {
        double term = 1.0 / (2 * i + 1);
        pi += sign * term;
        sign = -sign;
    }

    return 4 * pi;
}

int main() {
    int n = 10000;
    double result = estimatePI(n);
    printf("Estimated PI = %f\n", result);
    return 0;
}
