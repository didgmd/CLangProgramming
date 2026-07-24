<!-- question-meta
id: QB-FB-019
category: 程序填空
chapters: 10
concepts: 文件写入
difficulty: 常规
minutes: 8
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 逐字符写文件

## 题目

输入字符直到 `#`，将此前字符逐个写入临时文件并检查文件打开结果。

输入：以 `#` 结束的字符序列；程序无标准输出。

```c
#include <stdio.h>
int main(void)
{
    FILE * fp =
    /*〔1〕*/
    ;
    if(
    /*〔2〕*/
    ) return 1;
    int ch;
    while(
    /*〔3〕*/
    )
    /*〔4〕*/
    ;
    fclose(fp);
    return 0;
}
```

## 常见失分点


本题围绕“逐字符写文件”补全文件写入相关语句。各空代回后应共同检查初始化、循环边界、有效下标或指针范围以及最终输出。

<details>
<summary>参考答案与解析</summary>

### 各空答案

1. `〔1〕`：`tmpfile()`
2. `〔2〕`：`fp==NULL`
3. `〔3〕`：`(ch=getchar())!='#'&&ch!=EOF`
4. `〔4〕`：`fputc(ch,fp)`

### 关键说明

将各空代回后，程序的声明、初始化、循环边界和输出应形成完整逻辑。验证数据：输入 `abc#` 时文件中写入3个字符；不得在源码目录产生数据文件。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
int main(void)
{
    FILE * fp = tmpfile();
    if(fp == NULL) return 1;
    int ch;
    while((ch = getchar()) != '#' && ch != EOF) fputc(ch, fp);
    fclose(fp);
    return 0;
}
```
<!-- reference-c:end -->

</details>
