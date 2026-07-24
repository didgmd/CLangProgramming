/*
 * 例程 ID：EX-C08-039
 * 标题：实验演示 lab5.3
 * 教材位置：第 8 章 / lab5.3
 * 知识点：指针、数组与指针、字符串指针、动态内存
 * 来源：2023-2024-1/14_Lab5/03.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>

void modifyValue(int* num) {
    *num = *num * 2;
}

int main() {
    int value = 10;
    modifyValue(&value);
    printf("Modified value: %d\n", value);

    return 0;
}
