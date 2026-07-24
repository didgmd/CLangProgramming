<!-- question-meta
id: QB-FB-016
category: 程序填空
chapters: 6
concepts: 字符串、逆序
difficulty: 常规
minutes: 8
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 字符串正序后接逆序

## 题目

输入一个无空格字符串，输出其正序内容后紧接逆序内容。

输入：长度不超过49的无空格字符串；输出：正序串与逆序串的连接。

```c
#include <stdio.h>
#include <string.h>
int main(void)
{
    char s[50], d[100];
    if (scanf("%49s", s) != 1)
    return 1;
    int n = (int)
    /*〔1〕*/;
    for (int i = 0; i < n; i++)
    /*〔2〕*/;
    for (int i = 0; i < n; i++)
    d[n + i] = /*〔3〕*/;
    /*〔4〕*/;
    puts(d);
    return 0;
}
```

## 常见失分点


本题围绕“字符串正序后接逆序”补全字符串、逆序相关语句。各空代回后应共同检查初始化、循环边界、有效下标或指针范围以及最终输出。

<details>
<summary>参考答案与解析</summary>

### 各空答案

1. `〔1〕`：`strlen(s)`
2. `〔2〕`：`d[i]=s[i]`
3. `〔3〕`：`s[n-1-i]`
4. `〔4〕`：`d[2*n]='\0'`

### 关键说明

将各空代回后，程序的声明、初始化、循环边界和输出应形成完整逻辑。验证数据：输入 `abc` 应输出 `abccba`。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
#include <string.h>
int main(void)
{
    char s[50], d[100];
    if (scanf("%49s", s) != 1)
    {
        return 1;
    }
    int n = (int) strlen(s);
    for (int i = 0; i < n; i++)
    {
        d[i] = s[i];
    }
    for (int i = 0; i < n; i++)
    {
        d[n + i] = s[n - 1 - i];
    }
    d[2 * n] = '\0';
    puts(d);
    return 0;
}
```
<!-- reference-c:end -->

</details>
