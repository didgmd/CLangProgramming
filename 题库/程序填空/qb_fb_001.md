<!-- question-meta
id: QB-FB-001
category: 程序填空
chapters: 6
concepts: 字符统计、数组
difficulty: 常规
minutes: 8
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 统计大写字母

## 题目

输入一行字符，以字符 `#` 结束，统计其中大写英文字母的个数。

输入：一行以 `#` 结束的字符；输出：大写字母个数。

```c
#include <stdio.h>
int main(void)
{
    int ch, count = 0;
    while ((ch = /*〔1〕*/ ) != '#' && ch != EOF)
    {
        if ( /*〔2〕*/ )
        /*〔3〕*/;
    }
    printf("%d\n", count);
    return 0;
}
```

## 常见失分点


本题围绕“统计大写字母”补全字符统计、数组相关语句。各空代回后应共同检查初始化、循环边界、有效下标或指针范围以及最终输出。

<details>
<summary>参考答案与解析</summary>

### 各空答案

1. `〔1〕`：`getchar()`
2. `〔2〕`：`ch>='A'&&ch<='Z'`
3. `〔3〕`：`count++`

### 关键说明

将各空代回后，程序的声明、初始化、循环边界和输出应形成完整逻辑。验证数据：`AbC12#` 应输出 `2`。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
int main(void)
{
    int ch, count = 0;
    while ((ch = getchar()) != '#' && ch != EOF)
    {
        if (ch >= 'A' && ch <= 'Z')
        {
            count++;
        }
    }
    printf("%d\n", count);
    return 0;
}
```
<!-- reference-c:end -->

</details>
