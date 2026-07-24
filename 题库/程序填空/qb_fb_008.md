<!-- question-meta
id: QB-FB-008
category: 程序填空
chapters: 7、8
concepts: 函数、字符指针
difficulty: 常规
minutes: 8
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 函数复制字符串

## 题目

补全字符串复制函数，并输出复制得到的字符串。

无输入；输出：复制后的字符串。

```c
#include <stdio.h>
void copy(char * d, const char * s)
{
    while((
    /*〔1〕*/
    =
    /*〔2〕*/
    ) !=
    /*〔3〕*/
    )
    {
    }
}
int main(void)
{
    char d [100];
    copy(d, "pointer copy");
    puts(d);
    return 0;
}
```

## 常见失分点


本题围绕“函数复制字符串”补全函数、字符指针相关语句。各空代回后应共同检查初始化、循环边界、有效下标或指针范围以及最终输出。

<details>
<summary>参考答案与解析</summary>

### 各空答案

1. `〔1〕`：`*d++`
2. `〔2〕`：`*s++`
3. `〔3〕`：`'\0'`

### 关键说明

将各空代回后，程序的声明、初始化、循环边界和输出应形成完整逻辑。验证数据：应输出 `pointer copy`。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
void copy(char * d, const char * s)
{
    while((* d++ = * s++) != '\0')
    {
    }
}
int main(void)
{
    char d [100];
    copy(d, "pointer copy");
    puts(d);
    return 0;
}
```
<!-- reference-c:end -->

</details>
