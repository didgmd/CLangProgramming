<!-- question-meta
id: QB-PG-038
category: 编程题
chapters: 8
concepts: 字符指针、指针差
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 指针法求字符串长度

## 题目



不调用 `strlen`，使用两个指针之差求字符串长度。

### 输入格式

一行长度不超过99的字符串。

### 输出格式

输出字符串长度。

### 数据范围与边界

长度不包含末尾 `\0`，允许输入空行。

### 样例输入

```text
hello world
```

### 样例输出

```text
11
```

## 常见失分点



保留指向首字符的指针，只移动遍历指针；同时处理换行符和 `\0`，且不要把结束标志计入长度。计算指针差时注意相减方向，并严格匹配输出格式。

<details>
<summary>参考答案与解析</summary>

**解题思路：** 用 `start` 保留首字符位置，移动 `p` 直到遇到换行符或 `\0`，此时 `p - start` 即字符串长度。

**评分建议：** 输入与边界处理2分，核心算法5分，正确输出2分，代码规范1分。

**正常与边界测试：** `hello world`；空行；单字符；99个字符。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>

int main(void)
{
    char s[100];
    char *start;
    char *p;

    if (fgets(s, sizeof s, stdin) == NULL)
    {
        return 1;
    }

    start = s;
    p = s;

    while (*p != '\0' && *p != '\n')
    {
        p++;
    }

    printf("%d\n", (int)(p - start));

    return 0;
}
```
<!-- reference-c:end -->

</details>
