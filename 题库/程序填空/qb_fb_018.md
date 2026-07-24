<!-- question-meta
id: QB-FB-018
category: 程序填空
chapters: 6
concepts: 字符串输入
difficulty: 常规
minutes: 8
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 限制长度读取单词

## 题目

字符数组长度为10，补全 `scanf` 格式串，最多读入9个非空白字符。

输入：一个单词；输出：安全读入的最多9个字符。

```c
#include <stdio.h>
int main(void)
{
    char word[10];
    if (scanf( /*〔1〕*/, word) != 1)
        return 1;
    puts(word);
    return 0;
}
```

## 常见失分点


本题围绕“限制长度读取单词”补全字符串输入相关语句。各空代回后应共同检查初始化、循环边界、有效下标或指针范围以及最终输出。

<details>
<summary>参考答案与解析</summary>

### 各空答案

1. `〔1〕`：`"%9s"`

### 关键说明

将各空代回后，程序的声明、初始化、循环边界和输出应形成完整逻辑。验证数据：格式宽度不包含字符串末尾自动添加的 `\0`。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
int main(void)
{
    char word[10];
    if (scanf("%9s", word) != 1)
    {
        return 1;
    }
    puts(word);
    return 0;
}
```
<!-- reference-c:end -->

</details>
