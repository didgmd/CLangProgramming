<!-- question-meta
id: QB-TR-015
category: 读程序写结果
chapters: 6
concepts: 二维数组、循环
difficulty: 常规
minutes: 6
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 二维数组筛选求和

## 题目


写出程序的准确输出：

```c
#include <stdio.h>
int main(void)
{
    int a[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}, sum = 0;
    for (int i = 1; i <= 3; i++)
        for (int j = 1; j <= 3; j++)
            if (i % 2 == 0)
                sum += a[i - 1][j - 1];
    printf("%d\n", sum);
    return 0;
}
```

本题程序不读取外部输入。请写出程序运行后的精确输出。

## 常见失分点



跟踪“二维数组筛选求和”程序时，围绕二维数组、循环逐语句记录变量变化，并严格保留输出中的空格与换行。

<details>
<summary>参考答案与解析</summary>

**输出：**

```text
15
```

只在 `i==2` 时累加第二行 4、5、6。

</details>
