<!-- question-meta
id: QB-FB-009
category: 程序填空
chapters: 6
concepts: 数组、平均值
difficulty: 常规
minutes: 8
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 求数组平均值

## 题目

输入8个实数，补全程序并输出它们的平均值。

输入：8个实数；输出：平均值，保留2位小数。

```c
#include <stdio.h>
int main(void)
{
    double a [8],
    /*〔1〕*/
    ;
    for(int i = 0; i < 8; i++)
    {
        if(scanf("%lf", & a [i]) != 1) return 1;
        /*〔2〕*/
        ;
    }
    printf("%.2f\n",
    /*〔3〕*/
    );
    return 0;
}
```

## 常见失分点


本题围绕“求数组平均值”补全数组、平均值相关语句。各空代回后应共同检查初始化、循环边界、有效下标或指针范围以及最终输出。

<details>
<summary>参考答案与解析</summary>

### 各空答案

1. `〔1〕`：`sum=0.0`
2. `〔2〕`：`sum+=a[i]`
3. `〔3〕`：`sum/8.0`

### 关键说明

将各空代回后，程序的声明、初始化、循环边界和输出应形成完整逻辑。验证数据：输入 `1 2 3 4 5 6 7 8` 应输出 `4.50`。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
int main(void)
{
    double a [8], sum = 0.0;
    for(int i = 0; i < 8; i++)
    {
        if(scanf("%lf", & a [i]) != 1) return 1;
        sum += a [i];
    }
    printf("%.2f\n", sum / 8.0);
    return 0;
}
```
<!-- reference-c:end -->

</details>
