/*
 * 例程 ID：EX-C10-004
 * 标题：教材例程 10.3.2
 * 教材位置：第 10 章 / 10.3.2
 * 知识点：文件、顺序读写、随机读写、错误检测
 * 来源：2024-2025-1/20241129/10.3.2.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>
#include <stdlib.h>
int main()
{
    FILE *fp;
    char str[3][10];
    int i = 0;
    if ((fp = fopen("D:\\CC\\string.dat", "r")) == NULL) // 注意文件路径必须与前相同
    {
        printf("can′t open file!\n");
        exit(0);
    }
    while (fgets(str[i], 10, fp) != NULL)
    {
        printf("%s", str[i]);
        i++;
    }
    fclose(fp);
    return 0;
}
