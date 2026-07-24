/*
 * 例程 ID：EX-C05-008
 * 标题：教材例程 5.7
 * 教材位置：第 5 章 / 5.7
 * 知识点：while、do-while、for、break、continue
 * 来源：2024-2025-1/20241018_1022/5.7.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>
#include <math.h> //程序中用到数学函数fabs，应包含头文件math.h
int main()
{
    int sign = 1;                         // sign用来表示数值的符号
    double pi = 0.0, n = 1.0, term = 1.0; // pi开始代表多项式的值，最后代表π的值, n代表分母，term代表当前项的值
    while (fabs(term) >= 1e-6)            // 检查当前项term的绝对值是否大于或等于10-6
    {
        pi = pi + term;  // 把当前项term累加到pi中
        n = n + 2;       // n+2是下一项的分母
        sign = -sign;    // sign代表符号，下一项的符号与上一项符号相反
        term = sign / n; // 求出下一项的值term
    }
    pi = pi * 4;               // 多项式的和pi乘以4，才是π的近似值
    printf("pi=%10.8f\n", pi); // 输出π的近似值
    return 0;
}
