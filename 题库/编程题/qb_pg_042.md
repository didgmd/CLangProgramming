<!-- question-meta
id: QB-PG-042
category: 编程题
chapters: 10
concepts: 文件指针、格式化文件读写、累计与最大值
difficulty: 综合
minutes: 30
related_routines: EX-C10-001、EX-C10-002
compile_mode: c11-strict
legacy_features: 无
-->
# 成绩文件统计

## 题目

输入5个学生成绩。将成绩逐行写入文本文件`scores.txt`，关闭文件后重新以读方式打开，读取全部成绩并计算平均分和最高分。

### 输入格式

一行输入5个`double`范围内的成绩，以空白字符分隔。

### 输出格式

第一行按`average=平均分`输出平均分，第二行按`maximum=最高分`输出最高分，均保留两位小数。

### 数据范围与边界

恰输入5个格式合法的成绩。程序必须检查两次`fopen()`的结果，并关闭所有已经成功打开的文件。

### 样例输入

```text
60 70 80 90 100
```

### 样例输出

```text
average=80.00
maximum=100.00
```

## 常见失分点

- 混淆`"w"`和`"r"`两种打开模式；
- 未检查`fopen()`是否返回`NULL`；
- 写入后没有关闭文件，便直接重新打开读取；
- `fprintf()`或`fscanf()`的格式说明符与`double`不匹配；
- 最高分没有使用读回的第一个真实成绩初始化；
- 遗漏关闭已经成功打开的文件；
- 平均分或最高分没有按题目要求保留两位小数。

<details>
<summary>参考答案与解析</summary>

**解题思路：** 先读入5个成绩并用`fprintf()`写入文件。关闭文件后重新以`"r"`方式打开，用`fscanf()`读回数据，在读取过程中累计总分并更新最高分。

**评分建议：** 文件打开与检查2分，写入并关闭2分，重新打开与读取2分，统计计算2分，输出格式和资源关闭2分。

**正常与边界测试：** 普通成绩；全部相等；包含小数的成绩。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>

int main(void)
{
    double scores[5];
    double score;
    double sum = 0.0;
    double maximum = 0.0;
    FILE *fp;
    int i;

    for (i = 0; i < 5; i++)
    {
        if (scanf("%lf", &scores[i]) != 1)
        {
            return 1;
        }
    }

    fp = fopen("scores.txt", "w");
    if (fp == NULL)
    {
        return 1;
    }

    for (i = 0; i < 5; i++)
    {
        fprintf(fp, "%.2f\n", scores[i]);
    }

    fclose(fp);

    fp = fopen("scores.txt", "r");
    if (fp == NULL)
    {
        return 1;
    }

    for (i = 0; i < 5; i++)
    {
        if (fscanf(fp, "%lf", &score) != 1)
        {
            fclose(fp);
            return 1;
        }

        if (i == 0 || score > maximum)
        {
            maximum = score;
        }

        sum += score;
    }

    fclose(fp);

    printf("average=%.2f\n", sum / 5.0);
    printf("maximum=%.2f\n", maximum);

    return 0;
}
```
<!-- reference-c:end -->

</details>
