<!-- question-meta
id: QB-FB-006
category: 程序填空
chapters: 6
concepts: 字符串连接
difficulty: 常规
minutes: 8
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 字符串连接

## 题目

不用 `strcat`，把字符串 `src` 连接到 `dst` 的末尾。

无输入；输出：连接后的字符串。

```c
#include <stdio.h>
int main(void)
{
    char dst[100] = "C language ", src[] = "practice";
    int i = 0, j = 0;
    while ( /*〔1〕*/ )
        i++;
    while ( /*〔2〕*/ )
    /*〔3〕*/;
    /*〔4〕*/;
    puts(dst);
    return 0;
}
```

## 常见失分点


本题围绕“字符串连接”补全字符串连接相关语句。各空代回后应共同检查初始化、循环边界、有效下标或指针范围以及最终输出。

<details>
<summary>参考答案与解析</summary>

### 各空答案

1. `〔1〕`：`dst[i]!='\0'`
2. `〔2〕`：`src[j]!='\0'`
3. `〔3〕`：`dst[i++]=src[j++]`
4. `〔4〕`：`dst[i]='\0'`

### 关键说明

将各空代回后，程序的声明、初始化、循环边界和输出应形成完整逻辑。验证数据：应输出 `C language practice`。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
int main(void)
{
    char dst[100] = "C language ", src[] = "practice";
    int i = 0, j = 0;
    while (dst[i] != '\0')
    {
        i++;
    }
    while (src[j] != '\0')
    {
        dst[i++] = src[j++];
    }
    dst[i] = '\0';
    puts(dst);
    return 0;
}
```
<!-- reference-c:end -->

</details>
