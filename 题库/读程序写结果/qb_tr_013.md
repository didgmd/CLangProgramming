<!-- question-meta
id: QB-TR-013
category: 读程序写结果
chapters: 4
concepts: 逻辑与、if
difficulty: 常规
minutes: 6
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 逻辑与分支

## 题目


写出程序的准确输出：

```c
#include <stdio.h>
int main(void)
{
    int x = 2, y = 3, z = 4;
    if(x < y && y < z) x += z;
    else y -= x;
    printf("%d\n", x + y);
    return 0;
}
```

本题程序不读取外部输入。请写出程序运行后的精确输出。

## 常见失分点



跟踪“逻辑与分支”程序时，围绕逻辑与、if逐语句记录变量变化，并严格保留输出中的空格与换行。

<details>
<summary>参考答案与解析</summary>

**输出：**

```text
9
```

两个关系均为真，`x` 变为 6，再与 `y` 相加。

</details>
