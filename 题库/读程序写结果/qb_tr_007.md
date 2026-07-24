<!-- question-meta
id: QB-TR-007
category: 读程序写结果
chapters: 4
concepts: 悬空else
difficulty: 常规
minutes: 6
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 悬空else

## 题目


写出程序的准确输出：

```c
#include <stdio.h>
int main(void)
{
    int a = 1, b = 0, c = 0;
    if(a < b) if(b < 0) c = 0;
    else c++;
    printf("%d\n", c);
    return 0;
}
```

本题程序不读取外部输入。请写出程序运行后的精确输出。

## 常见失分点



跟踪“悬空else”程序时，围绕悬空else逐语句记录变量变化，并严格保留输出中的空格与换行。

<details>
<summary>参考答案与解析</summary>

**输出：**

```text
0
```

外层条件为假，整个内层 `if-else` 不执行。

</details>
