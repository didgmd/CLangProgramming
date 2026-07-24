<!-- question-meta
id: QB-FB-021
category: 程序填空
chapters: 6
concepts: 杨辉三角、数组边界
difficulty: 常规
minutes: 8
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 杨辉三角边界诊断

## 题目

补全杨辉三角边界和递推循环，避免访问负下标或本行之外的元素。

无输入；输出：杨辉三角第6行第3项。

```c
#include <stdio.h>
int main(void)
{
    int a[6][6] = {0};
    for (int i = 0; i < 6; i++)
    {
        /*〔1〕*/;
        for (int /*〔2〕*/; /*〔3〕*/ ; j++)
            a[i][j] = /*〔4〕*/;
    }
    printf("%d\n", a[5][2]);
    return 0;
}
```

## 常见失分点


本题围绕“杨辉三角边界诊断”补全杨辉三角、数组边界相关语句。各空代回后应共同检查初始化、循环边界、有效下标或指针范围以及最终输出。

<details>
<summary>参考答案与解析</summary>

### 各空答案

1. `〔1〕`：`a[i][0]=a[i][i]=1`
2. `〔2〕`：`j=1`
3. `〔3〕`：`j<i`
4. `〔4〕`：`a[i-1][j-1]+a[i-1][j]`

### 关键说明

将各空代回后，程序的声明、初始化、循环边界和输出应形成完整逻辑。验证数据：应输出 `10`；内部下标范围必须是 `1<=j<i`。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
int main(void)
{
    int a[6][6] = {0};
    for (int i = 0; i < 6; i++)
    {
        a[i][0] = a[i][i] = 1;
        for (int j = 1; j < i; j++)
        {
            a[i][j] = a[i - 1][j - 1] + a[i - 1][j];
        }
    }
    printf("%d\n", a[5][2]);
    return 0;
}
```
<!-- reference-c:end -->

</details>
