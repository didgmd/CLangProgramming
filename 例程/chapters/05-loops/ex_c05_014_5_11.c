/*
 * 例程 ID：EX-C05-014
 * 标题：教材例程 5.11
 * 教材位置：第 5 章 / 5.11
 * 知识点：while、do-while、for、break、continue
 * 来源：2024-2025-1/20241018_1022/5.11.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>
int main()
{
    char c;
    c = getchar();    // 输入一个字符给字符变量c
    while (c != '\n') // 检查c的值是否为换行符'\n'
    {
        if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z')) // c如果是字母
        {
            if ((c >= 'W' && c <= 'Z') || (c >= 'w' && c <= 'z'))
                c = c - 22;
            // 如果是26个字母中最后4个字母之一就使c-22
            else
                c = c + 4; // 如果是前面22个字母之一，就使c加4，即变成其后第4个字母
        }
        printf("%c", c); // 输出已改变的字符
        c = getchar();   // 再输入下一个字符给字符变量c
    }
    printf("\n");
    return 0;
}
