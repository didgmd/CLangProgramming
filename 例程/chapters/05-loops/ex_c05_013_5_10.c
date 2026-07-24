/*
 * 例程 ID：EX-C05-013
 * 标题：教材例程 5.10
 * 教材位置：第 5 章 / 5.10
 * 知识点：while、do-while、for、break、continue
 * 来源：2024-2025-1/20241018_1022/5.10.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>
#include <math.h>
int main()
{
    int n, k, i, m = 0;
    for (n = 101; n <= 200; n = n + 2) // n从100变化到200，对每个奇数n进行判定
    {
        k = sqrt(n);
        for (i = 2; i <= k; i++)
            if (n % i == 0)
                break;  // 如果n被i整除，终止内循环，此时i<k+1
        if (i >= k + 1) // 若i>=k+1，表示n未曾被整除
        {
            printf("%d ", n); // 应确定n是素数
            m = m + 1;        // m用来控制换行，一行内输出10个素数
        }
        if (m % 10 == 0)
            printf("\n"); // m累计到10的倍数，换行
    }
    printf("\n");
    return 0;
}
