<!-- question-meta
id: QB-FB-005
category: 程序填空
chapters: 6
concepts: 数组逆序
difficulty: 常规
minutes: 8
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 数组逆序

## 题目

补全程序，把给定7个整数原地逆序后输出。

无输入；输出：逆序后的7个整数。

```c
#include <stdio.h>
int main(void)
{
    int a[7] = {12, 9, 16, 5, 7, 2, 1};
    for (int k = 0; /*〔1〕*/ ; k++)
    {
        int t = /*〔2〕*/;
        a[k] = /*〔3〕*/;
        /*〔4〕*/;
    }
    for (int k = 0; k < 7; k++)
    printf("%d%c", a[k], k == 6 ? '\n' : ' ');
    return 0;
}
```

## 常见失分点


本题围绕“数组逆序”补全数组逆序相关语句。各空代回后应共同检查初始化、循环边界、有效下标或指针范围以及最终输出。

<details>
<summary>参考答案与解析</summary>

### 各空答案

1. `〔1〕`：`k<7/2`
2. `〔2〕`：`a[k]`
3. `〔3〕`：`a[6-k]`
4. `〔4〕`：`a[6-k]=t`

### 关键说明

将各空代回后，程序的声明、初始化、循环边界和输出应形成完整逻辑。验证数据：应输出 `1 2 7 5 16 9 12`。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
int main(void)
{
    int a[7] = {12, 9, 16, 5, 7, 2, 1};
    for (int k = 0; k < 7 / 2; k++)
    {
        int t = a[k];
        a[k] = a[6 - k];
        a[6 - k] = t;
    }
    for (int k = 0; k < 7; k++)
    {
        printf("%d%c", a[k], k == 6 ? '\n' : ' ');
    }
    return 0;
}
```
<!-- reference-c:end -->

</details>
