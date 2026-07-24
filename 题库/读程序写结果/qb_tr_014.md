<!-- question-meta
id: QB-TR-014
category: 读程序写结果
chapters: 6
concepts: 字符串、下标
difficulty: 常规
minutes: 6
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 偶数下标转大写

## 题目


写出程序的准确输出：

```c
#include <stdio.h>
int main(void)
{
    char s[] = "hello";
    for (int i = 0; s[i]; i++)
        if (i % 2 == 0)
            s[i] -= 32;
    puts(s);
    return 0;
}
```

本题程序不读取外部输入。请写出程序运行后的精确输出。

## 常见失分点



跟踪“偶数下标转大写”程序时，围绕字符串、下标逐语句记录变量变化，并严格保留输出中的空格与换行。

<details>
<summary>参考答案与解析</summary>

**输出：**

```text
HeLlO
```

下标 0、2、4 的小写字母转换为大写。

</details>
