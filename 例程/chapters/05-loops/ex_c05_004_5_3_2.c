/*
 * 例程 ID：EX-C05-004
 * 标题：教材例程 5.3.2
 * 教材位置：第 5 章 / 5.3.2
 * 知识点：while、do-while、for、break、continue
 * 来源：2024-2025-1/20241018_1022/5.3.2.c
 * 编译模式：gnu99-textbook
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#include <stdio.h>
int main()
{
    int i, sum = 0;
    printf("please enter i,i=?");
    scanf("%d", &i);
    do
    {
        sum = sum + i;
        i++;
    } while (i <= 10);
    printf("sum=%d\n", sum);
    return 0;
}
