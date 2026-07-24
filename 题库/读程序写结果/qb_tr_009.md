<!-- question-meta
id: QB-TR-009
category: 读程序写结果
chapters: 6
concepts: 二维字符数组、字符串
difficulty: 常规
minutes: 6
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 二维字符数组后缀

## 题目


写出程序的准确输出：

```c
#include <stdio.h>
#include <string.h>
int main(void)
{
    char ch[] = "abc", x[3][4];
    for (int i = 0; i < 3; i++)
        strcpy(x[i], ch);
    for (int i = 0; i < 3; i++)
        printf("%s", &x[i][i]);
    putchar('\n');
    return 0;
}
```

本题程序不读取外部输入。请写出程序运行后的精确输出。

## 常见失分点



跟踪“二维字符数组后缀”程序时，围绕二维字符数组、字符串逐语句记录变量变化，并严格保留输出中的空格与换行。

<details>
<summary>参考答案与解析</summary>

**输出：**

```text
abcbcc
```

三次输出的后缀依次为 `abc`、`bc`、`c`。

</details>
