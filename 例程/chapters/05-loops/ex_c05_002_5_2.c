/*
 * 例程 ID：EX-C05-002
 * 标题：教材例程 5.2
 * 教材位置：第 5 章 / 5.2
 * 知识点：while、do-while、for、break、continue
 * 来源：2024-2025-1/20241018_1022/5.2.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>
int main()
{
    int i = 1, sum = 0;
    do
    {
        sum = sum + i;
        i++;
    } while (i <= 100);
    printf("sum=%d\n", sum);
    return 0;
}
