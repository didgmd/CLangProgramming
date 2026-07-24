<!-- question-meta
id: QB-TR-027
category: 读程序写结果
chapters: 6
concepts: 杨辉三角、二维数组
difficulty: 常规
minutes: 6
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 杨辉三角小规模

## 题目


写出程序的准确输出：

```c
#include <stdio.h>
int main(void)
{
    int a [4] [4] =
    {
        {
            0
        }
    }
    ;
    for(int i = 0; i < 4; i++)
    {
        a [i] [0] = a [i] [i] = 1;
        for(int j = 1; j < i; j++) a [i] [j] = a [i - 1] [j - 1] + a [i - 1] [j];
    }
    printf("%d %d %d %d\n", a [3] [0], a [3] [1], a [3] [2], a [3] [3]);
    return 0;
}
```

本题程序不读取外部输入。请写出程序运行后的精确输出。

## 常见失分点



跟踪“杨辉三角小规模”程序时，围绕杨辉三角、二维数组逐语句记录变量变化，并严格保留输出中的空格与换行。

<details>
<summary>参考答案与解析</summary>

**输出：**

```text
1 3 3 1
```

第 4 行由上一行相邻元素之和得到。

</details>
