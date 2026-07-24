/*
 * 例程 ID：EX-C05-009
 * 标题：教材例程 5.8.1
 * 教材位置：第 5 章 / 5.8.1
 * 知识点：while、do-while、for、break、continue
 * 来源：2024-2025-1/20241018_1022/5.8.1.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>
int main()
{
    int f1 = 1, f2 = 1, f3;
    int i;
    printf("%12d\n%12d\n", f1, f2);
    for (i = 1; i <= 38; i++)
    {
        f3 = f1 + f2;
        printf("%12d\n", f3);
        f1 = f2;
        f2 = f3;
    }
    return 0;
}
