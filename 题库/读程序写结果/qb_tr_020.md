<!-- question-meta
id: QB-TR-020
category: 读程序写结果
chapters: 5
concepts: while、自减
difficulty: 常规
minutes: 6
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 循环后变量值

## 题目


写出程序的准确输出：

```c
#include <stdio.h>
int main(void)
{
    int i = 10, j = 0;
    while (--i)
        j++;
    printf("%d,%d\n", i, j);
    return 0;
}
```

本题程序不读取外部输入。请写出程序运行后的精确输出。

## 常见失分点



跟踪“循环后变量值”程序时，围绕while、自减逐语句记录变量变化，并严格保留输出中的空格与换行。

<details>
<summary>参考答案与解析</summary>

**输出：**

```text
0,9
```

`i` 从 9 到 1 时循环九次，减为 0 后结束。

</details>
