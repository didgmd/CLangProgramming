<!-- question-meta
id: QB-FB-017
category: 程序填空
chapters: 3
concepts: 字符编码
difficulty: 常规
minutes: 8
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 字符大小写转换

## 题目

输入两个字符，分别把小写字母转为大写、大写字母转为小写。

输入：两个字符；输出：转换后的两个字符。

```c
#include <stdio.h>
int main(void)
{
    /*〔3〕*/
    ;
    if(scanf(" %c %c", & a, & b) != 2) return 1;
    if(a >=
    /*〔4〕*/
    && a <= 'z') a = (char) (
    /*〔1〕*/
    );
    if(b >=
    /*〔5〕*/
    && b <= 'Z') b = (char) (
    /*〔2〕*/
    );
    printf("%c %c\n", a, b);
    return 0;
}
```

## 常见失分点


本题围绕“字符大小写转换”补全字符编码相关语句。各空代回后应共同检查初始化、循环边界、有效下标或指针范围以及最终输出。

<details>
<summary>参考答案与解析</summary>

### 各空答案

1. `〔1〕`：`a-'a'+'A'`
2. `〔2〕`：`b-'A'+'a'`
3. `〔3〕`：`char a,b`
4. `〔4〕`：`'a'`
5. `〔5〕`：`'A'`

### 关键说明

将各空代回后，程序的声明、初始化、循环边界和输出应形成完整逻辑。验证数据：输入 `g Q` 应输出 `G q`。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
int main(void)
{
    char a, b;
    if(scanf(" %c %c", & a, & b) != 2) return 1;
    if(a >= 'a' && a <= 'z') a = (char) (a - 'a' + 'A');
    if(b >= 'A' && b <= 'Z') b = (char) (b - 'A' + 'a');
    printf("%c %c\n", a, b);
    return 0;
}
```
<!-- reference-c:end -->

</details>
