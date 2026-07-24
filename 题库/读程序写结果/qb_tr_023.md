<!-- question-meta
id: QB-TR-023
category: 读程序写结果
chapters: 6
concepts: 数字字符串
difficulty: 常规
minutes: 6
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 字符串数字转换前导零

## 题目


写出程序的准确输出：

```c
#include <stdio.h>
int main(void)
{
    char s[] = "00124008";
    long n = 0;
    for (int i = 0; s[i]; i++)
        n = n * 10 + s[i] - '0';
    printf("%ld\n", n);
    return 0;
}
```

本题程序不读取外部输入。请写出程序运行后的精确输出。

## 常见失分点



跟踪“字符串数字转换前导零”程序时，围绕数字字符串逐语句记录变量变化，并严格保留输出中的空格与换行。

<details>
<summary>参考答案与解析</summary>

**输出：**

```text
124008
```

按十进制累积时前导零不改变数值。

</details>
