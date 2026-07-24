<!-- question-meta
id: QB-FB-013
category: 程序填空
chapters: 5、7
concepts: 函数、浮点运算
difficulty: 常规
minutes: 8
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 调和级数分组求和

## 题目

补全函数，计算从 `1/m` 到 `1/n` 的调和级数部分和。

无输入；输出：`1+1/2+...+1/10` 的值。

```c
#include <stdio.h>
double part(int m, int n)
{
    double /*〔1〕*/;
    for (int i = m; /*〔2〕*/ ; i++)
    /*〔3〕*/;
    return sum;
}
int main(void)
{
    printf("%.6f\n", /*〔4〕*/);
    return 0;
}
```

## 常见失分点


本题围绕“调和级数分组求和”补全函数、浮点运算相关语句。各空代回后应共同检查初始化、循环边界、有效下标或指针范围以及最终输出。

<details>
<summary>参考答案与解析</summary>

### 各空答案

1. `〔1〕`：`sum=0.0`
2. `〔2〕`：`i<=n`
3. `〔3〕`：`sum+=1.0/i`
4. `〔4〕`：`part(1,10)`

### 关键说明

将各空代回后，程序的声明、初始化、循环边界和输出应形成完整逻辑。验证数据：结果应保留6位小数。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
double part(int m, int n)
{
    double sum = 0.0;
    for (int i = m; i <= n; i++)
    {
        sum += 1.0 / i;
    }
    return sum;
}
int main(void)
{
    printf("%.6f\n", part(1, 10));
    return 0;
}
```
<!-- reference-c:end -->

</details>
