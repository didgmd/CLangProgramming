/*
 * 例程 ID：EX-C05-001
 * 标题：教材例程 5.1
 * 教材位置：第 5 章 / 5.1
 * 知识点：while、do-while、for、break、continue
 * 来源：2024-2025-1/20241018_1022/5.1.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：deterministic
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>
int main()
{
    int i = 1, sum = 0; // 定义变量i的初值为1,sum的初值为0
    while (i <= 100)    // 当i>100，条件表达式i<=100的值为假，不执行循环体
    {                   // 循环体开始
        sum = sum + i;  // 第1次累加后，sum的值为1
        i++;            // 加完后，i的值加1，为下次累加做准备
    } // 循环体结束
    printf("sum=%d\n", sum); // 输出1+2+3…+100的累加和
    return 0;
}
