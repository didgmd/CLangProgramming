/*
 * 例程 ID：EX-C07-010
 * 标题：教材例程 7.10
 * 教材位置：第 7 章 / 7.10
 * 知识点：函数、参数、递归、变量作用域
 * 来源：2024-2025-1/20241105_1108/7.10.c
 * 编译模式：gnu99-textbook
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#include <stdio.h>
int main()
{
    float average(float array[10]); // 函数声明
    float score[10], aver;
    int i;
    printf("input 10 scores:\n");
    for (i = 0; i < 10; i++)
        scanf("%f", &score[i]);
    printf("\n");
    aver = average(score); // 调用average函数
    printf("average score is %5.2f\n", aver);
    return 0;
}

float average(float array[10]) // 定义average函数
{
    int i;
    float aver, sum = array[0];
    for (i = 1; i < 10; i++)
        sum = sum + array[i]; // 累加学生成绩
    aver = sum / 10;
    return (aver);
}
