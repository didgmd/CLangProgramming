<!-- question-meta
id: QB-TR-028
category: 读程序写结果
chapters: 8
concepts: 指针参数、交换
difficulty: 常规
minutes: 6
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 指针交换值

## 题目


写出程序的准确输出：

```c
#include <stdio.h>
static void swap(int * a, int * b)
{
    int t = * a;
    * a = * b;
    * b = t;
}
int main(void)
{
    int x = 3, y = 8;
    swap(&x, &y);
    printf("%d %d\n", x, y);
    return 0;
}
```

本题程序不读取外部输入。请写出程序运行后的精确输出。

## 常见失分点



跟踪“指针交换值”程序时，围绕指针参数、交换逐语句记录变量变化，并严格保留输出中的空格与换行。

<details>
<summary>参考答案与解析</summary>

**输出：**

```text
8 3
```

函数通过解引用修改调用者的两个整数。

</details>
