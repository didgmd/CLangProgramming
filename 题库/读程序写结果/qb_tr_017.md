<!-- question-meta
id: QB-TR-017
category: 读程序写结果
chapters: 7
concepts: 递归
difficulty: 常规
minutes: 6
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 递归交替减法

## 题目


写出程序的准确输出：

```c
#include <stdio.h>
static long f(int n)
{
    return n <= 1 ? 2 : n - f(n - 1);
}
int main(void)
{
    printf("%ld\n", f(4));
    return 0;
}
```

本题程序不读取外部输入。请写出程序运行后的精确输出。

## 常见失分点



跟踪“递归交替减法”程序时，围绕递归逐语句记录变量变化，并严格保留输出中的空格与换行。

<details>
<summary>参考答案与解析</summary>

**输出：**

```text
1
```

逐层代入可得 `f(2)=0`、`f(3)=3`、`f(4)=1`。

</details>
