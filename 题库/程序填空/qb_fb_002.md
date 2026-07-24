<!-- question-meta
id: QB-FB-002
category: 程序填空
chapters: 6
concepts: 二维数组、递推
difficulty: 常规
minutes: 8
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 杨辉三角递推

## 题目

补全程序，输出杨辉三角的前7行。

无输入；输出：杨辉三角前7行。

```c
#include <stdio.h>
int main(void)
{
    int a [7] [7] =
    {
        0
    }
    ;
    for(int i = 0; i < 7; i++)
    {
        /*〔1〕*/
        ;
        for(int j = 1;
        /*〔2〕*/
        ; j++) a [i] [j] =
        /*〔3〕*/
        ;
        for(int j = 0;
        /*〔4〕*/
        ; j++) printf("%d%c", a [i] [j], j == i ? '\n' : ' ');
    }
    return 0;
}
```

## 常见失分点


本题围绕“杨辉三角递推”补全二维数组、递推相关语句。各空代回后应共同检查初始化、循环边界、有效下标或指针范围以及最终输出。

<details>
<summary>参考答案与解析</summary>

### 各空答案

1. `〔1〕`：`a[i][0]=a[i][i]=1`
2. `〔2〕`：`j<i`
3. `〔3〕`：`a[i-1][j-1]+a[i-1][j]`
4. `〔4〕`：`j<=i`

### 关键说明

将各空代回后，程序的声明、初始化、循环边界和输出应形成完整逻辑。验证数据：第1行应为 `1`，第7行应为 `1 6 15 20 15 6 1`。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
int main(void)
{
    int a [7] [7] =
    {
        0
    }
    ;
    for(int i = 0; i < 7; i++)
    {
        a [i] [0] = a [i] [i] = 1;
        for(int j = 1; j < i; j++) a [i] [j] = a [i - 1] [j - 1] + a [i - 1] [j];
        for(int j = 0; j <= i; j++) printf("%d%c", a [i] [j], j == i ? '\n' : ' ');
    }
    return 0;
}
```
<!-- reference-c:end -->

</details>
