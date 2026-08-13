# CW-LAB01 日期是当年第几天

- 状态：`ready`
- 已学章节：第1–4章
- 题目 ID：`QB-PG-005`
- 时长：90分钟（90 min）

实验报告提交：填写教师发放的实验报告模板，完成后保存为PDF格式并提交至超星学习通。

## 实验项目

日期序号计算

## 实验目的

1. 掌握闰年判断及二月天数的确定方法。
2. 掌握`switch`贯穿与日期累计方法。
3. 提高分支程序的编写、运行和调试能力。

## 实验步骤

1. 阅读题目：输入符合公历规则的年、月、日，输出该日期是当年的第几天。样例输入`2024 2 29`，样例输出`60`。
2. 确定`year`、`month`、`day`、闰年状态、二月天数和累计天数等变量。
3. 写出闰年判断条件；令累计天数从当前日开始，使用`switch`贯穿依次加入此前月份的天数。
4. 在`main`函数中依次完成数据读取、闰年判断、月份累计和整数结果输出。
5. 运行程序，观察不同月份进入`switch`后累计值的变化。
6. 使用下表逐项核对，并把实际结果填写到实验报告。

| 输入 | 预期输出 | 观察重点 |
|---|---:|---|
| 2024 1 1 | 1 | 闰年年初 |
| 2024 2 29 | 60 | 闰年2月29日 |
| 2023 3 1 | 60 | 普通年3月1日 |
| 2023 12 31 | 365 | 普通年年末 |

<div style="break-after: page; page-break-after: always;"></div>
## 参考完整程序

```c
#include <stdio.h>

int main(void)
{
    int year, month, day;
    int leap;
    int february = 28;
    int total;

    scanf("%d%d%d", &year, &month, &day);

    leap = (year % 400 == 0) || (year % 4 == 0 && year % 100 != 0);
    if (leap)
    {
        february = 29;
    }

    total = day;
    switch (month)
    {
        case 12: total += 30; /* fall through */
        case 11: total += 31; /* fall through */
        case 10: total += 30; /* fall through */
        case 9: total += 31;  /* fall through */
        case 8: total += 31;  /* fall through */
        case 7: total += 30;  /* fall through */
        case 6: total += 31;  /* fall through */
        case 5: total += 30;  /* fall through */
        case 4: total += 31;  /* fall through */
        case 3: total += february; /* fall through */
        case 2: total += 31;  /* fall through */
        case 1: break;
    }

    printf("%d\n", total);
    return 0;
}
```
