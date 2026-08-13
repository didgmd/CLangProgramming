# CW-LAB02 四类字符统计

- 状态：`ready`
- 已学章节：第1–5章
- 题目 ID：`QB-PG-019`
- 时长：90分钟（90 min）

实验报告提交：填写教师发放的实验报告模板，完成后保存为PDF格式并提交至超星学习通。

## 实验项目

四类字符统计

## 实验目的

1. 理解字符编码与英文字母、数字、空格和其他字符的分类条件。
2. 掌握`getchar()`逐字符读取和分类计数器的使用方法。
3. 能够使用混合字符、空行、纯数字和连续空格核对边界输入。

## 实验步骤

1. 阅读题目：读入一行字符，统计英文字母、数字、空格和其他字符的数量，按该顺序输出四个计数。样例输入`Ab 3!`，样例输出`2 1 1 1`。
2. 使用`letters`、`digits`、`spaces`和`others`四个整型计数器保存分类结果，使用`int ch`保存当前字符。
3. 使用`getchar()`逐字符读取；依次写出字母、数字、普通空格和其他字符的互斥分类条件，换行或`EOF`表示本行结束。
4. 完成循环、四类计数和按固定顺序输出的程序。
5. 运行程序，逐字符观察`ch`所属类别及相应计数器的变化。
6. 使用下表逐项核对，并把每一类的实际计数填写到实验报告。

| 输入 | 预期输出 | 观察重点 |
|---|---:|---|
| Ab 3! | 2 1 1 1 | 四类字符同时出现 |
| （直接回车） | 0 0 0 0 | 空行 |
| 12345 | 0 5 0 0 | 纯数字 |
| 三个普通空格 | 0 0 3 0 | 连续空格 |

<div style="break-after: page; page-break-after: always;"></div>
## 参考完整程序

```c
#include <stdio.h>

int main(void)
{
    int ch;
    int letters = 0;
    int digits = 0;
    int spaces = 0;
    int others = 0;

    while ((ch = getchar()) != '\n' && ch != EOF)
    {
        if ((ch >= 'A' && ch <= 'Z') || (ch >= 'a' && ch <= 'z'))
        {
            letters++;
        }
        else if (ch >= '0' && ch <= '9')
        {
            digits++;
        }
        else if (ch == ' ')
        {
            spaces++;
        }
        else
        {
            others++;
        }
    }

    printf("%d %d %d %d\n", letters, digits, spaces, others);
    return 0;
}
```
