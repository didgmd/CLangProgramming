/*
 * 例程 ID：EX-C08-032
 * 标题：教材例程 custom-in_class
 * 教材位置：第 8 章 / custom-in_class
 * 知识点：指针、数组与指针、字符串指针、动态内存
 * 来源：2024-2025-1/20241112_1115/In-Class.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>

int main(void)
{
    int c[4][5] = {{1, 2, 3, 4, 5}, {6, 7, 8, 9, 10}, {11, 12, 13, 14, 15}, {16, 17, 18, 19, 20}};
    int(*cp)[5];
    cp = c;
    printf("%d\n", *cp[2] + 3);   // 14
    printf("%d\n", *(c + 2)[0]);  // 11
    printf("%d\n", *(cp + 2)[0]); // 11
    printf("%d\n", *cp[2]);       // 11
    printf("%d\n", (*cp)[2]);     // 3
    printf("%d\n", (*cp)[12]);    // 13
    printf("%d\n", *(*cp + 2));   // 3
    return 0;
}
