<!-- question-meta
id: QB-FB-004
category: 程序填空
chapters: 8
concepts: 字符指针、字符串复制
difficulty: 常规
minutes: 8
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 复制指定位置后的字符串

## 题目

输入字符串和下标 `m`，把源串从下标 `m` 开始的后缀复制到目标数组。

输入：一个无空格字符串和合法下标 `m`；输出：复制得到的后缀。

```c
#include <stdio.h>
int main(void)
{
    char s[100], d[100];
    int m;
    if (scanf("%99s%d", s, &m) != 2)
    return 1;
    int /*〔1〕*/, j = 0;
    while ( /*〔2〕*/ )
    /*〔3〕*/;
    /*〔4〕*/;
    puts(d);
    return 0;
}
```

## 常见失分点


本题围绕“复制指定位置后的字符串”补全字符指针、字符串复制相关语句。各空代回后应共同检查初始化、循环边界、有效下标或指针范围以及最终输出。

<details>
<summary>参考答案与解析</summary>

### 各空答案

1. `〔1〕`：`i=m`
2. `〔2〕`：`s[i]!='\0'`
3. `〔3〕`：`d[j++]=s[i++]`
4. `〔4〕`：`d[j]='\0'`

### 关键说明

将各空代回后，程序的声明、初始化、循环边界和输出应形成完整逻辑。验证数据：输入 `abcdef 2` 应输出 `cdef`。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
int main(void)
{
    char s[100], d[100];
    int m;
    if (scanf("%99s%d", s, &m) != 2)
    {
        return 1;
    }
    int i = m, j = 0;
    while (s[i] != '\0')
    {
        d[j++] = s[i++];
    }
    d[j] = '\0';
    puts(d);
    return 0;
}
```
<!-- reference-c:end -->

</details>
