<!-- question-meta
id: QB-TR-026
category: 读程序写结果
chapters: 7
concepts: 递归、阶乘
difficulty: 常规
minutes: 6
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 递归阶乘

## 题目


写出程序的准确输出：

```c
#include <stdio.h>
static long long f(int n)
{
    return n <= 1 ? 1 : n * f(n - 1);
}
int main(void)
{
    printf("%lld\n", f(5));
    return 0;
}
```

本题程序不读取外部输入。请写出程序运行后的精确输出。

## 常见失分点



跟踪“递归阶乘”程序时，围绕递归、阶乘逐语句记录变量变化，并严格保留输出中的空格与换行。

<details>
<summary>参考答案与解析</summary>

**输出：**

```text
120
```

递归展开为 `5*4*3*2*1`。

</details>
