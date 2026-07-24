<!-- question-meta
id: QB-FB-014
category: 程序填空
chapters: 6
concepts: 字符串、数值转换
difficulty: 常规
minutes: 8
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 数字字符串转整数

## 题目

输入一个可带正负号的十进制数字字符串，将其转换为整数。

输入：一个数字字符串；输出：对应整数或 `invalid`。

```c
#include <stdio.h>
int main(void)
{
    char s[32];
    if (scanf("%31s", s) != 1)
    return 1;
    int i = 0, /*〔1〕*/, n = 0;
    if ( /*〔2〕*/ )
    {
        if (s[i] == '-')
        /*〔3〕*/;
        i++;
    }
    for (; s[i] != '\0'; i++)
    {
        if (s[i] < '0' || s[i] > '9')
        {
            puts("invalid");
            return 0;
        }
        /*〔4〕*/;
    }
    printf("%d\n", sign * n);
    return 0;
}
```

## 常见失分点


本题围绕“数字字符串转整数”补全字符串、数值转换相关语句。各空代回后应共同检查初始化、循环边界、有效下标或指针范围以及最终输出。

<details>
<summary>参考答案与解析</summary>

### 各空答案

1. `〔1〕`：`sign=1`
2. `〔2〕`：`s[i]=='-'||s[i]=='+'`
3. `〔3〕`：`sign=-1`
4. `〔4〕`：`n=n*10+s[i]-'0'`

### 关键说明

将各空代回后，程序的声明、初始化、循环边界和输出应形成完整逻辑。验证数据：输入 `-2048` 应输出 `-2048`。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
int main(void)
{
    char s[32];
    if (scanf("%31s", s) != 1)
    {
        return 1;
    }
    int i = 0, sign = 1, n = 0;
    if (s[i] == '-' || s[i] == '+')
    {
        if (s[i] == '-')
        {
            sign = -1;
        }
        i++;
    }
    for (; s[i] != '\0'; i++)
    {
        if (s[i] < '0' || s[i] > '9')
        {
            puts("invalid");
            return 0;
        }
        n = n * 10 + s[i] - '0';
    }
    printf("%d\n", sign * n);
    return 0;
}
```
<!-- reference-c:end -->

</details>
