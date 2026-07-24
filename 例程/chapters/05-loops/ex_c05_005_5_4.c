/*
 * 例程 ID：EX-C05-005
 * 标题：教材例程 5.4
 * 教材位置：第 5 章 / 5.4
 * 知识点：while、do-while、for、break、continue
 * 来源：2024-2025-1/20241018_1022/5.4.c
 * 编译模式：gnu99-textbook
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#include <stdio.h>
#define SUM 100000 // 指定符号常量SUM代表10万
int main()
{
    float amount, aver, total;
    int i;
    for (i = 1, total = 0; i <= 1000; i++)
    {
        printf("please enter amount:");
        scanf("%f", &amount);
        total = total + amount;
        if (total >= SUM)
            break;
    }
    aver = total / i;
    printf("num=%d\naver=%10.2f\n", i, aver);
    return 0;
}
