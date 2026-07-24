<!-- question-meta
id: QB-TR-002
category: 读程序写结果
chapters: 4
concepts: 嵌套if
difficulty: 常规
minutes: 6
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 嵌套if与后续语句

## 题目


写出程序的准确输出：

```c
#include <stdio.h>
int main(void)
{
    int a = 2, b = 3, c = 1;
    if (a > b)
        if (a > c)
            printf("%d\n", a);
        else
            printf("%d\n", b);
    printf("over!\n");
    return 0;
}
```

本题程序不读取外部输入。请写出程序运行后的精确输出。

## 常见失分点



跟踪“嵌套if与后续语句”程序时，围绕嵌套if逐语句记录变量变化，并严格保留输出中的空格与换行。

<details>
<summary>参考答案与解析</summary>

**输出：**

```text
over!
```

外层条件为假，嵌套分支不执行，最后的输出语句仍执行。

</details>
