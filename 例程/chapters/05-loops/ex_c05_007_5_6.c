/*
 * 例程 ID：EX-C05-007
 * 标题：教材例程 5.6
 * 教材位置：第 5 章 / 5.6
 * 知识点：while、do-while、for、break、continue
 * 来源：2024-2025-1/20241018_1022/5.6.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>
int main()
{
    int i, j, n = 0;
    for (i = 1; i <= 4; i++)
        for (j = 1; j <= 5; j++, n++) // n用来累计输出数据的个数
        {
            if (n % 5 == 0)
                printf("\n"); // 控制在输出5个数据后换行

            // if (i == 3 && j == 1) break;
            // if (i == 3 && j == 1) continue;

            printf("%d\t", i * j);
        }
    printf("\n");
    return 0;
}
