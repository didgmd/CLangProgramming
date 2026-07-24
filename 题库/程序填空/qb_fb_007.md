<!-- question-meta
id: QB-FB-007
category: 程序填空
chapters: 6
concepts: 字符分类、计数
difficulty: 常规
minutes: 8
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 字符分类统计

## 题目

输入一行字符，分别统计英文字母、数字、空格和其他字符的个数。

输入：一行字符；输出：四类字符的计数。

```c
#include <stdio.h>
int main(void)
{
    int ch, letters = 0, digits = 0, spaces = 0, others = 0;
    while((ch = getchar()) != '\n' && ch != EOF)
    {
        if(
        /*〔1〕*/
        ) letters++;
        else if(
        /*〔2〕*/
        ) digits++;
        else if(
        /*〔3〕*/
        ) spaces++;
        else
        /*〔4〕*/
        ;
    }
    printf("%d %d %d %d\n", letters, digits, spaces, others);
    return 0;
}
```

## 常见失分点


本题围绕“字符分类统计”补全字符分类、计数相关语句。各空代回后应共同检查初始化、循环边界、有效下标或指针范围以及最终输出。

<details>
<summary>参考答案与解析</summary>

### 各空答案

1. `〔1〕`：`(ch>='A'&&ch<='Z')||(ch>='a'&&ch<='z')`
2. `〔2〕`：`ch>='0'&&ch<='9'`
3. `〔3〕`：`ch==' '`
4. `〔4〕`：`others++`

### 关键说明

将各空代回后，程序的声明、初始化、循环边界和输出应形成完整逻辑。验证数据：输入 `Ab 3!` 应输出 `2 1 1 1`。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
int main(void)
{
    int ch, letters = 0, digits = 0, spaces = 0, others = 0;
    while((ch = getchar()) != '\n' && ch != EOF)
    {
        if((ch >= 'A' && ch <= 'Z') || (ch >= 'a' && ch <= 'z')) letters++;
        else if(ch >= '0' && ch <= '9') digits++;
        else if(ch == ' ') spaces++;
        else others++;
    }
    printf("%d %d %d %d\n", letters, digits, spaces, others);
    return 0;
}
```
<!-- reference-c:end -->

</details>
