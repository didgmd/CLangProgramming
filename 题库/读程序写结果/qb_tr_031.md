<!-- question-meta
id: QB-TR-031
category: 读程序写结果
chapters: 6
concepts: 杨辉三角、数组边界
difficulty: 常规
minutes: 6
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 杨辉三角错误边界辨析

## 题目


写出程序的准确输出：

```c
#include <stdio.h>
int main(void)
{
    int a[4][4] = {{0}};
    for (int i = 0; i < 4; i++)
    {
        a[i][0] = a[i][i] = 1;
        for (int j = 1; j < i; j++)
            a[i][j] = a[i - 1][j - 1] + a[i - 1][j];
    }
    printf("%d %d %d %d\n", a[3][0], a[3][1], a[3][2], a[3][3]);
    return 0;
}
```

本题程序不读取外部输入。请写出程序运行后的精确输出。

## 常见失分点



跟踪“杨辉三角错误边界辨析”程序时，围绕杨辉三角、数组边界逐语句记录变量变化，并严格保留输出中的空格与换行。

<details>
<summary>参考答案与解析</summary>

**输出：**

```text
1 3 3 1
```

内部循环从1开始并在 `j<i` 前结束，因此不会访问负下标或越过有效递推区。

</details>
