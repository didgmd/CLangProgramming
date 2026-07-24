<!-- question-meta
id: QB-TR-006
category: 读程序写结果
chapters: 4
concepts: 顺序if
difficulty: 常规
minutes: 6
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 多分支最大值

## 题目


写出程序的准确输出：

```c
#include <stdio.h>
int main(void)
{
    int a = 10, b = 4, c = 3;
    if(a < b) a = b;
    if(a < c) a = c;
    printf("%d,%d,%d\n", a, b, c);
    return 0;
}
```

本题程序不读取外部输入。请写出程序运行后的精确输出。

## 常见失分点



跟踪“多分支最大值”程序时，围绕顺序if逐语句记录变量变化，并严格保留输出中的空格与换行。

<details>
<summary>参考答案与解析</summary>

**输出：**

```text
10,4,3
```

两个条件均为假，三个变量保持原值。

</details>
