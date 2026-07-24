<!-- question-meta
id: QB-TR-001
category: 读程序写结果
chapters: 4
concepts: 赋值表达式、if
difficulty: 常规
minutes: 6
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 赋值表达式作条件

## 题目


写出程序的准确输出：

```c
#include <stdio.h>
int main(void)
{
    int a = 1, b = 3, c = 5;
    if (c = a + b)
        printf("yes");
    else
        printf("no");
    return 0;
}
```

本题程序不读取外部输入。请写出程序运行后的精确输出。

## 常见失分点



跟踪“赋值表达式作条件”程序时，围绕赋值表达式、if逐语句记录变量变化，并严格保留输出中的空格与换行。

<details>
<summary>参考答案与解析</summary>

**输出：**

```text
yes
```

`c=a+b` 得到非零值 4，因此条件为真。

</details>
