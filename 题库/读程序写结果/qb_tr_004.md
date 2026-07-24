<!-- question-meta
id: QB-TR-004
category: 读程序写结果
chapters: 5、6
concepts: 字符输入、循环
difficulty: 常规
minutes: 6
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 字符结束标志

## 题目


写出程序的准确输出：

```c
#include <stdio.h>
int main(void)
{
    int c;
    while ((c = getchar()) != '$' && c != EOF)
        putchar(c);
    printf("End!\n");
    return 0;
}
```

程序的标准输入为 `abcdefg$abcdefg`。请写出程序运行后的精确输出。

## 常见失分点



跟踪“字符结束标志”程序时，围绕字符输入、循环逐语句记录变量变化，并严格保留输出中的空格与换行。

<details>
<summary>参考答案与解析</summary>

**输出：**

```text
abcdefgEnd!
```

输入 `abcdefg$abcdefg` 时，美元符号后的字符不再处理。

</details>
