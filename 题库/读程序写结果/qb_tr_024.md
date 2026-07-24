<!-- question-meta
id: QB-TR-024
category: 读程序写结果
chapters: 6
concepts: 数组、递推
difficulty: 常规
minutes: 6
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 数组条件递推

## 题目


写出程序的准确输出：

```c
#include <stdio.h>
int main(void)
{
    int a[4];
    for (int i = 0; i < 4; i++)
    {
        a[i] = (i + 2) * (i + 3);
        if (i > 1)
            a[i] += a[i - 2];
    }
    for (int i = 0; i < 4; i++)
        printf("%d,", a[i]);
    return 0;
}
```

本题程序不读取外部输入。请写出程序运行后的精确输出。

## 常见失分点



跟踪“数组条件递推”程序时，围绕数组、递推逐语句记录变量变化，并严格保留输出中的空格与换行。

<details>
<summary>参考答案与解析</summary>

**输出：**

```text
6,12,26,42,
```

后两个元素分别加上前两个位置的值。

</details>
