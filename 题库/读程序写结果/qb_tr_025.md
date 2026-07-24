<!-- question-meta
id: QB-TR-025
category: 读程序写结果
chapters: 6
concepts: 二维字符数组
difficulty: 常规
minutes: 6
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 字符数组后缀变式

## 题目


写出程序的准确输出：

```c
#include <stdio.h>
#include <string.h>
int main(void)
{
    char s [] = "xyz", a [3] [4];
    for(int i = 0; i < 3; i++) strcpy(a [i], s);
    for(int i = 0; i < 3; i++) printf("%s", & a [i] [i]);
    return 0;
}
```

本题程序不读取外部输入。请写出程序运行后的精确输出。

## 常见失分点



跟踪“字符数组后缀变式”程序时，围绕二维字符数组逐语句记录变量变化，并严格保留输出中的空格与换行。

<details>
<summary>参考答案与解析</summary>

**输出：**

```text
xyzyzz
```

输出 `xyz`、`yz`、`z`。

</details>
