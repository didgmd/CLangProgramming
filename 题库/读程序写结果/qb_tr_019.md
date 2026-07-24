<!-- question-meta
id: QB-TR-019
category: 读程序写结果
chapters: 4
concepts: 条件运算符
difficulty: 常规
minutes: 6
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 三目运算符求大值

## 题目


写出程序的准确输出：

```c
#include <stdio.h>
int main(void)
{
    int a = 3, b = 4, c = 6;
    int d = a > b ? (a > c ? a : c) : b;
    printf("%d\n", d);
    return 0;
}
```

本题程序不读取外部输入。请写出程序运行后的精确输出。

## 常见失分点



跟踪“三目运算符求大值”程序时，围绕条件运算符逐语句记录变量变化，并严格保留输出中的空格与换行。

<details>
<summary>参考答案与解析</summary>

**输出：**

```text
4
```

由于 `a>b` 为假，整个条件表达式直接取 `b`。

</details>
