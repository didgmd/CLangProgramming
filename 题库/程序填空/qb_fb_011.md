<!-- question-meta
id: QB-FB-011
category: 程序填空
chapters: 5
concepts: 素数、循环
difficulty: 常规
minutes: 8
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 判断素数

## 题目

输入一个整数，补全试除过程并判断它是否为素数。

输入：一个整数；输出：`prime` 或 `not prime`。

```c
#include <stdio.h>
int main(void)
{
    int n, prime = 1;
    if (scanf("%d", &n) != 1)
    return 1;
    if ( /*〔1〕*/ )
    /*〔4〕*/;
    for (int i = 2; /*〔2〕*/ ; i++)
        if ( /*〔3〕*/ )
            prime = 0;
    puts(prime ? "prime" : "not prime");
    return 0;
}
```

## 常见失分点


本题围绕“判断素数”补全素数、循环相关语句。各空代回后应共同检查初始化、循环边界、有效下标或指针范围以及最终输出。

<details>
<summary>参考答案与解析</summary>

### 各空答案

1. `〔1〕`：`n<2`
2. `〔2〕`：`i*i<=n&&prime`
3. `〔3〕`：`n%i==0`
4. `〔4〕`：`prime=0`

### 关键说明

将各空代回后，程序的声明、初始化、循环边界和输出应形成完整逻辑。验证数据：`2` 为素数，`1` 不是素数。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
int main(void)
{
    int n, prime = 1;
    if (scanf("%d", &n) != 1)
    {
        return 1;
    }
    if (n < 2)
    {
        prime = 0;
    }
    for (int i = 2; i * i <= n && prime; i++)
    {
        if (n % i == 0)
        {
            prime = 0;
        }
    }
    puts(prime ? "prime" : "not prime");
    return 0;
}
```
<!-- reference-c:end -->

</details>
