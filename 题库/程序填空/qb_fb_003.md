<!-- question-meta
id: QB-FB-003
category: 程序填空
chapters: 6、7
concepts: 冒泡排序、函数
difficulty: 常规
minutes: 8
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 冒泡排序

## 题目

补全冒泡排序函数，把10个整数按升序排列并输出。

输入：10个整数；输出：升序排列结果。

```c
#include <stdio.h>
void bubble(int a[], int n)
{
    for (int i = 0; /*〔1〕*/ ; i++)
        for (int j = 0; /*〔2〕*/ ; j++)
            if ( /*〔3〕*/ )
            {
                int t = a[j];
                a[j] = a[j + 1];
                a[j + 1] = t;
            }
}
int main(void)
{
    int a[10];
    for (int i = 0; i < 10; i++)
    if (scanf("%d", &a[i]) != 1)
    return 1;
    /*〔4〕*/;
    for (int i = 0; i < 10; i++)
    printf("%d%c", a[i], i == 9 ? '\n' : ' ');
    return 0;
}
```

## 常见失分点


本题围绕“冒泡排序”补全冒泡排序、函数相关语句。各空代回后应共同检查初始化、循环边界、有效下标或指针范围以及最终输出。

<details>
<summary>参考答案与解析</summary>

### 各空答案

1. `〔1〕`：`i<n-1`
2. `〔2〕`：`j<n-1-i`
3. `〔3〕`：`a[j]>a[j+1]`
4. `〔4〕`：`bubble(a,10)`

### 关键说明

将各空代回后，程序的声明、初始化、循环边界和输出应形成完整逻辑。验证数据：输入 `10 9 8 7 6 5 4 3 2 1` 应输出升序序列。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
void bubble(int a[], int n)
{
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < n - 1 - i; j++)
        {
            if (a[j] > a[j + 1])
            {
                int t = a[j];
                a[j] = a[j + 1];
                a[j + 1] = t;
            }
        }
    }
}
int main(void)
{
    int a[10];
    for (int i = 0; i < 10; i++)
    {
        if (scanf("%d", &a[i]) != 1)
        {
            return 1;
        }
    }
    bubble(a, 10);
    for (int i = 0; i < 10; i++)
    {
        printf("%d%c", a[i], i == 9 ? '\n' : ' ');
    }
    return 0;
}
```
<!-- reference-c:end -->

</details>
