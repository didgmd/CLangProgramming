<!-- question-meta
id: QB-TR-003
category: 读程序写结果
chapters: 5
concepts: for、continue、自减
difficulty: 常规
minutes: 6
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 循环中的自减与continue

## 题目


写出程序的准确输出：

```c
#include <stdio.h>
int main(void)
{
    int y = 9;
    for (; y > 0; y--)
        if (y % 3 == 0)
        {
            printf("%d", --y);
            continue;
        }
    return 0;
}
```

本题程序不读取外部输入。请写出程序运行后的精确输出。

## 常见失分点



跟踪“循环中的自减与continue”程序时，围绕for、continue、自减逐语句记录变量变化，并严格保留输出中的空格与换行。

<details>
<summary>参考答案与解析</summary>

**输出：**

```text
852
```

命中 9、6、3 时先在输出表达式中自减，再执行循环更新。

</details>
