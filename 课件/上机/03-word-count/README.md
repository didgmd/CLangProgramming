# CW-LAB03 统计一行中的单词数

- 状态：`ready`
- 已学章节：第1–5章
- 题目 ID：`QB-PG-012`
- 时长：90分钟（90 min）

实验报告提交：填写教师发放的实验报告模板，完成后保存为PDF格式并提交至超星学习通。

## 实验项目

单词数量统计

## 实验目的

1. 理解单词边界以及空格、制表符形成的分隔关系。
2. 掌握逐字符循环和`in_word`状态变量的切换方法。
3. 能够正确处理连续空白、首尾空白和空行。

## 实验步骤

1. 阅读题目：读入一行字符，统计由空白分隔的单词个数。样例输入`C language practice`，样例输出`3`。
2. 设置`count=0`和`in_word=0`，使用`int ch`保存当前字符。
3. 使用`getchar()`逐字符读取；非空白且`in_word`为0时开始一个新单词并增加`count`，空白字符使`in_word`恢复为0。
4. 完成状态切换、单词计数和整数结果输出的程序。
5. 运行程序，逐字符观察`in_word`从0到1以及从1到0的变化。
6. 使用下表逐项核对，并把状态变化和实际结果填写到实验报告。

| 输入 | 预期输出 | 观察重点 |
|---|---:|---|
| （直接回车） | 0 | 空行 |
| C | 1 | 单个单词 |
| C　　language | 2 | 连续空格 |
| 　C language　 | 2 | 首尾空格 |
| C language practice | 3 | 普通句子 |

<div style="break-after: page; page-break-after: always;"></div>
## 参考完整程序

```c
#include <stdio.h>

int main(void)
{
    int ch;
    int count = 0;
    int in_word = 0;

    while ((ch = getchar()) != '\n' && ch != EOF)
    {
        int blank = ch == ' ' || ch == '\t';
        if (!blank && !in_word)
        {
            count++;
            in_word = 1;
        }
        else if (blank)
        {
            in_word = 0;
        }
    }

    printf("%d\n", count);
    return 0;
}
```
