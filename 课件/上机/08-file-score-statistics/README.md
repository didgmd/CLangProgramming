# CW-LAB08 成绩文件统计

- 状态：`ready`
- 已学章节：第1–10章
- 题目 ID：`QB-PG-042`
- 时长：90分钟（90 min）

实验报告提交：填写教师发放的实验报告模板，完成后保存为PDF格式并提交至超星学习通。

## 实验项目

成绩文件统计

## 实验目的

1. 掌握文本文件的打开、写入、关闭和重新读取过程。
2. 掌握格式化文件输入输出函数的使用方法。
3. 能够根据文件中的成绩计算平均值和最高值。

## 实验步骤

1. 阅读题目：输入5个`double`成绩，将其逐行写入`scores.txt`，重新读取后计算平均分和最高分。输入`60 70 80 90 100`时输出`average=80.00`和`maximum=100.00`。
2. 声明写文件流、读文件流、当前成绩、总分和最高分变量。
3. 以`"w"`方式打开文件并使用`fprintf()`逐行写入，关闭后以`"r"`方式重新打开，再使用`fscanf()`读取成绩。
4. 按照输入与写入、关闭与重开、读取与统计、关闭与输出的顺序完成程序，并检查两次文件打开结果。
5. 运行程序，观察`scores.txt`的五行内容，以及总分和最高分在读取过程中的变化。
6. 使用下表逐项核对，并把屏幕输出和生成的文件内容填写到实验报告。

| 输入 | `scores.txt`预期内容 | 预期输出 |
|---|---|---|
| 60 70 80 90 100 | `60.00`至`100.00`各占一行 | `average=80.00`；`maximum=100.00` |
| 75 75 75 75 75 | 五行`75.00` | `average=75.00`；`maximum=75.00` |
| 60.5 70.25 80 90.75 98.5 | 五个成绩均保留两位小数 | `average=80.00`；`maximum=98.50` |

<div style="break-after: page; page-break-after: always;"></div>
## 参考完整程序

```c
#include <stdio.h>

int main(void)
{
    FILE *write_file;
    FILE *read_file;
    double score;
    double total = 0.0;
    double maximum = 0.0;

    write_file = fopen("scores.txt", "w");
    if (write_file == NULL)
    {
        return 1;
    }

    for (int i = 0; i < 5; i++)
    {
        scanf("%lf", &score);
        fprintf(write_file, "%.2f\n", score);
    }
    fclose(write_file);

    read_file = fopen("scores.txt", "r");
    if (read_file == NULL)
    {
        return 1;
    }

    for (int i = 0; i < 5; i++)
    {
        fscanf(read_file, "%lf", &score);
        if (i == 0 || score > maximum)
        {
            maximum = score;
        }
        total += score;
    }
    fclose(read_file);

    printf("average=%.2f\n", total / 5.0);
    printf("maximum=%.2f\n", maximum);
    return 0;
}
```
