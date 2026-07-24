/*
 * 例程 ID：EX-C04-008
 * 标题：教材例程 4.6
 * 教材位置：第 4 章 / 4.6
 * 知识点：if、switch、条件表达式
 * 来源：2024-2025-1/20241011_1015/4.6.c
 * 编译模式：gnu99-textbook
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：教材兼容配置：保留与教材或旧版编译器相关的写法。
 */
#include <stdio.h>
int main()
{
    char grade;
    scanf("%c", &grade);
    printf("Your score:");
    switch (grade)
    {
    case 'A':
        printf("85～100\n");
        break;
    case 'B':
        printf("70～84\n");
        break;
    case 'C':
        printf("60～69\n");
        break;
    case 'D':
        printf("<60\n");
        break;
    default:
        printf("enter data error!\n");
    }
    return 0;
}
