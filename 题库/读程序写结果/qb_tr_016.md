<!-- question-meta
id: QB-TR-016
category: 读程序写结果
chapters: 4、5
concepts: switch、循环
difficulty: 常规
minutes: 6
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# switch输出

## 题目


写出程序的准确输出：

```c
#include <stdio.h>
int main(void)
{
    for (int i = 0; i < 3; i++)
    {
        switch (i)
        {
            case 0 : printf("%d", i);
            break;
            case 2 : printf("%d", i);
            break;
            default : printf("%d", i);
        }
    }
    return 0;
}
```

本题程序不读取外部输入。请写出程序运行后的精确输出。

## 常见失分点



跟踪“switch输出”程序时，围绕switch、循环逐语句记录变量变化，并严格保留输出中的空格与换行。

<details>
<summary>参考答案与解析</summary>

**输出：**

```text
012
```

三个循环值分别进入 case 0、default、case 2。

</details>
